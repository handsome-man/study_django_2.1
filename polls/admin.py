from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    # 模型名称
    model = Choice
    # 额外最多一次性加三条
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Content', {'fields': ['question_text'], 'classes': ['collapse']}),
        # Date Information 字段介绍
        # 'classes': ['collapse']为隐藏选项
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)