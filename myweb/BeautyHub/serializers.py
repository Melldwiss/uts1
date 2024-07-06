# serializers.py

from rest_framework import serializers
from .models import KategoriProduk, Produk, Review, MenuPenjualan

class KategoriProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriProduk  # Add this line
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk  # Add this line
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review  # Add this line
        fields = '__all__'

class MenuPenjualanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPenjualan  # Add this line
        fields = '__all__'
