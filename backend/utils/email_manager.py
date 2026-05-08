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
    :param context_vars: ديكشنري يحتوي على القيم المراد استبدالها + action_url (الرابط في الزر)
    :param sender_type: نوع المرسل (no-reply, support, security, welcome)
    """

    # مسار ملف النصوص
    json_path = os.path.join(settings.BASE_DIR, 'templates', 'emails', 'msg', 'ar.json')

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            full_data = json.load(f)
            email_texts = full_data['ar']['email'][email_key]
    except FileNotFoundError:
        print(f"❌ ملف ar.json غير موجود في: {json_path}")
        return 0
    except KeyError as e:
        print(f"❌ المفتاح {e} غير موجود في ar.json")
        return 0

    # إعداد المرسل
    display_name = f"Oda {sender_type.capitalize()}" if sender_type != 'no-reply' else "Oda"
    from_email = f"{display_name} <{sender_type}@oda.com>"

    # المتغيرات الافتراضية مع ما يمرره المستدعي
    full_context = {
        'appName': 'Oda',
        'supportEmail': 'support@oda.com',
        'securityEmail': 'security@oda.com',
        'action_url': '#',
        **context_vars,
    }

    # استبدال {variable} في نصوص JSON بالقيم الحقيقية
    processed_content = {}
    for key, text in email_texts.items():
        if isinstance(text, str):
            try:
                processed_content[key] = text.format(**full_context)
            except KeyError as e:
                processed_content[key] = text
                print(f"⚠️ المتغير {e} مطلوب في '{email_key}.{key}' ولم يُمرَّر.")

    # تحويل \n إلى <br> في التوقيع حتى يظهر صح في HTML
    if 'signature' in processed_content:
        processed_content['signature'] = processed_content['signature'].replace('\n', '<br>')

    # action_url للزر (يُمرَّر مباشرةً للقالب)
    processed_content['action_url'] = full_context['action_url']

    subject = processed_content.get('subject', f"تنبيه من {full_context['appName']}")

    # قالب HTML واحد لجميع أنواع الإيميلات
    template_path = 'emails/html/welcome.html'

    try:
        html_content = render_to_string(template_path, processed_content)
        text_content = strip_tags(html_content)
    except Exception as e:
        print(f"❌ خطأ في تحميل القالب '{template_path}': {e}")
        return 0

    # الإرسال
    msg = EmailMultiAlternatives(subject, text_content, from_email, [user_email])
    msg.attach_alternative(html_content, "text/html")

    try:
        result = msg.send()
        print(f"✅ إيميل ({email_key}) من {from_email} إلى {user_email}")
        return result
    except Exception as e:
        print(f"❌ فشل الإرسال: {e}")
        return 0
