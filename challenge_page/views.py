from django.shortcuts import render,redirect
from .models import challenge
from django.views.generic import ListView


# Create your views here.

def index(request):
	return render (request,"challenge_page/index.html")


class challengeListView(ListView):
	model = challenge
	template_name = 'challenge_page/index.html'

	def get_queryset(self):
		return challenge.objects.all().order_by('-deadline')


def challengeview(request):
	if request.method=='GET':
		sortlabel=request.GET.get('sortlabel', 'title')
		order=request.GET.get('order', 'ascending')

		if order == 'ascending':
			challenges = challenge.objects.all().order_by(sortlabel)
		else:
			challenges = challenge.objects.all().order_by('-'+sortlabel)		
		return render(request,'challenge_page/index.html',{'challenges' : challenges})
	else:
		challenges = challenge.objects.all()
		return render(request,'challenge_page/index.html',{'challenges' : challenges})
	


def register(request):
	if request.method=='POST':
		title=request.POST['title']
		deadline=request.POST['deadline']
		tags=request.POST['tags']
		ch = challenge()
		ch.title=title
		ch.deadline=deadline
		ch.tags=tags
		ch.save()	
		return redirect('/')
	else:
		return render(request,'challenge_page/register.html')
