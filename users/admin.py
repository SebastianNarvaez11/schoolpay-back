from django.contrib import admin
from import_export import resources
from django.contrib.auth.hashers import make_password
from import_export.admin import ImportExportModelAdmin
from .models import Admin, User, Student

# Register your models here.


class UserResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        value = row['password']
        row['password'] = make_password(value)

    class Meta:
        model = User


class UsersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UserResource


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = StudentResource


admin.site.register(Admin)
admin.site.register(User, UsersAdmin)
admin.site.register(Student, StudentAdmin)
