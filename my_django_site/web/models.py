from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100, verbose_name="名称")
    brand = models.CharField(max_length=100, verbose_name="品牌")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")

    def __str__(self):
        return f"{self.brand} {self.name}"
