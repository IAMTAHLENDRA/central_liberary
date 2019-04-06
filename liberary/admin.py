from django.contrib import admin
from .models import Book_Detail, Category_Table, Borrower_Detail, Student_Detail, Staff_Detail, Shelf_Detail, Language_Table
# Register your models here.

admin.site.register(Book_Detail)
admin.site.register(Category_Table)
admin.site.register(Borrower_Detail)
admin.site.register(Student_Detail)
admin.site.register(Staff_Detail)
admin.site.register(Shelf_Detail)
admin.site.register(Language_Table)

