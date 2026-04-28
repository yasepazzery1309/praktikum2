umur = int(input("Masukkan umur Anda: "))
pemahaman_algoritma = input("Apakah Anda memahami algoritma? (ya/tidak): ")

if umur >= 17 and pemahaman_algoritma.lower() == "ya":
    print("Anda sudah bisa menjadi mahasiswa TI!" )
else:    print("Maaf, Anda belum bisa untuk menjadi mahasiswa TI.")  
