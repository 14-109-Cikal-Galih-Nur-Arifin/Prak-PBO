nama = input("Masukkan nama: ")
nim = int(input("Masukkan nim: "))
resolusi = input("Masukkan Resolusi di tahun ini: ")

nama_file = "Me.txt"

with open(nama_file, 'w') as file:
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Resolusi: {resolusi}\n")
    
    print(f"File {nama_file} berhasil dibuat!")