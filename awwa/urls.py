from . import views
from awwa import views as user_views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('new_project/',views.new_project,name='add-project')
]
