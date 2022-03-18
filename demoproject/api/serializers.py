from rest_framework import serializers

from demo.models import Product, Cart


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = ['id', 'name', 'date', 'category_name', 'url', 'year', 'category']


class CartSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Cart
        fields = ['id', 'product', 'count']