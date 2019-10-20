from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.page,name = 'page'),
    url(r'^profile$',views.profile,name = 'profile'),
    url(r'^ownerprofile$',views.ownerprofile,name = 'ownerprofile'),
    url(r'^post$',views.post,name ='post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)