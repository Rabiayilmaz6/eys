from django.contrib import admin


from product.models import Category,Product,Images

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 1
# bu classdaki model kısmı hangi tabloya ait olduğunu gösterir estra ise en fazla kaç resimden oluşacağını gösterir
# kısaca image tablosundan eklenecek 1 tane alan oluştur demektir
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["categoryname", "status"]
    # bu class şunu ifade eder  categoryname ve status ekranda görünür category sayfasında
    #category sayfasına girdiğimizda sadece adı görünüyordu artık status değeri de görünür
    list_filter = ['status'] # filtreleme işlemleri için kullanılır yani sağ tarafta evet hayır buttonları olacak
                            # evet e bastığımızda statusu evet olanlar ekrana gelecek hayırda tersi
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["productname","category","price","image_tag","status"]
    readonly_fields = ["image_tag"]
    list_filter = ['status']
    inlines = [ProductImageInline] # sadece ilgili product ile ilgili olanaları ekler ve düzenler

class ImagesAdmin(admin.ModelAdmin):
    list_display = ["imagename","product","image_tag"]
    readonly_fields = ["image_tag"]

admin.site.register(Category, CategoryAdmin) # categoryadmin ile category ilişkilendirildi
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin) # images admin yazmazsak da çalışır fakat list_display çalışmaz yani içerikler yok