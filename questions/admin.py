from django.contrib import admin

from .models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    exclude = ('votes',)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Question, QuestionAdmin)
