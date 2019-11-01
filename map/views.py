from . import models
import json
import uuid
from datetime import datetime
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
#from .forms import PostingForm
from .models import PostData
from django.http import Http404

#Token 
def set_submit_token(request):
    submit_token = str(uuid.uuid4())
    request.session['submit_token'] = submit_token
    #print("Token1 :: "+str(submit_token))
    return submit_token

def exists_submit_token(request):
    token_in_request = request.POST.get('submit_token')
    token_in_session = request.session.pop('submit_token', '')
    print("TokenRequest :: "+str(token_in_request))
    print("TokenSession :: "+str(token_in_session))
    if not token_in_request:
        return False
    if not token_in_session:
        return False
    return token_in_request == token_in_session


@login_required
def map_TownHero(request):
    print("---map_TOWNHERO---")
    submit_token = set_submit_token(request)
    form = PostingForm(request.POST,request.FILES)
    context = {
        "posts":PostData.objects.all(),
        "forms":form,
        "submit_token":submit_token,

    }
    return render(request, 'application.html',context)

def post(request):
    print("---POST---")
    if not exists_submit_token(request):
        raise Http404('Dont Reload!!')
        #form = PostingForm(request.POST,request.FILES)
        #context = {
        #"forms":form,
        #"submit_token":submit_token,
        #}
        #return render(request, 'application.html')
    elif request.method == 'POST':
        submit_token = set_submit_token(request)
        form = PostingForm(request.POST,request.FILES)
        if form.is_valid():
            post = PostData()
            post.purpose = form.cleaned_data['purpose']
            post.message = form.cleaned_data['message']
            post.pic = form.cleaned_data['pic']
            post.user = request.user
            #print("create postdata objects")
            PostData.objects.create(
                purpose=post.purpose,
                user=post.user,
                message = post.message,
                pic = post.pic,
                post_flag = True,
            )
    context = {
        "forms":form,
        "posts":PostData.objects.all(),
        "submit_token":submit_token,
    }
    return render(request, 'application.html', context)

def delete(request):
    print("---Delete---")
    submit_token = set_submit_token(request)
    form = PostingForm(request.POST,request.FILES)
    context = {
        "forms":form,
        "posts":PostData.objects.all(),
        "submit_token":submit_token,
    }
    if request.method == 'POST' and request.body:
        id = request.POST.get("id")
        #print(id)
        post = PostData.objects.get(id=id)
        #print("post.post_flag = " + str(post.post_flag))
        post.post_flag = False
        #print("post.post_flag = " + str(post.post_flag))
        post.save()
    return render(request, 'application.html',context)
