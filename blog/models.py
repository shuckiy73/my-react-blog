from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.deconstruct import deconstructible

class Category(models.TextChoices):
    SALES = 'sales', 'Продажи'
    MARKETING = 'marketing', 'Маркетинг'
    BUSINESS = 'business', 'Бизнес'
    POLITICS = 'politics', 'Политика'
    ART = 'art', 'Искусство'

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

@deconstructible
class ImageSizeValidator:
    def __init__(self, max_size_mb=0.5):
        self.max_size_mb = max_size_mb

    def __call__(self, fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = self.max_size_mb
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError(
                f"File size exceeds the maximum limit of {megabyte_limit}MB."
            )

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок", help_text="Заголовок блога")
    slug = models.SlugField(max_length=600, unique_for_date='publish', verbose_name="Слаг")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post', verbose_name="Автор", help_text="Выберите автора для поста")
    category = models.CharField(
        max_length=50, choices=Category.choices, default=Category.SALES,
        verbose_name="Категория", help_text="Категория для поста"
    )
    image = models.ImageField(
        upload_to='images/',
        null=True,
        validators=[ImageSizeValidator(max_size_mb=0.5)],
        verbose_name="Изображение", help_text="Изображение должно быть меньше 500MB"
    )
    readTime = models.IntegerField(
        null=True, verbose_name="Время чтения", help_text="Время чтения для поста")
    body = RichTextUploadingField(verbose_name="Текст поста", help_text="Ваш блог")
    featured = models.BooleanField(
        default=False, verbose_name="Избранный", help_text="Отметьте, чтобы сделать пост избранным")
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")
    STATUS_CHOICES = (('draft', 'Черновик'), ('published', 'Опубликовано'))
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='draft',
        verbose_name="Статус"
    )
    objects = models.Manager()
    published = PublishedManager()

    # tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def save(self, *args, **kwargs):
        if self.featured:
            try:
                temp = Post.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Post.DoesNotExist:
                pass
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title