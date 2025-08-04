from flask_login import LoginManager

# من الأفضل تعليق أو حذف هذه الأسطر مؤقتاً حتى تنتهي من الترحيل
# from .model import Reader, Author, ReaderAdmin, ReaderSuperAdmin, AuthorAdmin, AuthorSuperAdmin, Center, Teacher, Student, Owner

# تصميم login_manager.user_loader للقارئ والكاتب و مشرف لقارئ ومشرف للكاتب و مشرف عالي للقاري و مشرف عالي للقاري و مركز تعليمي و معلم مركز تعليمي و طالب مركز تعليمي و مالك
# @LoginManager.user_loader
# def load_user(user_id):
#     user = Reader.query.get(user_id)  # قارئ
#     if user:
#         return user
#     user = Author.query.get(user_id)  # كاتب
#     if user:
#         return user
#     user = ReaderAdmin.query.get(user_id)  # مشرف قارئ
#     if user:
#         return user
#     user = ReaderSuperAdmin.query.get(user_id)  # مشرف عالي قارئ
#     if user:
#         return user
#     user = AuthorAdmin.query.get(user_id)  # مشرف كاتب
#     if user:
#         return user
#     user = AuthorSuperAdmin.query.get(user_id)  # مشرف عالي كاتب
#     if user:
#         return user
#     user = Center.query.get(user_id)  # مركز تعليمي
#     if user:
#         return user
#     user = Teacher.query.get(user_id)  # معلم مركز تعليمي
#     if user:
#         return user
#     user = Student.query.get(user_id)  # طالب مركز تعليمي
#     if user:
#         return user
#     user = Owner.query.get(user_id)  # مالك
#     return None