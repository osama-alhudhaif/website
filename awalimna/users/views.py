from django.shortcuts import render
import datetime

def profile_view(request):
    # 1. هذا هو "السياق" (قاموس بايثون)
    context = {
        'username': 'أحمد علي',                  # مثال لنص (String)
        'age': 28,                               # مثال لرقم (Integer)
        'skills': ['بايثون', 'جانغو', 'CSS'],    # مثال لقائمة (List)
        'profile_details': {                     # مثال لقاموس (Dictionary)
            'job': 'مطور ويب',
            'country': 'السعودية'
        },
        'join_date': datetime.date(2023, 1, 15) # (سنستخدمه لاحقاً مع الفلاتر)
    }
    
    # 2. نمرر السياق إلى القالب
    return render(request, 'profile.html', context) 