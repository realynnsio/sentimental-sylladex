# README.md
**REV: 20 Sep 2023. Jawaban Tugas 3 ditambahkan.**

**REV: 27 Sep 2023. Jawaban Tugas 4 ditambahkan.**

Aplikasi ini pernah di-*deploy* di Adaptable melalui link [berikut.](https://sentimental-sylladex.adaptable.app/main/)

## TUGAS 4

### 1.
Django UserCreationForm adalah modul bawaan dari Django yang digunakan untuk membuat user baru yang dapat menggunakan aplikasi web yang sedang dikembangkan. UserCreationForm memiliki tiga bidang: nama pengguna, password1, dan password2 (yang digunakan untuk mengonfirmasi password1). Untuk menggunakan UserCreationForm, kita perlu mengimpornya terlebih dahulu dari django. contrib. auth.

#### PROS:
* **Mempercepat Waktu Development.** Penggunaan UserCreationForm dari Django yang dapat langsung menangani registrasi user mengurangi beban dari developer untuk membuat formulir registrasi kustom dari awal.
* **Validasi otomatis.** UserCreationForm memiliki sistem validasinya sendiri untuk username dan password agar aman dan sesuai ketentuan. Developer tidak perlu mengimplementasikan validasi lagi.
* **Integrasi yang lebih mudah.** Karena UserCreationForm ini adalah modul dari Django, ia sangat kompatibel dengan sistem authentication bawaan Django. 
* **Security.** Penggunaan UserCreationForm menambahkan layer keamanan yang baik dengan melakukan hashing terhadap kata sandi user.

#### CONS:
* **Customization terbatas.** Walau developer dapat menambahkan bidang tambahan dalam UserCreationForm, bila ada terlalu banyak perubahan yang ingin dilakukan, akan lebih baik untuk membuat formulir pendaftaran custom saja.
* **Tampilan terbatas.** Tampilan HTML dari UserCreationForm mungkin tidak sesuai dengan desain dari aplikasi. Bila seperti ini, developer harus mengeluarkan upaya tambahan untuk menyesuaikan penampilan FrontEnd-nya.
* **Validasi yang Dibatasi.** Ketentuan username dan password & validasi yang diterapkan oleh UserCreationForm mungkin terlalu membatasi bagi aplikasi yang ingin dikembangkan. 
* **Dependencies.** Bila menggunakan UserCreationForm, pembuatan user akan menggunakan sistem authentication Django. Bila ingin menggunakan sistem authentication lain, ada banyak kerjaan tambahan yang harus dilakukan oleh developer.

*(Source: https://www.javatpoint.com/django-usercreationform)*

### 2.
Dalam Django, autentikasi memverifikasi bahwa seorang user benar merupakan user tersebut sedangkan otorisasi menentukan apa yang boleh dilakukan oleh user yang telah diautentikasi.

Kedua hal ini penting untuk keamanan dan perlindungan data. Autentikasi dan otorisasi dalam Django memverifikasi identitas pengguna sehingga tidak sembarang orang dapat mengakses aplikasi, serta mencegah pengguna dalam mengakses atau mengubah data yang seharusnya tidak dapat mereka akses.

*(Source: https://docs.djangoproject.com/en/4.2/topics/auth/)*

### 3.
Cookie dalam konteks aplikasi web adalah sepotong data dari website yang disimpan dalam web browser. Cookies ini dapat diakses kembali oleh website yang menyimpannya di kemudian hari. Ia digunakan untuk memberitahu server bahwa seorang user telah kembali ke website & memberikan informasi kepada website tersebut untuk menampilkan pengaturan dan konten yang sesuai dengan kunjungan-kunjungan user sebelumnya.

Django menyediakan session framework yang dapat menyimpan dan mengambil data berdasarkan setiap pengunjung situs. Django mengabstraksi proses pengiriman & penerimaan cookie dengan menempatkan session ID cookie di sisi klien namun menyimpan semua data terkait di sisi server. Hal ini membuat datanya sendiri tidak disimpan di sisi klien, membuatnya lebih baik dalam konteks keamanan.

*(Source: https://www.trendmicro.com/vinfo/us/security/definition/cookies, https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions)*

### 4.
Penggunaan cookies dalam pengembangan web biasanya aman, namun ada juga risiko yang perlu diwaspadai. Cookies dapat mengungkapkan informasi pribadi dari seorang user, seperti riwayat penelusuran ataupun lokasi mereka. Dalam situs-situs yang tidak terenkripsi, hal ini dapat membahayakan user karena peretas akan dapat menyadap dan memanipulasi data ini dalam waktu-waktu tertentu (ex. saat user menggunakan wifi publik). Selain itu, cookies mungkin tidak berfungsi dengan baik di platform-platform yang berbeda karena ukuran dan formatnya yang bervariasi. Cookies juga dapat meningkatkan jumlah data yang ditransfer antara server dan browser, sehingga menghabiskan lebih banyak bandwidth dan sumber daya.

*(Source: https://www.linkedin.com/advice/0/how-do-cookies-affect-web-performance-seo-skills-web-applications)*

### 5.
Pertama, untuk mengimplementasikan sistem registrasi saya menambahkan dulu fungsi `register()` pada file `views.py` yang ada pada `main`. Fungsi ini akan dipanggil saat user ingin meregistrasi diri melalui page `register.html` dan menghandlenya dengan `UserCreationForm`. Setelah membuat membuat metode untuk registrasi pada `views.py`, saya membuat page `register.html` pada `main/templates/` agar fungsi tersebut dapat diakses. Setelah dua hal ini selesai, saya menambahkan fungsi `register()` ke dalam berkas `urls.py` dan `path('register/', register, name='register')` ke dalam `urlpattern`s-nya.

Untuk mekanisme login, saya kurang lebih melakukan hal yang sama: membuat fungsi `login_user()` pada `views.py` (yang menggunakan `authenticate` dari `django.contrib.auth`) kemudian membuat page `login.html` pada `main/templates/` agar fungsi tersebut dapat diakses. Saya menambahkan `login_user()` ke dalam `urls.py` dan `path('login/', login_user, name='login')` ke dalam `urlpatterns`-nya juga.

Beda dengan fungsi register dan fungsi login, setelah fungsi `logout_user()` saya buat pada `views.py`, saya tidak membuat page HTML spesifik untuk pengaksesannya. Saya hanya menambahkan button logout pada `main.html`. Saya juga menambahkan `logout_user()` ke berkas `urls.py` dan `urlpatterns` agar ia bisa digunakan.

Agar user diwajibkan untuk login terlebih dahulu sebelum melihat page `main.html`, saya menambahkan line `@login_required(login_url='/login')` di atas fungsi `show_main()`.

Setelah mengimplementasikan ketiga hal ini, saya mencoba membuat akun dulu di server lokal untuk mengecek bahwa semuanya telah terimplementasi dengan baik.

Step selanjutnya yang saya lakukan adalah mengimplementasikan cookies terlebih dahulu. Saya melakukan hal ini dengan mengimport beberapa modul pada `views.py` seperti `datetime`, `HttpResponseRedirect`, dan `reverse`, kemudian mengatur ulang beberapa fungsi yang sudah saya buat sebelumnya. Saya mengganti isi dari blok `if user is not None` dengan membuat response baru yang menggunakan metode `set_cookie()` untuk variable `last_login` dan mengganti isi dari fungsi `logout_user()` agar memanggil metode `delete_cookie(‘last_login’)`. Saya juga menambahkan context pada fungsi `show_main()` berupa `‘last_login’: request.COOKIES[‘last_login’]` dan mengganti `‘name’` menjadi `request.user.username` agar nama yang ditampilkan sesuai dengan user yang sedang log in dan informasi terakhir kali login dapat ditampilkan pada page `main.html`. Saya kemudian menambahkan line pada `main.html` yang memberitahu user sesi terakhir login mereka.

Setelah mengetes bahwa semua perubahan yang saya buat telah berjalan dengan lancar, saya kemudian menghubungkan setiap `Item` yang ada dengan `User` yang sesuai. Saya pertama menambahkan field `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada class Item yang saya miliki. Kemudian saya mengganti fungsi `create_item()` pada `views.py` agar `item.user` di set dulu sebagai `request.user` sebelum di-save ke database. Kemudian pada `show_main()`, saya memfilter items yang ditunjukkan dengan `Item.objects.filter(user=request.user)` agar seorang user hanya dapat melihat item-item yang mereka sendiri tambahkan. 

Saat tambahan-tambahan ini sudah selesai, saya lakukan `python manage.py makemigrations` dan `python manage.py migrate` untuk mengimplementasikannya. Saya juga menambahkan akun lagi untuk mengecek apakah fungsi-fungsi ini sudah sesuai.

Terakhir, agar tiap akun yang saya miliki hanya memiliki 3 dummy data, saya menambahkan juga tombol increase amount, decrease amount, dan delete item pada page `main.html` saya. Saya membuat fungsi untuk penerapan 3 buttons ini pada `views.py` dengan mengambil `pk` yang sesuai dengan item yang ingin ditambahkan/dikurangi/dihapus, kemudian memfilter `Item` dengan `pk` tersebut dari dataset yang ada dan menambahkan/mengurangi `amount`-nya atau langsung melakukan `data.delete()` bila ingin menghapusnya. Saat menambahkan dan mengurangi amount item, saya menambahkan `data.save()` juga agar perubahan yang terjadi dapat disimpan. Terakhir, saya menambahkan `return redirect(‘main:show_main’)` agar halaman langsung ditunjukkan kembali untuk memperlihatkan perubahan yang telah dilakukan. Saya menambahkan ketiga fungsi ini pada `urls.py` agar bisa diakses oleh user.

Setelah melakukan semua ini, saya menyelesaikan Tugas 4 dengan menjawab pertanyaan-pertanyaan yang diberikan pada `README.md`.

<br>
<br>
<br>

## TUGAS 3
1. ### Apa perbedaan antara form POST dan form GET dalam Django?
**POST** dan **GET** biasanya digunakan untuk tujuan yang berbeda.

Salah satu kegunaan **POST** adalah saat Django berurusan dengan login form. Saat form ini dikembalikan dengan metode **POST**, browser akan menggabungkan data yang telah dimasukkan, *encode* data tersebut, mengirimkannya ke server, kemudian menerima kembali responsnya. Sebaliknya, **GET** menggabungkan data yang dimasukkan ke dalam string lalu menggunakannya untuk membuat sebuah URL. URL ini berisi alamat tujuan pengiriman data serta *keys* dan *values* dari data tersebut.

Setiap permintaan yang dapat mengubah keadaan sistem - seperti permintaan yang dapat mengubah database - sebaiknya menggunakan **POST**. **GET** hanya patut digunakan untuk permintaan yang tidak mempengaruhi keadaan sistem.

<br>

2. ### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML, JSON, dan HTML memiliki beberapa perbedaan dalam konteks pengiriman data. Selain *syntax*-nya yang berbeda-beda, HTML berfungsi dalam menentukan bagaimana data ditampilkan pada *webpage*, hal ini berbeda dengan XML dan JSON yang merupakan format dari data yang ada, bukan format penampilannya.

**XML**: digunakan untuk menyimpan data. Lebih fleksibel dan *secure* untuk digunakan namun memiliki format penulisan yang lebih kompleks.

**JSON**: digunakan untuk menyimpan data. Mudah untuk ditulis dan dimengerti karena memiliki format yang simpel namun tidak se-fleksibel ataupun se-*secure* XML.

![Perbedaan XML dan JSON.](https://miro.medium.com/v2/resize:fit:786/format:webp/1*dvI7HYftuM3CokPLB7KTdw.png "Visualisasi perbedaan antara XML dan JSON.")

**HTML**: digunakan untuk membuat tampilan dan struktur halaman web dengan struktur yang berisi elemen-elemen seperti `<div>, <p>, <a>,` dll.

![HTML.](https://www.simplilearn.com/ice9/free_resources_article_thumb/Bold_italic_underline%20tag.PNG "Visualisasi syntax HTML.")

<br>

3. ### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? 
Salah satu alasan JSON sering digunakan dalam aplikasi web modern adalah karena ia memiliki syntax dalam format *key-value pair* yang membuatnya lebih simpel dan mudah dibaca dibandingkan dengan XML. Ia tidak membutuhkan *tag*, atribut, maupun skema khusus juga. Selain itu, JSON juga mendukung berbagai tipe data seperti string, angka, objek, dan array.

Keuntungan lain dari penggunaan JSON adalah ia dapat dikonversi *dari* suatu objek Javascript ataupun dikonversi *menjadi* sebuah objek JavaScript. Aspek ini sangat memudahkan para *web developer* yang menggunakan Javascript sebagai *scripting language* utama mereka.

<br>

4. ### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
* ##### Membuat input `form` untuk menambahkan objek model pada app sebelumnya.

Untuk melakukan step ini, saya membuat berkas `forms.py` pada folder `main` yang saya isi dengan `ModelForm` baru sebagai berikut:

```
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]

```
Setelahnya, saya membuat file `create_item.html` dalam folder `templates` yang menentukan bagaimana *webpage* form saya akan ditampilkan pada akhirnya. Di sini saya juga menambahkan CSS seperlunya.

Setelah dua hal ini selesai saya implementasi, saya kemudian membuat function baru dalam `views.py` bernama `create_item()` yang akan menangani logic untuk pembuatan item oleh pengguna & memberikan konteks yang diperlukan oleh `create_item.html`. Function tersebut saya buat seperti berikut:

```
def create_item(request):
    context = { 'app_name': 'The Sentimental Sylladex' }

    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context['form'] = form
    return render(request, "create_item.html", context)
```

Saya meng-*import* function yang telah saya buat ini ke dalam `urls.py` dan menambahkan `path('create-item', create_item, name='create_item')` ke dalam list `url_patterns` agar dapat diakses oleh user. Terakhir, saya menambahkan *button* dalam `main.html` yang me-*redirect* user ke laman pembuatan item ini.

<br>

* ##### Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

Untuk mengimplementasikan step ini, saya membuat beberapa fungsi dalam `views.py` seperti `show_html`, `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`. Untuk fungsi yang pertama, saya menginterpretasikannya sebagai fungsi baru yang menampilkan **hanya objek-objek dalam database** sebagai laman HTML yang sederhana. Dengan pemahaman ini, saya kemudian membuat template HTML yang simpel sebagai berikut:

```
<p>Name: {data.name}</p>
<p>Amount: {data.amount}</p>
<p>Description: {data.description}</p>
            
<hr>
```

Fungsi `show_html()` saya melakukan *loop* untuk mengakses semua data yang ada dalam database lalu menambahkannya ke dalam template HTML ini. Setelah semua data ditambahkan, HTML yang sudah lengkap akan dikembalikan kepada user sebagai sebuah HttpResponse.

Untuk fungsi `show_xml` dan `show_json`, saya mengimplementasikannya seperti berikut:

```
data = Item.objects.all()
return HttpResponse(serializers.serialize("dataType", data), content_type="application/dataType")
```

Dengan mengganti `dataType` dengan xml dan json.

Untuk fungsi `show_xml_by_id` dan `show_json_by_id`, saya kurang lebih menggunakan fungsi yang sama dengan sebelumnya namun dengan menambahkan parameter `id` ke dalam function-nya dan mengganti bagian `data = Item.objects.all()` dengan `data = Item.objects.filter(pk=id)`.

<br>

* ##### Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.

Untuk step ini, saya meng-*import* functions yang telah saya buat dalam step sebelumnya ke dalam `urls.py` dan menambahkan:

```
path('html', show_html, name='show_html'),
    path('xml', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),    
```

ke dalam list `url_patterns` agar fungsi-fungsi ini dapat diakses oleh user.

<br>

5. ### *Screenshots* dari Postman

![HTML Postman](/README_img/html_postman.jpg?raw=true "HTML Postman")

![XML Postman](/README_img/xml_postman.jpg?raw=true "XML Postman")

![JSON Postman](/README_img/json_postman.jpg?raw=true "JSON Postman")

![XML-by-ID Postman](/README_img/xml_by_id.jpg?raw=true "XML-by-ID Postman")

![JSOn-by-ID Postman](/README_img/json_by_id.jpg?raw=true "JSOn-by-ID Postman")

<br>
<br>
<br>

## TUGAS 2
* ### Cara Mengimplementasikan Checklist
Pada direktori lokal komputer saya, saya membuat folder baru bernama `sentimental_sylladex`. Di folder ini saya mengaktifkan *virtual environment*, memasang *dependencies*, dan kemudian membuat proyek Django dengan perintah `django-admin startproject sentimental_sylladex .` Saya kemudian membuat aplikasi `main` dan mendaftarkannya ke dalam proyek.

Dalam aplikasi `main` ini, saya membuat `main.html` yang sesuai dengan visi saya untuk Tugas 2 dan melengkapinya dengan *in-line* css untuk mengatur unsur estetikanya. Kemudian, saya menambahkan model ke dalam aplikasi ini dengan nama `Item` yang memiliki atribut `name`, `amount`, dan `description` sesuai ketentuan tugas.
    
Setelah melakukan migrasi untuk model ini, saya membuat sebuah fungsi pada `views.py` untuk `main.html` yang menampilkan nama aplikasi, nama saya, dan kelas saya. Terakhir, saya mengonfigurasi *routing* URL pada aplikasi `main` dan pada proyek sebelum akhirnya melakukan *deployment* untuk aplikasi ini pada Adaptable dan membuat `README.md` file untuk melengkapinya.

* ### Bagan
![Gambar bagan.](https://i.ibb.co/Yk3X6Bn/homestuck-reference.png "Inilah gambar bagan-nya.")

* ### Virtual Environment
1. __Mengapa kita menggunakan *virtual environment*?__ Adanya lingkungan virtual memungkinkan kita untuk memiliki beberapa versi `python` pada satu mesin yang memiliki *libraries* dan *dependencies* masing-masing sembari menjaganya agar tetap terpisah dari satu sama lain. Hal ini memungkinkan kita untuk mengerjakan banyak proyek Django dengan versi yang berbeda-beda tanpa munculnya *error* maupun *clashes*.

2. __Apakah tetap dapat membuat aplikasi web berbasis Django tanpa *virtual environment*?__ Walau sebenarnya bisa, pembuatan aplikasi web berbasis Django tanpa menggunakan *virtual environment* meningkatkan risiko *error* apabila kita mengerjakan banyak aplikasi web yang berbeda dalam waktu yang sama, sehingga hal ini dianggap *bad practice* dan tidak dianjurkan.

* ### MVC, MVT, dan MVVM
1. **MVC** adalah singkatan dari Model-View-Controller. Pada *design pattern* ini, Model mengatur data serta penyimpanannya, View menjadi bagian yang menampilkan informasi kepada user (*User Interface*), dan Controller menjadi bagian yang menghubungkan Model dan View serta menangani *request-request* dari user.

2. **MVT** adalah singkatan dari Model-View-Template. Pada *design pattern* ini, Model memiliki peran yang hampir sama dengan model dalam MVC, yaitu untuk mengelola data beserta penyimpanannya. Beda dengan peran View dalam MVC, View dalam MVT memiliki peran untuk menghubungkan antara Template dengan Model dan melakukan *render* untuk tampilan di-*request* oleh user. Template pada MVT terdiri dari file-file HTML yang mengatur layout dan tata letak web akhir yang akan ditampilkan ke user.

3. **MVVM** adalah singkatan dari Model-View-ViewModel. Pada *design pattern* ini, Model memiliki peran dalam mengatur data dan penyimpanannya seperti MVC dan MVT. View pada MVVM bertanggung jawab dalam menampilkan informasi yang di-*request* pengguna. ViewModel dalam MVVM berperan dalam memproses data dari Model agar sesuai dengan tampilan yang ditentukan oleh View. 

Dari ketiga *pattern* ini, perbedaan utamanya adalah komponen-komponen yang dimiliki setiap *design pattern* tersebut beserta relasi hubungan antara setiap komponen-komponennya.
