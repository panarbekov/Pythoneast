from django.db import models

class BaseModel(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Имя"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения"
    )

    def __str__(self):
        if self.name:
            return self.name
        return self.id
    
    class Meta:
        abstract = True
