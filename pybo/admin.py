from django.contrib import admin
from .models import Question
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Question)
