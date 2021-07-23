from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here

class QuestionInline(admin.StackedInline):
    model = Question.lessons.through
    extra = 5
    

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

class ChoiceAdmin(admin.ModelAdmin):
    model = Choice
    list_display = ['choice_content']
    # inlines = [QuestionInline]

class ChoiceInline(admin.StackedInline):
    model = Choice.questions.through
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ChoiceInline]
    list_display = ['question_text']
    



# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Question,QuestionAdmin)

