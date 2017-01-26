from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from board import views
from django.conf.urls import url
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^board/', include('board.urls')),
    url(r'^$', views.index, name='index'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
