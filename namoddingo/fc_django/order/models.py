from django.db import models

# Create your models here.
class Order(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE,verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_data = models.DateTimeField(auto_now=True, verbose_name='등록 일자')

    def __str__(self):
        return str(self.member) + '' + str(self.product)

    class Meta:
        db_table = 'fast_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'