# BeautyHub/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KategoriProdukViewSet, ProdukViewSet, ReviewViewSet, MenuPenjualanViewSet

router = DefaultRouter()
router.register(r'kategori-produk', KategoriProdukViewSet)
router.register(r'produk', ProdukViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'menu-penjualan', MenuPenjualanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
