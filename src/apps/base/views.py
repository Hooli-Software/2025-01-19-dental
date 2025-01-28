from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'base/home/index.html'


class AboutView(TemplateView):
    template_name = 'base/about/index.html'


class ContactView(TemplateView):
    template_name = 'base/contact/index.html'


class PriceListView(TemplateView):
    template_name = 'base/price-list/index.html'
