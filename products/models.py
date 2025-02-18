import uuid
from django.db import models

# Category Model
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
# Product Model
class Product(models.Model):
    def products_pic_path(instance, filename):
        """
        Function to define the upload path for user profile pictures.
        Example: media/products/profile.jpg
        """
        return f'products/{filename}'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    productName = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available_status = models.BooleanField(default=True)
    image = models.ImageField(upload_to=products_pic_path, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name