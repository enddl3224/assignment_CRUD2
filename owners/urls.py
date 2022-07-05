from django.urls import path

from owners.views import OwnersView
from owners.views import DogsView

urlpatterns = [
    path('/owners', OwnersView.as_view()),
    path('/dogs', DogsView.as_view()),
]