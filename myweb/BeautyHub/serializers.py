from rest_framework import serializers
from .models import KategoriProduk, Produk

class KategoriProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriProduk
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'
