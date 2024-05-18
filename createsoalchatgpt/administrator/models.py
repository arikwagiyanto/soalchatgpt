from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Pengguna(models.Model):
    Jk=(
        ('Laki-laki','Laki-laki'),
        ('Perempuan','Perempuan')
        )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama_pengguna = models.CharField(max_length=200, blank=True, null=True)
    alamat = models.TextField (blank=True, null=True,verbose_name='Alamat pengguna')
    nik = models.CharField(max_length=100, blank=True, null=True)
    no_hp = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nama_pengguna
    class Meta:
        verbose_name_plural ="Pengguna"

class Panitia(models.Model):
    Jk=(
        ('Laki-laki','Laki-laki'),
        ('Perempuan','Perempuan')
        )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama_pengguna = models.CharField(max_length=200, blank=True, null=True)
    alamat = models.TextField (blank=True, null=True,verbose_name='Alamat Panitia')
    nik = models.CharField(max_length=100, blank=True, null=True)
    no_hp = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.Panitia
    class Meta:
        verbose_name_plural ="Panitia"

class Guru(models.Model):
    nama = models.CharField(max_length=200, blank= True, null= False)
    aktif = models.BooleanField(default= True)
    banner_satu = models.FileField(upload_to='banner/gambar',blank=True, 
    null=True,max_length=300)
    banner_dua = models.FileField(upload_to='banner/gambar',blank=True, 
    null=True,max_length=300)
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    class Meta:
        verbose_name_plural ="Data Guru"
    def __str__(self):
        return f"Nama: {self.nama}"
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.nama)
        return super().save(*args, **kwargs)

# class Barang(models.Model):
#     KETERANGAN=(
#         ('Baru', 'Baru'),
#         ('Lama' , 'Lama'),
#     )
#     kategori = models.ForeignKey(Soal, null=True, blank=True, 
#     related_name="barang", on_delete=models.SET_NULL)
#     penjual = models.ForeignKey(Pengguna, null=True, blank=True, 
#     related_name="penjual", on_delete=models.SET_NULL)
#     nama_barang = models.CharField(max_length=200, blank=True, null=True)
#     gambar = models.FileField(upload_to='barang/gambar',blank=True, 
#     null=True,max_length=300)
#     gambar_satu = models.FileField(upload_to='barang/gambar',blank=True, 
#     null=True,max_length=300)
#     gambar_dua = models.FileField(upload_to='barang/gambar',blank=True, 
#     null=True,max_length=300)
#     gambar_tiga = models.FileField(upload_to='barang/gambar',blank=True, 
#     null=True,max_length=300)
#     gambar_empat = models.FileField(upload_to='barang/gambar',blank=True, 
#     null=True,max_length=300)
#     gambar_lima = models.FileField(upload_to='barang/gambar',blank=True, 
#     null=True,max_length=300)
#     slug = models.SlugField(max_length=200, unique=True)
#     keterangan = models.TextField(blank=True, null=True)
#     harga = models.PositiveIntegerField(blank=True, null=True)
#     no_whatsup = models.PositiveBigIntegerField(blank=True, null=True,)
#     tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
#     diskon = models.IntegerField(default=0, blank=True, null=True, 
#     verbose_name="Diskon (%)")
#     dibeli = models.IntegerField(default=0, blank=True, null=True)
#     aktif = models.BooleanField(default=False)
#     keterangan_barang = models.CharField(max_length=200, null=True, choices=KETERANGAN)
#     @property
    
#     def setelah_diskon(self):
#         if self.diskon == 0 :
#             nilai_diskon = self.harga
#         else:
#             jml = self.diskon / 100
#             nilai_diskon = self.harga - (jml * self.harga)
#         return nilai_diskon
    
#     class Meta:
#         verbose_name_plural ="Data Barang"
#     def __str__(self):
#         return self.nama_barang
#     def save(self, *args, **kwargs): # new
#         if not self.slug:
#             self.slug = slugify(self.nama_barang)
#         return super().save(*args, **kwargs)