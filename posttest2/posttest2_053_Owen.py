# Tema: Sistem Manajemen Toko Buah
class Buah:
    jumlah_buah = 0

    def __init__(self, kode, nama, harga, stok):
        self.__kode = kode
        self._nama = nama
        self._harga = harga
        self._stok = stok

        Buah.jumlah_buah += 1

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        if nilai > 0:
            self._harga = nilai
        else:
            print("Harga tidak boleh nol atau negatif!")

    @property
    def stok(self):
        return self._stok

    @stok.setter
    def stok(self, jumlah):
        if jumlah >= 0:
            self._stok = jumlah
        else:
            print("Stok tidak boleh negatif!")

    def tampilkan_data(self):
        print("Kode  :", self.__kode)
        print("Nama  :", self._nama)
        print("Harga :", f"Rp{self._harga:,}")
        print("Stok  :", self._stok, "kg")

class BuahLokal(Buah):
    def __init__(self, kode, nama, harga, stok, asal_daerah):
        super().__init__(kode, nama, harga, stok)

        self.asal_daerah = asal_daerah

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jenis : Buah Lokal")
        print("Asal  :", self.asal_daerah)


class BuahImpor(Buah):

    def __init__(self, kode, nama, harga, stok, negara_asal):
        super().__init__(kode, nama, harga, stok)

        self.negara_asal = negara_asal

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jenis : Buah Impor")
        print("Negara:", self.negara_asal)

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
        print("Nama :", self.nama)
        print("No HP:", self.nomor_hp)


class Transaksi:
    def __init__(self, pelanggan, buah, jumlah):
        self.pelanggan = pelanggan
        self.buah = buah
        self.jumlah = jumlah

    def hitung_total(self):
        return self.buah.harga * self.jumlah

    def tampilkan_transaksi(self):
        print("Pelanggan :", self.pelanggan.nama)
        print("Buah      :", self.buah._nama)
        print("Jumlah    :", self.jumlah, "kg")
        print("Total     :", f"Rp{self.hitung_total():,}")

class TokoBuah:

    nama_toko = "Fresh Fruit Market"

    def __init__(self):

        self.daftar_buah = []
        self.daftar_transaksi = []

    def tambah_buah(self, buah):
        self.daftar_buah.append(buah)

    def buat_transaksi(self, pelanggan, buah, jumlah):
        transaksi = Transaksi(pelanggan, buah, jumlah)
        self.daftar_transaksi.append(transaksi)

    def tampilkan_buah(self):
        print("\n=== DAFTAR BUAH ===")

        for buah in self.daftar_buah:
            buah.tampilkan_data()
            print("--------------------")

    def tampilkan_transaksi(self):
        print("\n=== DAFTAR TRANSAKSI ===")

        for transaksi in self.daftar_transaksi:
            transaksi.tampilkan_transaksi()
            print("--------------------")


print("========================================")
print("   SISTEM MANAJEMEN TOKO BUAH")
print("========================================")

buah1 = BuahLokal(
    "B01",
    "Apel",
    30000,
    20,
    "Malang"
)

buah2 = BuahLokal(
    "B02",
    "Jeruk",
    25000,
    15,
    "Pontianak"
)

buah3 = BuahImpor(
    "B03",
    "Anggur",
    80000,
    10,
    "Australia"
)

buah4 = BuahImpor(
    "B04",
    "Apel Fuji",
    60000,
    12,
    "Jepang"
)

pelanggan1 = Pelanggan(
    "Andi",
    "081234567890"
)

pelanggan2 = Pelanggan(
    "Siti",
    "082345678901"
)

toko = TokoBuah()

toko.tambah_buah(buah1)
toko.tambah_buah(buah2)
toko.tambah_buah(buah3)
toko.tambah_buah(buah4)

toko.tampilkan_buah()


toko.buat_transaksi(
    pelanggan1,
    buah1,
    2
)

toko.buat_transaksi(
    pelanggan2,
    buah3,
    1
)

toko.tampilkan_transaksi()
print("\n=== PENGUJIAN INHERITANCE ===")
print("\nData Buah Lokal:")
buah1.tampilkan_data()
print("\nData Buah Impor:")
buah3.tampilkan_data()

print("\n=== AKSES ATRIBUT PROTECTED ===")
print("Nama buah :", buah1._nama)
print("Harga buah:", buah1._harga)
print("Stok buah :", buah1._stok)