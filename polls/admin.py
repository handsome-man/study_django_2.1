from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# StackedInline显示在多行
# class ChoiceInline(admin.StackedInline):
#     # 模型名称
#     model = Choice
#     # 额外最多一次性加三条
#     extra = 3


# TabularInline显示在一行，还额外增加一个删除按钮
class ChoiceInline(admin.TabularInline):
    # 模型名称
    model = Choice
    # 额外最多一次性加三条
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 在对象的更改列表页面上显示的字段名称元组
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 添加过滤器
    list_filter = ['pub_date']
    # 添加搜索功能
    search_fields = ['question_text']

    fieldsets = [
        ('Question Content', {'fields': ['question_text'], 'classes': ['collapse']}),
        # Date Information 字段介绍
        # 'classes': ['collapse']为隐藏选项
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)