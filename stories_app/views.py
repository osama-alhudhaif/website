from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpRequest, HttpResponse # type: ignore

# --- 🏠 CORE & GENERAL VIEWS ---
def website(request: HttpRequest) -> HttpResponse:
    """الصفحة الرئيسية - تعرض قالب website.html"""
    return render(request, 'core_general/website.html')

def about(request: HttpRequest) -> HttpResponse:
    """صفحة عن الموقع - تعرض قالب about.html"""
    return render(request, 'core_general/about.html')

def contact(request: HttpRequest) -> HttpResponse:
    """صفحة تواصل معنا - تعرض قالب contact.html"""
    return render(request, 'core_general/contact.html')

def privacy(request: HttpRequest) -> HttpResponse:
    """صفحة سياسة الخصوصية - تعرض قالب privacy.html"""
    return render(request, 'core_general/privacy.html')

def terms_conditions(request: HttpRequest) -> HttpResponse:
    """صفحة شروط وأحكام الاستخدام - تعرض قالب terms_conditions.html"""
    return render(request, 'core_general/terms_conditions.html')

def error(request: HttpRequest) -> HttpResponse:
    """صفحة خطأ عام - تعرض قالب error.html"""
    return render(request, 'core_general/error.html')

# --- 👤 AUTHENTICATION & ACCOUNTS VIEWS ---
def register(request: HttpRequest) -> HttpResponse:
    """تسجيل حساب جديد - تعرض قالب register.html"""
    return render(request, 'auth_accounts/register.html')

def login_view(request: HttpRequest) -> HttpResponse:
    """تسجيل الدخول - تعرض قالب login.html"""
    return render(request, 'auth_accounts/login.html')

def logout_view(request: HttpRequest):
    """الخروج من الحساب - توجيه للصفحة الرئيسية"""
    # يجب إضافة منطق الخروج هنا لاحقًا
    return redirect('website') 

def forgot_password(request: HttpRequest) -> HttpResponse:
    """نسيت كلمة المرور - تعرض قالب forgot_password.html"""
    return render(request, 'auth_accounts/forgot_password.html')

def reset_password(request: HttpRequest, uidb64, token) -> HttpResponse:  # type: ignore
    """إعادة تعيين كلمة المرور - تعرض قالب reset_password.html"""
    # يجب إضافة منطق التحقق من التوكن هنا لاحقًا
    return render(request, 'auth_accounts/reset_password.html')

def delete_account(request: HttpRequest) -> HttpResponse:
    """حذف الحساب - تعرض قالب delete_account.html"""
    return render(request, 'auth_accounts/delete_account.html')

# --- 📝 PROFILES & MANAGEMENT VIEWS ---
def reader_profile(request: HttpRequest, username) -> HttpResponse: # type: ignore
    """الملف الشخصي للقارئ - تعرض قالب reader_profile.html"""
    return render(request, 'profiles_management/reader_profile.html')

def writer_profile(request: HttpRequest, username) -> HttpResponse: # type: ignore
    """الملف الشخصي للكاتب - تعرض قالب writer_profile.html"""
    return render(request, 'profiles_management/writer_profile.html')

def subscriptions(request: HttpRequest) -> HttpResponse:
    """إدارة الاشتراكات - تعرض قالب subscriptions.html"""
    return render(request, 'profiles_management/subscriptions.html')

# --- 📚 STORIES & CONTENT VIEWS ---
def read_story(request: HttpRequest, story_id) -> HttpResponse: # type: ignore
    """عرض القصة - تعرض قالب read_story.html"""
    return render(request, 'stories_content/read_story.html')

def write_story(request: HttpRequest, story_id=None) -> HttpResponse: # type: ignore
    """كتابة/تعديل قصة - تعرض قالب write_story.html"""
    return render(request, 'stories_content/write_story.html')

def review_story(request: HttpRequest, story_id) -> HttpResponse: # type: ignore
    """مراجعة القصة - تعرض قالب review_story.html"""
    return render(request, 'stories_content/review_story.html')

def update_story_status(request: HttpRequest, story_id) -> HttpResponse: # type: ignore
    """تحديث حالة القصة - تعرض قالب update_story_status.html"""
    return render(request, 'stories_content/update_story_status.html')

# --- 🏷️ GENRES & CATEGORIES VIEWS ---
def category_page(request: HttpRequest) -> HttpResponse:
    """صفحة عرض التصنيفات - تعرض قالب category_page.html"""
    return render(request, 'stories_content/category_page.html') 

def genre_stories(request: HttpRequest, genre_name) -> HttpResponse: # type: ignore
    """عرض القصص حسب النوع - تعرض القالب الخاص بالنوع"""
    # سيحاول Django إيجاد القالب في مسار مثل genres/horror.html
    return render(request, f'genres/{genre_name}.html')

# --- 🏫 EDUCATIONAL CENTERS VIEWS ---
def register_center(request: HttpRequest) -> HttpResponse:
    """تسجيل مركز تعليمي - تعرض قالب register_center.html"""
    return render(request, 'educational_centers/register_center.html')

def create_center_account(request: HttpRequest) -> HttpResponse:
    """إنشاء حساب المركز - تعرض قالب create_center_account.html"""
    return render(request, 'educational_centers/create_center_account.html')

def center_profile(request: HttpRequest) -> HttpResponse:
    """الملف الشخصي للمركز - تعرض قالب center_profile.html"""
    return render(request, 'educational_centers/center_profile.html')

def teacher_accounts(request: HttpRequest) -> HttpResponse:
    """إدارة حسابات المعلمين - تعرض قالب teacher_accounts.html"""
    return render(request, 'educational_centers/teacher_accounts.html')

def children_accounts(request: HttpRequest) -> HttpResponse:
    """إدارة حسابات الأطفال - تعرض قالب children.html"""
    return render(request, 'educational_centers/children.html')

# --- ⚙️ ADMIN & REPORTING VIEWS ---
def admin_page(request: HttpRequest) -> HttpResponse:
    """لوحة تحكم المشرف - تعرض قالب admin_page.html"""
    return render(request, 'admin_reporting/admin_page.html')

def statistics(request: HttpRequest) -> HttpResponse:
    """عرض الإحصائيات - تعرض قالب statistics.html"""
    return render(request, 'admin_reporting/statistics.html')

def accept_educational_center(request: HttpRequest, center_id) -> HttpResponse: # type: ignore
    """قبول مركز تعليمي - تعرض قالب accept_educational_center.html"""
    return render(request, 'admin_reporting/accept_educational_center.html')