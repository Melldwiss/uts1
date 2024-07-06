# BeautyHub/views.py

from rest_framework import viewsets
from .models import KategoriProduk, Produk, Review, MenuPenjualan
from .serializers import KategoriProdukSerializer, ProdukSerializer, ReviewSerializer, MenuPenjualanSerializer

class KategoriProdukViewSet(viewsets.ModelViewSet):
    queryset = KategoriProduk.objects.all()
    serializer_class = KategoriProdukSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MenuPenjualanViewSet(viewsets.ModelViewSet):
    queryset = MenuPenjualan.objects.all()
    serializer_class = MenuPenjualanSerializer
