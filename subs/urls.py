from django.urls import path
from .views import SubsView

app_name = 'subs'

urlpatterns = [
    path('', SubsView.as_view(), name='all'),
]
