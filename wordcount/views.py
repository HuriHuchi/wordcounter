from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")
    # 첫 번째 인자는 request 객체
    # 두 번째 인자는 template
    # 세 번째 인자는 dictionary형 객체

def about(request):
    return render(request, "about.html")

def result(request):
    text = request.GET["fulltext"]
    words = text.split()
    word_dict = {}

    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return render(request, "result.html", {"full" : text, "total":len(words), "count":word_dict.items()})