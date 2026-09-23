Deskripsi Program:
Sistem Manajemen Toko Buah program berbasis OOP dengan menggunakan Python. Program ini dibuat untuk membantu pengelolaan data buah, data pelanggan, serta transaksi pembelian di sebuah toko buah sederhana.

 Fitur Program
* Menampilkan data buah.
* Menampilkan data pelanggan.
* Melakukan transaksi pembelian buah.
* Menghitung total pembayaran beserta pajak.
* Mengubah data menggunakan setter dengan validasi.
* Melakukan validasi kode buah dan nama pelanggan menggunakan static method.

 Struktur Class

 1. Class `Buah`

Menyimpan informasi mengenai buah yang dijual.

Atribut
* `kode`
* `nama`
* `harga` (private)
* `stok` (private)

Method

* `tampilkan_data()`
* `ubah_nama_toko()` (class method)
* `kode_valid()` (static method)

 2. Class `Pelanggan`

Menyimpan informasi pelanggan.

Atribut
* `nama`
* `nomor_hp` (private)

Method
* `tampilkan_data()`
* `total_pelanggan()` (class method)
* `nama_valid()` (static method)

 3. Class `Transaksi`
Mengelola transaksi pembelian antara pelanggan dan buah.
Atribut
* `buah`
* `pelanggan`
* `jumlah` (private)

Method
* `hitung_total()`
* `cetak_struk()`
* `total_data_transaksi()` (class method)
* `hitung_diskon()` (static method)


Program memiliki tiga class utama yaitu `Buah`, `Pelanggan`, dan `Transaksi`. Setiap class dibuat menjadi beberapa objek pada bagian pengujian program.

 Encapsulation
Atribut penting seperti harga, stok, nomor HP, dan jumlah pembelian dibuat **private** sehingga hanya dapat diakses melalui getter dan setter.

 Property
Getter menggunakan `@property` dan setter menggunakan `@property.setter` dengan validasi agar data yang dimasukkan tetap benar.

 Class Method
Digunakan untuk mengubah atribut kelas dan menampilkan informasi yang dimiliki seluruh objek, seperti nama toko dan jumlah pelanggan.

 Static Method
Digunakan sebagai fungsi bantuan untuk melakukan validasi data dan perhitungan diskon tanpa bergantung pada objek tertentu.

