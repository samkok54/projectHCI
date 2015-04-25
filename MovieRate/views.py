from django.shortcuts import redirect, render
from MovieRate.models import Movie,Comment
from datetime import datetime 
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import time 
def home_page(request):
    if (request.method == 'POST' and request.POST.get('Add_send_Detail','') == 'submit_send_data'):
        if request.POST['name_text'] != '' :
            Movie.objects.create(name=request.POST['name_text'],
                             detail=request.POST['detail_text'],
                             release_date=request.POST['date_text'],
                             rate=0,
                             viewer=0,
                             poster=request.POST['poster_url'],
                             add_date=datetime.now(),
                              )
        return redirect('/')
    if (request.method == 'POST' and request.POST.get('back_send','') == 'Back_send' ):
        return redirect('/')
    if (request.method == 'POST' and request.POST.get('send_add_data','') == 'send_Add Movie' ):
        return redirect('/')
    if(request.method == 'POST' and request.POST.get(
                                    'delete', '') == 'delete'):
        id_data = request.POST['id_delete']
        Movie.objects.get(pk=id_data).delete()
        return redirect('/')

    # login
    if(request.method == 'POST' and request.POST.get('send_login', '') == 'send'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

    # logout
    if(request.method == 'POST' and request.POST.get('submit_logout_page', '') == 'go_logout'):
        auth.logout(request)

    # register
    if(request.method == 'POST' and request.POST.get('send_register', '') == 'send'):
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if request.POST['password1'] == request.POST['password2']:
            if User.objects.filter(username=username).count() == 0:
                new_user = User.objects.create_user(username, email, password)
                new_user.is_staff = True
                new_user.save() 
    movies = Movie.objects.all()
    Day = int(time.strftime("%Y%m%d"))
    IDcomming=[]
    IDnow=[]
    if Movie.objects.count() != 0:
        for movie in movies:
            if str(movie.release_date) != "" :
                date=str(movie.release_date).split("-")
                F=""
                for j in range (len(date)) :
                    F=F+str(date[j])
                dates=int(F)
            else :
                dates=Day
            if Day<dates :
                IDcomming.append(movie.id)
            else :
                IDnow.append(movie.id)

    return render(request, 'home.html', {
        'movies': movies,'IDcomming':IDcomming,'IDnow':IDnow
                  })


def edit_page(request, movie_id):
    if (request.method == 'POST' and request.POST.get('send_Edit','') == 'send_edit'):
        movie_ = Movie.objects.get(id=movie_id)
        return render(request, 'edit.html', {'movie_': movie_})
    # แก้ไข รายละเอียดหนัง
    if (request.method == 'POST' and request.POST.get('Update_send_Detail','') == 'submit_send_update'):
        #movie_id = request.POST['id_update']
        movie_ = Movie.objects.get(id=movie_id)
        if request.POST['name_text'] != '':
            movie_.name = request.POST['name_text']
        if request.POST['detail_text'] != '':
            movie_.detail = request.POST['detail_text']
        if request.POST['date_text'] != '':
            movie_.release_date=request.POST['date_text']
        if request.POST['poster_url'] != '':
            movie_.poster=request.POST['poster_url']
        movie_.add_date = movie_.add_date
        movie_.save()
        return redirect('/movie_detail/%d' % int(movie_.id))
    return redirect('/detail')

def add_page(request):
    if request.method == 'POST':
        return redirect('/add_movie')
    return render(request, 'add.html',)

def movie_detail_page(request, movie_id):
    movie_ = Movie.objects.get(id=movie_id)
    comments = Comment.objects.filter(movie=movie_)
    # rating
    if (request.method == 'POST' and request.POST.get('send_rate','') == 'send_rate'):
        star = float(request.POST.get('star',0))
        point = int(movie_.viewer)*float(movie_.rate)
        movie_.viewer=int(movie_.viewer)+1
        movie_.rate=float(format(((point+star)/movie_.viewer),'.1f'))
        movie_.save()

    # กรณีใส่คอมเมนต์
    if (request.method == 'POST' and request.POST.get('send_comment','') == 'send_Comment'):
        if request.POST['user_name'] != '' and request.POST['comment_text'] != '' :
            Comment.objects.create(
                                      user = request.POST['user_name'],
                                      comment_text = request.POST['comment_text'],
                                      date = datetime.now(),
                                      like = 0, 
                                      movie = movie_,)
            movie_.countcom=int(movie_.countcom)+1
            movie_.save()
            return redirect('/movie_detail/%d' % int(movie_id))
    # กรณีกดไลค์
    if(request.method == 'POST' and request.POST.get('send_like', '') == 'submit_like'):
        id_comment = request.POST['id_send_like']
        comment_ = Comment.objects.get(id=id_comment)
        add_like = int(comment_.like) + 1
        comment_.like = add_like
        comment_.save()
        return redirect('/movie_detail/%d' % int(movie_id))
    return render(request, 'detail.html', {'movie_': movie_,'comments': comments})

def login_page(request):
    if(request.method == 'POST' and request.POST.get('submit_login_page', '') == 'go_login'):
        return redirect('/accounts/login/')
    return render(request, 'registration/login.html')

def register_page(request):
    if(request.method == 'POST' and request.POST.get('submit_regis_page', '') == 'go_regis'):
        return redirect('/accounts/registration/')
    return render(request, 'registration/registration_form.html')

def movie_comming(request):
    movies = Movie.objects.all()
    Day = int(time.strftime("%Y%m%d"))
    IDcomming=[]
    IDnow=[]
    if Movie.objects.count() != 0:
        for movie in movies:
            if str(movie.release_date) != "" :
                date=str(movie.release_date).split("-")
                F=""
                for j in range (len(date)) :
                    F=F+str(date[j])
                dates=int(F)
            else :
                dates=Day
            if Day<dates :
                IDcomming.append(movie.id)

    return render(request, 'commingsoon.html', {
        'movies': movies,'IDcomming':IDcomming
                  })

def movie_now(request):
    movies = Movie.objects.all()
    Day = int(time.strftime("%Y%m%d"))
    IDcomming=[]
    IDnow=[]
    if Movie.objects.count() != 0:
        for movie in movies:
            if str(movie.release_date) != "" :
                date=str(movie.release_date).split("-")
                F=""
                for j in range (len(date)) :
                    F=F+str(date[j])
                dates=int(F)
            else :
                dates=Day
            if Day>=dates :
                IDnow.append(movie.id)

    return render(request, 'movienow.html', {
        'movies': movies,'IDnow':IDnow
                  })


