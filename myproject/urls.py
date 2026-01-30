from django.contrib import admin
from django.urls import path
from todo import views # This tells Django to look at your todo folder's views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home), # This handles the main home page
]