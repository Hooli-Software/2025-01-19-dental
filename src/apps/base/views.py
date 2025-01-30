from django.views.generic import TemplateView


class FooterMixin():
    is_footer_transparent = True
    footer_class = 'space-pt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer_class'] = f"{'bg-light' if not self.is_footer_transparent else ''} {self.footer_class}" # noqa
        return context


class HomeView(FooterMixin, TemplateView):
    is_footer_transparent = False
    template_name = 'base/home/index.html'


class AboutView(FooterMixin, TemplateView):
    is_footer_transparent = False
    template_name = 'base/about/index.html'


class ContactView(FooterMixin, TemplateView):
    is_footer_transparent = False
    template_name = 'base/contact/index.html'


class PriceListView(FooterMixin, TemplateView):
    template_name = 'base/price-list/index.html'


class FAQView(FooterMixin, TemplateView):
    is_footer_transparent = False
    footer_class = 'space-lg-pt'
    template_name = 'base/faq/index.html'


class GalleryView(TemplateView):
    template_name = 'base/gallery/index.html'


class VideoReviewsView(FooterMixin, TemplateView):
    footer_class = 'space-lg-pt'
    template_name = 'base/video-reviews/index.html'
