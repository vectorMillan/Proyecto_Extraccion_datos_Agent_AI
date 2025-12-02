from django.contrib import admin
from .models import Tesis, PostgraduateProgram

# Register your models here.
@admin.register(PostgraduateProgram)
class PostgraduateProgramAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tesis)
class TesisAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor_name', 'program', 'created_at')
    list_filter = ('program',)
    search_fields = ('titulo', 'autor_name')

