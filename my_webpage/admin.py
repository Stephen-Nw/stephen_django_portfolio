from django.contrib import admin

from .models import Project, Testimonial

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'github_url', 'category')
    list_filter = ('category', 'date')
    prepopulated_fields = {'slug': ('name',)}


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('date', 'name')
    list_filter = ('date',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
