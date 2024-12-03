from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status', 'featured', 'category', 'readTime')
    list_filter = ('status', 'category', 'publish', 'author', 'featured')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('-status', '-publish')

    # Перевод отображаемых имен в административной панели
    list_display_links = ('title', 'author', 'publish', 'status', 'featured', 'category', 'readTime')
    list_filter_links = ('status', 'category', 'publish', 'author', 'featured')
    search_fields_links = ('title', 'body')
    prepopulated_fields_links = {'slug': ('title',)}
    raw_id_fields_links = ('author',)
    date_hierarchy_links = 'publish'
    ordering_links = ('-status', '-publish')

    # Перевод заголовков
    list_display_verbose_names = {
        'title': 'Заголовок',
        'author': 'Автор',
        'publish': 'Дата публикации',
        'status': 'Статус',
        'featured': 'Избранный',
        'category': 'Категория',
        'readTime': 'Время чтения'
    }

    list_filter_verbose_names = {
        'status': 'Статус',
        'category': 'Категория',
        'publish': 'Дата публикации',
        'author': 'Автор',
        'featured': 'Избранный'
    }

    search_fields_verbose_names = {
        'title': 'Заголовок',
        'body': 'Текст поста'
    }

    prepopulated_fields_verbose_names = {
        'slug': 'Слаг'
    }

    raw_id_fields_verbose_names = {
        'author': 'Автор'
    }

    date_hierarchy_verbose_names = 'Дата публикации'

    ordering_verbose_names = {
        '-status': 'Статус',
        '-publish': 'Дата публикации'
    }
