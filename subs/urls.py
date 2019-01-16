from django.urls import path
from .views import SubsView, SubView

app_name = 'subs'

urlpatterns = [
    path('', SubsView.as_view(), name='all'),
    path('<slug:slug>/', SubView.as_view(), name='r'),
]
