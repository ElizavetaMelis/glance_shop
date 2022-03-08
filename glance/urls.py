
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
    path('catalog/', include('applications.catalog.urls')),
    path('orders/', include('applications.orders.urls')),
    path('products/', include('applications.products.urls')),
    path('reviews/', include('applications.reviews.urls')),
]
