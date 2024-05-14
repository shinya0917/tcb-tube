from django.urls import path
from .views import nippoListView, nippoDetailView

urlpatterns = [
    path("", nippoListView),
    path("detail/<int:number>", nippoDetailView),
]