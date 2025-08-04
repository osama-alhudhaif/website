# flask_libs.py

from flask import Flask
from flask_babel import Babel
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# إعدادات أساسية
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'

# تهيئة المكتبات
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
csrf = CSRFProtect(app)
babel = Babel(app)

# ممكن تضيف هنا أي إعدادات أو دوال مشتركة

