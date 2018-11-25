from django.contrib import admin

from .models import Question, Quiz, Choice, Category

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Choice)
admin.site.register(Category)
