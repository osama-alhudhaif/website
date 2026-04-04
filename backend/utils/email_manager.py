import json
import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_oda_email(user_email, email_key, context_vars, sender_type='no-reply'):
    """
    دالة إرسال الإيميلات الاحترافية لمنصة Oda
    :param user_email: بريد المستلم
    :param email_key: المفتاح الموجود في ar.json (مثل 'welcome', 'loginAlert')
    :param context_vars: ديكشنري يحتوي على القيم المراد استبدالها (userName, link, إلخ)
    :param sender_type: نوع المرسل (no-reply, support, security, welcome)
    """
    
    # 1. تحديد مسار ملف النصوص ar.json (موجود خارج مجلد backend بمرة واحدة)
    json_path = os.path.join(settings.BASE_DIR, '..', 'locales', 'ar.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            full_data = json.load(f)
            # الوصول لنصوص النوع المحدد من الإيميلات في القسم العربي
            email_texts = full_data['ar']['email'][email_key]
    except (FileNotFoundError, KeyError) as e:
        print(f"❌ خطأ في تحميل بيانات الإيميل لـ {email_key}: {e}")
        return 0

    # 2. إعداد المرسل بناءً على النوع (بريد @oda.com الرسمي)
    # مثال: sender_type='security' سيجعل المرسل 'Oda Security <security@oda.com>'
    display_name = f"Oda {sender_type.capitalize()}" if sender_type != 'no-reply' else "Oda"
    from_email = f"{display_name} <{sender_type}@oda.com>"

    # 3. دمج المتغيرات مع النصوص (Formatting)
    # إضافة متغيرات عامة لمنصة Oda ليتم استبدالها في النصوص تلقائياً
    full_context = {
        'appName': 'Oda',
        'supportEmail': 'support@oda.com',
        'securityEmail': 'security@oda.com',
        **context_vars
    }

    # معالجة النصوص واستبدال الأقواس {userName} بالقيم الحقيقية
    processed_content = {}
    for key, text in email_texts.items():
        if isinstance(text, str):
            try:
                processed_content[key] = text.format(**full_context)
            except KeyError as e:
                # في حال نسيان تمرير متغير مطلوب في context_vars
                processed_content[key] = text
                print(f"⚠️ تحذير: المتغير {e} مطلوب في نص {email_key} ولم يتم تمريره.")
    
    # عنوان الرسالة
    subject = processed_content.get('subject', f"تنبيه من {full_context['appName']}")

    # 4. دمج النصوص مع قالب الـ HTML (الناتج من MJML)
    # يبحث Django عن القالب في templates/emails/html/welcome.html مثلاً
    template_path = f'emails/html/{email_key}.html'
    
    try:
        html_content = render_to_string(template_path, processed_content)
        text_content = strip_tags(html_content) # نسخة نصية احتياطية
    except Exception as e:
        print(f"❌ خطأ في معالجة قالب الـ HTML: {e}")
        return 0

    # 5. الإرسال الفعلي
    msg = EmailMultiAlternatives(
        subject, 
        text_content, 
        from_email, 
        [user_email]
    )
    msg.attach_alternative(html_content, "text/html")
    
    # تنفيذ الإرسال (سيوضع في التيرمينال حالياً بسبب إعداد ConsoleBackend)
    try:
        result = msg.send()
        print(f"✅ تم إرسال إيميل ({email_key}) بنجاح من {from_email} إلى {user_email}")
        return result
    except Exception as e:
        print(f"❌ فشل إرسال الإيميل: {e}")
        return 0