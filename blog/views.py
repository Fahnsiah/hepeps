from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import BlogCategory, Blog


def index(request, pk=0):

    query_list = Blog.objects.filter(publish=True)

    query_text = request.GET.get('q')
    if query_text:
        query_text = query_text.strip()
        query_list = query_list.filter(
            Q(title__icontains=query_text) |
            Q(description__icontains=query_text) |
            Q(blog_category__name__icontains=query_text) |
            Q(post_by__first_name__icontains=query_text) |
            Q(post_by__last_name__icontains=query_text)
        )
    else:
        if pk != '0':
            query_list = Blog.objects.filter(id=pk)

    paginator = Paginator(query_list, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)

    except PageNotAnInteger:
        queryset = paginator.page(1)

    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    content = {
            'result_list': queryset,
            'page_request_var': page_request_var,
            }

    return render(request, 'blog/index.html', content)


def category_blog(request, pk):

    blog_category = get_object_or_404(BlogCategory, id=pk)
    query_list = Blog.objects.filter(blog_category=blog_category)
    category_blog_list = query_list

    query_text = request.GET.get('q')
    if query_text:
        query_list = query_list.filter(
            Q(title__icontains=query_text) |
            Q(description__icontains=query_text) |
            Q(blog_category__name__icontains=query_text) |
            Q(post_by__first_name__icontains=query_text) |
            Q(post_by__last_name__icontains=query_text)
        )

    paginator = Paginator(query_list, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)

    except PageNotAnInteger:
        queryset = paginator.page(1)

    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    content = {
            'category_blog_list': category_blog_list,
            'result_list': queryset,
            'page_request_var': page_request_var,
            }

    return render(request, 'blog/index.html', content)

# def category_blog(request, cid, pk=0):
#
#     blog_category = get_object_or_404(BlogCategory, id=cid)
#     query_list = Blog.objects.filter(blog_category=blog_category)
#     category_blog_list = query_list
#
#     if pk == '0':
#         query_text = request.GET.get('q')
#         if query_text:
#             query_list = query_list.filter(
#                 Q(title__icontains=query_text) |
#                 Q(description__icontains=query_text) |
#                 Q(blog_category__name__icontains=query_text) |
#                 Q(post_by__first_name__icontains=query_text) |
#                 Q(post_by__last_name__icontains=query_text)
#             )
#     else:
#         query_list = query_list.filter(id=pk)
#
#     paginator = Paginator(query_list, 1)
#     page_request_var = 'page'
#     page = request.GET.get(page_request_var)
#     try:
#         queryset = paginator.page(page)
#
#     except PageNotAnInteger:
#         queryset = paginator.page(1)
#
#     except EmptyPage:
#         queryset = paginator.page(paginator.num_pages)
#
#     content = {
#             'category_blog_list': category_blog_list,
#             'result_list': queryset,
#             'page_request_var': page_request_var,
#             }
#
#     return render(request, 'blog/index.html', content)

    # if request.method == 'POST':
    #     # get title of posted blog
    #     post_title = request.POST.get('post_title')
    #
    #     if post_title != '' and post_title is not None:
    #         title_query = title_query.filter(post_title__icontains=post_title)
    #
    #     paginator = Paginator(title_query, 1)
    #
    # else:
    #     page = request.GET.get('page')
    #     posts = paginator.get_page(page)
    #     if pk != '0':
    #         posts = Blog.objects.filter(id=pk)

    # content = {'bg': bg,
    #            'title_query': title_query,
    #            'posts': posts,
    #            }
    #
    # return render(request, 'blog/index.html', content)
# def single(request, id):
#     mypost = title_query = Blog.objects.get(id=id)
#     nextpost= Blog.objects.filter(id__gt=mypost.id).order_by('id').first()
#     prevpost = Blog.objects.filter(id__lt=mypost.id).order_by('id').last()
#     content = {
#         'mypost':mypost,
#         'prevpost':prevpost,
#         'nextpost':nextpost
#     }
#
#     return (request,'blog/single_post.html', content)