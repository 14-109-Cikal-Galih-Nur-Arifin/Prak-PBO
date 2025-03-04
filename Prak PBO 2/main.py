dictionary = {}

jumlah_mahasiswa = int(input("Masukkan jumlah siswa: "))

for i in range(jumlah_mahasiswa):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    nilai = int(input(f"Masukkan nilai untuk {nama}: "))
    dictionary.update({nama: nilai})  

print("dictionary =", dictionary)
