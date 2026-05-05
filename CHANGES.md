# سجل التغييرات — مشروع أودا (website)

> آخر تحديث: 2026-05-05  
> المستودع: https://github.com/osama-alhudhaif/website

---

## الهيكل العام للمشروع

```
website/
├── backend/                  ← Django REST Framework
│   ├── apps/
│   │   ├── accounts/         ← نظام المستخدمين والمصادقة
│   │   └── stories/          ← القصص والترجمة
│   ├── core/                 ← إعدادات Django الرئيسية
│   ├── utils/                ← أدوات مساعدة (email, validators)
│   ├── templates/            ← قوالب البريد الإلكتروني
│   ├── requirements.txt
│   └── manage.py
├── frontend/                 ← React 19 + TypeScript + Vite
│   └── src/
│       ├── pages/            ← الصفحات
│       ├── profile/          ← مكونات البروفايل
│       ├── config/           ← إعدادات API
│       └── constants/        ← ثوابت المشروع
├── Dockerfile
├── railway.toml
└── package.json
```

---

## Backend — Django REST Framework

### الإصدارات
| مكتبة | الإصدار |
|---|---|
| Django | 6.0.3 |
| djangorestframework | 3.16.1 |
| psycopg2-binary | 2.9.11 |
| gunicorn | 23.0.0 |
| whitenoise | 6.9.0 |
| django-cors-headers | 4.9.0 |
| drf-yasg | 1.21.15 |
| requests | 2.32.5 |
| python-dotenv | 1.2.2 |

---

### نقاط API — Accounts (`/api/v1/accounts/`)

| الطريقة | المسار | الوصف |
|---|---|---|
| POST | `/register/` | تسجيل مستخدم جديد |
| POST | `/login/` | تسجيل الدخول — يُرجع token |
| GET / PUT / DELETE | `/me/` | بروفايل المستخدم الحالي |
| GET / PUT / DELETE | `/me/` | حذف الحساب |
| POST | `/verify-email/<uid>/<token>/` | التحقق من البريد |
| POST | `/password-reset/` | طلب إعادة تعيين كلمة المرور |
| POST | `/password-reset/confirm/<uid>/<token>/` | تأكيد إعادة التعيين |
| POST | `/change-password/` | تغيير كلمة المرور |
| GET / POST | `/subscriptions/` | قائمة / إنشاء اشتراك |
| GET | `/subscriptions/current/` | الاشتراك النشط الحالي |
| GET | `/subscriptions/pricing/` | عروض الأسعار |
| POST | `/toggle-dark-mode/` | تبديل الوضع الداكن |
| GET / POST | `/follows/` | متابعة مستخدم |
| DELETE | `/unfollow/<user_id>/` | إلغاء المتابعة |
| GET | `/users/<user_id>/followers/` | قائمة المتابِعين |
| GET | `/users/<user_id>/following/` | قائمة الذين يتابعهم |
| GET | `/authors/<user_id>/` | بروفايل كاتب عام |
| GET | `/notifications/` | قائمة الإشعارات |
| GET | `/notifications/unread-count/` | عدد الإشعارات غير المقروءة |
| POST | `/notifications/<pk>/mark-read/` | تعيين إشعار كمقروء |

---

### نقاط API — Stories (`/api/v1/stories/`)

| الطريقة | المسار | الوصف |
|---|---|---|
| GET | `/stories/` | قائمة القصص المنشورة (paginated) |
| POST | `/stories/` | رفع قصة جديدة (multipart) |
| GET | `/stories/<id>/` | تفاصيل قصة + يزيد views_count |
| PUT / PATCH | `/stories/<id>/` | تعديل القصة (للمؤلف فقط) |
| DELETE | `/stories/<id>/` | حذف القصة (للمؤلف فقط) |
| POST | `/stories/<id>/like/` | إعجاب / إلغاء إعجاب |
| GET | `/stories/<id>/is_liked/` | هل أعجب المستخدم بالقصة؟ |
| GET / POST | `/stories/<id>/comments/` | التعليقات |
| DELETE | `/comments/<pk>/` | حذف تعليق |
| GET / POST | `/stories/<id>/ratings/` | التقييمات (1–5) |
| GET | `/stories/<id>/my-rating/` | تقييم المستخدم الحالي |
| POST | `/translate/` | ترجمة نص |
| GET | `/translate/languages/` | اللغات المدعومة |

---

### نماذج قاعدة البيانات

#### User (accounts.User — يرث من AbstractUser)
| الحقل | النوع | الوصف |
|---|---|---|
| username | CharField | اسم المستخدم |
| email | EmailField | البريد الإلكتروني |
| first_name / last_name | CharField | الاسم الكامل |
| phone | CharField | رقم الهاتف |
| country | CharField | البلد |
| gender | CharField | الجنس |
| date_of_birth | DateField | تاريخ الميلاد |
| role | CharField (choices) | reader / writer / both / FOUNDER / HIGH_ADMIN... |
| dark_mode_enabled | BooleanField | تفضيل الوضع الداكن |
| status | CharField | حالة الحساب |

#### Story
| الحقل | النوع | الوصف |
|---|---|---|
| title | TextField | عنوان القصة |
| file_path | FileField | ملف القصة (PDF أو TXT) |
| description | TextField | وصف القصة |
| author | FK → User | المؤلف |
| status | CharField | published / draft |
| genre | CharField | التصنيف الأدبي |
| language | CharField | لغة القصة |
| tags | TextField | الوسوم |
| views_count | IntegerField | عدد المشاهدات |
| likes_count | IntegerField | عدد الإعجابات |

#### Comment
| الحقل | النوع |
|---|---|
| story | FK → Story |
| user | FK → User |
| content | TextField |
| is_approved | BooleanField |
| created_at / updated_at | DateTimeField |

#### Rating
| الحقل | النوع |
|---|---|
| story | FK → Story |
| user | FK → User |
| rating | IntegerField (1–5) |

#### StoryLike
| الحقل | النوع |
|---|---|
| story | FK → Story |
| user | FK → User |

#### Subscription
| الحقل | النوع |
|---|---|
| user | FK → User |
| plan_type | CharField |
| is_active | BooleanField |
| start_date / end_date | DateTimeField |

---

### محرك الترجمة (`backend/apps/stories/api/translation.py`)

#### قبل التحديث
كان يستخدم MyMemory API الخارجي فقط — جودة محدودة وحد أقصى للطلبات.

#### بعد التحديث (2026-05-05)
**المحرك الأساسي: Ollama محلياً**
```
URL:   http://192.168.1.5:11434/api/generate
Model: qwen2.5-coder:32b
```

**prompt المستخدم:**
```
You are a literary translator. Translate the following text from {source} to {target}.
Preserve the literary style, tone, and artistic nuance.
Return ONLY the translated text, no explanations.

Text:
{text}
```

**الاحتياط التلقائي:** إذا رفض Ollama الاتصال (`ConnectionError`) يتحول فوراً إلى MyMemory.

**اللغات المدعومة:** ar, en, fr, de, es, it, pt, ru, zh, ja, ko, tr, fa, ur, hi

---

## Frontend — React 19 + TypeScript + Vite

### المكتبات الرئيسية
| مكتبة | الإصدار |
|---|---|
| react | ^19.0.0 |
| react-router-dom | ^7.0.0 |
| react-dom | ^19.0.0 |
| react-country-flag | ^3.1.0 |
| country-list | ^2.4.1 |

### الصفحات الموجودة (`frontend/src/pages/`)
| الملف | الوصف |
|---|---|
| `login.tsx` | صفحة تسجيل الدخول |
| `register.tsx` | صفحة إنشاء حساب |
| `forgot-password.tsx` | نسيت كلمة المرور |
| `reset-password.tsx` | إعادة تعيين كلمة المرور |
| `verify-email.tsx` | التحقق من البريد الإلكتروني |
| `notifications.tsx` | قائمة الإشعارات |
| `upload-story.tsx` | رفع قصة جديدة |

---

## التحديثات حسب التاريخ

### 2026-05-05 — ترقية محرك الترجمة
- **الملف:** `backend/apps/stories/api/translation.py`
- استبدال MyMemory بـ Ollama (qwen2.5-coder:32b) كمحرك أساسي
- إضافة fallback تلقائي إلى MyMemory عند عدم توفر Ollama

### 2026-05-01 — إصلاح ثغرات npm
- تحديث حزم Node.js لمعالجة 12 ثغرة أمنية

### 2026-04-30 — تحديث .gitignore
- استبعاد ملفات قاعدة البيانات وملفات Visual Studio Cache

### 2026-04-26 — ميزات الإعجاب والإشعارات
- إضافة نظام الإعجابات (StoryLike)
- إضافة نظام الإشعارات
- تحسين بطاقات القصص في الواجهة الأمامية

### 2026-04-17 — إصلاحات أمنية
- إزالة الملفات الحساسة من git
- تحديث .gitignore
- إصلاح 12 ثغرة أمنية في المصادقة ومنع path traversal ومعدل الطلبات

### 2026-04-13 — إطلاق المشروع
- المصادقة الكاملة (login, register, token)
- خدمة الترجمة (MyMemory)
- تقديم ملفات الوسائط
- إصلاحات شاملة للإنتاج

### 2026-04-12 — صفحة الإعدادات
- إضافة صفحة إعدادات الحساب في الواجهة
- تحديث backend API للإعدادات

### 2026-04-11 — إصلاح توافق Django 6.0.4
- حل مشكلة `PurePosixPath` مع Vite assets
- تصحيح `validate_file_name` للتوافق مع pathlib

---

## متغيرات البيئة المطلوبة (`backend/.env`)

```env
SECRET_KEY=...
DEBUG=False
DATABASE_URL=postgresql://user:pass@host/db
ALLOWED_HOSTS=...
ODA_SUPPORT_EMAIL=support@oda.com
EMAIL_HOST=...
EMAIL_PORT=587
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...
```

---

## تشغيل المشروع محلياً

```bash
# Backend
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# Frontend
cd frontend
npm install
npm run dev

# Ollama (للترجمة)
ollama run qwen2.5-coder:32b
```

---

## النشر (Railway)

المشروع مهيأ للنشر على Railway عبر `railway.toml` و`Dockerfile`.

```toml
# railway.toml
[build]
builder = "dockerfile"

[deploy]
startCommand = "gunicorn core.wsgi:application"
```
