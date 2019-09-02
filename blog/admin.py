from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import WriteupCategory, WriteupArticle, WriteupCTF, WriteupTag, ReviewArticle

# Register your models here.
admin.site.register(WriteupCTF)
admin.site.register(WriteupCategory)
admin.site.register(WriteupArticle, MarkdownxModelAdmin)
admin.site.register(WriteupTag)
admin.site.register(ReviewArticle)

