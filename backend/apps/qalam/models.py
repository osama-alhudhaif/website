from django.conf import settings
from django.db import models
from stories.models import Story


class QalamSession(models.Model):
    MODE_CHOICES = [
        ("chat", "Chat"),
        ("translation", "Translation"),
        ("summary", "Summary"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="qalam_sessions",
    )
    story = models.ForeignKey(
        Story,
        on_delete=models.SET_NULL,
        related_name="qalam_sessions",
        null=True,
        blank=True,
    )
    mode = models.CharField(max_length=32, choices=MODE_CHOICES, default="chat")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"QalamSession #{self.pk} ({self.mode})"


class QalamMessage(models.Model):
    ROLE_CHOICES = [
        ("system", "System"),
        ("user", "User"),
        ("assistant", "Assistant"),
    ]

    session = models.ForeignKey(
        QalamSession,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"{self.role} message in session {self.session_id}"


class TranslationJob(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("running", "Running"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="translation_jobs",
    )
    story = models.ForeignKey(
        Story,
        on_delete=models.SET_NULL,
        related_name="translation_jobs",
        null=True,
        blank=True,
    )
    source_language = models.CharField(max_length=32)
    target_language = models.CharField(max_length=32)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="pending")
    progress = models.PositiveIntegerField(default=0)
    source_text = models.TextField()
    translated_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"TranslationJob #{self.pk} ({self.status})"

