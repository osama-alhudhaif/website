تمام، هذا هو ملف `README.md` كامل ومنسق، يشمل جميع الأقسام المهمة لمشروعك "عوالمنا" مع تشغيل Flask + API، ومكتوب بأسلوب احترافي وواضح:

````markdown
# 🌟 Awallimna - The Arabic Stories Platform

منصة إلكترونية للقصص والروايات تهدف لتقديم تجربة قراءة وكتابة سلسة للمستخدم العربي، مع دعم الذكاء الاصطناعي والترجمة التلقائية، ضمن واجهة تفاعلية تعتمد على Flask وFastAPI وتقنيات حديثة في الواجهة الأمامية.

---

## 📋 Overview

Awallimna is a storytelling platform that empowers users to read, write, and share Arabic stories across multiple genres. The system includes a main user interface (Flask) and a separate API (FastAPI), designed to be scalable, multilingual, and AI-assisted.

---

## 🚀 Running Methods

### ✅ Method 1 - Using `start_services.bat` (Recommended)

```bash
# Just double-click the file:
start_services.bat
````

---

### 🐍 Method 2 - Run All Services via Python

```bash
# Step 1: Install dependencies
pip install -r awallimna/requirements.txt
pip install -r api/requirements.txt

# Step 2: Run both services
python start_all_services.py
```

---

### 🔁 Method 3 - Manual Separate Execution

```bash
# Terminal 1 - Run Flask main site
cd awallimna
python run.py

# Terminal 2 - Run FastAPI backend
cd api
python main.py
```

---

## 🌐 Service Details

| Service        | URL                                            | Port | Description              |
| -------------- | ---------------------------------------------- | ---- | ------------------------ |
| Main Site      | [http://127.0.0.1:8080](http://127.0.0.1:8080) | 8080 | Frontend Flask interface |
| API            | [http://127.0.0.1:8088](http://127.0.0.1:8088) | 8088 | FastAPI backend          |
| Production URL | [https://awallimna.com](https://awallimna.com) | -    | Deployment (optional)    |

---

## 🔧 Requirements

### 📦 Flask App (`awallimna/requirements.txt`)

```txt
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Login==0.6.3
Flask-Migrate==4.0.5
Flask-CORS==4.0.0
Flask-Bcrypt==1.0.1
Flask-Mail==0.9.1
Flask-WTF==1.1.1
Flask-Caching==2.1.0
Flask-JWT-Extended==4.5.3
Flasgger==0.9.7.1
WTForms==3.0.1
Werkzeug==2.3.7
Jinja2==3.1.2
MarkupSafe==2.1.3
itsdangerous==2.1.2
click==8.1.7
blinker==1.6.3
```

### ⚙️ FastAPI App (`api/requirements.txt`)

```txt
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
python-multipart==0.0.6
mysql-connector-python==8.2.0
```

---

## ⚠️ Important Notes

* ✅ Python version: 3.7 or higher
* ⚠️ Avoid port conflicts (8080, 8088)
* 🛑 Use `Ctrl+C` to stop services manually
* 🧠 Adjust database configs in `api/config.py` if needed

---

## 🐛 Troubleshooting

### ❌ "Port already in use"

```bash
# Check what’s using the port
netstat -ano | findstr :8080
netstat -ano | findstr :8088

# Kill the process
taskkill /PID [ProcessID] /F
```

### ❌ "ModuleNotFoundError"

```bash
pip install -r awallimna/requirements.txt
pip install -r api/requirements.txt
```

### ❌ "Database connection error"

* تأكد من تشغيل MySQL
* أو عدّل بيانات الاتصال داخل `api/config.py`

---

## 📁 Project Structure

```plaintext
awallimna/
├── run.py               # Flask app starter
├── main.py              # Entry point (if used)
├── templates/           # Jinja2 HTML templates
├── static/              # Static JS/CSS/Images
├── requirements.txt     # Flask dependencies
└── ...

api/
├── main.py              # FastAPI app
├── config.py            # Database configs
├── controller/          # Logic + Routing
├── model/               # ORM models
├── decorators/          # Shared decorators
└── requirements.txt     # API dependencies

Python App/              # Kivy app (mobile)
awallimna/               # Flutter app (future)
```

---

## 🔄 Changelog

* ✅ Added multilingual support (i18next)
* ✅ Improved error handling and logs
* ✅ Added batch/script auto-run
* ✅ Organized project into modules
* ✅ Fixed database injection risks

---

## 📞 Support

If you face any issue:

1. تأكد من إصدار Python
2. تأكد من تثبيت المتطلبات
3. تأكد من أن المنافذ غير مستخدمة
4. راجع إعدادات الاتصال بقاعدة البيانات

---

## 📝 License

جميع الحقوق محفوظة © Osamah Alhudhaif – 2025

---

**#awallimna\_0.1**

```

---

### ✅ ملاحظات إضافية:
- بإمكانك ترفعه مباشرة كملف `README.md` في جذر الريبو.
- إذا كنت تبي أضيف قسم "مستقبلي" (Future Plans)، أو ملف `LICENSE`, أو `contributing.md`، قل لي أجهزها لك.

تبيني أرفقه لك بصيغة ملف جاهز؟
```
# awallimna
