from rest_framework import viewsets
from .models import KategoriProduk, Produk
from .serializers import KategoriProdukSerializer, ProdukSerializer

class KategoriProdukViewSet(viewsets.ModelViewSet):
    queryset = KategoriProduk.objects.all()
    serializer_class = KategoriProdukSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
