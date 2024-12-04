from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('',home,name='home'),

    path('',Affichage.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)