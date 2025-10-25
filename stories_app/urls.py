from django.urls import path
from . import views

urlpatterns = [ # type: ignore
    # 🏠 CORE & GENERAL URLs
    # ------------------------------------------------------------------
    path('', views.website, name='website'), # الصفحة الرئيسية # type: ignore
    path('about/', views.about, name='about'), # type: ignore
    path('contact/', views.contact, name='contact'), # type: ignore
    path('privacy/', views.privacy, name='privacy'), # type: ignore
    path('terms/', views.terms_conditions, name='terms_conditions'), # type: ignore
    path('error/', views.error, name='error'), # لصفحات الأخطاء العامة  # type: ignore

    # 👤 AUTHENTICATION & ACCOUNTS URLs
    # ------------------------------------------------------------------
    path('register/', views.register, name='register'), # تسجيل قارئ/كاتب # type: ignore
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), # دالة الخروج (غير مذكورة في القوالب لكن ضرورية) # type: ignore
    path('forgot_password/', views.forgot_password, name='forgot_password'), # type: ignore
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'), # رابط إعادة التعيين يتطلب توكن # type: ignore
    path('delete_account/', views.delete_account, name='delete_account'), # type: ignore

    # 📝 PROFILES & MANAGEMENT URLs
    # ------------------------------------------------------------------
    path('profile/reader/<str:username>/', views.reader_profile, name='reader_profile'), # type: ignore
    path('profile/writer/<str:username>/', views.writer_profile, name='writer_profile'), # type: ignore
    path('subscriptions/', views.subscriptions, name='subscriptions'), # type: ignore

    # 📚 STORIES & CONTENT URLs
    # ------------------------------------------------------------------
    path('story/<int:story_id>/', views.read_story, name='read_story'), # لعرض القصة برقم تعريفي  # type: ignore
    path('story/write/', views.write_story, name='write_story'), # type: ignore
    path('story/edit/<int:story_id>/', views.write_story, name='edit_story'), # لاستخدام نفس دالة الكتابة للتعديل  # type: ignore
    path('story/review/<int:story_id>/', views.review_story, name='review_story'), # type: ignore
    path('story/<int:story_id>/update_status/', views.update_story_status, name='update_story_status'), # type: ignore

    # 🏷️ GENRES & CATEGORIES URLs
    # ------------------------------------------------------------------
    path('categories/', views.category_page, name='category_page'), # صفحة عرض التصنيفات # type: ignore 
    path('category/<str:genre_name>/', views.genre_stories, name='genre_stories'), # لعرض قصص حسب النوع  # type: ignore
    # (يمكن استخدام دالة واحدة (genre_stories) لكل أنواع القصص مثل adventure, horror, إلخ)

    # 🏫 EDUCATIONAL CENTERS URLs
    # ------------------------------------------------------------------
    path('center/register/', views.register_center, name='register_center'), # type: ignore
    path('center/create_account/', views.create_center_account, name='create_center_account'), # type: ignore
    path('center/profile/', views.center_profile, name='center_profile'), # type: ignore
    path('center/teachers/', views.teacher_accounts, name='teacher_accounts'), # type: ignore
    path('center/children/', views.children_accounts, name='children_accounts'), # type: ignore

    # ⚙️ ADMIN & REPORTING URLs
    # ------------------------------------------------------------------
    path('admin_dashboard/', views.admin_page, name='admin_page'), # type: ignore
    path('admin/statistics/', views.statistics, name='statistics'), # type: ignore
    path('admin/accept_center/<int:center_id>/', views.accept_educational_center, name='accept_educational_center'), # type: ignore
]