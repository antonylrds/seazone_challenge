from django.urls import path

from .views import AdsListView, AdsDetailView

urlpatterns = [
    path('', AdsListView.as_view()),
    path('/<int:ad_id>', AdsDetailView.as_view()),
]