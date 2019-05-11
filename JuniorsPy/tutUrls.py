from django.urls import path
from .views import leadView

urlpatterns = [
    path('api/lead/', leadView.LeadListCreate.as_view()),
]