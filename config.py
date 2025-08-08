import os
# 1. قم باستيراد Type و Dict من مكتبة typing
from typing import Type, Dict


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    # قاعدة البيانات MySQL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://osamh64:password@localhost/data_awalimna'
    # إذا كنت تستخدم SQLite، يمكنك استخدام السطر التالي بدلاً من ذلك
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///awalimna.db'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///awallimna.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'simple'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    
    # إعدادات البريد الإلكتروني
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'your-email@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'your-password'
    
    # تعطيل CSRF مؤقتاً
    WTF_CSRF_ENABLED = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# 2. أضف تلميح النوع هنا
config: Dict[str, Type[Config]] = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

env_config = os.getenv('FLASK_ENV', 'default')
# Note: This line should be moved to your Flask application initialization file
# app.config.from_object(config[env_config])
