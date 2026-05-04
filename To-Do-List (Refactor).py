# To-Do-List by Ghithrif Asyraf
# Refactored for Clean Code and Readability by Gemini

from datetime import datetime
import os

WAKTU_VALID = ["Pagi", "Siang", "Sore", "Malam"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_date(prompt):
    while True:
        tanggal_str = input(prompt)
        if not tanggal_str:
            return None
        try:
            return datetime.strptime(tanggal_str, '%d-%m-%Y')
        except ValueError:
            print("❌ Format tanggal tidak valid. Gunakan format DD-MM-YYYY.")

def get_valid_waktu(prompt):
    while True:
        waktu = input(prompt).capitalize()
        if not waktu:
            return None
        if waktu in WAKTU_VALID:
            return waktu
        print(f"❌ Waktu tidak valid. Pilih: {', '.join(WAKTU_VALID)}")

def sort_data(data):
    """Mengurutkan data berdasarkan tanggal menggunakan Bubble Sort."""
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            tgl_j = datetime.strptime(data[j][1], "%d-%m-%Y")
            tgl_next = datetime.strptime(data[j+1][1], "%d-%m-%Y")
            if tgl_j > tgl_next:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def create(data):
    while True:
        clear_screen()
        print("--- Tambah Tugas Baru ---")
        tugas = input("Masukkan tugas: ")
        if not tugas:
            print("❌ Tugas tidak boleh kosong.")
            input("Tekan ENTER untuk coba lagi...")
            continue
            
        tanggal = get_valid_date("Masukkan tanggal (DD-MM-YYYY): ")
        waktu = get_valid_waktu("Masukkan waktu (Pagi/Siang/Sore/Malam): ")
        
        data.append([tugas, tanggal.strftime('%d-%m-%Y'), waktu])
        print(f"\n✅ Tugas '{tugas}' berhasil ditambahkan.")
        
        pilihan = input("\nTambah lagi? (y/n): ").lower()
        if pilihan != 'y':
            break
    return data

def read(data, nama_user, show_header=True):
    if not data:
        print("\n📭 To-Do List masih kosong.")
        return False
    
    sort_data(data)
    if show_header:
        print(f"\n📋 {nama_user}'s To-Do List:")
        print("-" * 30)
        
    for i, (tugas, tgl, wkt) in enumerate(data, 1):
        print(f"{i}. [{tgl}] {tugas} ({wkt})")
    return True

def update(data):
    clear_screen()
    if not read(data, "", show_header=False):
        input("\nTekan ENTER untuk kembali...")
        return data

    try:
        idx = int(input("\nNomor tugas yang ingin diedit: ")) - 1
        if 0 <= idx < len(data):
            print("\n*Kosongkan jika tidak ingin mengubah*")
            tugas_baru = input(f"Tugas baru ({data[idx][0]}): ")
            tgl_baru = get_valid_date(f"Tanggal baru ({data[idx][1]}): ")
            wkt_baru = get_valid_waktu(f"Waktu baru ({data[idx][2]}): ")

            if tugas_baru: data[idx][0] = tugas_baru
            if tgl_baru:   data[idx][1] = tgl_baru.strftime('%d-%m-%Y')
            if wkt_baru:   data[idx][2] = wkt_baru
            
            print("\n✅ Tugas diperbarui!")
        else:
            print("❌ Nomor tidak ditemukan.")
    except ValueError:
        print("❌ Input harus angka.")
    
    input("\nTekan ENTER...")
    return data

def delete(data):
    clear_screen()
    if not read(data, "", show_header=False):
        input("\nTekan ENTER...")
        return data

    try:
        idx = int(input("\nNomor tugas yang ingin dihapus: ")) - 1
        if 0 <= idx < len(data):
            removed = data.pop(idx)
            print(f"\n✅ Tugas '{removed[0]}' dihapus.")
        else:
            print("❌ Nomor tidak valid.")
    except ValueError:
        print("❌ Input harus angka.")
    
    input("\nTekan ENTER...")
    return data

def cari_tanggal(data):
    clear_screen()
    tgl_cari = get_valid_date("Masukkan tanggal yang dicari (DD-MM-YYYY): ")
    if tgl_cari:
        tgl_str = tgl_cari.strftime('%d-%m-%Y')
        hasil = [d for d in data if d[1] == tgl_str]
        
        print(f"\n🔍 Hasil untuk tanggal {tgl_str}:")
        if hasil:
            for i, (tugas, _, wkt) in enumerate(hasil, 1):
                print(f"{i}. {tugas} ({wkt})")
        else:
            print("Tidak ada tugas.")
    input("\nTekan ENTER...")
    return data

def main():
    data = []
    clear_screen()
    print("Welcome to To-Do-List Program")
    nama_user = input("Masukkan nama Anda: ") or "User"

    while True:
        clear_screen()
        print(f"======= To-Do-List Program 📝 =======")
        print(f"Halo, {nama_user} ✨\n")
        print("1. Tambah Tugas      5. Cari Tugas")
        print("2. Lihat Tugas       6. Ganti Nama")
        print("3. Perbarui Tugas    7. Keluar")
        print("4. Hapus Tugas")
        
        pilihan = input("\nMasukkan pilihan (1-7): ")

        if pilihan == '1': data = create(data)
        elif pilihan == '2': 
            clear_screen()
            read(data, nama_user)
            input("\nTekan ENTER untuk kembali...")
        elif pilihan == '3': data = update(data)
        elif pilihan == '4': data = delete(data)
        elif pilihan == '5': data = cari_tanggal(data)
        elif pilihan == '6': 
            nama_user = input("Masukkan nama baru: ") or nama_user
        elif pilihan == '7':
            print(f"\nTerima kasih {nama_user}, sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid.")
            input("Tekan ENTER...")

if __name__ == "__main__":
    main()