from django.shortcuts import render
from django.http import HttpResponse
from django.contib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='signin')
def search(request):
    user_object = user.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)
    
    if request.method=='POST':
        username = request.POST['username']
        username_object = user_objects.filter(username__icontain=username)
       
        username_profile = []
        username_profile_list = []
        
        for users in username_object:
            username_profile.append(users.id)
            
        for ids in username_profile:
            profile_lists = profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
            
       username_profile_list = list(chain("username_profile_list))   
    return render(request, 'serach.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})

                


