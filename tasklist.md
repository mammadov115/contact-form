
### ✅ 1. **Layihənin Başlanğıcı**

* [+] Django virtual mühit yarat (Poetry, venv və ya pipenv ilə)
* [+] Yeni Django layihəsi yarat (`django-admin startproject contact_project`)
* [+] Yeni app yarat (`python manage.py startapp contact`)
* [+] App-i `settings.py` faylında `INSTALLED_APPS`-ə əlavə et
* [+] `.env` faylı yarat və `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` kimi dəyişənləri ora köçür
* [+] `settings.py` faylında `django-environ` və ya `python-decouple` ilə env konfiqurasiyası qur

---

### 🗃️ 2. **Model (Verilənlər Bazası Dizaynı)**

* [+] `ContactMessage` modeli yarat:

  * `name` – CharField
  * `email` – EmailField
  * `subject` – CharField
  * `message` – TextField
  * `created_at` – DateTimeField (auto\_now\_add=True)
* [+] `__str__` metodu əlavə et
* [+] Admin paneldə modeli qeydiyyatdan keçir
* [+] `python manage.py makemigrations && migrate` ilə bazanı yenilə

---

### 🧠 3. **Form**

* [+] `ContactForm` adlı `forms.Form` və ya `forms.ModelForm` sinifi yarat
* [+] Validasiya qaydaları yaz (məsələn, minimum uzunluq, düzgün e-mail)

---

### 👁️ 4. **View (Biznes Məntiqi)**

* [+] `contact_view(request)` adlı funksiya yaradaraq aşağıdakıları et:

  * GET istəyi zamanı boş forma göstər
  * POST istəyi zamanı form məlumatlarını al və yadda saxla
  * Məlumat uğurla göndəriləndə istifadəçiyə "Təşəkkür" mesajı göstər
  * Form səhvdirsə, səhvlərlə birlikdə geri qaytar

---

### 🌐 5. **Template (Şablon Dizaynı)**

* [+] `contact_form.html` adlı şablon faylı yarat

  * Form input sahələri (`name`, `email`, `subject`, `message`)
  * CSRF token əlavə et
  * Göndər düyməsi
* [+] `base.html` şablonu yaradaraq layout-un təməlini qur
* [+] `form.errors` və `success` mesajları göstər
* [+] Stil üçün `style.css` əlavə et (əgər istəsən)

---

### 🔁 6. **URL Routing**

* [+] App içində `urls.py` faylı yarat
* [+] `urlpatterns` içində `contact/` route-u qeyd et
* [+] Project `urls.py` faylında app URL-ləri include et

---

### 🧪 7. **Testlər və Göstəricilər**

* [+] Forma POST istəyi ilə düzgün işləyir?
* [+] Admin paneldə daxil olan mesajlar görünürmü?
* [+] Form validasiyası işləyirmi?
* [+] Boş və səhv məlumatlar üçün error mesajları çıxırmı?

---

### ⚙️ 8. **Əlavə Tasklar (İstəyə bağlı)**

* [+] `SuccessMessageMixin` və ya `messages` framework istifadə et
* [+] CAPTCHA (Google reCAPTCHA) əlavə et
* [+] Email göndərişi əlavə et (form göndəriləndə adminə mail getsin)
* [ ] Docker və ya CI/CD pipeline qur (deployment üçün)
* [ ] Unit testlər yaz (`tests.py`)


<!-- iwwx yqry plqg onhq -->
captcha ve email qeydlerini notionda yaz