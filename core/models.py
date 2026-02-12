from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=120)
    sku = models.CharField(max_length=40, unique=True)
    category = models.CharField(max_length=80, blank=True)
    short_desc = models.CharField(max_length=1000, blank=True)

    pressure_range = models.CharField(max_length=80, blank=True)
    dial_size = models.CharField(max_length=50, blank=True)
    case_material = models.CharField(max_length=50, blank=True)
    connection = models.CharField(max_length=80, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    img_url = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ("NEW","New"),
        ("PROCESSING","Processing"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="NEW")

    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=120, blank=True)

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order #{self.id} - {self.full_name} ({self.status})"
    
    @property
    def total_amount(self):
        return sum(item.total_price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name = "items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.quantity*self.unit_price
    
    def __str__(self):
        return f"{self.product.name} x{self.quantity}"