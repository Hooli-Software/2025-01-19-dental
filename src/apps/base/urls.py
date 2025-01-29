from django.urls import path

from . import views


urlpatterns = (
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('price-list/', views.PriceListView.as_view(), name='price-list'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('video-reviews/', views.VideoReviewsView.as_view(), name='video-reviews')  # noqa
)
