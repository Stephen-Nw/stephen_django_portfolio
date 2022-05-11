from django.shortcuts import render

from .models import Project, Testimonial
from .contact_email import send_email
from .photo_edit import portfolio_item_image

# Create your views here.


def index(request):
    all_projects = Project.objects.all()
    all_testimonials = Testimonial.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_email(name, email, subject, message)

        return render(request, "webpage/index.html", {
            'projects': all_projects,
            'testimonials': all_testimonials,
            'send_message': True,
        })

    return render(request, "webpage/index.html", {
        'projects': all_projects,
        'testimonials': all_testimonials
    })


def portfolio_item(request, slug):
    project_item = Project.objects.get(slug=slug)
    img_one = project_item.image_one.url
    img_two = project_item.image_two.url
    project_image = portfolio_item_image(img_one, img_two)
    return render(request, "webpage/portfolio-details.html", {
        'project_item': project_item,
        'project_image': project_image
    })
