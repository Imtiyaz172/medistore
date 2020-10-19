from django.contrib import admin
from . import models
admin.site.site_header='Zaas Property'


# Register your models here.
class LogoModel(admin.ModelAdmin):
    list_display    = ["__str__","Title", "Status"]
    search_fields   = ['Title']
    list_per_page   = 20
    list_filter     = ["Title", "Status"]

admin.site.register(models.Logo, LogoModel)

class categoryModel(admin.ModelAdmin):
    list_display    = ["__str__","Title", "Status"]
    search_fields   = ['Title']
    list_per_page   = 20
    list_filter     = ["Title", "Status"]

admin.site.register(models.category, categoryModel)

class sliderModel(admin.ModelAdmin):
    list_display    = ["Title", "Status"]
    search_fields   = ['Title']
    list_per_page   = 20
    list_filter     = ["Title", "Status"]

admin.site.register(models.slider, sliderModel)

class serviceModel(admin.ModelAdmin):
    list_display    = ["Title", "Status"]
    search_fields   = ['Title']
    list_per_page   = 20
    list_filter     = ["Title", "Status"]

admin.site.register(models.service, serviceModel)


class about_usModel(admin.ModelAdmin):
    list_display    = ["Title", "Status"]
    search_fields   = ['Title']
    list_per_page   = 20
    list_filter     = ["Title", "Status"]

admin.site.register(models.about_us, about_usModel)



class store_locationModel(admin.ModelAdmin):
    list_display    = ["Title", "Status"]
    search_fields   = ['Title']
    list_per_page   = 20
    list_filter     = ["Title", "Status"]

admin.site.register(models.store_location, store_locationModel)


class user_messageModel(admin.ModelAdmin):
    list_display    = ["name", "email","date"]
    search_fields   = ['name']
    list_per_page   = 20
    list_filter     = ["Status"]

admin.site.register(models.user_message, user_messageModel)


class productModel(admin.ModelAdmin):
    list_display    = ["name", "category","power","new_price","company","view"]
    search_fields   = ['name',"category","indication","therapeutic_class"]
    list_per_page   = 20
    list_filter     = ["Status","category"]

admin.site.register(models.product, productModel)



class tipsModel(admin.ModelAdmin):
    list_display    = ["disease_name", "view"]
    search_fields   = ['disease_name']
    list_per_page   = 20
    list_filter     = ["Status"]

admin.site.register(models.tips, tipsModel)


class beauty_careModel(admin.ModelAdmin):
    list_display    = ["tips_name", "view"]
    search_fields   = ['tips_name']
    list_per_page   = 20
    list_filter     = ["Status"]

admin.site.register(models.beauty_care, beauty_careModel)

class coronaModel(admin.ModelAdmin):
    list_display    = ["tips_name", "view"]
    search_fields   = ['tips_name']
    list_per_page   = 20
    list_filter     = ["Status"]

admin.site.register(models.corona, coronaModel)

class health_careModel(admin.ModelAdmin):
    list_display    = ["tips_name", "view"]
    search_fields   = ['tips_name']
    list_per_page   = 20
    list_filter     = ["Status"]

admin.site.register(models.health_care,health_careModel)


class ContactModel(admin.ModelAdmin):
    list_display    = ["name", "email"]
    search_fields   = ['name']
    list_per_page   = 20
    

admin.site.register(models.Contact, ContactModel)

class user_regModel(admin.ModelAdmin):
    list_display    = ["Name",  "email"]
    search_fields   = ['Name']
    list_per_page   = 20
    

admin.site.register(models.user_reg, user_regModel)

class CartModel(admin.ModelAdmin):
    list_display    = ["user_reg","product", "quantity"]
    search_fields   = []
    list_per_page   = 40
    def product(self, instance):
        return instance.product.name
    def user_reg(self, instance):
        return instance.user_reg.Name
    
    

admin.site.register(models.Cart, CartModel)

