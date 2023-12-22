import time
from termcolor import colored

def mengetik(teks):
    for karakter in teks:
        print(colored(karakter, 'green'), end='', flush=True)
        time.sleep(0.05)

def desain_hacker():
    print(colored(" ___________________________________________________________", 'green'))
    print(colored("|                                                           |", 'green'))
    print(colored("|            KAMI SEGENAP MAHASISWA PAI SEMESTER 7          |", 'green'))
    print(colored("|               MENGUCAPKAN SELAMAT & SUKSES                |", 'green'))
    print(colored("|___________________________________________________________|", 'green'))
    print("")
    
def teks_credit_tengah_bingkai(credit):
    lebar_bingkai = 40
    panjang_credit = len(credit)
    sisa_lebar = lebar_bingkai - 2 - panjang_credit

    bingkai_atas = colored('+' + '-' * (lebar_bingkai - 2) + '+', 'green')
    bingkai_tengah = colored('| ' + ' ' * (sisa_lebar // 2) + credit + ' ' * (sisa_lebar - sisa_lebar // 2) + ' |', 'green')
    bingkai_bawah = colored('+' + '-' * (lebar_bingkai - 2) + '+', 'green')
    print(bingkai_atas)
    print(bingkai_tengah)
    print(bingkai_bawah)

credit = "@pyyaml | INSTITUT PESANTREN BABAKAN "
    
pesan = "Selamat Dan Sukses Atas Beralih Status \nSekolah Tinggi Ma'had Ali Cirebon (STAIMA) \nMenjadi Institut Pesantren Babakan (IPEBA) \nSemoga Ini Menjadi Langkah Awal \nUntuk Lebih Banyak Prestasi Dan Kemajuan.\n\n[Hadad Fauzi]\nSemoga Menjelma Menjadi Bintang Yang Terang\n\n[Ahmad Fauzan]\nTidak Ada Kata-Kata,Yang Perlu Bukti Nyata\n\n[Abdullah]\nSemoga Do'a Dan Harapan Akan Selalu Bersemayam Untuk Orang-Orang Yang Kuat.\n\n[Luwih Muin]\nSemoga Semakin Berkualitas lagi\n\n[PAI Semester 7]\nSukses Terus Institut Pesantren Babakan, Dari Kami Sekian Dan Terima Kasih\n\n"

desain_hacker()
mengetik(pesan)
teks_credit_tengah_bingkai(credit)
print("")
