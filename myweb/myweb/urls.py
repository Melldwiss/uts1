from django.urls import path, include
from rest_framework.routers import DefaultRouter
from BeautyHub.views import KategoriProdukViewSet, ProdukViewSet

router = DefaultRouter()
router.register(r'kategori-produk', KategoriProdukViewSet)
router.register(r'produk', ProdukViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]

