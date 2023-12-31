from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Тег')

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        ordering = ['is_main']

    def __str__(self):
        return f'{self.tag.name} {self.article.title}'