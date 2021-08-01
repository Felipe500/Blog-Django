from django.contrib import admin
from .models import Post




class PostAdmin(admin.ModelAdmin):
	list_display = ['author', 'title']
	search_fields =  ['author', 'title']


admin.site.register(Post, PostAdmin)



# Register your models here.
