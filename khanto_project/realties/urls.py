from django.urls import path

from .views import RealtiesListView, RealtiesDetailsView

urlpatterns = [
    path('', RealtiesListView.as_view()),
    path('/<int:realty_id>', RealtiesDetailsView.as_view()),
]