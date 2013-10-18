from django.views.generic import TemplateView, ListView
from .models import Country


class CountryList(ListView):
    model = Country
