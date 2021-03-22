from django.db import models

# Create your models here.

class StuClassName(models.Model):
    class_name = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.class_name
    class Meta:
        db_table = 'class_name'


class StudentInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique= True)
    password = models.CharField(('password'), max_length=128)
    class_name = models.ForeignKey(StuClassName, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    is_active = models.BooleanField(default = False, 
                                   blank = True, 
                                    null = True
                                    )

    def __str__(self):
            return self.first_name
    class Meta:
        db_table = 'student_data'

        
