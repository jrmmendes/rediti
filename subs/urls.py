from django.urls import path
from .views import (SubsView, SubView, CreateSubView,
                    CreateThreadView, CreatePostView)

app_name = 'subs'

urlpatterns = [
    path('', SubsView.as_view(), name='all'),
    path('new/', CreateSubView.as_view(), name='new'),
    path('new-thread/', CreateThreadView.as_view(), name='new_thread'),
    path('new-post/', CreatePostView.as_view(), name='create_post'),
    path('<slug:slug>/', SubView.as_view(), name='r'),
]
