from abc import ABC, abstractmethod


# ABSTRACT CLASS
class Buah(ABC):
    jumlah_buah = 0

    def __init__(self, kode, nama, harga, stok):
        self.__kode = kode          # Private
        self._nama = nama           # Protected
        self._harga = harga         # Protected
        self._stok = stok           # Protected
        Buah.jumlah_buah += 1

    @property
    def kode(self):
        return self.__kode

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

    # Method konkret: dapat digunakan oleh semua subclass
    def tampilkan_ringkasan(self):
        print(f"{self._nama} | Harga: Rp{self._harga:,} | Stok: {self._stok} kg")

    # Abstract method 1
    @abstractmethod
    def tampilkan_data(self):
        pass

    # Abstract method 2
    @abstractmethod
    def tampilkan_asal(self):
        pass

    # Operator overloading: buah dibandingkan berdasarkan harga
    def __lt__(self, buah_lain):
        if not isinstance(buah_lain, Buah):
            return NotImplemented
        return self.harga < buah_lain.harga

    def __str__(self):
        return f"{self._nama} (Rp{self._harga:,}/kg)"


class BuahLokal(Buah):
    def __init__(self, kode, nama, harga, stok, asal_daerah):
        super().__init__(kode, nama, harga, stok)
        self.asal_daerah = asal_daerah

    def tampilkan_data(self):
        print(f"Kode: {self.kode} | Nama: {self._nama}")
        print(f"Harga: Rp{self.harga:,} | Stok: {self.stok} kg")
        print("Jenis: Buah Lokal")

    def tampilkan_asal(self):
        print(f"Asal daerah: {self.asal_daerah}")


class BuahImpor(Buah):
    def __init__(self, kode, nama, harga, stok, negara_asal):
        super().__init__(kode, nama, harga, stok)
        self.negara_asal = negara_asal

    def tampilkan_data(self):
        print(f"Kode: {self.kode} | Nama: {self._nama}")
        print(f"Harga: Rp{self.harga:,} | Stok: {self.stok} kg")
        print("Jenis: Buah Impor")

    def tampilkan_asal(self):
        print(f"Negara asal: {self.negara_asal}")


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

    def tampilkan_ringkasan(self):
        print(f"Pelanggan: {self.nama} | No. HP: {self.nomor_hp}")


class Transaksi:
    def __init__(self, pelanggan, buah, jumlah):
        self.pelanggan = pelanggan
        self.buah = buah
        self.jumlah = jumlah

    def hitung_total(self):
        return self.buah.harga * self.jumlah

    def tampilkan_transaksi(self):
        print(f"Pelanggan: {self.pelanggan.nama}")
        print(f"Buah: {self.buah._nama}")
        print(f"Jumlah: {self.jumlah} kg")
        print(f"Total: Rp{self.hitung_total():,}")


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
        return transaksi

    def tampilkan_buah(self):
        print("\\n=== DAFTAR BUAH ===")
        for buah in self.daftar_buah:
            buah.tampilkan_data()
            buah.tampilkan_asal()
            print("--------------------")

    def tampilkan_transaksi(self):
        print("\\n=== DAFTAR TRANSAKSI ===")
        for transaksi in self.daftar_transaksi:
            transaksi.tampilkan_transaksi()
            print("--------------------")

    def tampilkan_ringkasan(self):
        print(f"Toko: {self.nama_toko} | Jumlah jenis buah: {len(self.daftar_buah)}")


def cetak_ringkasan(objek):
    objek.tampilkan_ringkasan()


if __name__ == "__main__":
    print("========================================")
    print("     SISTEM MANAJEMEN TOKO BUAH")
    print("========================================")

    print("\\n=== BUKTI ABSTRACT CLASS ===")
    try:
        buah_abstrak = Buah("B00", "Contoh", 10000, 5)
    except TypeError as error:
        print("TypeError berhasil ditangkap:")
        print(error)

    buah1 = BuahLokal("B01", "Apel", 30000, 20, "Malang")
    buah2 = BuahLokal("B02", "Jeruk", 25000, 15, "Pontianak")
    buah3 = BuahImpor("B03", "Anggur", 80000, 10, "Australia")
    buah4 = BuahImpor("B04", "Apel Fuji", 60000, 12, "Jepang")

    pelanggan1 = Pelanggan("Andi", "081234567890")
    pelanggan2 = Pelanggan("Siti", "082345678901")

    toko = TokoBuah()
    for buah in [buah1, buah2, buah3, buah4]:
        toko.tambah_buah(buah)

    toko.tampilkan_buah()

    toko.buat_transaksi(pelanggan1, buah1, 2)
    toko.buat_transaksi(pelanggan2, buah3, 1)
    toko.tampilkan_transaksi()


    print("\\n=== POLIMORFISME VIA PEWARISAN ===")
    for buah in [buah1, buah3]:
        buah.tampilkan_data()

    print("\\n=== DUCK TYPING ===")
    cetak_ringkasan(pelanggan1)
    cetak_ringkasan(toko)

    print("\\n=== OPERATOR OVERLOADING ===")
    print(f"{buah2} lebih murah daripada {buah1}: {buah2 < buah1}")
