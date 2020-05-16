from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.
# class IndexView(View):
#     #请求为get时
#     def get(self,request):
#         return HttpResponse('index.html')
#     #请求为post时
#     def post(self,request):
#         return HttpResponse('index.html')
 
def index(request):
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': 1,
    # }
    # print(request.)
    # return HttpResponse(template.render(context, request))
    if request.method == 'GET':
        return render(request, 'polls/index.html')
    elif request.method == 'POST':
        return HttpResponse("post")

# def index(request):
#     with open(os.path.join(BASE_DIR, 'public/html/index.html')) as f:
#         contents = f.read().rstrip()
#     return HttpResponse(contents)
    #count=2
    #return HttpResponse("You've polled {}.".format(count))
    #return HttpResponse(os.path.join(BASE_DIR, 'db.sqlite3'))