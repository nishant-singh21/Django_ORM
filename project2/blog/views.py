from django.http import HttpResponse

def post_detail(request):
    return HttpResponse("Hello Blog Home")

def post_profile(request, post_id):
    return HttpResponse(f"Post ID: {post_id}")