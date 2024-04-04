from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'projectapp'

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectCreateView.as_view(), name='detail'),
]