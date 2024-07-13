from rest_framework import serializers

from main.models import Product, Review
#
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product, Review
        fields = "__all__"
#
#
class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
#
#
class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product, Review
        fields = ["title", "description", "price", "reviews"]