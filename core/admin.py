from django.contrib import admin

from core.models import Record, Question, Step


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "language", "voice_record")


class Question_details(admin.ModelAdmin):
    list_display    = ('question','display_question_on_page')
    list_filter     = ('display_question_on_page',)   
    search_fields   = ['question']


class Step_detail(admin.ModelAdmin):
    list_display    = ('page_number','duration_in_sec','no_question_to_display')
    search_fields   = ['page_number']
    list_filter     = ('page_number',)

admin.site.register(Question,Question_details)
admin.site.register(Step,Step_detail)
