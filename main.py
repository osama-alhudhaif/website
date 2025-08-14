import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, abort # pyright: ignore[reportUnusedImport, reportUnknownVariableType]
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_caching import Cache
from flask_jwt_extended import JWTManager
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user # pyright: ignore[reportUnknownVariableType, reportUnusedImport]
from wtforms import StringField, PasswordField, SubmitField # type: ignore
from wtforms.validators import InputRequired, Length, ValidationError # pyright: ignore[reportUnusedImport]
from flask_wtf import FlaskForm # type: ignore
from flask_migrate import Migrate
from flask_cors import CORS # type: ignore

# --- تحميل متغيرات البيئة ---
load_dotenv()
secret_key = os.getenv('AWALLIMNA_SECRET_KEY')
jwt_secret_key = os.getenv('AWALLIMNA_JWT_SECRET_KEY')
if not secret_key or not jwt_secret_key:
    raise ValueError("خطأ: لم يتم العثور على المفاتيح السرية.")

# --- إعدادات التطبيق ---
Awallimna = Flask(__name__, template_folder="templates", static_folder="static")
Awallimna.config['SECRET_KEY'] = secret_key
Awallimna.config['JWT_SECRET_KEY'] = jwt_secret_key
Awallimna.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/data_awalimna'
Awallimna.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- تهيئة إضافات Flask ---
db = SQLAlchemy(Awallimna)
migrate = Migrate(Awallimna, db)
bcrypt = Bcrypt(Awallimna)
mail = Mail(Awallimna)
csrf = CSRFProtect(Awallimna)
cache = Cache(Awallimna) # ملاحظة: إذا لم تكن تستخدم الكاش، يمكنك تعطيله لتجنب التحذير
jwt = JWTManager(Awallimna)
login_manager = LoginManager()
login_manager.init_app(Awallimna)
login_manager.login_view = 'login'
migrate = Migrate(Awallimna, db)

# =====================================================================
# --- موديلات قاعدة البيانات (Database Models) ---
# =====================================================================

class Story(db.Model):
    __tablename__ = 'story'
    id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)
    author_id = db.Column(db.String(255), nullable=True)
    creation_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    status = db.Column(db.String(100), nullable=True)
    approved_by_admin_id = db.Column(db.String(255), nullable=True)
    genre = db.Column(db.String(255), nullable=True)  # النوع باللغة الإنجليزية
    category = db.Column(db.String(100), nullable=True)  # الفئة باللغة العربية
    views_count = db.Column(db.Integer, default=0)
    likes_count = db.Column(db.Integer, default=0)

    def __init__(self, title, content=None, author_id=None, genre=None, category=None): # type: ignore
        self.title = title
        self.content = content
        self.author_id = author_id
        self.genre = genre
        self.category = category

    def __repr__(self):
        return f'<Story {self.title}>'

# مثال للاستعلام الصحيح حسب genre أو category
# story_in_category = Story.query.filter_by(genre=arabic_name).all() # type: ignore


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Student(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# --- قاموس الفئات المركزي ---
CATEGORIES = {
    'comedy': 'كوميديا',
    'science_fiction': 'خيال علمي',
    'fiction': 'خيال',
    'romance': 'الرومانسي',
    'crime_investigation': 'جريمة وتحقيق',
    'horror': 'الرعب',
    'adventure': 'مغامرة',
    'drama': 'دراما',
    'historical': 'تاريخي',
    'theft': 'سرقة',
    'war': 'حرب',
    'fantasy':'فانتازي',
    'children': 'اطفال'
}

# --- قاموس الصفات المركزي ---
pages = {
    'about': 'عن الموقع',
    'accept_educational_center': 'قبول مركز التعليم',
    'admin_page': 'صفحة المسؤول',
    'adventure': 'مغامرة',
    'base': 'الأساس',
    'category_page': 'صفحة الفئة',
    'center_profile': 'ملف تعريف المركز',
    'children': 'الأطفال',
    'comedy': 'كوميديا',
    'confirmation_sent_email': 'تأكيد إرسال البريد الإلكتروني',
    'contact': 'اتصل بنا',
    'create_center_account': 'إنشاء حساب مركز التعليم',
    'crime_investigation': 'الجريمة والتحقيق',
    'deleted_confirmation': 'تأكيد الحذف',
    'delete_account': 'حذف الحساب',
    'drama': 'دراما',
    'error': 'خطأ',
    'fantasy': 'فانتازيا',
    'fiction': 'خيال',
    'forgot_password': 'استعادة كلمة المرور',
    'historic': 'تاريخي',
    'historical': 'تاريخي',
    'horror': 'رعب',
    'login': 'تسجيل الدخول',
    'paths': 'المسارات',
    'privacy': 'سياسة الخصوصية',
    'reader_profile': 'ملف تعريف القارئ',
    'read_story': 'قراءة القصة',
    'register': 'التسجيل',
    'register_center': 'تسجيل مركز التعليم',
    'reset_password': 'إعادة تعيين كلمة المرور',
    'review_story': 'مراجعة القصة',
    'romance': 'الرومانسي',
    'science_fiction': 'خيال علمي',
    'sent_educational_center': 'إرسال مركز التعليم',
    'statistics': 'الإحصائيات',
    'story_functions': 'وظائف القصة',
    'subscriptions': 'الاشتراكات',
    'teacher_accounts': 'حسابات المعلمين',
    'terms_conditions': 'الشروط والأحكام',
    'theft': 'سرقة',
    'update_story_status': 'تحديث حالة القصة',
    'war': 'حرب',
    'website': 'الموقع',
    'writer_profile': 'ملف تعريف الكاتب',
    'write_story': 'كتابة القصة'
}

# --- قاموس انواع الحسابات المركزي ---
ACCOUNT_TYPES = {
    'reader': 'قارئ',
    'admin_author': 'كاتب',
    'admin_reader': 'قارئ',
    'admin_author': 'كاتب',
    'super_admin_reader': 'قارئ',
    'super_admin_author': 'كاتب',
    'educational_center': 'مركز تعليمي',
    'educational_center_teacher': 'معلم',
    'educational_center_student': 'طالب',
    "owner": "مالك الموقع",
}

# --- إعدادات ومُعالِجات عامة ---
@login_manager.user_loader
def load_user(user_id): # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
    return None

@Awallimna.context_processor # pyright: ignore[reportUntypedFunctionDecorator]
def inject_categories_and_user():
    user_info = session.get('user', None)
    return dict(categories=CATEGORIES, user=user_info)

@Awallimna.errorhandler(404)
def not_found_error(error): # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
    return render_template('error.html', error_code=404, error_message="الصفحة غير موجودة"), 404

# =====================================================================
# ---  عرض جميع روابط الصفحات  ---
# =====================================================================

@Awallimna.route("/apis", methods=["GET", "POST"])
def paths():
    templates_dir = os.path.join(os.path.dirname(__file__), "templates")
    pages = [f for f in os.listdir(templates_dir) if f.endswith(".html")]
    # توليد قائمة بالروابط لكل صفحة
    links: list[str] = []
    for page in pages:
        # إزالة .html للحصول على اسم المسار
        route = page.replace('.html', '')
        # بعض الصفحات مثل index قد تكون مختلفة، هنا نفترض أن اسم المسار هو اسم الملف بدون .html
        links.append(f'<li><a href="/{route}">{page}</a></li>')
    # بناء HTML بسيط
    html = f"""
    <html>
    <head><title>جميع صفحات الموقع</title></head>
    <body>
        <h1>جميع صفحات الموقع وروابطها</h1>
        <ul>
            {''.join(links)}
        </ul>
    </body>
    </html>
    """
    return html

# =====================================================================
# --- المسارات الرئيسية والتفاعلية ---
# =====================================================================

@Awallimna.route("/")
def index():
    return render_template('website.html')

# story_in_category = Story.query.filter_by(genre=arabic_name).all()  # type: ignore

def show_category(category_slug): # type: ignore
    arabic_name = CATEGORIES.get(category_slug) # type: ignore
    if not arabic_name:
        abort(404)
    
    story_in_category = Story.query.filter_by(category=arabic_name).all() # type: ignore
    
    return render_template(
        'category_page.html', 
        category_name_arabic=arabic_name, 
        story=story_in_category
    )

# =====================================================================
# --- مسارات المصادقة والملفات الشخصية ---
# =====================================================================
@Awallimna.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # ... منطق تسجيل الدخول
        pass
    return render_template("login.html")

@Awallimna.route("/logout")
def logout():
    session.pop('user', None)
    flash("تم تسجيل الخروج بنجاح", "info")
    return redirect(url_for('login'))

@Awallimna.route("/register")
def register():
    return render_template("register.html")
    
@Awallimna.route("/reader_profile")
def reader_profile():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template("reader_profile.html")

@Awallimna.route("/author_profile")
def author_profile():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template("author_profile.html")

@Awallimna.route("/forgot_password")
def forgot_password():
    return render_template("forgot_password.html")

@Awallimna.route("/reset_password")
def reset_password():
    return render_template("reset_password.html")

@Awallimna.route("/delete_account")
def delete_account():
    return render_template("delete_account.html")

# =====================================================================
# --- مسارات القصص والمحتوى ---
# =====================================================================
@Awallimna.route("/write_story")
def write_story():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template("write_story.html")

@Awallimna.route("/read_story/<int:story_id>")
def read_story(story_id): # type: ignore
    story = story.query.get_or_404(story_id) # type: ignore
    return render_template("read_story.html", story=story)

@Awallimna.route("/review_story")
def review_story():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template("review_story.html")

@Awallimna.route("/story_functions")
def story_functions():
    return render_template("story_functions.html")

# =====================================================================
# --- مسارات المراكز التعليمية والإدارة ---
# =====================================================================
@Awallimna.route("/accept_educational_center")
def accept_educational_center():
    return render_template("accept_educational_center.html")

@Awallimna.route("/center_profile")
def center_profile():
    return render_template("center_profile.html")

@Awallimna.route("/create_center_account")
def create_center_account():
    return render_template("create_center_account.html")
    
@Awallimna.route("/register_center")
def register_center():
    return render_template("register_center.html")

@Awallimna.route("/sent_educational_center")
def sent_educational_center():
    return render_template("sent_educational_center.html")
    
@Awallimna.route("/teacher_accounts")
def teacher_accounts():
    return render_template("teacher_accounts.html")

@Awallimna.route("/admin_page")
def admin_page():
    return render_template("admin_page.html")

@Awallimna.route("/update_story_status")
def update_story_status():
    return render_template("update_story_status.html")
    
@Awallimna.route("/statistics")
def statistics():
    return render_template("statistics.html")

# =====================================================================
# --- مسارات الصفحات المتنوعة والإعلامية ---
# =====================================================================
@Awallimna.route("/terms_conditions")
def terms_conditions():
    return render_template("terms_conditions.html")

@Awallimna.route("/subscriptions")
def subscriptions():
    return render_template("subscriptions.html")
    
@Awallimna.route("/confirmation_sent_email")
def confirmation_sent_email():
    return render_template("confirmation_sent_email.html")
    
@Awallimna.route("/deleted_confirmation")
def deleted_confirmation():
    return render_template("deleted_confirmation.html")

# =====================================================================
# --- تشغيل التطبيق ---
# =====================================================================
if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    ssl_context = ("cert.pem", "key.pem")  # تأكد من وجود الملفين في نفس مجلد السكربت أو ضع المسار الصحيح
    Awallimna.run(host=host, port=port, debug=True, ssl_context=ssl_context)