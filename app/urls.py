from django.urls import path

from . import views

urlpatterns = [path("", views.cadastros), path("<int:id>", views.consulta_att_delete)]
