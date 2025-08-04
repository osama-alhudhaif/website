# 🌟 Awallimna - The Arabic Stories Platform

## 📋 Overview

Awallimna is an electronic platform for Arabic stories that allows users to read and write various types of literary narratives.

## 🚀 Running Methods

### Method 1 (Easiest) - Batch File

```bash
# Double-click the file
start_services.bat
```

### Method 2 - Direct Python

```bash
# Install dependencies first
pip install -r awallimna/requirements.txt
pip install -r api/requirements.txt

# Run all services
python start_all_services.py
```

### Method 3 - Separate Execution

```bash
# First Terminal - Main Site
cd awallimna
python run.py

# Second Terminal - API
cd api
python main.py
```

## 📋 Service Information

| Service | URL | Port | Description |
|---------|-----|------|-------------|
| Main Site | <http://127.0.0.1:8080> | 8080 | Primary user interface |
| API | <http://127.0.0.1:8088> | 8088 | Application Programming Interface |
| Hostname Test | hppts:awallimna.com | 1 | Website test |

## 🔧 Requirements

### For the Main Site

- Flask==2.3.3
- Flask-SQLAlchemy==3.0.5
- Flask-Login==0.6.3
- Flask-Migrate==4.0.5
- Flask-CORS==4.0.0
- Flask-Bcrypt==1.0.1
- Flask-Mail==0.9.1
- Flask-WTF==1.1.1
- Flask-Caching==2.1.0
- Flask-JWT-Extended==4.5.3
- Flasgger==0.9.7.1
- WTForms==3.0.1
- Werkzeug==2.3.7
- Jinja2==3.1.2
- MarkupSafe==2.1.3
- itsdangerous==2.1.2
- click==8.1.7
- blinker==1.6.3

### For the API

- fastapi==0.104.1
- uvicorn==0.24.0
- sqlalchemy==2.0.23
- pydantic==2.5.0
- python-multipart==0.0.6
- mysql-connector-python==8.2.0

## ⚠️ Important Notes

1. **Ensure Python 3.7+ is installed**
2. **Check for all necessary files**
3. **Use Ctrl+C to stop all services**
4. **If there are errors, check the used ports**

## 🐛 Troubleshooting

### Issue: "Port already in use"

```bash
# Find processes using the port
netstat -ano | findstr :8080
netstat -ano | findstr :8088

# Stop the process using PID
taskkill /PID [ProcessID] /F
```

### Issue: "Module not found"

```bash
# Reinstall dependencies
pip install -r awallimna/requirements.txt
pip install -r api/requirements.txt
```

### Issue: "Database connection error"

```bash
# Ensure MySQL is running
# Or adjust database settings in api/config.py
```

## 📁 Project Structure

```
awallimna/
├── main.py              # Main application file
├── run.py               # Start-up script
├── requirements.txt     # Dependencies for the site
├── templates/           # HTML templates
├── static/              # Static files
└── ...

api/
├── main.py              # API main file
├── config.py            # Database settings
├── requirements.txt     # Dependencies for API
├── controller/          # Control units
├── model/               # Data models
└── decorators/          # Decorators

Python App/             # Kivy application
awallimna/              # Flutter application
```

## 📞 Support

If you encounter any issues, please check:

1. Python version (should be 3.7+)
2. All dependencies are installed correctly
3. Ports aren't used by other applications
4. Database settings

## 🔄 Latest Updates

- Fixed SQL injection vulnerabilities
- Improved error handling
- Added a separate configuration file
- Resolved import redundancies
- Enhanced start-up scripts
- Update release 0.0.7
# awalimna_0.7
