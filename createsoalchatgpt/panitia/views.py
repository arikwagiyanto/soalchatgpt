from django.shortcuts import render # type: ignore
from django.contrib.auth.decorators import login_required
from website.decorators import ijinkan_pengguna

@login_required(login_url='loginPage')
@ijinkan_pengguna(yang_diizinkan=['panitia'])
def beranda_panitia(request):
    context = {
        'judul': 'Halaman Beranda',
        'menu': 'beranda_panitia',
    }
    return render(request, 'beranda_panitia.html', context)

@ijinkan_pengguna(yang_diizinkan=['panitia'])
@login_required(login_url='loginPage')
def kelolajadwal(request):
    context = {
        'judul': 'Halaman kelola jadwal',
        'menu': 'kelolajadwal',
    }
    return render(request, 'kelolajadwal.html', context)

@ijinkan_pengguna(yang_diizinkan=['panitia'])
@login_required(login_url='loginPage')
def lihatsoal(request):
    context = {
        'judul': 'Halaman lihat soal',
        'menu': 'lihatsoal',
    }
    return render(request, 'lihatsoal.html', context)

@ijinkan_pengguna(yang_diizinkan=['panitia'])
@login_required(login_url='loginPage')
def cetaksoal(request):
    context = {
        'judul': 'Halaman cetak soal',
        'menu': 'cetaksoal',
    }
    return render(request, 'cetaksoal.html', context)
