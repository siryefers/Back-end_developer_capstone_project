#define URL route for index() view
from django.urls import path
from . import views


urlpatterns = [

    path('menu/', views.MenuItemsView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),


]
