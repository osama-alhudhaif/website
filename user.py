# لتحديد نوع الحساب
import json # type: ignore
from enum import Enum

# import json file  user.json
with open("user.json", "r", encoding="utf-8") as file:
    user_data = json.load(file)

# تعريف أنواع المستخدمين
# بناءً على البيانات من user.json
# وتحديد نوع الحساب
# وتحديد صلاحيات الحساب
# user_data يجب أن يحتوي على مفتاح "user_type" لتحديد نوع الحساب
class UserType(Enum):
    READER = 1
    WRITER = 2
    admin_READER = 3
    admin_WRITER = 4
    super_admin_READER = 5
    super_admin_WRITER = 6
    educational_center = 7
    educational_center_teacher = 8
    educational_center_student = 9
    owner = 10
