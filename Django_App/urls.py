from django.contrib import admin
from django.urls import path
from Django_App import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
    # path('submitcontact',views.submitcontact, name='submitcontact'),
    path('login' ,views.login, name='login'),
    path('logout',views.logout, name='logout'),

]
   