import requests
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import ViaCep
from .forms import ViaCepForm


class ViaCepListView(FormView):
    template_name = "viacep/list.html"
    form_class = ViaCepForm
    success_url = reverse_lazy("home")  # ajuste conforme sua URL

    def form_valid(self, form):
        cep = form.cleaned_data["cep"].replace("-", "").strip()
        url = f"https://viacep.com.br/ws/{cep}/json/"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if "erro" not in data:
                cep_obj, created = ViaCep.objects.get_or_create(
                    cep=cep,
                    defaults={
                        "logradouro": data.get("logradouro", ""),
                        "bairro": data.get("bairro", ""),
                        "localidade": data.get("localidade", ""),
                        "uf": data.get("uf", ""),
                    }
                )

                self.object = cep_obj
                return super().form_valid(form)

            else:
                form.add_error("cep", "CEP inválido.")
                return self.form_invalid(form)

        else:
            form.add_error("cep", "Erro ao consultar a API.")
            return self.form_invalid(form)