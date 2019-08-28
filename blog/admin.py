from django.contrib import admin
from .models import WriteupCategory, WriteupArticle, WriteupCTF, WriteupTag, ReviewArticle

# Register your models here.
admin.site.register(WriteupCTF)
admin.site.register(WriteupCategory)
admin.site.register(WriteupArticle)
admin.site.register(WriteupTag)
admin.site.register(ReviewArticle)

