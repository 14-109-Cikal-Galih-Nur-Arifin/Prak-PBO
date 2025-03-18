import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child:
    def __init__(self, father, mother):
        self.father_blood_type = father.blood_type
        self.mother_blood_type = mother.blood_type
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        # Menentukan golongan darah anak berdasarkan golongan darah orang tua
        if self.father_blood_type == "A" and self.mother_blood_type == "A":
            return "A"
        elif self.father_blood_type == "A" and self.mother_blood_type == "O":
            return random.choice(["A", "O"])
        elif self.father_blood_type == "O" and self.mother_blood_type == "A":
            return random.choice(["A", "O"])
        elif self.father_blood_type == "A" and self.mother_blood_type == "B":
            return random.choice(["A", "B", "AB"])
        elif self.father_blood_type == "B" and self.mother_blood_type == "A":
            return random.choice(["A", "B", "AB"])
        elif self.father_blood_type == "B" and self.mother_blood_type == "B":
            return "B"
        elif self.father_blood_type == "B" and self.mother_blood_type == "O":
            return random.choice(["B", "O"])
        elif self.father_blood_type == "O" and self.mother_blood_type == "B":
            return random.choice(["B", "O"])
        elif self.father_blood_type == "O" and self.mother_blood_type == "O":
            return "O"
        elif self.father_blood_type == "AB" and self.mother_blood_type == "A":
            return random.choice(["A", "B", "AB"])
        elif self.father_blood_type == "A" and self.mother_blood_type == "AB":
            return random.choice(["A", "B" "AB"])
        elif self.father_blood_type == "AB" and self.mother_blood_type == "B":
            return random.choice(["A", "B", "AB"])
        elif self.father_blood_type == "B" and self.mother_blood_type == "AB":
            return random.choice(["A", "B", "AB"])
        elif self.father_blood_type == "AB" and self.mother_blood_type == "O":
            return random.choice(["A", "B"])
        elif self.father_blood_type == "O" and self.mother_blood_type == "AB":
            return random.choice(["A", "B"])
        else:
            return "Unknown blood type"

# Input golongan darah orang tua
father_blood_type = input("Masukkan golongan darah ayah (A, B, AB, O): ").strip().upper()
mother_blood_type = input("Masukkan golongan darah ibu (A, B, AB, O): ").strip().upper()

# Membuat objek Father dan Mother
father = Father(father_blood_type)
mother = Mother(mother_blood_type)

# Membuat objek Child
child = Child(father, mother)

# Menampilkan hasil golongan darah anak
print("Anak memiliki golongan darah:", child.blood_type)