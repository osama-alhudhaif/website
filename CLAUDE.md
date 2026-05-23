# Oda Website — Claude Code Working Agreement

## Stack

- **Backend:** Django + PostgreSQL في `backend/`
- **Frontend:** React + TypeScript + Vite في `backend/frontend/`
- **Admin path:** `/oda-secret-access/`
- **API base:** `/api/v1/`
- **venv:** `/home/osama-alhudhaif/Desktop/website/oda/`
- **Production target:** Ubuntu native + Railway

## Conventions

- Commits بالعربي أو الإنجليزي conventional (`feat:`, `fix:`, `chore:`, إلخ)
- ممنوع feature جديدة — فقط remediation للإطلاق
- اشتغل على branch منفصل لكل مهمة (`day-N-task-name`)
- كل مهمة فرعية = commit منفصل بوصف واضح

## Known issues

- مجلد `profel` typo، لازم يصير `profile` (ليس مهمة اليوم)
- Static files: `document_root` في `core/urls.py` يشير لـ `frontend/dist` بدل `STATIC_ROOT`
- URLs حرفية (مثل `localhost:8000`, `127.0.0.1`) في `frontend/src/` تحتاج ترحيل لـ `VITE_API_URL`

## Don't touch without explicit approval

- ملفات `.env` الفعلية (الـ `.env.example` فقط مسموح)
- `package.json` و `pubspec.yaml` (الـ dependencies)
- **`git push origin main` ممنوع تماماً** — المستخدم يدفع بنفسه بعد المراجعة

---

## ⚠️ Human-in-the-loop Protocol

أنت تشتغل بنمط "موافقة قبل كل خطوة فعل". القاعدة الذهبية:
**ما تنفّذ أي أمر يعدّل state إلا بموافقة صريحة عبر `~/ask-human.sh`.**

### قبل كل خطوة فعل:

1. **حدّد الخطوة** بدقة (الأمر/التعديل المحدّد)
2. **حضّر السؤال** بالصيغة الإلزامية (تحت)
3. **استدعِ:** `RESULT=$(~/ask-human.sh "السؤال")`
4. **تصرف بناءً على RESULT:**
   - `approve` → نفّذ المهمة، ثم انتقل للخطوة التالية
   - `reject` → اقرأ القسم "كيف تتعامل مع الرفض" تحت
   - `stop` → احفظ commit بعنوان `wip: stopped at user request`، أرسل `~/.claude-notify.sh "🛑 توقفت بطلب المستخدم"`، اخرج
   - `timeout` → نفس stop

### الاستثناءات (لا تحتاج موافقة):

- قراءة الملفات: `cat`, `ls`, `grep`, `find`, `head`, `tail`
- أوامر تشخيصية: `git status`, `git log`, `git diff`, `manage.py check`
- إنشاء ملفات tracking داخلية في الـ branch الحالي: `FOLLOWUPS.md`, `NOTES.md`, `urls_audit.md`
- عرض المخرجات للمستخدم

كل ما عدا ذلك = يحتاج موافقة.

### صيغة السؤال الإلزامية:

```
🤔 *الخطوة التالية*

*بسوي:* <الفعل المحدّد، مع الأمر إن أمكن>

*ليش:* <السبب التقني/المنطقي>

*الأثر:* <ما الذي يتغيّر، حجم التغيير، آمن للتراجع أو لا>

*البديل:* <إن وجد — وليش هذا الخيار أفضل>
```

#### مثال صحيح:

```
🤔 *الخطوة التالية*

*بسوي:* `python manage.py collectstatic --noinput`

*ليش:* أصول Django admin (CSS/JS) لازم تنتقل من venv لمجلد `staticfiles/` عشان admin يفتح بصورته الكاملة

*الأثر:* راح يُنشأ مجلد `staticfiles/` فيه ~٢٠٠ ملف. ما يحذف ولا يعدّل أي ملف موجود. آمن للتراجع (احذف المجلد فقط)

*البديل:* لا يوجد — هذي الخطوة القياسية في Django
```

#### مثال خاطئ:

```
أكمل؟
```

(غير واضح، ممنوع)

---

### كيف تتعامل مع الرفض:

الرفض **ليس نهاية المحادثة** — هو دعوة لحوار قصير. عند `reject`:

**الخطوة ١:** اسأل عن السبب أولاً:

```bash
RESULT2=$(~/ask-human.sh "🤔 رفضت الخطوة السابقة.

تبيني أوضّح ليش أقترحها؟ أو عندك بديل في بالك؟

*موافق* = وضّح لي ليش تقترحها
*رفض* = عندي بديل
*إيقاف* = أوقف وأرشف")
```

**الخطوة ٢:** بناءً على الرد:

- لو `approve` (يبي توضيح):
  - اشرح ليش تقترح الخطوة بالتفصيل عبر `~/.claude-notify.sh`
  - ثم ارجع لصيغة السؤال الإلزامية واطلب موافقة جديدة

- لو `reject` (عنده بديل):
  - أرسل: `~/.claude-notify.sh "اكتب الخطوة البديلة في تيليجرام، راح أنتظر ٣٠ ثانية ثم أقرأها"`
  - استخدم `getUpdates` للحصول على رسالته النصية
  - فهم البديل، ثم ارجع لصيغة السؤال الإلزامية بالخطة الجديدة

- لو `stop` → احفظ وأرشف واخرج

---

### استخدم `~/.claude-notify.sh` (إعلان فقط، بدون انتظار) لـ:

- بدء الجلسة: `~/.claude-notify.sh "🚀 بدأت اليوم ١"`
- تقدم رئيسي: `~/.claude-notify.sh "✅ خلصت Static Fix، بدأت URL Audit"`
- نهاية الجلسة: `~/.claude-notify.sh "🎉 خلصت اليوم ١"`
- خطأ تحاول التعامل معه: `~/.claude-notify.sh "⚠️ خطأ في X، أحاول إصلاحه"`
- شرح موسّع لقرار (بعد رفض): `~/.claude-notify.sh "<الشرح>"`

---

## End-of-session Protocol

عند الانتهاء من المهمة المطلوبة (أو عند `stop` / `timeout`):

**الخطوة ١:** تأكد إن كل شي محفوظ:
- `git status` يطلع clean
- جميع الـ commits على الـ branch المنفصل
- **ممنوع `git push`** — يبقى مهمة المستخدم

**الخطوة ٢:** أرسل ملخص النتائج:

```bash
~/.claude-notify.sh "🎉 خلصت اليوم ١
- عدد commits: X
- branch: day-1-static-and-audit
- ملفات معدّلة: Y
- ملفات جديدة: Z
- تفاصيل في git log"
```

**الخطوة ٣:** اسأل عن إطفاء الكمبيوتر:

```bash
RESULT=$(~/ask-human.sh "🏁 *انتهت المهمة*

*الحالة:* كل شي محفوظ في commits محلية على branch منفصل، جاهز للمراجعة و push

*السؤال:* أطفي الكمبيوتر؟

*موافق:* الجهاز يطفى بعد ٣٠ ثانية
*رفض:* الجهاز يبقى شغّال
*إيقاف:* مثل رفض")
```

**الخطوة ٤:** بناءً على RESULT:

- `approve`:
```bash
  ~/.claude-notify.sh "💤 الجهاز يطفى خلال ٣٠ ثانية"
  sleep 30 && systemctl poweroff
```

- `reject` / `stop` / `timeout`:
```bash
  ~/.claude-notify.sh "👋 الجهاز يبقى شغّال"
```
  واخرج

---

## Working principles

- ابدأ بـ plan mode قبل أي تنفيذ — اعرض الخطة الكاملة، واطلب موافقة على الخطة قبل البدء
- بعد كل تعديل ميكانيكي، شغّل التحقق المناسب (`manage.py check`, `npm run build`, `git status`)
- لا تتعدى نطاق المهمة المطلوبة — لو شفت مشاكل ثانية، اكتبها في `FOLLOWUPS.md`
- لو conflict أو خطأ يمنع المتابعة، استخدم `~/ask-human.sh` فوراً ولا تحاول تتعدى الإشكال بحلول هشّة
