from django.urls import path
from .views import * 

urlpatterns = [
    path('', welcome),
    path('post/<int:pk>', post),
    path('login', signin),
    path('logout', signout),
    path('profile', profile),
    path('register', signup),
]

