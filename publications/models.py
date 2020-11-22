from django.db import models
from core.models import BaseModel


class Publication(BaseModel):
    text = models.TextField(
        null=True, blank=True,
        verbose_name="Текст публикации"    
    )

    image = models.ImageField(
        null=True, blank=True,
        verbose_name="Картинка публикации",
        upload_to="publication_pictures"
    )
