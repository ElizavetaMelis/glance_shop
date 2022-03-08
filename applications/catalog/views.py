
from rest_framework import generics
from applications.catalog.models import Catalog
from applications.catalog.serializers import CatalogSerializer


class CatalogListView(generics.ListAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

