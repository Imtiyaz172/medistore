
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', views.about_us),
    path('corona/', views.corona),
    path('contact/', views.contact,name="contact"),
    path('store/',views.products),
    path('store/<int:id>',views.product_detail),
    path('tips/',views.tips),
    path('tips/<int:id>',views.tips_detail),
    path('beauty/',views.beauty),
    path('beauty/<int:id>',views.beauty_detail),
    path('health/',views.health),
    path('health/<int:id>',views.health_detail),
    path('cart/', views.cart),
    path('delete/<int:id>', views.delete_prod),
    path('login/', views.login),
    path('logout/', views.logout),
    path('reg/', views.user_register),
]
