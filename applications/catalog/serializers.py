from rest_framework import serializers

from applications.catalog.models import Catalog


class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if not instance.parent:
            rep.pop('parent')
        return rep
