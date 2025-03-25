# Inisialisasi daftar tugas
tugas_list = []

# Fungsi untuk menampilkan daftar tugas
def tampilkan_daftar_tugas():
    # Cek apakah daftar tugas kosong
    if not tugas_list:
        print("Daftar Tugas kosong.")
    else:
        print("Daftar Tugas:")
        # Iterasi melalui daftar tugas dan tampilkan
        for index, tugas in enumerate(tugas_list):
            print(f"{index + 1}. {tugas}")

# Fungsi untuk menambahkan tugas
def tambah_tugas(tugas):
    # Cek apakah tugas yang dimasukkan kosong
    if not tugas:
        print("Error: Tugas tidak boleh kosong.")
        return
    # Tambahkan tugas ke dalam daftar
    tugas_list.append(tugas)
    print("Tugas berhasil ditambahkan!")

# Fungsi untuk menghapus tugas berdasarkan nomor
def hapus_tugas(no_tugas):
    try:
        # Konversi nomor tugas ke integer
        no_tugas = int(no_tugas)
        # Cek apakah nomor tugas valid
        if no_tugas < 1 or no_tugas > len(tugas_list):
            raise IndexError("Tugas dengan nomor {} tidak ditemukan.".format(no_tugas))
        # Hapus tugas dari daftar
        tugas_list.pop(no_tugas - 1)
        print("Tugas berhasil dihapus!")
    except ValueError:
        # Tangani error jika input bukan angka
        print("Error: Masukkan nomor yang valid.")
    except IndexError as e:
        # Tangani error jika nomor tugas tidak ditemukan
        print(e)

# Loop utama program
while True:
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")
    
    # Ambil input pengguna untuk aksi yang dipilih
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    
    if pilihan == '1':
        # Input tugas yang ingin ditambahkan
        tugas = input("Masukkan tugas yang ingin ditambahkan: ")
        tambah_tugas(tugas)
    elif pilihan == '2':
        # Input nomor tugas yang ingin dihapus
        no_tugas = input("Masukkan nomor tugas yang ingin dihapus: ")
        hapus_tugas(no_tugas)
    elif pilihan == '3':
        # Tampilkan daftar tugas
        tampilkan_daftar_tugas()
    elif pilihan == '4':
        print("Keluar dari program.")
        break
    else:
        # Tangani input tidak valid
        print("Error: Pilihan tidak valid.")