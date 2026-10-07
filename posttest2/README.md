# 🍎 Sistem Manajemen Toko Buah - Posttest 2

## Deskripsi

Program ini merupakan pengembangan dari **Posttest 1** dengan tema:

> **Sistem Manajemen Toko Buah**

Program dibuat menggunakan bahasa pemrograman **Python** dengan menerapkan konsep **Pemrograman Berorientasi Objek (PBO)**.

Pada Posttest 2, program dikembangkan dengan menambahkan:
- Relasi UML
  - Association
  - Aggregation
  - Composition
- Inheritance
- Superclass dan subclass
- `super().__init__()`
- Method overriding
- Protected attribute
- Private attribute

---

## Struktur Class

Program terdiri dari beberapa class:

1. `Buah` → Superclass
2. `BuahLokal` → Subclass dari `Buah`
3. `BuahImpor` → Subclass dari `Buah`
4. `Pelanggan`
5. `Transaksi`
6. `TokoBuah`

---

# 1. Relasi UML

## A. Association (Asosiasi)

Association adalah hubungan antara dua class yang saling berinteraksi tetapi tidak memiliki hubungan kepemilikan yang kuat.

Pada program ini, **Transaksi berasosiasi dengan Pelanggan dan Buah**.

Bagian kode:

```python
class Transaksi:

    def __init__(self, pelanggan, buah, jumlah):
        self.pelanggan = pelanggan
        self.buah = buah
        self.jumlah = jumlah
```

`Transaksi` menerima objek `pelanggan` dan `buah`.

Contoh penggunaannya:

```python
toko.buat_transaksi(
    pelanggan1,
    buah1,
    2
)
```

Artinya transaksi menggunakan objek `Pelanggan` dan objek `Buah`.

### Kesimpulan Association

```text
Pelanggan -------- Transaksi -------- Buah
```

Hubungan tersebut merupakan **Association** karena objek transaksi berinteraksi dengan pelanggan dan buah.

---

# 2. Aggregation (Agregasi)

Aggregation adalah hubungan "memiliki" antara suatu class dengan object lain, tetapi object yang dimiliki masih dapat berdiri sendiri.

Pada program ini, **TokoBuah memiliki daftar buah**.

Bagian kode:

```python
class TokoBuah:

    def __init__(self):
        self.daftar_buah = []
```

Kemudian buah ditambahkan menggunakan:

```python
def tambah_buah(self, buah):
    self.daftar_buah.append(buah)
```

Objek buah dibuat terlebih dahulu di luar class `TokoBuah`:

```python
buah1 = BuahLokal(
    "B01",
    "Apel",
    30000,
    20,
    "Malang"
)
```

Kemudian dimasukkan ke dalam toko:

```python
toko.tambah_buah(buah1)
```

Artinya objek buah dapat dibuat tanpa harus dibuat oleh `TokoBuah`.

### Kesimpulan Aggregation

```text
TokoBuah ◇-------- Buah
```

Simbol `◇` menunjukkan **Aggregation**.

---

# 3. Composition (Komposisi)

Composition adalah hubungan kepemilikan yang lebih kuat. Object bagian dibuat dan dikelola oleh object utama.

Pada program ini, **TokoBuah membuat dan menyimpan objek Transaksi**.

Bagian kode:

```python
class TokoBuah:

    def __init__(self):
        self.daftar_transaksi = []
```

Kemudian transaksi dibuat di dalam method `buat_transaksi()`:

```python
def buat_transaksi(self, pelanggan, buah, jumlah):
    transaksi = Transaksi(pelanggan, buah, jumlah)
    self.daftar_transaksi.append(transaksi)
```

Objek `Transaksi` dibuat oleh `TokoBuah` dan langsung dimasukkan ke dalam daftar transaksi milik toko.

### Kesimpulan Composition

```text
TokoBuah ◆-------- Transaksi
```

Simbol `◆` menunjukkan **Composition**.

---

# 4. Inheritance (Pewarisan)

Inheritance adalah konsep pewarisan sifat dan method dari superclass kepada subclass.

Pada program ini terdapat satu superclass dan dua subclass.

### Superclass

```python
class Buah:
```

### Subclass

```python
class BuahLokal(Buah):
```

dan

```python
class BuahImpor(Buah):
```

Struktur inheritance:

```text
              Buah
             /    \
            /      \
     BuahLokal   BuahImpor
```

`BuahLokal` dan `BuahImpor` mewarisi atribut dan method dari class `Buah`.

---

# 5. Penggunaan super().__init__()

Kedua subclass memanggil constructor dari superclass menggunakan:

```python
super().__init__(kode, nama, harga, stok)
```

Contoh:

```python
class BuahLokal(Buah):

    def __init__(self, kode, nama, harga, stok, asal_daerah):
        super().__init__(kode, nama, harga, stok)

        self.asal_daerah = asal_daerah
```

Pada `BuahImpor`:

```python
class BuahImpor(Buah):

    def __init__(self, kode, nama, harga, stok, negara_asal):
        super().__init__(kode, nama, harga, stok)

        self.negara_asal = negara_asal
```

Dengan `super().__init__()`, atribut dari superclass dapat digunakan oleh subclass.

---

# 6. Atribut Unik pada Subclass

Setiap subclass memiliki minimal satu atribut tambahan yang berbeda.

## BuahLokal

Memiliki atribut:

```python
self.asal_daerah = asal_daerah
```

Contohnya:

```text
Asal : Malang
```

## BuahImpor

Memiliki atribut:

```python
self.negara_asal = negara_asal
```

Contohnya:

```text
Negara : Australia
```

Jadi:

```text
BuahLokal → asal_daerah
BuahImpor → negara_asal
```

---

# 7. Method Overriding

Method overriding adalah ketika subclass memiliki method dengan nama yang sama dengan method superclass tetapi memberikan perilaku tambahan atau berbeda.

Pada superclass terdapat:

```python
def tampilkan_data(self):
    print("Kode  :", self.__kode)
    print("Nama  :", self._nama)
    print("Harga :", f"Rp{self._harga:,}")
    print("Stok  :", self._stok, "kg")
```

Method tersebut kemudian dioverride oleh `BuahLokal`:

```python
def tampilkan_data(self):
    super().tampilkan_data()
    print("Jenis : Buah Lokal")
    print("Asal  :", self.asal_daerah)
```

Dan oleh `BuahImpor`:

```python
def tampilkan_data(self):
    super().tampilkan_data()
    print("Jenis : Buah Impor")
    print("Negara:", self.negara_asal)
```

Dengan demikian, method `tampilkan_data()` memiliki perilaku tambahan sesuai jenis buah.

---

# 8. Protected Attribute

Protected attribute pada Python ditandai dengan satu underscore `_`.

Pada superclass `Buah` terdapat:

```python
self._nama = nama
self._harga = harga
self._stok = stok
```

Contohnya:

```python
self._nama
self._harga
self._stok
```

Atribut tersebut dapat digunakan oleh class turunan seperti `BuahLokal` dan `BuahImpor`.

Contoh akses:

```python
print("Nama buah :", buah1._nama)
print("Harga buah:", buah1._harga)
print("Stok buah :", buah1._stok)
```

---

# 9. Private Attribute

Private attribute ditandai dengan dua underscore `__`.

Pada class `Buah` terdapat:

```python
self.__kode = kode
```

Atribut `__kode` merupakan atribut private sehingga penggunaannya dibatasi pada class `Buah`.

Private attribute digunakan untuk menjaga data tertentu agar tidak diakses secara langsung dari luar class.

---

# 10. Contoh Objek yang Digunakan

Program membuat beberapa objek buah.

### Buah Lokal

```python
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
```

### Buah Impor

```python
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
```

### Pelanggan

```python
pelanggan1 = Pelanggan(
    "Andi",
    "081234567890"
)

pelanggan2 = Pelanggan(
    "Siti",
    "082345678901"
)
```

---

# 11. Pengujian Program

Program menguji beberapa fitur yang telah dibuat.

### Menampilkan buah

```python
toko.tampilkan_buah()
```

### Membuat transaksi

```python
toko.buat_transaksi(
    pelanggan1,
    buah1,
    2
)
```

### Menampilkan transaksi

```python
toko.tampilkan_transaksi()
```

### Pengujian inheritance

```python
buah1.tampilkan_data()
buah3.tampilkan_data()
```

### Pengujian protected attribute

```python
print("Nama buah :", buah1._nama)
print("Harga buah:", buah1._harga)
print("Stok buah :", buah1._stok)
```

---

# 12. Kesesuaian dengan Ketentuan Posttest 2

| Ketentuan | Implementasi |
|---|---|
| Association | `Transaksi` berhubungan dengan `Pelanggan` dan `Buah` |
| Aggregation | `TokoBuah` memiliki `daftar_buah` |
| Composition | `TokoBuah` membuat dan menyimpan `Transaksi` |
| 1 Superclass | `Buah` |
| 2 Subclass | `BuahLokal` dan `BuahImpor` |
| `super().__init__()` | Digunakan pada kedua subclass |
| Atribut unik subclass | `asal_daerah` dan `negara_asal` |
| Method overriding | `tampilkan_data()` |
| Protected attribute | `_nama`, `_harga`, `_stok` |
| Private attribute | `__kode` |

---

# 13. Kesimpulan

Program **Sistem Manajemen Toko Buah** telah dikembangkan dengan menerapkan konsep Pemrograman Berorientasi Objek.

Program telah memenuhi konsep yang diminta pada Posttest 2, yaitu:

- **Association**
- **Aggregation**
- **Composition**
- **Inheritance**
- **Superclass dan subclass**
- **`super().__init__()`**
- **Atribut unik pada subclass**
- **Method overriding**
- **Protected attribute**
- **Private attribute**

Dengan demikian, program telah dikembangkan dari Posttest 1 dengan menambahkan konsep **Relasi UML dan Inheritance** sesuai dengan ketentuan Posttest 2.
