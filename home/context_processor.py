import datetime
from contact.models import Contact
from blog.models import BlogCategory, Blog


def basic_info(request):
    blog_links = Blog.objects.filter(publish=True).order_by('-id')[:15]
    blog_category_links = BlogCategory.objects.filter(publish=True).order_by('-id')[:10]
    current_year = datetime.datetime.now().year
    if current_year != 2020:
        copy_right_year = '2020-' + str(current_year)
    else:
        copy_right_year = str(current_year)

    footer_blog = Blog.objects.filter(publish=True).order_by('-id')[:9]
    contact_info = Contact.objects.all().first()

    content = {
        'blog_category_links': blog_category_links,
        'blog_links': blog_links,
        'copy_right_year': copy_right_year,
        'contact_info': contact_info,
        'footer_blog': footer_blog,
    }

    return content

