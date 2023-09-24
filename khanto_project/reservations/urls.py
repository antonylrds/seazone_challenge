from django.urls import path

from .views import ReservationListView, ReservationDetailView

urlpatterns = [
    path("", ReservationListView.as_view()),
    path("/<int:reservation_id>", ReservationDetailView.as_view()),
]