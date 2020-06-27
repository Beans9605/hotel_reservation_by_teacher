from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('modify/<int:pk>', views.reservation_modify, name="reservation_modify"),
    # path('check/', view)
]
