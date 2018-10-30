from django.db import models
class timetable(models.Model):
    slot_no = models.ForeignKey('slot_timings',on_delete=models.CASCADE)
    day = models.CharField(primary_key= True,max_length=50)
    c_name = models.ForeignKey('course',on_delete=models.CASCADE)
    rid = models.ForeignKey('room',on_delete=models.CASCADE)
    class_type = models.IntegerField(null = True)
   
class Section(models.Model):
    section_id = models.IntegerField(primary_key= True)
    section_name = models.CharField(max_length=50)

class criteria_ta(models.Model):
    Criteria = models.IntegerField(primary_key = True)
    Grade = models.IntegerField(null = True)
    Count = models.IntegerField(null = True)
    c_name = models.ForeignKey('course',on_delete=models.CASCADE)


class almanac(models.Model):
    date = models.DateField(primary_key = True)
    day = models.CharField(max_length=250)
   
class Event(models.Model):
    date =  models.ForeignKey('almanac',on_delete=models.CASCADE)
    event_name = models.CharField(max_length=250)
    event_type = models.CharField(max_length=250)

class schedule_history(models.Model):
    present_date = models.DateField()
    resc_date = models.DateField()
    slot_no = models.ForeignKey('slot_timings',on_delete=models.CASCADE)
    day=models.CharField(max_length=250)

    #faculty_id = models.ForeignKey('faculty',on_delete=models.CASCADE)
    #c_name = models.ForeignKey('course',on_delete=models.CASCADE)

class ta_alloc(models.Model):
    c_name = models.ForeignKey('course',on_delete=models.CASCADE)
    sid = models.ForeignKey('Student',on_delete=models.CASCADE)
    student_first_name=models.CharField(max_length=250)

class duration(models.Model):
    exam_type = models.CharField(max_length=250)
    timeperiod = models.IntegerField(null = True)
    start_time = models.TimeField()
    end_time = models.TimeField()
   
class room(models.Model):
    rid=models.IntegerField(primary_key =True)
    day= models.CharField(max_length=250)
    slot_no = models.ForeignKey('slot_timings',on_delete=models.CASCADE)
    availability_status=models.IntegerField()
    capacity=models.CharField(max_length=250)
   
class slot_timings(models.Model):
    slot_no=models.IntegerField(primary_key= True)
    start_time= models.TimeField()
    end_time= models.TimeField()

class Student(models.Model):
    sid= models.IntegerField(primary_key=True)
    student_first_name=models.CharField(max_length=250)
    student_middle_name=models.CharField(max_length=250)
    student_last_name=models.CharField(max_length=250)
    student_dob=models.DateField()
    student_gender=models.CharField(max_length=250)
    student_email=models.CharField(max_length=250)
    student_mobile=models.CharField(max_length=15)
    student_blood_group=models.CharField(max_length=250)
    student_mother_tongue=models.CharField(max_length=250)
    student_registered_year=models.DateField(max_length=100)
    student_registered_degree=models.IntegerField()
    student_registered_degree_duration=models.DateField()
    student_cur_yearofstudy = models.DateField()
    student_cur_sem=models.IntegerField()
    student_academic_status=models.CharField(max_length=15)
class course(models.Model):
    cid= models.IntegerField()
    c_name=models.CharField(primary_key=True,max_length=250)
    no_credits=models.IntegerField()
    no_hours=models.IntegerField()
    fid=models.ForeignKey('faculty',on_delete=models.CASCADE)   
class student_course(models.Model):
    sid = models.ForeignKey('Student',on_delete=models.CASCADE)
    c_name = models.ForeignKey('course',on_delete=models.CASCADE)

class student_grade(models.Model):
    sid = models.ForeignKey('Student',on_delete=models.CASCADE)
    c_name = models.ForeignKey('course',on_delete=models.CASCADE)
    grade =  models.IntegerField()
       
class faculty(models.Model):
    fid=models.IntegerField(primary_key=True)
    day_1=models.CharField(max_length=30)
    day_2=models.CharField(max_length=30)
    day_3=models.CharField(max_length=30)
    fname=models.CharField(max_length=30)
class Faculty_Meetings(models.Model):
    slot_no = models.IntegerField()
    start_time= models.CharField(max_length=250)
    end_time= models.CharField(max_length=250)
    purpose=models.CharField(max_length=250)
