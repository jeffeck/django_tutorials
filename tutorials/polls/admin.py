from django.contrib import admin

from .models import Choice, Question 

# Basic model registration
# admin.site.register(Question)
admin.site.register(Choice)



# Custom model registration
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3




# Further customizations with fieldsets
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # Pagination
    # Search Boxes
    # Filters
    # Date hierarchies
    # Column Header order
    


admin.site.register(Question, QuestionAdmin)
