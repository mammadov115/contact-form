
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
* [+] Docker və ya CI/CD pipeline qur (deployment üçün)
* [+] Unit testlər yaz (`tests.py`)



## 🧩 1. Layihəyə API infrastrukturu əlavə et

- [+] `djangorestframework` paketini `pyproject.toml` və ya `requirements.txt`-ə əlavə et
- [+] `INSTALLED_APPS`-ə `"rest_framework"` əlavə et
- [+] `config/urls.py` faylında API URL-ləri üçün baza `path("api/", ...)` qeyd et

---

## 📦 2. API üçün Serializer hazırla

- [+] `core/serializers.py` faylı yarat  
- [+] `ContactSerializer` sinfi yaz:
  - `name`, `email`, `subject`, `message` sahələrini daxil et
  - `email` sahəsinə validasiya əlavə et (istəyə görə xüsusi `validate_email`)
  - Validasiya errorlarını uyğun mesajlarla yaz

---

## 🧱 3. API View-larını qur

### Sadə `APIView` və ya `GenericAPIView` ilə başla (DRF)

- [+] `core/api_views.py` və ya `core/views.py` içində `ContactFormAPIView` yarat
- [+] `POST` metodu əlavə et:
  - Gələn datanı serializer ilə yoxla
  - `is_valid()` olduqda form məlumatlarını `Contact` modelinə yaz (və ya sadəcə email göndər)
  - Əgər uğurlu olarsa `201 Created`, uğursuz olarsa `400 Bad Request` qaytar

---

## 🌐 4. API URL-lərini yaz

- [+] `core/api_urls.py` və ya `core/urls.py` daxilində yeni API üçün `urlpatterns` yarat
- [+] `path("contact/", ContactFormAPIView.as_view())` əlavə et
- [+] `config/urls.py`-də `include("core.api_urls")` ilə birləşdir

---

## 🛡️ 5. Email göndərişini aktiv et (əgər edirsənsə)

- [+] API ilə gələn məlumat uğurludursa, eyni zamanda admin emailinə yönəlt
- [+] DRF-də bu hissəni `serializer.save()` və ya `perform_create` içində et

---

## ✅ 6. API üçün Unit Testlər yaz

- [ ] `core/tests/test_api.py` və ya `tests.py` daxilində yeni test sinfi əlavə et
- [ ] Uğurlu `POST` test et (`201`)
- [ ] Yanlış email və ya boş sahə ilə testlər et (`400`)
- [+] Email göndərişinin olub-olmadığını yoxlayan testlər də əlavə et (mock ilə)

---

## 🧪 7. API endpointlərini Postman və ya cURL ilə yoxla

- [+] `POST http://localhost:8000/api/contact/` sorğusu göndər
- [+] JSON cavabların düzgün gəlib-gəlmədiyini yoxla

---

## 🛡️ 8. Təhlükəsizlik və optimallaşdırma (son mərhələdə)

- [+] API throttling (rate limit) aktiv et (`REST_FRAMEWORK` içində)
- [-] CSRF exempt etməyi düşün (əgər public API olacaqsa)
- [+] Response-larda `detail`, `errors`, `status` kimi strukturlaşdırma əlavə et
- [+] Swagger və ya `drf-spectacular` ilə API sənədləşməsi əlavə et (istəyə görə)

---

## 🔚 9. CI/CD üçün testləri genişləndir

- [+] `.github/workflows/django.yml`-a API testləri də daxil et
- [+] `python manage.py test` ilə həm MVT, həm də API testləri işləsin



