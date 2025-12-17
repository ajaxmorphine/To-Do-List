#To-Do-List by Ghithrif Asyraf
from datetime import datetime
import os
    
def create(data):
    while True: 
        os.system('cls')
        try:
            tugas = str(input("Masukkan tugas yang ingin ditambahkan: "))
            tanggal = str(input("Masukkan tanggal tugas (format DD-MM-YYYY): "))
            waktu = str(input("Masukkan waktu saat ini dengan format (Pagi/Siang/Sore/Malam): ")).capitalize()
            if tugas == "" and tanggal == "" and waktu == "":
                raise ValueError("Bagian tidak boleh dikosongkan.")
            try:
                datetime.strptime(tanggal, '%d-%m-%Y')
            except ValueError:
                raise ValueError("Format tanggal tidak valid. Gunakan format DD-MM-YYYY.")
            waktu_valid = ["Pagi", "Siang", "Sore", "Malam" ]
            if waktu not in waktu_valid:
                raise ValueError(f"\nWaktu harus salah satu dari: {', '.join(waktu_valid)}.")
        except ValueError as e:
            os.system('cls')
            print(f"{e}\nHarap dicoba lagi!!!")
            input("Tekan ENTER untuk mencoba kembali...")
            tugas, tanggal, waktu = "", "", ""
        else:
            data.append([tugas, tanggal, waktu])
            os.system('cls')
            print(f"\n✅ Tugas {tugas} berhasil ditambahkan.")
            while True:
                answer_continue = str(input("\nApakah Anda ingin menambahkan tugas lagi? (y/n): ")).lower()
                if answer_continue == "y":
                    os.system('cls')
                    break
                elif answer_continue == "n":
                    input("\nTekan ENTER untuk kembali ke Menu Utama...")
                    os.system('cls')
                    return data
                else:
                    print("\nInput tidak valid, masukkan 'y' atau 'n'.")
                    os.system('cls')
                    
def read(data):
    if not data:
        print("Tidak ada tugas dalam To-Do List. Lakukan input tugas terlebih dahulu!")
        return False
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            tgl_j = datetime.strptime(data[j][1], "%d-%m-%Y")
            tgl_next = datetime.strptime(data[j+1][1], "%d-%m-%Y")
            if tgl_j > tgl_next:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
    print(f"\n📋 {nama_user} To-Do List:\n")
    for i in range(len(data)):
        tugas = data[i][0]
        tanggal = data[i][1]
        waktu = data[i][2]
        print(f"{i+1}. Tugas: {tugas}, Tanggal: {tanggal}, Waktu: {waktu}")

def update(data):
    if not data:
        print("\nTidak ada tugas dalam To-Do List untuk diedit. Lakukan input tugas terlebih dahulu!")
        input("\nTekan ENTER untuk kembali ke Menu Utama...")
        return data
    while True:
        os.system('cls')
        read(data)
        try:
            index = int(input("\nMasukkan nomor tugas yang ingin diedit: ")) - 1
            if index < 0 or index >= len(data):
                raise IndexError
        except:
            os.system('cls')
            print("Nomor tugas tidak valid. Silakan coba lagi.")
            input("Tekan ENTER untuk kembali...")
            continue
        tugas, tanggal, waktu = data[index]
        os.system('cls')
        print(f"\nTugas yang dipilih:\n")
        print(f"Tugas: {tugas}, Tanggal: {tanggal}, Waktu: {waktu}\n")
        tugas_baru   = input("Masukkan tugas baru (kosong = tidak mengubah): ")
        tanggal_baru = input("Masukkan tanggal baru (DD-MM-YYYY) (kosong = tidak mengubah): ")
        waktu_baru   = input("Masukkan waktu baru (Pagi/Siang/Sore/Malam) (kosong = tidak mengubah): ").capitalize()
        if tanggal_baru:
            try:
                datetime.strptime(tanggal_baru, "%d-%m-%Y")
            except:
                os.system('cls')
                print("Format tanggal tidak valid.")
                input("Tekan ENTER untuk kembali...")
                continue
        waktu_valid = ["Pagi", "Siang", "Sore", "Malam"]
        if waktu_baru and waktu_baru not in waktu_valid:
            os.system('cls')
            print("Waktu tidak valid.")
            input("Tekan ENTER untuk kembali...")
            continue
        data[index][0] = tugas_baru if tugas_baru else tugas
        data[index][1] = tanggal_baru if tanggal_baru else tanggal
        data[index][2] = waktu_baru if waktu_baru else waktu
        os.system('cls')
        print("\n✅ Tugas berhasil diperbarui!")
        input("\nTekan ENTER untuk kembali ke Menu Utama...")
        return data

def delete(data):
    while True:
        try:
            if not data:
                print("\nTidak ada tugas dalam To-Do List untuk dihapus.")
                input("\nTekan ENTER untuk kembali ke Menu Utama...")
                return data
            os.system('cls')
            read(data)
            pilihan = int(input("\nMasukkan nomor tugas yang ingin dihapus: ")) - 1
            if pilihan < 0 or pilihan >= len(data):
                raise IndexError("Nomor tugas tidak valid.")
        except ValueError:
            os.system('cls')
            print("Input harus berupa angka.")
            input("Tekan ENTER untuk mencoba kembali...")
        except IndexError as e:
            os.system('cls')
            print(f"{e}\nHarap dicoba lagi!!!")
            input("Tekan ENTER untuk mencoba kembali...")
        else:
            nama_tugas = data[pilihan][0]
            del data[pilihan]
            os.system('cls')
            print(f"\n✅ Tugas '{nama_tugas}' berhasil dihapus.")
            input("\nTekan ENTER untuk kembali ke Menu Utama...")
            return data

def cari_tanggal(data):
    if not data:
        print("\nTidak ada tugas untuk dicari.")
        input("Tekan ENTER untuk kembali...")
        return data
    tanggal = input("Masukkan tanggal (DD-MM-YYYY): ")
    try:
        datetime.strptime(tanggal, "%d-%m-%Y")
        hasil = [item for item in data if item[1] == tanggal]
        os.system('cls')
        print(f"\n📋 {nama_user} To-Do List pada tanggal {tanggal}:\n")
        if hasil:
            for i in range(len(hasil)):
                item = hasil[i]
                tugas = item[0]
                waktu = item[2]
            print(f"{i+1}. Tugas: {tugas}, Waktu: {waktu}")
        else:
            print("\nTidak ada tugas ditemukan.")
        input("\nTekan ENTER untuk kembali...")
    except:
        print("\nFormat tanggal tidak valid.")
        input("Tekan ENTER untuk kembali...")
    return data

def input_nama(nama_user = ""):
    os.system('cls')
    print("Hello World!")
    nama_user = str(input("\nMasukkan nama Anda: "))
    if nama_user == "":
        nama_user = "User"
    return nama_user

def ToDoListMenu():
    os.system('cls')
    print("======= To-Do-List Program📝 ==============")
    print(f"\nHalo, {nama_user}✨")
    print("\n1. Tambah Tugas          5. Cari Tugas ")
    print("2. Lihat Tugas           6. Ganti Nama User")
    print("3. Perbarui Tugas        7. Keluar")
    print("4. Hapus Tugas")
    try:
        pilihan = int(input("\nMasukkan pilihan (1 - 7): "))
        if pilihan < 1 or pilihan > 7:
            print("\nPilihan hanya antara 1 sampai 7.")
            input("\nTekan ENTER untuk mencoba kembali...")
            return 0
        else:
            return pilihan
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
        input("\nTekan ENTER untuk mencoba kembali...")
        
data = []
pilihan = 0
nama_user = input_nama()
os.system('cls')
while (pilihan != 7):
    pilihan = ToDoListMenu()
    if (pilihan == 1):
        os.system('cls')
        data = create(data)
    elif (pilihan == 2):
        os.system('cls')
        read(data)
        input("\nTekan ENTER untuk kembali ke Menu Utama...")
    elif (pilihan == 3):
        os.system('cls')
        data = update(data)
    elif (pilihan == 4):
        os.system('cls')
        data = delete(data)
    elif (pilihan == 5):
        os.system('cls')
        data = cari_tanggal(data)
    elif (pilihan == 6):
        os.system('cls')
        nama_user = input_nama()
print(f"Terimakasih telah menggunakan To-Do List Program📝, {nama_user}. Sampai jumpa lagi!")
input("\nTekan ENTER untuk keluar...")
os.system('cls')