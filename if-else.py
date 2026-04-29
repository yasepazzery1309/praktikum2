# # nilai = 85

# # if nilai >= 90:
# #     print("Predikat: A")
# # elif nilai >= 80:
# #     print("Predikat: B")
# # elif nilai >= 70:
# #     print("Predikat: C")
# # else:
# #     print("Predikat: D")
  
# username = "admin"
# password = "123"

# if username == "admin" and password == "123":
#     print("Login berhasil!")
# else:
#     print("Username atau password salah.")

# punya_tiket = True
# umur = 12

# if punya_tiket:
#     if umur >= 13:
#         print("Boleh menonton film remaja.")
#     else:
#         print("Boleh menonton film anak-anak.")
# else:
#     print("Silakan beli tiket terlebih dahulu.")


# usia = 20
# status = "Dewasa" if usia >= 18 else "Anak-anak"
# print(status)

hari = "Senin"

match hari:
    case "Sabtu" | "Minggu":
        print("Waktunya libur!")
    case "Senin":
        print("Mulai bekerja.")
    case _:
        print("Hari kerja biasa.")



