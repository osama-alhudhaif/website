# -*- coding: utf-8 -*-
# اسم الملف: config_manager.py
# الوصف: يحتوي هذا الملف على إعدادات التكوين الأساسية، الثوابت،
#        وهيكل البيانات الوصفي لمنصة "عوالمنا".

# ==============================================================================
# القسم الأول: إعدادات الاتصال الأساسية والثوابت
# ==============================================================================

# --- إعدادات الاتصال بقاعدة البيانات ---
MYSQL_DB_NAME = "awallimna_db"
SQLITE_DB_FILE = "awallimna.db"
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""  # يجب تعيين كلمة المرور المناسبة في بيئة الإنتاج

# ---------------------------------------

# ==============================================================================
# القسم الثاني: قاموس الإعدادات والمعلومات المرجعية (config_data)
# ==============================================================================

# القاموس التالي يمثل الهيكل البرمجي للمعلومات الوصفية والقواعد.
# استخدم هذا القاموس للوصول إلى الإعدادات والقواعد برمجياً في أجزاء أخرى من التطبيق.
config_data = { # pyright: ignore[reportUnknownVariableType]
    "preamble": """مرحباً بك في ملف الإعدادات والقوانين الخاص بمنصة "عوالمنا".
هذا الملف يحتوي على التعريفات الأساسية، هياكل البيانات، وقواعد الاستخدام.""",

    "terms": {
        "database_technologies": {
            "sqlite3": "مكتبة بايثون للتعامل مع قواعد بيانات SQLite.",
            "mysql.connector": "مكتبة بايثون للتعامل مع قواعد بيانات MySQL.",
            "Error": "فئة تستخدم للتعامل مع الأخطاء في mysql.connector.",
            "connect": "دالة لإنشاء اتصال بقاعدة البيانات.",
            "cursor": "كائن يستخدم لتنفيذ استعلامات SQL.",
            "MySQL": "نظام إدارة قواعد البيانات العلائقية.",
            "MySQL-models": "هياكل أو نماذج البيانات المستخدمة في قاعدة بيانات MySQL.",
            "SQLite3": "نظام إدارة قواعد البيانات العلائقية.",
            "SQLite3-models": "هياكل أو نماذج البيانات المستخدمة في قاعدة بيانات SQLite3."
        },
        "suggested_classes": {
            "MySQLDatabase": "كلاس قد يمثل التعامل مع قاعدة بيانات MySQL.",
            "SQLite3Database": "كلاس قد يمثل التعامل مع قاعدة بيانات SQLite3.",
            "Database": "كلاس أساسي قد يمثل قاعدة بيانات عامة.",
            "create-database": "إشارة إلى دالة محتملة لإنشاء قاعدة بيانات جديدة."
        },
        "roles_and_users": {
            "reader": "القارئ للقصص والروايات.",
            "author": "الكاتب للقصص والروايات.",
            "Education-Center": "مركز تعليمي.",
            "Education-Center-teacher": "معلم تابع لمركز تعليمي.",
            "Education-Center-student": "طالب تابع لمركز تعليمي.",
            "role": "دور المستخدم العام في المشروع.",
            "admin_reader": "قارئ إداري، لديه صلاحيات إضافية.",
            "admin_author": "كاتب إداري، لديه صلاحيات إضافية.",
            "super-admin-reader": "قارئ إداري ذو صلاحيات خاصة (Super Admin Reader).",
            "super-admin-author": "كاتب إداري ذو صلاحيات خاصة (Super Admin author).",
            "role_list": ['reader', 'admin_reader', 'super-admin-reader', 'author', 'admin_author', 'super-admin-author', 'Education-Center', 'Education-Center-teacher', 'Education-Center-student'],
            "role_user": "الحقل الذي يحدد دور المستخدم المسجل."
        },
        "admin_terms": {
            # تم تصحيح الكلمة من ruler®ulation إلى regulation
            "regulation / Rulers & Regulations": "القوانين واللوائح المستخدمة في المشروع.",
            "regulation-list_reference": "النص الكامل للقوانين واللوائح (مُدرج في قسم 'rulers_and_regulations').",
            "Top Management / الإدارة العليا": "تشير إلى مالك المشروع/المؤسس (osamh64@awalimna.com) أو من ينوب عنه رسمياً."
        }
    },

    "data_models": {
        "notes": [
            "ملاحظة هامة: هياكل البيانات أدناه هي للتوثيق والتصميم فقط.",
            "لا تقوم بإنشاء جداول قاعدة البيانات تلقائياً من هذا القاموس.",
            "لإنشاء الجداول، يجب استخدام أوامر SQL CREATE TABLE بشكل منفصل أو استخدام ORM (Object-Relational Mapper).",
            "---",
            "بناءً على طلبك بجعل كل شيء (not null)، تم تحديث الحقول الأساسية.",
            "لكن، إجبار المستخدم على إدخال *كل* معلومة (مثل الهاتف والعنوان وتاريخ الميلاد والجنس) قد يكون غير عملي ويقلل من تجربة المستخدم.",
            "يوصى بجعل الحقول التعريفية والأساسية فقط (not null) وترك الحقول الثانوية اختيارية (nullable).",
            "الحقول أدناه تعكس مزيجاً من الضروري (not null) والموصى به كـ (nullable) للتوازن.",
            "---",
            "تلميح تصميمي: قد يكون من الأفضل دمج جدولي `readers` و `authors` في جدول واحد `users` مع نظام أدوار مرن (ربما جدول `user_roles` منفصل) لتبسيط الإدارة والسماح للمستخدمين بأدوار متعددة مستقبلاً إذا لزم الأمر."
        ],
        "tables": {
            "readers": {
                "description": "1. بيانات القارئ (reader)",
                "table_name_comment": "# جدول: readers (أو يمكن دمجه مع جدول users)",
                "columns": {
                    "id": {"type": "INT", "constraints": "PRIMARY KEY AUTO_INCREMENT UNIQUE", "comment": "R-IDnum"},
                    "username": {"type": "VARCHAR(255)", "constraints": "UNIQUE NOT NULL"},
                    "password": {"type": "VARCHAR(255)", "constraints": "NOT NULL", "comment": "يجب تخزينها مشفرة (hashed)"},
                    "email": {"type": "VARCHAR(255)", "constraints": "UNIQUE NOT NULL"},
                    "address": {"type": "TEXT", "constraints": "NULL", "comment": "(اختياري)"},
                    "date_of_birth": {"type": "DATE", "constraints": "NULL", "comment": "(اختياري)"},
                    "gender": {"type": "VARCHAR(10)", "constraints": "NULL", "comment": "('male', 'female', 'other') (اختياري)"},
                    "level": {"type": "VARCHAR(50)", "constraints": "NULL", "comment": "(اختياري)"},
                    "country": {"type": "VARCHAR(100)", "constraints": "NULL", "comment": "(اختياري)"},
                    "role_user": {"type": "VARCHAR(50)", "constraints": "NOT NULL DEFAULT 'reader'", "comment": "Values: {'reader', 'admin_reader', 'super-admin-reader'}"},
                    "registration_date": {"type": "DATETIME", "constraints": "NOT NULL DEFAULT CURRENT_TIMESTAMP"},
                    "appointed_by_super_admin_id": {"type": "INT", "constraints": "NULL", "comment": "FOREIGN KEY REFERENCES (ID in a relevant admin/user table)"} # توضيح المرجع
                }
            },
            "authors": {
                "description": "2. بيانات الكاتب (author)",
                "table_name_comment": "# جدول: authors (أو يمكن دمجه مع جدول users)",
                "columns": {
                    "id": {"type": "INT", "constraints": "PRIMARY KEY AUTO_INCREMENT UNIQUE", "comment": "W-IDnum"},
                    "username": {"type": "VARCHAR(255)", "constraints": "UNIQUE NOT NULL"},
                    "password": {"type": "VARCHAR(255)", "constraints": "NOT NULL", "comment": "مشفرة"},
                    "email": {"type": "VARCHAR(255)", "constraints": "UNIQUE NOT NULL"},
                    "address": {"type": "TEXT", "constraints": "NULL", "comment": "(اختياري)"},
                    "date_of_birth": {"type": "DATE", "constraints": "NULL", "comment": "(اختياري)"},
                    "gender": {"type": "VARCHAR(10)", "constraints": "NULL", "comment": "(اختياري)"},
                    "level": {"type": "VARCHAR(50)", "constraints": "NULL", "comment": "(اختياري)"},
                    "country": {"type": "VARCHAR(100)", "constraints": "NULL", "comment": "(اختياري)"},
                    "role_user": {"type": "VARCHAR(50)", "constraints": "NOT NULL DEFAULT 'author'", "comment": "Values: {'author', 'admin-author', 'super-admin-author'}"},
                    "registration_date": {"type": "DATETIME", "constraints": "NOT NULL DEFAULT CURRENT_TIMESTAMP"},
                    "appointed_by_super_admin_id": {"type": "INT", "constraints": "NULL", "comment": "FOREIGN KEY REFERENCES (ID in a relevant admin/user table)"} # توضيح المرجع
                },
                "relationship_notes": [
                    "story_list: علاقة One-to-Many. لا تخزن كقائمة في هذا الجدول.",
                    "يتم تحقيقها عبر جدول 'stories' الذي يحتوي على حقل 'author_id' (INT, NOT NULL, FOREIGN KEY REFERENCES authors(id)).",
                    "معرف القصة الفريد (مثل W-IDnum-S-IDnum) يتم إنشاؤه برمجياً عند الحاجة."
                ]
            },
            "stories": {
                "description": "3. بيانات القصة (story)",
                "table_name_comment": "# جدول: stories",
                "columns": {
                    "id": {"type": "INT", "constraints": "PRIMARY KEY AUTO_INCREMENT UNIQUE", "comment": "S-IDnum"},
                    "title": {"type": "VARCHAR(255)", "constraints": "NOT NULL"},
                    "content": {"type": "LONGTEXT", "constraints": "NOT NULL", "comment": "مناسب للنصوص الطويلة"}, # LONGTEXT أفضل للقصص الطويلة
                    "author_id": {"type": "INT", "constraints": "NOT NULL", "comment": "FOREIGN KEY REFERENCES authors(id)"}, # الربط بالكاتب
                    "creation_date": {"type": "DATETIME", "constraints": "NOT NULL DEFAULT CURRENT_TIMESTAMP"},
                    "last_updated": {"type": "DATETIME", "constraints": "NULL", "comment": "يُحدّث عند التعديل"},
                    "status": {"type": "VARCHAR(20)", "constraints": "NOT NULL DEFAULT 'pending'", "comment": "Possible values: 'pending', 'approved', 'rejected', 'suspended'"}, # تم إضافة suspended وتوضيح القيم
                    "approved_by_admin_id": {"type": "INT", "constraints": "NULL", "comment": "FOREIGN KEY REFERENCES (ID in a relevant admin/user table)"}, # يجب أن يكون لديه دور أدمن
                    "genre": {"type": "VARCHAR(100)", "constraints": "NULL"}, # حقل لنوع القصة (مغامرة، دراما، إلخ) (اختياري)
                    "slug": {"type": "VARCHAR(255)", "constraints": "UNIQUE NULL", "comment": "For SEO friendly URLs (اختياري, فريد إذا وُجد)"} # حقل اختياري لـ URL
                },
                "generation_note": "معرّف القصة الكامل (مثل W-IDnum-S-IDnum) يُنشأ برمجياً عند الحاجة للعرض أو في الـ URLs."
            },
            "education_centers": {
                "description": "4. بيانات المراكز التعليمية (Education Centers)",
                "table_name_comment": "# جدول: education_centers",
                "columns": {
                    "id": {"type": "INT", "constraints": "PRIMARY KEY AUTO_INCREMENT UNIQUE", "comment": "EC-IDnum"},
                    "name": {"type": "VARCHAR(255)", "constraints": "NOT NULL"},
                    "email": {"type": "VARCHAR(255)", "constraints": "UNIQUE NOT NULL"},
                    "password": {"type": "VARCHAR(255)", "constraints": "NOT NULL", "comment": "مشفرة"},
                    "address": {"type": "TEXT", "constraints": "NOT NULL"},
                    "phone": {"type": "VARCHAR(20)", "constraints": "NOT NULL"},
                    "license_number": {"type": "VARCHAR(100)", "constraints": "UNIQUE NOT NULL", "comment": "رقم الترخيص"},
                    "status": {"type": "VARCHAR(20)", "constraints": "NOT NULL DEFAULT 'pending'", "comment": "pending, approved, rejected"},
                    "role_user": {"type": "VARCHAR(50)", "constraints": "NOT NULL DEFAULT 'Education-Center'"},
                    "registration_date": {"type": "DATETIME", "constraints": "NOT NULL DEFAULT CURRENT_TIMESTAMP"},
                    "approved_by_admin_id": {"type": "INT", "constraints": "NULL", "comment": "FOREIGN KEY REFERENCES (ID in a relevant admin/user table)"}
                }
            }
        },
        "suggested_additional_tables": {
            "teachers": "جدول للمعلمين: id, user_id (FK to users), center_id (FK to education_centers), etc.",
            "students": "جدول للطلاب: id, user_id (FK to users), center_id (FK to education_centers), etc.",
            "users": "جدول موحد للمستخدمين: id, username, password, email, role, etc.",
            "user_roles": "جدول ربط للأدوار المتعددة: user_id, role_name"
        }
    },

    "project_pages": {
        "description": "صفحات المشروع و البيانات المستخدمة والبيانات المطلوبة (للتوثيق):",
        "pages": {
            "accept_educational_center.html": "صفحة قبول مركز التعليم (للأدمن)",
            "admin_page.html": "صفحة لوحة تحكم الأدمن (العادي والسوبر)",
            # ... (يمكن إضافة باقي الصفحات هنا للتوثيق) ...
            "author_profile.html": "صفحة ملف تعريف الكاتب (عامة)",
            "write_story.html": "صفحة كتابة/تعديل قصة (للكاتب)"
        }
    },

    # هذا القسم هو الصحيح لإدارة البريد الإلكتروني
    "emails": {
        "description": "رسائل البريد الإلكتروني المخصصة (emails) وكل بريد والاستعمال الخاص فيه:",
        "addresses": {
            "osamh64@awalimna.com": "بريد المالك/المؤسس (خاص وسري للتواصل المباشر مع الإدارة العليا).",
            "awalimna@awalimna.com": "البريد الرسمي للمنصة، يستخدم للمعاملات الرسمية والتواصل الصادر من الموقع لجهات أو بيانات رسمية.",
            "help@awalimna.com": "البريد الخاص بالمساعدة والدعم الفني للمستخدمين والرد على استفساراتهم.",
            "gifts@awalimna.com": "البريد المستخدم للتواصل الصادر من الموقع بخصوص الهدايا والمكافآت للمستخدمين بناءً على تفاعلهم أو مسابقات.",
            "noreply@awalimna.com": "بريد لا يرد عليه (No-Reply)، يستخدم للإشعارات الآلية (مثل تأكيد التسجيل، استعادة كلمة المرور، تحديثات الحالة).",
        },
        "notes": [
            "يجب التأكد من أن خادم البريد الإلكتروني مهيأ لإرسال رسائل من هذه العناوين بشكل صحيح.",
            "قد تحتاج إلى إعداد سجلات SPF و DKIM لضمان وصول الرسائل."
        ]
    },

    "url_structures": {
        "description": "هياكل الروابط (URL Patterns) المقترحة للموقع:",
        "patterns": {
            # --- General & Auth ---
            "home": "awallimna/home",                                 # الصفحة الرئيسية
            "login": "awallimna/login",                           # صفحة تسجيل الدخول
            "logout": "awallimna/logout",                         # رابط تسجيل الخروج (عادة لا يكون صفحة، بل عملية)
            "register": "awallimna/register",                     # صفحة التسجيل العام (قارئ/كاتب)
            "register_center": "awallimna/register/center",       # صفحة تسجيل مركز تعليمي
            "forgot_password": "awallimna/forgot-password",       # صفحة نسيت كلمة المرور
            "reset_password": "awallimna/reset-password/<token>", # صفحة إعادة تعيين كلمة المرور (تحتاج توكن)
            # --- Profiles & Settings ---
            "reader_profile": "awallimna/profile/reader/@<username>", # ملف تعريف القارئ (باستخدام اسم المستخدم)
            "author_profile": "awallimna/profile/author/@<username>", # ملف تعريف الكاتب
            "center_profile": "awallimna/profile/center/<center_slug_or_id>", # ملف تعريف المركز (باستخدام ID أو اسم فريد)
            "user_settings": "awallimna/settings",                 # صفحة الإعدادات الرئيسية للمستخدم
            "edit_profile": "awallimna/settings/profile",          # صفحة تعديل الملف الشخصي
            "change_password": "awallimna/settings/password",      # صفحة تغيير كلمة المرور
            "delete_account": "awallimna/settings/delete-account", # صفحة حذف الحساب
            # --- Story ---
            "write_story": "awallimna/author/stories/new",        # صفحة كتابة قصة جديدة
            "edit_story": "awallimna/author/stories/edit/<story_id>", # صفحة تعديل قصة موجودة
            "my_stories": "awallimna/author/stories",             # قائمة قصص الكاتب
            "read_story": "awallimna/story/<story_slug_or_id>",   # صفحة قراءة قصة (استخدام slug أفضل لـ SEO)
            "stories_by_genre": "awallimna/stories/genre/<genre_slug>", # عرض القصص حسب النوع
            "all_stories": "awallimna/stories",                   # استعراض كل القصص (مع ترقيم صفحات)
            # --- Search ---
            "search_results": "awallimna/search",                 # صفحة نتائج البحث (المعاملات في query string ?q=...)
            # --- Admin ---
            "admin_dashboard": "awallimna/admin",                 # لوحة تحكم الأدمن
            "admin_users": "awallimna/admin/users",               # إدارة المستخدمين (للأدمن)
            "admin_stories": "awallimna/admin/stories",           # إدارة القصص (للأدمن)
            "admin_centers": "awallimna/admin/centers",           # إدارة المراكز (للأدمن)
            "admin_settings": "awallimna/admin/settings",         # إعدادات إدارية أخرى
            # --- Static Pages ---
            "terms_conditions": "awallimna/terms",                # صفحة الشروط والأحكام
            "privacy_policy": "awallimna/privacy",                # صفحة سياسة الخصوصية
            "about_us": "awallimna/about",                        # صفحة عنا
            "contact_us": "awallimna/contact"                     # صفحة اتصل بنا
        },
        "notes": [
            "العناصر بين <> هي متغيرات ديناميكية في الرابط (مثل <username>, <story_id>, <token>, <genre_slug>).",
            "يفضل استخدام 'slug' (جزء نصي فريد مشتق من العنوان أو الاسم) في الروابط لتحسين SEO حيثما أمكن.",
            "هذه مجرد أمثلة مقترحة، يمكن تعديلها وتوسيعها حسب تصميم التطبيق الفعلي.",
            "استخدم أسماء ذات معنى باللغة الإنجليزية لأسماء المتغيرات في الكود الفعلي للـ routing (مثل `user_id`, `story_slug`)."
        ]
    },

    "rulers_and_regulations": {
        "title": "قواعد وقوانين منصة \"عوالمنا\" للقصص والروايات (Rulers & Regulations) -- النسخة المحدثة --",
        "reference_comment": "# النص الكامل موجود في المتغير 'text' أدناه.",
        "text": """
##############################################################################
#                                                                            #
#                      بسم الله نبدأ،،                                      #
#                                                                            #
#   قواعد وقوانين منصة "عوالمنا" للقصص والروايات (Rulers & Regulations)   #
#                      -- النسخة المحدثة --                                 #
#                                                                            #
##############################################################################

**مقدمة:**

أهلاً وسهلاً بكم جميعاً في منصة "عوالمنا"، بيتكم الرقمي للإبداع القصصي ومشاركة الحكايات. سواء كنتم قراءً شغوفين (readers)، أو كتاباً ملهمين (authors)، أو جزءاً من مركز تعليمي (Education-Center) يسعى لتنمية المواهب، هذه القواعد وُضعت لضمان بيئة آمنة، محترمة، ومُثرية للجميع. نرجو منكم قراءتها بعناية والالتزام بها.

**1. المبادئ العامة:**

1.1. **الاحترام المتبادل:** التعامل باحترام هو أساس مجتمعنا. يُمنع منعاً باتاً التنمر، الإساءة، التشهير، خطاب الكراهية، أو أي شكل من أشكال التمييز ضد أي مستخدم أو مجموعة.
1.2. **المحتوى الهادف:** نشجع على نشر المحتوى الإبداعي الأصيل والهادف الذي يثري القارئ العربي.
1.3. **الملكية الفكرية:** يجب أن يكون المحتوى المنشور (القصص، التعليقات، إلخ) من إبداعك الخاص أو لديك الحقوق الكاملة لنشره. يُمنع سرقة المحتوى أو انتهاك حقوق الطبع والنشر للآخرين. عند الاقتباس، يجب ذكر المصدر بوضوح.
1.4. **الالتزام بالقوانين:** يجب الالتزام بالقوانين المعمول بها في بلد المستخدم وفي القوانين الدولية المتعلقة بالنشر الإلكتروني وحقوق الملكية الفكرية.
1.5. **البيئة الآمنة:** يُمنع نشر أي محتوى إباحي، عنيف بشكل مفرط، أو يروج لأنشطة غير قانونية أو خطرة.

**2. قواعد خاصة بالكتاب (authors):**

2.1. **أصالة المحتوى:** القصص والروايات المنشورة يجب أن تكون من تأليفك الأصلي.
2.2. **جودة المحتوى:** نسعى لتقديم محتوى جيد للقراء. يُفضل مراجعة النصوص لغوياً وإملائياً قبل النشر.
2.3. **التصنيف المناسب:** يرجى تصنيف قصصك ضمن النوع (Genre) المناسب لتسهيل وصول القراء إليها.
2.4. **عدم التحايل:** يُمنع استخدام أساليب التحايل لزيادة المشاهدات أو التقييمات بشكل غير حقيقي.
2.5. **حقوق النشر:** أنت تحتفظ بحقوق النشر لقصصك، ولكن بنشرك على "عوالمنا"، فإنك تمنح المنصة ترخيصاً غير حصري لعرض وتوزيع قصتك ضمن خدمات المنصة.
2.6. **الموافقة الإدارية:** قد تخضع القصص الجديدة أو المعدلة لمراجعة إدارية (admin_author أو super-admin-author) قبل الموافقة على نشرها لضمان التزامها بالقواعد. حالات القصة الممكنة: (pending, approved, rejected, suspended).

**3. قواعد خاصة بالقراء (Readers):**

3.1. **التفاعل البناء:** نشجع على ترك التعليقات والتقييمات البناءة التي تفيد الكاتب وتثري النقاش.
3.2. **الابتعاد عن الإساءة:** يُمنع استخدام التعليقات لمهاجمة الكاتب أو القراء الآخرين.
3.3. **الإبلاغ عن المخالفات:** إذا وجدت محتوى أو سلوكاً مخالفاً للقواعد، يرجى استخدام أدوات الإبلاغ المتوفرة أو التواصل مع الدعم الفني (help@awalimna.com).

**4. قواعد خاصة بالمراكز التعليمية (Education-Centers):**

4.1. **الهدف التعليمي:** يجب أن يكون استخدام المنصة من قبل المراكز التعليمية بهدف تعليمي واضح، مثل تدريب الطلاب على الكتابة، تشجيع القراءة، أو تنظيم مسابقات إبداعية.
4.2. **بيانات صحيحة:** يجب تقديم بيانات صحيحة عند تسجيل المركز (اسم المركز، المسؤول، البريد الإلكتروني).
4.3. **إدارة الحسابات:** المركز مسؤول عن إدارة حسابات المعلمين (Education-Center-teacher) والطلاب (Education-Center-student) التابعين له وضمان التزامهم بقواعد المنصة.
4.4. **خصوصية الطلاب:** يجب الالتزام بسياسات حماية خصوصية الطلاب، خاصة القاصرين منهم، والحصول على الموافقات اللازمة إذا تطلب الأمر.
4.5. **الموافقة على التسجيل:** يخضع تسجيل المراكز التعليمية لموافقة الإدارة العليا (Top Management) لضمان جديتها وملاءمتها لأهداف المنصة. حالة الطلب: (pending, approved, rejected).

**5. الأدوار الإدارية والصلاحيات:**

5.1. **الأدوار:** المنصة تحتوي على أدوار إدارية مختلفة (admin_reader, admin_author, super-admin-reader, super-admin-author) بصلاحيات محددة لإدارة المحتوى والمستخدمين.
5.2. **التعيين:** يتم تعيين الأدوار الإدارية من قبل الإدارة العليا (Top Management) أو من ينوب عنهم (مثل super-admin). قد يتم تسجيل الشخص الذي قام بالتعيين (appointed_by_super_admin_id).
5.3. **المسؤولية:** يتحمل أصحاب الأدوار الإدارية مسؤولية استخدام صلاحياتهم بما يخدم مصلحة المنصة والمستخدمين وفقاً لهذه القواعد.

**6. تعديل القواعد والإجراءات:**

6.1. **حق التعديل:** تحتفظ الإدارة العليا (Top Management) بالحق في تعديل هذه القواعد والقوانين في أي وقت. سيتم إشعار المستخدمين بالتغييرات الجوهرية.
6.2. **الإجراءات عند المخالفة:** قد تؤدي مخالفة هذه القواعد إلى إجراءات تتراوح بين تحذير المستخدم، حذف المحتوى المخالف، تعليق الحساب مؤقتاً (suspended)، أو حذفه نهائياً، وذلك حسب تقدير الإدارة.
6.3. **التواصل:** لأي استفسارات حول هذه القواعد، يمكن التواصل مع الدعم الفني (help@awalimna.com) أو الإدارة (awalimna@awalimna.com للمعاملات الرسمية).

**7. إخلاء المسؤولية:**

7.1. منصة "عوالمنا" هي منصة لنشر المحتوى الذي ينشئه المستخدمون. الآراء والأفكار المطروحة في القصص والتعليقات تعبر عن أصحابها فقط ولا تمثل بالضرورة رأي إدارة المنصة.
7.2. تسعى المنصة لتوفير بيئة آمنة، لكنها لا تضمن خلوها التام من المحتوى أو السلوكيات المخالفة، وتشجع المستخدمين على الإبلاغ الفوري عنها.

**نشكر لكم تفهمكم وتعاونكم لجعل "عوالمنا" مكاناً أفضل للإبداع والتواصل.**

# ========= نهاية قسم القواعد والقوانين (النسخة المحدثة) =========
"""
    },

    "search_syntax": {
        "description": "قواعد البحث المقترحة في المنصة:",
        "syntax": {
            "@<username>": "للبحث عن حساب مستخدم (قارئ أو كاتب) أو مركز تعليمي باستخدام اسم المستخدم أو معرف فريد للمركز.",
            "#<story_title_or_tag>": "للبحث عن قصة باستخدام عنوانها، جزء منه، أو وسم (tag) مرتبط بها."
        },
        "examples": [
            "للبحث عن المستخدم 'AhmedAli': اكتب `@AhmedAli`",
            "للبحث عن قصة بعنوان 'رحلة النجوم': اكتب `#رحلة النجوم` أو `#النجوم`",
            "للبحث عن قصص المغامرات: اكتب `#مغامرة` (إذا تم دعم البحث بالوسوم)"
        ],
        "notes": [
            "يمكن تطوير البحث ليشمل البحث داخل محتوى القصص، حسب المؤلف، حسب النوع، إلخ.",
            "يجب معالجة هذه الصيغ الخاصة في الواجهة الخلفية (backend) لتوجيه البحث بشكل صحيح."
        ]
    }
}

# ==============================================================================
# القسم الثالث: الثوابت المشتقة (للاستخدام المباشر في الكود)
# ==============================================================================

# يتم اشتقاق قوائم الأدوار من config_data لسهولة الصيانة وتجنب التكرار
try:
    # تأكد من أن المسار داخل config_data صحيح
    ROLES_LIST = config_data['terms']['roles_and_users']['role_list'] # type: ignore

    # استخدام list comprehensions لإنشاء قوائم فرعية للأدوار
    ADMIN_ROLES = [r for r in ROLES_LIST if 'admin' in r] # type: ignore # هذي adimn العادي فقط
    SUPER_ADMIN_ROLES = [r for r in ROLES_LIST if 'super-admin' in r] # type: ignore # هذي الادوار العليا فقط
    author_ROLES = [r for r in ROLES_LIST if 'author' in r] # pyright: ignore[reportUnknownVariableType] # يشمل author, admin-author, super-admin-author
    BASE_author_ROLE = 'author' # الدور الأساسي للكتابة
    READER_ROLES = [r for r in ROLES_LIST if 'reader' in r] # pyright: ignore[reportUnknownVariableType] # يشمل reader, admin_reader, super-admin-reader
    BASE_READER_ROLE = 'reader' # الدور الأساسي للقراءة
    CENTER_ROLES = [r for r in ROLES_LIST if 'Education-Center' in r] # type: ignore # يشمل Center, teacher, student
    BASE_CENTER_ROLE = 'Education-Center' # الدور الرئيسي للمركز
    OTHER_ROLES = [r for r in ROLES_LIST if r not in ADMIN_ROLES + SUPER_ADMIN_ROLES + author_ROLES + READER_ROLES + CENTER_ROLES] # type: ignore # السلطة العليا فقط

except KeyError as e:
    # طباعة رسالة خطأ واضحة إذا لم يتم العثور على المفتاح
    print(f"خطأ فادح: لم يتم العثور على المفتاح المتوقع في config_data عند تعريف الأدوار المشتقة: {e}")
    print("سيتم استخدام قوائم فارغة للأدوار، قد يتسبب هذا في مشاكل في التطبيق.")
    ROLES_LIST = [] # type: ignore
    ADMIN_ROLES = [] # type: ignore
    SUPER_ADMIN_ROLES = [] # pyright: ignore[reportConstantRedefinition]
    author_ROLES = []
    BASE_author_ROLE = None
    READER_ROLES = [] # type: ignore
    BASE_READER_ROLE = None # type: ignore
    CENTER_ROLES = [] # type: ignore
    BASE_CENTER_ROLE = None # type: ignore

# ==============================================================================
# القسم الرابع: التشغيل الاختباري (عند تنفيذ الملف مباشرة للتحقق)
# ==============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("  تنفيذ ملف الإعدادات `config_manager.py` (وضع الاختبار والتحقق) ")
    print("=" * 70)

    print("\n--- 1. اختبار الوصول للإعدادات الأساسية ---")
    print(f"اسم قاعدة بيانات MySQL: {MYSQL_DB_NAME}")
    print(f"ملف قاعدة بيانات SQLite: {SQLITE_DB_FILE}")
    print(f"مضيف MySQL: {MYSQL_HOST}")
    print(f"مستخدم MySQL: {MYSQL_USER}")
    print(f"كلمة مرور MySQL: {'تم تعيينها (لكن لا يجب عرضها)' if MYSQL_PASSWORD else 'فارغة (للاختبار المحلي)'}")
    print("-" * 30)

    print("\n--- 2. اختبار الوصول للبيانات من config_data (أمثلة) ---")
    # استخدام .get() لتجنب الأخطاء إذا كان المفتاح غير موجود
    preamble = config_data.get("preamble", "لم يتم العثور على المقدمة.") # type: ignore
    print(f"المقدمة (أول 100 حرف): {preamble[:100]}...")

    db_tech_mysql = config_data.get("terms", {}).get("database_technologies", {}).get("MySQL", "غير معرف") # type: ignore
    print(f"وصف MySQL: {db_tech_mysql}")

    reader_table_cols = config_data.get("data_models", {}).get("tables", {}).get("readers", {}).get("columns", {}) # type: ignore
    print(f"عدد الأعمدة في جدول القراء (readers): {len(reader_table_cols)}") # type: ignore
    print(f"نوع عمود البريد الإلكتروني للقارئ: {reader_table_cols.get('email', {}).get('type', 'غير معرف')}")

    help_email = config_data.get('emails', {}).get('addresses', {}).get('help@awalimna.com', 'بريد الدعم غير محدد') # type: ignore
    print(f"بريد الدعم الفني: {help_email}")

    login_url = config_data.get('url_structures', {}).get('patterns', {}).get('login', 'رابط الدخول غير محدد') # type: ignore
    print(f"رابط صفحة تسجيل الدخول المقترح: {login_url}")

    search_syntax_user = config_data.get('search_syntax', {}).get('syntax', {}).get('@<username>', 'غير معرف') # type: ignore
    print(f"صيغة البحث عن مستخدم: {search_syntax_user}")
    print("-" * 30)

    print("\n--- 3. اختبار الثوابت المشتقة (الأدوار) ---")
    print(f"قائمة الأدوار الكاملة: {ROLES_LIST}")
    print(f"الأدوار الإدارية (Admin): {ADMIN_ROLES}")
    print(f"أدوار الإدارة العليا (Super Admin): {SUPER_ADMIN_ROLES}")
    print(f"أدوار الكتاب (author): {author_ROLES} (الأساسي: {BASE_author_ROLE})")
    print(f"أدوار القراء (Reader): {READER_ROLES} (الأساسي: {BASE_READER_ROLE})")
    print(f"أدوار المراكز التعليمية (Center): {CENTER_ROLES} (الأساسي: {BASE_CENTER_ROLE})")
    print("-" * 30)

    # يمكنك إضافة اختبارات أخرى هنا للتحقق من أقسام أخرى في config_data
    # مثال: طباعة جزء من القواعد والقوانين
    # regulations_text = config_data.get('rulers_and_regulations', {}).get('text', '')
    # print("\n--- 4. مقتطف من القواعد والقوانين ---")
    # print(regulations_text[100:500] + "...") # طباعة جزء من النص

    print("\n=" * 70)
    print("  انتهى التنفيذ الاختباري لـ `config_manager.py`. ")
    print("  تأكد من أن جميع المخرجات تبدو صحيحة ومتوقعة.")
    print("=" * 70)