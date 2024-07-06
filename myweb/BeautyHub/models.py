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

class Review(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    rating = models.IntegerField()
    komentar = models.TextField()

    def __str__(self):
        return f"{self.produk.nama} - {self.rating}"

class MenuPenjualan(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    tanggal_penjualan = models.DateTimeField(auto_now_add=True)
    jumlah = models.PositiveIntegerField()
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produk.nama} - {self.jumlah} - {self.tanggal_penjualan}"
