# Program Buku Telepon

class Kontak:
    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor

class BukuTelepon:
    def __init__(self):
        self.kontak_list = []

    def tambah_kontak(self, kontak):
        self.kontak_list.append(kontak)
        print("Kontak telah ditambahkan!")

    def cari_kontak(self, nama):
        for kontak in self.kontak_list:
            if kontak.nama.lower() == nama.lower():
                print("Nama: ", kontak.nama)
                print("Nomor: ", kontak.nomor)
                return
        print("Kontak tidak ditemukan!")

    def hapus_kontak(self, nama):
        for kontak in self.kontak_list:
            if kontak.nama.lower() == nama.lower():
                self.kontak_list.remove(kontak)
                print("Kontak telah dihapus!")
                return
        print("Kontak tidak ditemukan!")

    def tampilkan_kontak(self):
        if not self.kontak_list:
            print("Buku telepon kosong!")
        else:
            print("Daftar Kontak:")
            for kontak in self.kontak_list:
                print("Nama: ", kontak.nama)
                print("Nomor: ", kontak.nomor)

def main():
    buku_telepon = BukuTelepon()
    while True:
        print("\n=== Buku Telepon ===")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Hapus Kontak")
        print("4. Tampilkan Semua Kontak")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan Anda (1/2/3/4/5): ")
        if pilihan == "1":
            nama = input("Masukkan nama kontak: ")
            nomor = input("Masukkan nomor kontak: ")
            kontak = Kontak(nama, nomor)
            buku_telepon.tambah_kontak(kontak)
        elif pilihan == "2":
            nama = input("Masukkan nama kontak yang ingin dicari: ")
            buku_telepon.cari_kontak(nama)
        elif pilihan == "3":
            nama = input("Masukkan nama kontak yang ingin dihapus: ")
            buku_telepon.hapus_kontak(nama)
        elif pilihan == "4":
            buku_telepon.tampilkan_kontak()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == '__main__':
    main()


# Penjelasan program:

# Kelas Kontak digunakan untuk merepresentasikan satu kontak dalam buku telepon. Kontak memiliki atribut nama dan nomor.
# Kelas BukuTelepon digunakan untuk merepresentasikan keseluruhan buku telepon. Buku telepon memiliki atribut kontak_list yang berisi daftar kontak yang telah ditambahkan ke buku telepon.
# Fungsi tambah_kontak digunakan untuk menambahkan kontak baru ke daftar kontak di buku telepon.

# Fungsi cari_kontak digunakan untuk mencari kontak berdasarkan nama. Jika kontak ditemukan, maka nama dan nomornya akan ditampilkan. Jika tidak ditemukan, maka pesan "Kontak tidak ditemukan!" akan ditampilkan.
# Fungsi hapus_kontak digunakan untuk menghapus kontak dari daftar kontak di buku telepon berdasarkan nama. Jika kontak ditemukan dan berhasil dihapus, maka pesan "Kontak telah dihapus!" akan ditampilkan. Jika tidak ditemukan, maka pesan "Kontak tidak ditemukan!" akan ditampilkan.
# Fungsi tampilkan_kontak digunakan untuk menampilkan semua kontak yang telah ditambahkan ke daftar kontak di buku telepon. Jika daftar kontak kosong, maka pesan "Buku telepon kosong!" akan ditampilkan.
# Fungsi main adalah fungsi utama yang digunakan untuk menjalankan program. Di dalam fungsi main, akan ditampilkan menu pilihan untuk user. User dapat memilih untuk menambahkan kontak, mencari kontak, menghapus kontak, menampilkan semua kontak, atau keluar dari program. Setiap pilihan akan memanggil fungsi yang sesuai di dalam kelas BukuTelepon.
# Program dijalankan dengan memanggil fungsi main pada bagian akhir program.
# Program di atas menggabungkan konsep Python Primer (menggunakan input dan output pada console), OOP (menggunakan kelas dan objek), Array Based Sequence (menggunakan list untuk menyimpan daftar kontak), dan rekursif (tidak digunakan dalam program ini). Program dapat digunakan untuk membuat buku telepon sederhana yang dapat menambahkan, mencari, dan menghapus kontak.