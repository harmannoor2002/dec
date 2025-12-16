from django.urls import path
from char_count.views import char_count

urlpatterns = [
    path('char_count/', char_count),
]

