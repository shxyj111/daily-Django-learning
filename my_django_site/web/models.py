from django.db import models


class Phone(models.Model):
    """手机型号"""
    name = models.CharField(max_length=100, verbose_name='型号')
    brand = models.CharField(max_length=50, verbose_name='品牌')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    description = models.TextField(default='', blank=True, verbose_name='描述')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'phone'
        ordering = ['-created_at']
        verbose_name = '手机'
        verbose_name_plural = '手机'

    def __str__(self):
        return f'{self.brand} {self.name}'
