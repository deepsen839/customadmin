from django.db import models
from django.core.validators import FileExtensionValidator
from tinymce.models import HTMLField 

# Create your models here.
class ProductCard(models.Model):
    logo = models.FileField(upload_to='static/product_card/',
    blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["gif", "jpg", "jpeg", "png", "svg"]
            )
        ],
    
    
    )

    descrption =  HTMLField()
