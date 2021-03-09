from django.urls import reverse
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='images/category/', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Size(models.Model):
    SIZES = (
        ('xs', 'extra small'),
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large'),
        ('xl', 'extra large'),
        ('o', 'one size')
    )
    size = models.CharField(max_length=2, choices=SIZES, blank=True)
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
    def __str__(self):
        return self.size



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True, )
    product_name = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        unique=True,
    )
    price = models.FloatField(null=True, blank=True)
    price_with_sale = models.FloatField(null=True, blank=True)
    composition = models.TextField(max_length=400, null=True, blank=True)
    discription = models.TextField()
    image = models.ImageField(upload_to='images/')
    back_image = models.ImageField(upload_to='images/', blank=True)
    third_image = models.ImageField(upload_to='images/', blank=True)
    forth_image = models.ImageField(upload_to='images/', blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    size = models.TextField(max_length=255, null=True, blank=True)
    sizes = models.ManyToManyField(Size, null=True, blank=True)
    color = models.TextField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('created',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.product_name

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('my_shop.views.product_detail', args=[self.id, self.slug])

