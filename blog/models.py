from django.db import models
from team.models import Team


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    publish = models.BooleanField(default=True)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.name

    @property
    def name_and_count(self):
        return self.name + ' (' + str(self.blog_count) + ')'

    @property
    def blog_count(self):
        return Blog.objects.filter(blog_category=self).count()


class Blog(models.Model):
    blog_category = models.ForeignKey(BlogCategory, max_length=100, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    blog_img = models.FileField(upload_to='blog')
    img_title = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    post_by = models.ForeignKey(Team, default=1, verbose_name="Post By", on_delete=models.SET_DEFAULT)
    publish = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title

    @property
    def post_author(self):
        return 'Posted by ' + self.post_by.first_name + ' ' + self.post_by.last_name + \
               ' on ' + str(self.post_date)

    # def category_count(self):
    #     # Your filter criteria can go here.
    #     return self.blog_category_set.count()


