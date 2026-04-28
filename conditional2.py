# Input dari pengguna
nilai_nilai = float(input("Masukkan nilai nilai Anda: "))
jenis_kelamin = input("Masukkan jenis kelamin Anda (L/P): ")

# Conditional statement
if nilai_nilai >= 80:
    print("Anda lulus")
    if jenis_kelamin.lower() == "l":
        print("Selamat atas lulus, Anda dapat melanjutkan ke jenjang S1")
    elif jenis_kelamin.lower() == "p":
        print("Selamat atas lulus, Anda dapat melanjutkan ke jenjang S1")
    else:
        print("Jenis kelamin yang dimasukkan tidak valid")
else:
    print("Anda tidak lulus")
    if jenis_kelamin.lower() == "l":
        print("Anda dapat mengulang ujian atau mengikuti program khusus")
    elif jenis_kelamin.lower() == "p":
        print("Anda dapat mengulang ujian atau mengikuti program khusus")
    else:
        print("Jenis kelamin yang dimasukkan tidak valid")