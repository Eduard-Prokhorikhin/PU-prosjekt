from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', include('posts.urls'), name='posts'),
    # path('post/', include('posts.urls'), name='post_detail'),
    path('rentProduct/<int:pk>', views.rent_product, name='rentProduct'),
    # path('resetAllAvailability', views.reset_all_availability, name='resetAllAvailability'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls'), name='account'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
