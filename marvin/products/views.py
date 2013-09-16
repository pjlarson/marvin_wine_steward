from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "marvin_app/index.django.html"