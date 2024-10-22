from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da Tag')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Conteúdo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    tags = models.ManyToManyField(Tag, verbose_name='Tags')

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    def __str__(self):
        return self.title
