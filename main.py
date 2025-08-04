from flask import Flask, render_template, request
from typing import Dict, Any
from center_country import countries
from center_language import languages

app = Flask(__name__, template_folder="templates")

# Context processor عشان نمرر current_user للقوالب (بدون flask-login)
@app.context_processor # type: ignore
def inject_current_user() -> Dict[str, Any]:
    return dict(current_user=None)

# قائمة الصفحات للمرجعية
page_list = [
    "accept_educational_center",
    "adventure",
    "center_profile", 
    "children",
    "comedy",
    "confirmation_sent_email",
    "create_center_account",
    "crime_investigation",
    "deleted_confirmation",
    "delete_account",
    "drama",
    "fantasy",
    "fiction",
    "historic",
    "historical",
    "horror",
    "reader_profile",
    "reset_password",
    "romance",
    "science_fiction",
    "statistics",
    "subscriptions",
    "terms_conditions",
    "theft",
    "war",
    "writer_profile",
    "write_story",
    "forgot_password",
    "review_story",
    "admin_page",
    "story_functions",
    "header",
    "footer",
    "paths",
    "read_story",
    "teacher_accounts",
    "sent_educational_center",
    "update_story_status",
    "register_center"
]

@app.route("/")
def home():
    return render_template("website.html", countries=countries, languages=languages)

# Add specific routes for commonly referenced pages
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username_or_email = request.form.get("username_or_email")
        password = request.form.get("password")
        
        error = None
        if not username_or_email or not password:
            error = "يرجى إدخال اسم المستخدم/الإيميل وكلمة المرور"
        
        if error:
            return render_template("login.html", countries=countries, languages=languages, error=error)
        
        success = "تم تسجيل الدخول بنجاح!"
        return render_template("login.html", countries=countries, languages=languages, success=success)
    
    return render_template("login.html", countries=countries, languages=languages)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        full_name = request.form.get("full_name") # type: ignore
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        user_type = request.form.get("user_type") # type: ignore
        gender = request.form.get("gender") # type: ignore
        birth_date = request.form.get("birth_date") # type: ignore
        country = request.form.get("country") # type: ignore
        language = request.form.get("language") # type: ignore
        terms = request.form.get("terms")

        error = None
        if not terms:
            error = "يجب الموافقة على الشروط والأحكام"
        elif not username or not email or not password:
            error = "يرجى تعبئة الحقول الأساسية"
        elif password != confirm_password:
            error = "كلمتا المرور غير متطابقتين"

        if error:
            return render_template("register.html", countries=countries, languages=languages, error=error)
        
        success = "تم التسجيل بنجاح!"
        return render_template("register.html", countries=countries, languages=languages, success=success)

    return render_template("register.html", countries=countries, languages=languages)

# Generic route for other pages - fixed the condition
@app.route("/<page_name>")
def render_page(page_name): # type: ignore
    if page_name in page_list:
        return render_template(f"{page_name}.html", countries=countries, languages=languages)
    else:
        return render_template("404.html", countries=countries, languages=languages), 404

# Error handlers
@app.errorhandler(404)
def page_not_found(e): # type: ignore
    return render_template("404.html", countries=countries, languages=languages), 404

@app.errorhandler(500)
def internal_server_error(e): # type: ignore
    return render_template("500.html", countries=countries, languages=languages), 500

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    app.run(host=host, port=port, debug=True)