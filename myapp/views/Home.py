'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from myapp.models import MentorPost


@login_required(login_url='/signin')
def index(request):
	#collection.setObjectClass(MentorPost.class);
	#blog = BlogPost(title="abc")
	#blog.published_date = datetime(2014,1,6,0,0,0)
	#blog.save()
	#for blog in BlogPost.objects:
		#print(blog.title)
	#return HttpResponse(BlogPost.objects);
	posts = MentorPost.objects
	for post in posts:
		print(post.imagelink)
		
	context = {'posts':posts,'user_type':request.session['user_type'],'user_id':request.user,}
	return render(request,'myapp/index.html', context)