from django.contrib import admin
from django.urls import path
from django.urls.conf import include

admin.site.site_header = "Anky Candles Admin"
admin.site.site_title = "Anky Candles Admin Portal"
admin.site.index_title = "Welcome to Anky Candles Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Django_App.urls'))
]
 