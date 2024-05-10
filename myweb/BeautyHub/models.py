from django.db import models

class KategoriProduk(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey(KategoriProduk, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
