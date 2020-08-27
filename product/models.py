from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    detail = models.TextField(max_length=2500)
    rating = models.IntegerField(default=0)
    img_url = models.FileField(upload_to='product', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.category.name


order_status_choices = (
    ('ordered', 'Ordered'),
    ('purchased', 'Purchased'),
    ('cancelled', 'Cancelled'),
)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    website = models.CharField(max_length=100)
    postal_address = models.TextField(blank=True, null=True)
    order_status = models.CharField(max_length=50, choices=order_status_choices, default='ordered')
    responded = models.BooleanField(default=False)
    response = models.TextField(blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.product.title + ' (' + self.name + ')'
