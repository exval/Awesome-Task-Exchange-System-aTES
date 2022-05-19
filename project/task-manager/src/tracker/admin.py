from django.contrib import admin

from tracker.models import User, Task

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'public_id')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	pass
