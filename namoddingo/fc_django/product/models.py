from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품 가격')
    description = models.TextField(verbose_name='상품 설명')
    stuck = models.IntegerField(verbose_name='재고')
    register_data = models.DateTimeField(auto_now=True, verbose_name='등록 일자')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fast_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'