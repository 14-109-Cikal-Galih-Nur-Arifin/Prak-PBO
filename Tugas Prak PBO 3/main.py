import math

class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        return Calculator(self.value / other.value)

    def __pow__(self, other):
        return Calculator(self.value ** other.value)

    def log(self, base=math.e):
        return Calculator(math.log(self.value, base))

    def __repr__(self):
        return str(self.value)

def main():
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. ^")
    print("6. log")
    
    pilihan = input("Masukkan pilihan operasi (1-6): ")

    if pilihan in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
        
        a = Calculator(num1)
        b = Calculator(num2)

        if pilihan == "1":
            hasil = a + b
            print(f"Hasil penjumlahan {num1} + {num2} = {hasil}")
        elif pilihan == "2":
            hasil = a - b
            print(f"Hasil pengurangan {num1} - {num2} = {hasil}")
        elif pilihan == "3":
            hasil = a * b
            print(f"Hasil perkalian {num1} * {num2} = {hasil}")
        elif pilihan == "4":
            hasil = a / b
            print(f"Hasil pembagian {num1} / {num2} = {hasil}")
        elif pilihan == "5":
            hasil = a ** b
            print(f"Hasil pangkat {num1} ^ {num2} = {hasil}")

    elif pilihan == "6":
        num = float(input("Masukkan angka untuk logaritma: "))
        a = Calculator(num)
        base = float(input("Masukkan basis logaritma (default e): ") or math.e)
        hasil = a.log(base)
        print(f"Hasil logaritma dari {num} dengan basis {base} = {hasil}")

    else:
        print("Pilihan tidak valid.")

main()