from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'food', 'body', 'active', 'date_added']
    list_editable = ['active']
    list_filter = ['active', 'date_added']
    search_fields = ['name', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        self.message_user(request, "Selected comments have been approved.")

    approve_comments.short_description = "Approve selected comments"
