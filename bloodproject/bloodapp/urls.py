from . import views
from django.urls import path,include

urlpatterns = [

    path('',views.demo,name='demo'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('donate',views.donate,name='donate'),
    path('logout',views.logout,name='logout'),
    path('fillform',views.fillform,name='fillform'),
    # path('placedet',views.placedet,name='placedet')

]