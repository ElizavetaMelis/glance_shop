from django.urls import path

from applications.catalog.views import CatalogListView

urlpatterns = [
    path('list/', CatalogListView.as_view())
]
