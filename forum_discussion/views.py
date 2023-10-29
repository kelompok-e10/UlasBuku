from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseNotFound

from django.http import JsonResponse
from forum_discussion.models import Header, Replies

# Create your views here.
def view_forum(request):
    return render(request, "forum.html")


def get_header_json(request):
    discussion_headers = Header.objects.all()
    discussion_data = []

    for header in discussion_headers:
        book_info = header.get_book_info()
        if book_info:
            discussion_data.append({
                'book_info': book_info,
                'review': header.review,
                'rating': header.rating,
                'date_added': header.date,
                'user': header.user.username if header.user else "Anonymous",
            })

    return JsonResponse(discussion_data, safe=False)

def delete_discussion(request, id):
    product = Header.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('forum_discussion:view_forum'))

@login_required
@csrf_exempt
def add_discussion_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        rating = request.POST.get("rating")
        try:
            rating = float(rating)
        except (ValueError, TypeError, rating < 0 or rating > 5):
            return HttpResponseBadRequest("Masukkan bilangan positif kurang dari 5.")
        
        review = request.POST.get("review")
        user = request.user

        new_header = Header(book_title=title, rating=rating, review=review, user=user)
        new_header.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def add_reply_ajax(request):
    if request.method == 'POST':
        reply = request.POST.get("reply")
        user = request.user

        new_reply = Replies(reply=reply, user=user)
        new_reply.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()