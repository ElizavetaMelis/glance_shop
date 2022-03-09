from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from glance import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
    path('catalog/', include('applications.catalog.urls')),
    path('orders/', include('applications.orders.urls')),
    path('products/', include('applications.products.urls')),
    path('reviews/', include('applications.reviews.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
