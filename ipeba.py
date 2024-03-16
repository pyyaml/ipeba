import time
from termcolor import colored

def mengetik(teks):
    for karakter in teks:
        print(colored(karakter, 'green'), end='', flush=True)
        time.sleep(0.05)

def desain_hacker():
    print(colored(" ___________________________________________________________", 'green'))
    print(colored("|                                                           |", 'green'))
    print(colored("|            KAMI SEGENAP MAHASISWA KKN DESA KEDONGDONG     |", 'green'))
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
    
pesan = "Selamat Mengerjakan Ujian Komprehensif  \n16 Maret 2024 \nSampai 20 Maret 2024 \nSemoga Sukses Sehat Samaelalu \nDan Dimudahkan Dalam Pengerjaan Ujian nya. \n\n[Noval Hadi]\nJangan Lupa HP Pada di Kumpulin wir\n\n[Luwih Muin]\nSebelum Ujian Doa Dulu Yah\n\n[Annas Abi Hamzah]\nJangan Pada Nyontek hehe\n\n[Ahmad Zaky]\nIngat Tuhan Melihat Malaikat Mencatat\n\n[KKN KEDONGDONG]\nSukses Terus Institut Pesantren Babakan, Dari Kami Sekian Dan Terima Kasih\n\n"

desain_hacker()
mengetik(pesan)
teks_credit_tengah_bingkai(credit)
print("")
