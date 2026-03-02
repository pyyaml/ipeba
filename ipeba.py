import time
import os
from termcolor import colored

# Konfigurasi untuk responsivitas
class Config:
    TYPING_SPEED = 0.02  # Kecepatan mengetik (detik)
    TERMINAL_WIDTH = os.get_terminal_size().columns
    PRIMARY_COLOR = 'cyan'
    ACCENT_COLOR = 'green'
    TEXT_COLOR = 'white'

def mengetik(teks, kecepatan=Config.TYPING_SPEED):
    """Efek mengetik dengan kecepatan yang dapat disesuaikan"""
    for karakter in teks:
        print(colored(karakter, Config.TEXT_COLOR), end='', flush=True)
        time.sleep(kecepatan)
    print()  # Newline di akhir

def buat_garis(panjang=None, karakter='─'):
    """Membuat garis horizontal yang responsif"""
    if panjang is None:
        panjang = min(Config.TERMINAL_WIDTH - 2, 70)
    return colored(karakter * panjang, Config.ACCENT_COLOR)

def buat_bingkai_header(judul):
    """Membuat header dengan bingkai modern"""
    max_width = min(Config.TERMINAL_WIDTH - 4, 70)
    panjang_judul = len(judul)
    
    if panjang_judul > max_width - 4:
        judul = judul[:max_width - 7] + "..."
        panjang_judul = len(judul)
    
    padding_kiri = (max_width - panjang_judul) // 2
    padding_kanan = max_width - panjang_judul - padding_kiri
    
    print(buat_garis(max_width + 2))
    print(colored("│ ", Config.PRIMARY_COLOR) + 
          colored(" " * padding_kiri + judul + " " * padding_kanan, 'white') + 
          colored(" │", Config.PRIMARY_COLOR))
    print(buat_garis(max_width + 2))
    print()

def buat_bingkai_teks(teks, width=None):
    """Membuat bingkai untuk teks dengan padding otomatis"""
    if width is None:
        width = min(Config.TERMINAL_WIDTH - 4, 70)
    
    # Bagi teks menjadi baris jika terlalu panjang
    baris_teks = []
    for baris in teks.split('\n'):
        if len(baris) > width - 4:
            # Wrap text
            kata_kata = baris.split(' ')
            baris_saat_ini = ""
            for kata in kata_kata:
                if len(baris_saat_ini) + len(kata) + 1 <= width - 4:
                    baris_saat_ini += kata + " "
                else:
                    if baris_saat_ini:
                        baris_teks.append(baris_saat_ini.strip())
                    baris_saat_ini = kata + " "
            if baris_saat_ini:
                baris_teks.append(baris_saat_ini.strip())
        else:
            baris_teks.append(baris)
    
    print(colored("┌" + "─" * (width - 2) + "┐", Config.PRIMARY_COLOR))
    for baris in baris_teks:
        padding = width - len(baris) - 4
        print(colored("│ ", Config.PRIMARY_COLOR) + 
              colored(baris + " " * padding, 'white') + 
              colored(" │", Config.PRIMARY_COLOR))
    print(colored("└" + "���" * (width - 2) + "┘", Config.PRIMARY_COLOR))
    print()

def desain_header_modern():
    """Header desain modern dengan emoji dan warna"""
    print()
    buat_bingkai_header("✨ INSTITUT PESANTREN BABAKAN ✨")
    print(colored("Kami segenap mahasiswa KKN Desa Kedongdong", 'cyan'))
    print(colored("mengucapkan selamat dan sukses untuk kalian semua", 'cyan'))
    print()

def tampilkan_pesan_utama(pesan):
    """Tampilkan pesan utama dengan efek mengetik"""
    print(colored("📋 PENGUMUMAN UJIAN KOMPREHENSIF", 'yellow'))
    print()
    mengetik(pesan, kecepatan=0.01)
    print()

def tampilkan_credit(credit):
    """Tampilkan credit dengan format modern"""
    print(colored("👥 CREDIT & UCAPAN", 'magenta'))
    buat_bingkai_teks(credit)

def tampilkan_pesan_doa():
    """Tampilkan pesan-pesan motivasi dari peserta"""
    pesan_doa = [
        ("Noval Hadi", "Jangan lupa HP pada di kumpulin!"),
        ("Luwih Muin", "Sebelum ujian doa dulu yah 🙏"),
        ("Annas Abi Hamzah", "Jangan pada nyontek hehe 😄"),
        ("Ahmad Zaky", "Ingat Tuhan melihat, Malaikat mencatat"),
    ]
    
    print(colored("💬 PESAN DARI TEMAN-TEMAN", 'green'))
    print()
    for nama, pesan in pesan_doa:
        print(colored(f"  {nama}: ", 'cyan') + colored(pesan, 'white'))
    print()

def penutup():
    """Pesan penutup yang inspiratif"""
    print(colored("═" * min(Config.TERMINAL_WIDTH - 2, 70), 'yellow'))
    print(colored("✨ Sukses terus Institut Pesantren Babakan ✨", 'yellow'))
    print(colored("Semoga kalian sehat, dimudahkan, dan sukses! 🎓", 'green'))
    print(colored("═" * min(Config.TERMINAL_WIDTH - 2, 70), 'yellow'))
    print()

# ============== MAIN EXECUTION ============== 
if __name__ == "__main__":
    # Header
    desain_header_modern()
    
    # Pesan Utama
    pesan_utama = (
        "Selamat Mengerjakan Ujian Komprehensif!\n"
        "16 Maret 2024 - 20 Maret 2024\n\n"
        "Semoga kalian sehat, sukses,\n"
        "dan dimudahkan dalam pengerjaan ujian.\n"
    )
    tampilkan_pesan_utama(pesan_utama)
    
    # Credit
    credit = "@pyyaml | INSTITUT PESANTREN BABAKAN"
    tampilkan_credit(credit)
    
    # Pesan Doa
    tampilkan_pesan_doa()
    
    # Penutup
    penutup()