from django.contrib import admin
from django.urls import path
from Asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Loginview),
    path('todo/', todo),
    path('todoochir/<int:son>/', ochirish),
    path('logout/',Logaut),
    path('register/',register)
]
