from django.contrib import admin
from .models import Post, Comment, Author, AuthorProfile, Tag

# from django.contrib.admin.sites import NotRegistered
# from django_celery_results.models import TaskResult
# from django_celery_results.admin import TaskResultAdmin as DefaultTaskResultAdmin
#
# try:
#     admin.site.unregister(TaskResult)
# except NotRegistered:
#     pass
#
# @admin.register(TaskResult)
# class TaskResultAdmin(DefaultTaskResultAdmin):
#     list_display = ('task_id', 'status', 'result',)
#     list_filter = ('status',)
#     search_fields = ('result',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'tag_list')
    ordering = ('author', '-rating',)
    list_filter = ('author', 'rating')
    search_fields = ('title', 'content')
    search_help_text = 'Введите часть заголовка или контента'

    # fields = ('author', 'title', 'rating', 'tags')
    # readonly_fields = ('rating', )

    fieldsets = (
    (None, {'fields': ('title', 'author')}),
    ('Общая информация', {'fields': ('rating', 'tags')}),
    ('Дополнительная информация', {'fields': ('content',), 'classes': ('collapse',)}),
    )

    def tag_list(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())

    tag_list.short_description = 'Тэги'

    @admin.action(description='Увеличить рейтинг постов на 3')
    def add_rating(self, request, queryset):
        for post in queryset:
            post.rating += 3
            post.save()
        self.message_user(request, f'{queryset.count()} посто обновлено')
    actions = [add_rating]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = 'Введите автора'

admin.site.register(Author, AuthorAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = 'Введите часть тэга'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post']
    ordering = ('author',)
    list_filter = ('author',)
    search_fields = ('text',)
    search_help_text = 'Введите часть коммента'


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ['author', 'website']
    ordering = ('author',)
    list_filter = ('author',)
    search_fields = ('bio',)
    search_help_text = 'Введите часть биографии'