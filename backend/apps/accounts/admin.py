from django.contrib import admin
from accounts.models import User, Subscription, Follow


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'country', 'status', 'has_active_subscription_display', 'date_joined']
    list_filter = ['role', 'status', 'dark_mode_enabled']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    readonly_fields = ['date_joined', 'last_login']

    def has_active_subscription_display(self, obj):
        return obj.has_active_subscription()
    has_active_subscription_display.boolean = True
    has_active_subscription_display.short_description = 'اشتراك نشط'


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan_type', 'status', 'is_active', 'start_date', 'end_date', 'days_remaining_display']
    list_filter = ['plan_type', 'status', 'is_active']
    search_fields = ['user__username', 'user__email']
    readonly_fields = ['created_at', 'updated_at']

    def days_remaining_display(self, obj):
        return obj.days_remaining()
    days_remaining_display.short_description = 'الأيام المتبقية'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'following', 'created_at']
    list_filter = ['created_at']
    search_fields = ['follower__username', 'following__username']
    readonly_fields = ['created_at']
