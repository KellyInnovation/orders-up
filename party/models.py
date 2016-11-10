from django.db import models

class Party(models.Model):
	drink = models.CharField(max_length=30, default='water')
	food = models.CharField(max_length=400, null=True, blank=True)

	order_price = models.DecimalField(max_digits=1000, decimal_places=0, default=0)

	special_instructions = models.CharField(max_length=500, null=True, blank=True)	

	hostess = models.OneToOneField('hostess.Hostess', null=True, blank=True)
	


# class GuestOrder(models.Model):

# 	drink = models.CharField(max_length=30, default='water')
# 	food = models.CharField(max_length=400, null=True, blank=True)

# 	special_instructions = models.CharField(max_length=500, null=True, blank=True)	

# 	guest = models.ForeignKey('guest.Guest', related_name='guest_order')

# # Create your models here.
