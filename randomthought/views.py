from django.shortcuts import render

# Create your views here.
def randomthought(request):
    return render(request,
                  'randomthought/randomthought_view.html')