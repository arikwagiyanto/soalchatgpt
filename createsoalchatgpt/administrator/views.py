from django.shortcuts import render # type: ignore
from django.contrib.auth.decorators import login_required
from website.decorators import ijinkan_pengguna, pilihan_login

@login_required(login_url='loginPage')
@pilihan_login
def beranda(request):
    context = {
        'judul': 'Halaman Beranda',
        'menu': 'beranda',
    }
    return render(request, 'beranda.html', context)

@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def pengguna(request):
    context = {
        'judul': 'Halaman pengguna',
        'menu': 'pengguna',
    }
    return render(request, 'pengguna.html', context)

@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def cekjadwal(request):
    context = {
        'judul': 'Halaman lihat jadwal',
        'menu': 'cekjadwal',
    }
    return render(request, 'lihatjadwal.html', context)

@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def ceksoal(request):
    context = {
        'judul': 'Halaman lihat soal',
        'menu': 'ceksoal',
    }
    return render(request, 'lihatsoal.html', context)
