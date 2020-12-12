from django.shortcuts import render
from random import randint

# Create your views here.
def chat(request, user_id):
    return render(request, "index.html", context = {
        "h1" : "abcxyz",
        "abc" : [randint(1, 10) for _ in range(5)]
        "title" : "SOme title"
    })

def user_profile(request, user_id):
    user = get_user(user_id)
    return render(request, "user.html", context = {
        "name" : user.name,
        "id" : user.id
    })