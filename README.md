# README.md
Aplikasi ini sudah di-*deploy* di Adaptable melalui link [berikut.](https://sentimental-sylladex.adaptable.app/main/)

* ## Cara Mengimplementasikan Checklist
Pada direktori lokal komputer saya, saya membuat folder baru bernama `sentimental_sylladex`. Di folder ini saya mengaktifkan *virtual environment*, memasang *dependencies*, dan kemudian membuat proyek Django dengan perintah `django-admin startproject sentimental_sylladex .` Saya kemudian membuat aplikasi `main` dan mendaftarkannya ke dalam proyek.

Dalam aplikasi `main` ini, saya membuat `main.html` yang sesuai dengan visi saya untuk Tugas 2 dan melengkapinya dengan *in-line* css untuk mengatur unsur estetikanya. Kemudian, saya menambahkan model ke dalam aplikasi ini dengan nama `Item` yang memiliki atribut `name`, `amount`, dan `description` sesuai ketentuan tugas.
    
Setelah melakukan migrasi untuk model ini, saya membuat sebuah fungsi pada `views.py` untuk `main.html` yang menampilkan nama aplikasi, nama saya, dan kelas saya. Terakhir, saya mengonfigurasi *routing* URL pada aplikasi `main` dan pada proyek sebelum akhirnya melakukan *deployment* untuk aplikasi ini pada Adaptable dan membuat `README.md` file untuk melengkapinya.

* ## Bagan
![Gambar bagan.](https://i.ibb.co/Yk3X6Bn/homestuck-reference.png "Inilah gambar bagan-nya.")

* ## Virtual Environment
1. __Mengapa kita menggunakan *virtual environment*?__ Adanya lingkungan virtual memungkinkan kita untuk memiliki beberapa versi `python` pada satu mesin yang memiliki *libraries* dan *dependencies* masing-masing sembari menjaganya agar tetap terpisah dari satu sama lain. Hal ini memungkinkan kita untuk mengerjakan banyak proyek Django dengan versi yang berbeda-beda tanpa munculnya *error* maupun *clashes*.

2. __Apakah tetap dapat membuat aplikasi web berbasis Django tanpa *virtual environment*?__ Walau sebenarnya bisa, pembuatan aplikasi web berbasis Django tanpa menggunakan *virtual environment* meningkatkan risiko *error* apabila kita mengerjakan banyak aplikasi web yang berbeda dalam waktu yang sama, sehingga hal ini dianggap *bad practice* dan tidak dianjurkan.

* ## MVC, MVT, dan MVVM
1. **MVC** adalah singkatan dari Model-View-Controller. Pada *design pattern* ini, Model mengatur data serta penyimpanannya, View menjadi bagian yang menampilkan informasi kepada user (*User Interface*), dan Controller menjadi bagian yang menghubungkan Model dan View serta menangani *request-request* dari user.

2. **MVT** adalah singkatan dari Model-View-Template. Pada *design pattern* ini, Model memiliki peran yang hampir sama dengan model dalam MVC, yaitu untuk mengelola data beserta penyimpanannya. Beda dengan peran View dalam MVC, View dalam MVT memiliki peran untuk menghubungkan antara Template dengan Model dan melakukan *render* untuk tampilan di-*request* oleh user. Template pada MVT terdiri dari file-file HTML yang mengatur layout dan tata letak web akhir yang akan ditampilkan ke user.

3. **MVVM** adalah singkatan dari Model-View-ViewModel. Pada *design pattern* ini, Model memiliki peran dalam mengatur data dan penyimpanannya seperti MVC dan MVT. View pada MVVM bertanggung jawab dalam menampilkan informasi yang di-*request* pengguna. ViewModel dalam MVVM berperan dalam memproses data dari Model agar sesuai dengan tampilan yang ditentukan oleh View. 

Dari ketiga *pattern* ini, perbedaan utamanya adalah komponen-komponen yang dimiliki setiap *design pattern* tersebut beserta relasi hubungan antara setiap komponen-komponennya.
