from distutils.command.upload import upload
from django.db import models
from django.utils.text import slugify
from PIL import Image

# resize image before upload in Admin - https://resizing.app/features/resize-jpeg/ (W: 400px)

# Create your models here.


class Project(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    description = models.TextField()
    image_one = models.ImageField(upload_to='images')
    image_two = models.ImageField(upload_to='images')
    image_three = models.ImageField(upload_to='images')
    slug = models.SlugField(unique=True)
    github_url = models.URLField(default="N/A")
    project_url = models.CharField(max_length=200, default="N/A")

    def __str__(self):
        return f"{self.name}"

    # def save(self, *args, **kwargs):
    #     img_one = Image.open(self.image_one)
    #     img_width = int(img_one.width)
    #     img_height = int(img_one.height)

    #     new_width = 300
    #     new_height = 300
    #     # new_height = int((new_width * img_height) / img_width)

    #     image_one = img_one.thumbnail((new_width, new_height))
    #     # self.image_one.save()

    #     super(Project, self).save(*args, **kwargs)


class Testimonial(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="images")
    comment = models.TextField()

    def __str__(self):
        return f"{self.name}"
