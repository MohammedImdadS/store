from django.contrib import admin
from .models import BaseProducts,Category,Carousel,Contact
# Register your models here.

class BaseProductsAdmin(admin.ModelAdmin):
	list_display =('__str__','category')

	class Meta:
		model = BaseProducts


admin.site.register(BaseProducts,BaseProductsAdmin)
admin.site.register(Category)
admin.site.register(Carousel)
admin.site.register(Contact)