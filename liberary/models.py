from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Staff_Detail(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    is_admin = models.BooleanField()
    designation = models.CharField(max_length=30)

    def __str__(self):
    	return self.user_name + " - " + self.designation

class Student_Detail(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
   # student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=30)

    Male = 'Male'
    Female = 'Female'
    Other = 'Other'
    sex_choices = (
        (Male, 'Male'),
        (Female, 'Female'),
        (Other, 'Other')
    )
    sex = models.CharField(max_length=7, choices=sex_choices,default='Male')

    Computer_Scince_and_Engineeirng = 'CSE'
    Mechanical_engineering = 'MECH'
    Civil_Engineering = 'CIVIL'
    Electrical_Engineering = 'Electrical'
    Information_Technology = 'IT'
    branch_choices = (
        (Computer_Scince_and_Engineeirng, 'CSE'),
        (Mechanical_engineering, 'MECH'),
        (Civil_Engineering, 'CIVIL'),
        (Electrical_Engineering, 'Electrical'),
        (Information_Technology, 'IT')
    )
    branch = models.CharField(max_length=10, choices=branch_choices)
    semester = models.IntegerField()
    contact_number = models.CharField(max_length=12)

    def __str__(self):
    	return str(self.pk) + " - " +  self.student_name + " - " + self.branch + "-" + str(self.semester) + "th sem"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Student_Detail.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.Student_detail.save()

class Shelf_Detail(models.Model):
    floor = models.IntegerField()
    shelf_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.shelf_id) + " - " + str(self.floor) + "th floor"

class Category_Table(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Language_Table(models.Model):
    language_id = models.AutoField(primary_key=True)
    language_name = models.CharField(max_length=50)

    def __str__(self):
        return self.language_name

class Book_Detail(models.Model):
    ISBN = models.AutoField (primary_key=True)
    book_title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    publication_date = models.DateField("Date")
    language_id = models.ForeignKey(Language_Table, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category_Table, on_delete=models.CASCADE)
    online = models.BooleanField()
    no_of_copies_available_offline = models.IntegerField(default=0)
    shelf_id = models.ForeignKey(Shelf_Detail, on_delete=models.CASCADE)

    def __str__(self):
    	return self.book_title + " - " + self.author

    def get_absolute_url(self):
        return reverse('liberary:book_details', kwargs={'id': self.pk})



class Borrower_Detail(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    ISBN = models.ForeignKey(Book_Detail, on_delete=models.CASCADE)
    borrowed_from_date = models.DateField("Date")
    borrowed_to_date = models.DateTimeField(default=timezone.now)
    actual_return_date = models.DateTimeField(default=timezone.now)
    issued_by = models.ForeignKey(Staff_Detail, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("User", "ISBN"),)


    def __str__(self):
    	return str(self.student_id) + " - " + str(self.ISBN)

