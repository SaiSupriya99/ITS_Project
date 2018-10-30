from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import faculty,student_grade,timetable,Section,criteria_ta,almanac,schedule_history,ta_alloc,room,slot_timings, Student,student_course,Event,duration,course,Faculty_Meetings

admin.site.register(faculty)
admin.site.register(student_grade)
admin.site.register(timetable)
admin.site.register(Section)
admin.site.register(criteria_ta)
admin.site.register(almanac)
admin.site.register(schedule_history)
admin.site.register(ta_alloc)
admin.site.register(room)
admin.site.register(slot_timings)
admin.site.register(Student)
admin.site.register(student_course)
admin.site.register(Event)
admin.site.register(duration)
admin.site.register(course)
admin.site.register(Faculty_Meetings)
