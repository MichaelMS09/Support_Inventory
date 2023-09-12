Nama        : Michael Marcellino Satyanegara

NPM         : 2206083325

Kelas       : PBP E

Adaptable   : [Support Inventory](https://support.adaptable.app/main/)

# Checklist Tugas

*Checklist* untuk tugas ini adalah sebagai berikut.

## A. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step*.
### 1. Membuat sebuah proyek Django baru.
1. Pastikan bahwa kita sudah *download* aplikasi Django terlebih dahulu. Kalian bisa melakukan *download* pada link berikut [Django](https://www.djangoproject.com/).
2. Buatlah direktori utama (folder utama) yang akan kita gunakan untuk membuat sebuah proyek Django baru.
3. Kita buka *command prompt* untuk Windows atau *terminal shell* untuk Unix pada direktori utama tersebut.
4. Pada *command prompt* atau *terminal shell*, buatlah *virtual environment* dengan menjalankan sebuah perintah.
    ```
    python -m venv env
    ```
    Penggunaan virtual enviroment ini bertujuan melakukan isolasi pada aplikasi yang dibuat agar tidak terjadi tabrakan/gangguan terhadap versi lain yang ada pada komputer kita.
5. Setelah kita buat *virtual environment*, sekarang kita aktifkan *virtual environment* tersebut dengan perintah.

    ```
    env\Scripts\activate.bat -> (Untuk Windows)

                        Atau
    
    source env/bin/activate -> (Untuk Mac/Linux)
    ```
    Kita dapat mengetahui *Virtual environment* aktif, saat baris input pada terminal kita ditandai dengan (env).
6. Buatlah *file* baru dengan nama `requirements.txt` pada direktori utama dan tambahkan beberapa *dependencies* ke dalam *file* tersebut.
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
7. Setelah membuat file, sekarang kita *install file* `requirements.txt` yang berisi beberapa *dependencies* dengan perintah.
    ```
    pip install -r requirements.txt
    ```
8. Setelah install berhasil, sekarang kita buat proyek Django baru dengan perintah.
    ```
    django-admin startproject {Nama App} .
    ```
    Keterangan : {Nama App} itu bebas sesuai dengan nama proyek Django yang kita inginkan.
9. Sekarang kita akan melakukan konfigurasi proyek dan menjalankan server. Yang perlu kita lakukan pertama adalah kita buka *file* dengan nama `setting.py` di dalam direktori proyek (direktori dengan nama app kita), lalu pada bagian `ALLOWED_HOSTS` kita tambahkan `*`.
    ```
    ...
    ALLOWED_HOSTS = ["*"]
    ...
    ```
    Hal ini bertujuan agar dengan menetapkan nilai ["*"], kita dapat mengizinkan akses ke semua *host*, sehingga aplikasi dapat diakses secara luas.
10. Setelah itu, kita kembali ke *command prompt* atau *terminal shell*, lalu kita jalankan server django dengan perintah.
    ```
    python manage.py runserver -> (Untuk Windows)

                Atau

    ./manage.py runserver -> (Untuk Unix)
    ```
11. Untuk melihat hasil proyek django yang berhasil kita buat, kita dapat melihatnya pada peramban web berikut [http://localhost:8000](http://localhost:8000).
12. Terakhir untuk mematikan server, kita dapat menekan `Ctrl + C` pada *command prompt* atau *terminal shell*. Setelah itu, kita dapat menonaktifkan *virtual environment* dengan perintah berikut.
    ```
    deactivate
    ```
### 2. Membuat aplikasi dengan nama `main` pada proyek tersebut.
1. Buka kembali *command prompt* atau *terminal shell* pada direktori utama proyek Django. Lalu aktifkan *virtual environment* tersebut dengan perintah.

    ```
    env\Scripts\activate.bat -> (Untuk Windows)

                        Atau
    
    source env/bin/activate -> (Untuk Mac/Linux)
    ```
2. Untuk membuat aplikasi baru dengan nama `main`. Kita perlu melakukan perintah berikut.
    ```
    python manage.py startapp main
    ```
    Setelah melakukan perintah, maka akan muncul direktori baru dengan nama `main` yang nanti akan berisi struktur awal untuk membuat aplikasi.
3. Agar `main` dapat dijalankan, kita perlu untuk mendaftarkan aplikasi `main` ke dalam proyek dengan perintah berikut.
    > Pada direktori proyek terdapat berkas dengan nama settings.py

    > Buka berkas tersebut, lalu pada bagian `INSTALLED_APPS`, kita tambahkan 'main' ke dalam daftar aplikasi.

    ```java
    INSTALLED_APPS = [
        ...,
        'main',
        ...
    ]
    ```
### 3. Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.
1. Untuk melakukan *routing*, yang pertama kita lakukan adalah membuat berkas baru dengan nama `urls.py` di dalam direktori `main`.
2. Isi berkas tersebut dengan kode berikut.
    ```java
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    Tujuan dari pembuatan berkas ini adalah untuk bertanggung jawab dalam mengatur rute URL yang terkait dengan aplikasi `main`.
### 4. Membuat model pada aplikasi `main` dengan nama Item dan memiliki atribut wajib sebagai berikut.
> `name` sebagai nama item dengan tipe CharField.

> `amount` sebagai jumlah item dengan tipe IntegerField.

> `description` sebagai deskripsi item dengan tipe TextField.

1. Untuk membuat model, yang pertama kita lakukan adalah membuka berkas `models.py` pada direktori aplikasi `main`.
2. Isi berkas tersebut dengan kode berikut.
    ```java
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        date = models.DateField(auto_now_add=True)
        amount = models.IntegerField()
        description = models.TextField()
    ```
    Penjelasan : `name`, `date`, `amount`, dan `description` adalah atribut atau *field* pada model. Setiap *field* memiliki tipe data yang sesuai seperti `CharField`, `DateField`, `IntegerField`, dan `TextField`.
3. Sebelum kita mengaplikasikan aplikasi kita, kita harus melakukan migrasi model terlebih dahulu. Migrasi ini adalah instruksi untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kodemu.
4. Untuk membuat migrasi model, buka kembali *command prompt* atau *terminal shell* pada direktori `main` dan jalankan perintah berikut.
    ```
    python manage.py makemigrations
    ```
    Tujuan perintah ini adalah menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data.
5. Setelah itu, untuk menerapkan migrasi ke dalam basis data lokal, kita perlu menjalankan perintah berikut.
    ```
    python manage.py migrate
    ```
### 5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Untuk membuat sebuah fungsi, yang pertama kita lakukan adalah membuka berkas `views.py` pada direktori aplikasi `main`.
2. Tambahkan kode berikut pada baris *import*.
    ```java
    from django.shortcuts import render
    ```
    Fungsi dari kode tersebut adalah untuk me-render tampilan HTML dengan menggunakan data yang diberikan.
3. Isi kembali berkas tersebut dengan fungsi `show_main` yang berisi kode berikut.

    ```java
    def show_main(request):
    context = {
        'app': '{Nama App kalian}',
        'name': '{Nama kalian}',
        'class': '{Kelas kalian}'
    }

    return render(request, "main.html", context)
    ```
    Pada bagian `main.html` itu merupakan berkas yang kita buat dalam direktori `templates` dan direktori tersebut berada di dalam direktori aplikasi `main` sebagai tempat untuk menampilkan tampilan HTML. **(Jadi jika berkas `main.html` ini belum dibuat, lebih baik dibuat terlebih dahulu)**.
4. Setelah itu, buka berkas `main.html` yang berada di dalam direktori `templates`.
5. Isi berkas tersebut dengan kode berikut.
    ```html
    ...
    <h5>App: </h5>
    <p>{{ app }}<p>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ...
    ```
    Penjelasan : Sintaks Django `{{ app }}`, `{{ name }}` dan `{{ class }}` merupakan tempat untuk menampilkan nilai yang telah didefinisikan dalam `context` yang ada pada berkas `views.py`.
### 6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Sama seperti poin pada nomor 3. Yang pertama kita lakukan untuk melakukan *routing* adalah membuat berkas baru dengan nama `urls.py` di dalam direktori `main`.
2. Isi berkas tersebut dengan kode berikut.
    ```java
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    Tujuan dari pembuatan berkas ini adalah untuk bertanggung jawab dalam mengatur rute URL yang terkait dengan aplikasi `main`.
    
    > Namun, karena tadi kita sudah melakukannya sekarang kita lanjutkan ke *step* berikutnya.
3. Sekarang kita akan menambahkan rute URL dalam `urls.py` proyek (Direktori proyek dengan nama app kita) untuk menghubungkannya ke tampilan `main`. Yang pertama kita lakukan adalah membuka berkas `urls.py` di dalam direktori proyek dengan nama app kita, bukan yang ada di dalam direktori aplikasi `main`.
4. Tambahkan kode berikut pada baris *import*.
    ```java
    ...
    from django.urls import path, include
    ...
    ```
    Penjelasan : Fungsi **include** digunakan untuk melakukan *import* rute URL dari aplikasi main ke dalam berkas `urls.py` proyek.
5. Isi kembali berkas tersebut dengan kode berikut pada bagian `urlpatterns`.
    ```java
    urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
    ]
    ```
    Penjelasan : Path URL `'main/'` akan diarahkan ke rute yang didefinisikan dalam berkas `urls.py` aplikasi `main`.
6. Setelah itu, kita dapat menjalankan aplikasi kita dengan menyalakan server Django dengan perintah berikut. (Jalankan pada *command prompt* atau *terminal shell*)
    ```
    python manage.py runserver
    ```
7. Untuk melihat hasil proyek django yang berhasil kita buat, kita dapat melihatnya pada peramban web berikut [http://localhost:8000](http://localhost:8000).
### 7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Buatlah akun [Adaptable.io](https://adaptable.io/) dengan menggunakan akun [GitHub](https://github.com/) yang digunakan sebagai tempat untuk menyimpan repositori proyek aplikasi Djago kalian.
2. Jika sudah membuat akun dan *login* pada Adaptable, tekan tombol `NEW APP`. Pilih `Connect an Existing Repository`.
3. Pilihlah repositori proyek aplikasi Djago kalian sebagai basis aplikasi yang akan di-*deploy*. Pilih *branch* yang ingin dijadikan sebagai *deployment branch*.
4. Sebagai *template deployment*, pilihlah `Python App Template`.
5. Selanjutnya sebagai tipe basis data yang akan digunakan, pilihlah `PostgreSQL`.
6. Lakukan penyesuaian *setting* versi Python yang kalian miliki. Untuk mengeceknya, nyalakan *virtual environment* dan jalankan perintah python --version. Lalu pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn {nama repositori kalian}.wsgi`.
7. Setelah itu, masukkan nama aplikasi yang kalian buat dan nama ini akan menjadi *domain* situs web aplikasi kalian.
8. Terakhir, centang bagian `HTTP Listener on PORT` dan lakukan `Deploy App` untuk memulai proses *deployment* aplikasi kalian. Tunggu sampai semua *`Deployment Status`* berwarna hijau yang menandakan keberhasilan pembuatan aplikasi kalian pada Adapatable.

## B. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Alt text](DjangoWorkFlow.png)

### PENJELASAN
1. *Workflow* dimulai dari *user* yang meminta *request* kepada Django. Django akan menerima request tersebut dengan menggunakan URL (`url.py`). 

2. Setelah itu, URL akan memanggil VIEWS (`views.py`) yang akan mengatur berbagai macam bentuk interaksi seperti meminta, mengelola dan menyajikan data yang nanti akan diolah oleh MODELS (`model.py`) yang dilanjutkan ke dalam *APP Database*. Data yang didapatkan dari MODELS tersebut akan dikirim oleh VIEWS ke TEMPLATE (`main.html`) dan akan ditampilkan dalam bentuk berkas HTML.

3. Pada berkas HTML, berisi berbagai macam kode html seperti kode untuk membuat list, tabel, menentukan warna font, mangatur format penulisan, menentukan ukuran font dan masih banyak lagi. Selain itu, pada berkas HTML juga mengandung *tag template* Django agar dapat memasukan data yang ada pada berkas `views.py` ke dalam berkas `main.html`. 

4. Setelah semua selesai diolah, data tersebut akan ditampilkan dalam bentuk *rendered web page* kepada *user*.

## C. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
1. Tujuan kita menggunakan *virtual enviroment* :

> Menciptakan tempat khusus agar proyek perangkat lunak yang kita kerjakan dapat bekerja dengan lebih teratur dan lebih aman. 

> Mengisolasi proyek-proyek lain sehingga tidak ada konflik dalam melakukan pekerjaan. Hal ini bertujuan karena terkadang untuk setiap proyek yang kita kerjakan memerlukan spesifikasi atau versi yang berbeda dari spesifikasi utama perangkat kita.

> Dapat melakukan *install* untuk paket-paket Python yang diperlukan dalam proyek tanpa merusak instalasi Python *Global* pada perangkat kita. Selain itu, kita juga dapat menghapus paket tersebut dengan bebas selama berada dalam *virtual enviroment* tanpa memperhatikan dampak pada sistem operasi utama perangkat kita.

2. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*. Namun, hal ini sangatlah tidak direkomendasikan karena jika kita melakukan *install* Django ke lingkungan *default/global* maka kita hanya akan dapat menargetkan satu versi Django di perangkat kita dan hal ini bisa menjadi masalah jika kita ingin membuat situs web baru yang menggunakan versi Django terbaru sambil mempertahankan situs web yang bergantung pada versi Django yang lama.

    Oleh karena itu, kita disarankan untuk menggunakan *virtual environment* dalam membuat aplikasi web berbasis Django agar kita dapat menggunakan berbagai versi Django dalam perangkat kita untuk menciptakan berbagai jenis proyek baru berbasis Django. Selain itu, agar menambah keamanan dalam membuat proyek tanpa perlu memperhatikan dampak pada sistem operasi utama pada perangkat kita.

## D. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah sebuah pola arsitektur dalam membuat sebuah aplikasi dengan cara memisahkan kode menjadi tiga bagian yang akan digunakan dalam pengembangan perangkat lunak (membuat aplikasi berbasis web). Tujuan utama dari memisahkan kode menjadi tiga bagian ini adalah untuk mempermudah proses pengembangan, perawatan, dan pengelolaan kode yang lebih terstruktur dan rapi.

### Perbedaaan
1. MVC (Model-View-Controller):

    Memisahkan kode menjadi 3 bagian yaitu:

* Model

    Bertugas dalam menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.

* View

    Bertugas dalam menampilkan informasi dalam bentuk *Graphical User Interface* (GUI).

* Controller

    Bertugas dalam menghubungkan serta mengatur *model* dan *view* agar dapat saling terhubung. *Controller* akan mengambil data hasil pengolahan model dan mengaturnya di bagian view untuk ditampilkan kepada pengguna.

2. MVT (Model-View-Template):

    Memiliki konsep yang sama seperti MVC, MVT memiliki *Model* dan *View* yang bertugas dalam menyiapkan dan menampilkan informasi. Namun, dalam MVT terdapat komponen *Template* yang bertugas dalam mengatur data agar dapat ditampilkan dalam HTML. Konsep ini juga bekerja khusus dalam kerangka kerja web Django untuk pengembangan aplikasi web berbasis Python.

3. MVVM (Model-View-ViewModel):

    Memisahkan kode menjadi 3 bagian yaitu:

* Model

    Bertugas dalam merepresentasikan data yang akan digunakan pada logika bisnis. Umumnya kelas-kelas yang ada di dalamnya berupa **POJO** atau **Plain Old Java Object** dan **Data Classes** jika kita menggunakan Kotlin.

* View

    *Layer* yang berisi UI dari aplikasi untuk mengatur bagaimana informasi akan ditampilkan. *Layer* ini akan berisi kelas-kelas, seperti *Activity* dan *Fragment*.

* ViewModel

    Bertugas untuk berinteraksi dengan ***model*** di mana data yang ada akan diteruskan ke *layer **view***.