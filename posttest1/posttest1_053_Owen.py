# Tema:Sistem Managemen Toko Buah
class Buah:
    nama_toko = "Fresh Fruit Market"
    satuan = "kg"
    pajak = 0.10

    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.__harga = harga
        self.__stok = stok

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai):
        if nilai > 0:
            self.__harga = nilai
        else:
            print("Harga tidak boleh nol atau negatif!")

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, jumlah):
        if jumlah >= 0:
            self.__stok = jumlah
        else:
            print("Stok tidak boleh negatif!")

    def tampilkan_data(self):
        print(f"[{self.kode}] {self.nama}")
        print(f"Harga : Rp{self.harga:,}/{Buah.satuan}")
        print(f"Stok  : {self.stok} {Buah.satuan}")

    @classmethod
    def ubah_nama_toko(cls, nama_baru):
        cls.nama_toko = nama_baru

    @staticmethod
    def kode_valid(kode):
        return kode.startswith("B")


class Pelanggan:
    jumlah_pelanggan = 0

    def __init__(self, nama, nomor_hp):
        self.nama = nama
        self.__nomor_hp = nomor_hp
        Pelanggan.jumlah_pelanggan += 1

    @property
    def nomor_hp(self):
        return self.__nomor_hp

    @nomor_hp.setter
    def nomor_hp(self, nomor):
        if nomor.isdigit() and len(nomor) >= 10:
            self.__nomor_hp = nomor
        else:
            print("Nomor HP tidak valid!")

    def tampilkan_data(self):
        print(f"Nama Pelanggan : {self.nama}")
        print(f"No HP          : {self.nomor_hp}")

    @classmethod
    def total_pelanggan(cls):
        print("Total pelanggan :", cls.jumlah_pelanggan)

    @staticmethod
    def nama_valid(nama):
        return nama.replace(" ", "").isalpha()

class Transaksi:
    total_transaksi = 0

    def __init__(self, buah, pelanggan, jumlah):
        self.buah = buah
        self.pelanggan = pelanggan
        self.__jumlah = jumlah
        Transaksi.total_transaksi += 1

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, nilai):
        if nilai > 0:
            self.__jumlah = nilai
        else:
            print("Jumlah beli harus lebih dari 0!")

    def hitung_total(self):
        total = self.buah.harga * self.jumlah
        total += total * Buah.pajak
        return total

    def cetak_struk(self):
        print("\n===== STRUK PEMBELIAN =====")
        print("Toko       :", Buah.nama_toko)
        print("Pelanggan  :", self.pelanggan.nama)
        print("Buah       :", self.buah.nama)
        print("Jumlah     :", self.jumlah, "kg")
        print("Total Bayar: Rp{:,.0f}".format(self.hitung_total()))

    @classmethod
    def total_data_transaksi(cls):
        print("Jumlah transaksi :", cls.total_transaksi)

    @staticmethod
    def hitung_diskon(total):
        if total >= 100000:
            return total * 0.05
        return 0


print("=== DATA BUAH ===")
buah1 = Buah("B01", "Apel", 30000, 20)
buah2 = Buah("B02", "Jeruk", 25000, 15)

buah1.tampilkan_data()
buah2.tampilkan_data()

print("\n=== DATA PELANGGAN ===")
pel1 = Pelanggan("Andi", "081234567890")
pel2 = Pelanggan("Siti", "082345678901")

pel1.tampilkan_data()
pel2.tampilkan_data()

print("\n=== TRANSAKSI ===")
trx1 = Transaksi(buah1, pel1, 2)
trx2 = Transaksi(buah2, pel2, 4)

trx1.cetak_struk()
trx2.cetak_struk()

print("\n=== CLASS METHOD ===")
Buah.ubah_nama_toko("Toko Buah Sejahtera")
print("Nama toko baru :", Buah.nama_toko)

Pelanggan.total_pelanggan()
Transaksi.total_data_transaksi()

print("\n=== STATIC METHOD ===")
print("Kode B01 valid :", Buah.kode_valid("B01"))
print("Kode X01 valid :", Buah.kode_valid("X01"))

print("Nama 'Andi' valid :", Pelanggan.nama_valid("Andi"))
print("Nama 'Andi123' valid :", Pelanggan.nama_valid("Andi123"))

diskon = Transaksi.hitung_diskon(trx2.hitung_total())
print("Diskon transaksi 2 : Rp{:,.0f}".format(diskon))

print("\n=== SETTER ===")
buah1.harga = 35000
buah1.stok = 25
pel1.nomor_hp = "08123456789"
trx1.jumlah = 3

buah1.tampilkan_data()
pel1.tampilkan_data()
trx1.cetak_struk()

print("\n=== SETTER TIDAK VALID ===")
buah1.harga = -1000
buah1.stok = -5
pel1.nomor_hp = "123ABC"
trx1.jumlah = 0