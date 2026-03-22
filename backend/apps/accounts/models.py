from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta

class User(AbstractUser):
    # الحقول المطلوبة من ملف READER و WRITER في الـ SQL
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    level = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, default='active')

    class Role(models.TextChoices):
        FOUNDER = 'FOUNDER', 'مؤسس'
        HIGH_ADMIN = 'HIGH_ADMIN', 'ادمن عالي'
        REGULAR = 'REGULAR', 'عادي'
        READER = 'READER', 'حساب قاري'
        WRITER = 'WRITER', 'حساب كاتب'
        MUAASIS = 'MUAASIS', 'المؤسس'
        EDU_CENTER = 'EDU_CENTER', 'المركز التعليمي'
        TEACHER = 'EDU_CENTER_TEACHER', 'معلم في مركز تعليمي'
        STUDENT = 'EDU_CENTER_STUDENT', 'طالب في مركز تعليمي'
        GUEST = 'GUEST', 'زائر'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.REGULAR)

    # تفضيلات الوضع الداكن (متاح للجميع)
    dark_mode_enabled = models.BooleanField(default=False)

    def has_active_subscription(self):
        """التحقق من وجود اشتراك نشط"""
        subscription = self.subscriptions.filter(
            is_active=True,
            end_date__gt=timezone.now()
        ).first()
        return subscription is not None

    def get_active_subscription(self):
        """الحصول على الاشتراك النشط"""
        return self.subscriptions.filter(
            is_active=True,
            end_date__gt=timezone.now()
        ).first()

    def is_educational_user(self):
        """التحقق إذا كان المستخدم من المركز التعليمي"""
        return self.role in [
            self.Role.EDU_CENTER,
            self.Role.TEACHER,
            self.Role.STUDENT
        ]


class Subscription(models.Model):
    """موديل الاشتراكات"""

    class PlanType(models.TextChoices):
        MONTHLY = 'MONTHLY', 'شهري'
        YEARLY = 'YEARLY', 'سنوي'
        EDUCATIONAL = 'EDUCATIONAL', 'تعليمي'

    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'نشط'
        EXPIRED = 'EXPIRED', 'منتهي'
        CANCELLED = 'CANCELLED', 'ملغى'
        PENDING = 'PENDING', 'معلق'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    plan_type = models.CharField(
        max_length=20,
        choices=PlanType.choices,
        default=PlanType.MONTHLY
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    is_active = models.BooleanField(default=False)

    # الأسعار
    monthly_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1.00  # 1 دولار
    )
    yearly_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=10.00  # 10 دولارات
    )
    educational_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=5.00  # سعر خاص للتعليمي
    )

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # معلومات الدفع
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    payment_reference = models.CharField(max_length=255, null=True, blank=True)
    auto_renew = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.get_plan_type_display()}"

    def activate(self):
        """تفعيل الاشتراك"""
        self.is_active = True
        self.status = self.Status.ACTIVE
        self.start_date = timezone.now()

        if self.plan_type == self.PlanType.MONTHLY:
            self.end_date = self.start_date + timedelta(days=30)
        elif self.plan_type == self.PlanType.YEARLY:
            self.end_date = self.start_date + timedelta(days=365)
        elif self.plan_type == self.PlanType.EDUCATIONAL:
            self.end_date = self.start_date + timedelta(days=365)

        self.save()

    def get_price(self):
        """الحصول على السعر المناسب"""
        if self.plan_type == self.PlanType.MONTHLY:
            return self.monthly_price
        elif self.plan_type == self.PlanType.YEARLY:
            return self.yearly_price
        elif self.plan_type == self.PlanType.EDUCATIONAL:
            return self.educational_price
        return self.monthly_price

    def days_remaining(self):
        """الأيام المتبقية للاشتراك"""
        if not self.is_active or not self.end_date:
            return 0
        remaining = self.end_date - timezone.now()
        return max(0, remaining.days)


class Follow(models.Model):
    """موديل المتابعة بين المستخدمين"""
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['follower', 'following']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.follower.username} يتابع {self.following.username}"