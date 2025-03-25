import math

def hitung_akar_kuadrat():
    while True:
        try:
            input_angka = input("Masukkan angka: ")
            
            # Mengubah input menjadi angka
            angka = float(input_angka)

            # Memeriksa jika angka negatif atau nol
            if angka < 0:
                print("Input tidak valid. Harap masukkan angka positif.")
            elif angka == 0:
                print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
            else:
                # Menghitung akar kuadrat
                akar = math.sqrt(angka)
                print(f"Akar kuadrat dari {angka} adalah {akar}.")
                break

        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")

# Memanggil fungsi
hitung_akar_kuadrat()