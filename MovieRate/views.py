from django.shortcuts import redirect, render, render_to_response
from MovieRate.models import Movie, Comment, Movie_xml
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Q
import time


def home_page(request):
    if (request.method == 'POST' and request.POST.get(
      'Add_send_Detail', '') == 'submit_send_data'):
        if request.POST['name_text'] != '':
            Movie.objects.create(
                             name=request.POST['name_text'],
                             detail=request.POST['detail_text'],
                             lead_actors=request.POST['actor_text'],
                             director=request.POST['director_text'],
                             genre=request.POST['genre_text'],
                             release_date=request.POST['date_text'],
                             rate=0,
                             viewer=0,
                             poster=request.POST['poster_url'],
                             picture=request.POST['pic_url'],
                             clip=request.POST['clip_url'],
                             add_date=datetime.now(),
                                 )
            Movie_xml()
        return redirect('/')
    movies = Movie.objects.all()
    #found=''
    movies_s=[]
    str_f=0
    search=''
    if (request.method == 'GET' and request.GET.get('ss', '') == 'submit_search'):
        if request.GET['search_box'] != '':
            search = request.GET['search_box']
            for movie in movies:
                 checkcount=0
                 if movie.name.lower().find(search.lower()) != -1: 
                     checkcount=1
                 elif movie.detail.lower().find(search.lower()) != -1:
                     checkcount=1
                 elif movie.director.lower().find(search.lower()) != -1:
                     checkcount=1
                 elif movie.lead_actors.lower().find(search.lower()) != -1:
                     checkcount=1
                 elif movie.genre.lower().find(search.lower()) != -1:
                     checkcount=1
                 if checkcount==1: 
                     movies_s.append(movie.id)
                     str_f=1
        if str_f != 1: str_f=2
            

    if (request.method == 'POST' and request.POST.get(
      'back_send', '') == 'Back_send'):
        return redirect('/')
    if (request.method == 'POST' and request.POST.get(
      'send_add_data', '') == 'send_Add Movie'):
        return redirect('/')
    if(request.method == 'POST' and request.POST.get(
      'delete', '') == 'delete'):
        id_data = request.POST['id_delete']
        Movie.objects.get(pk=id_data).delete()
        Movie_xml()
        return redirect('/')
    # login
    if(request.method == 'POST' and request.POST.get(
      'send_login', '') == 'send'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
	
        if user is not None:
            auth.login(request, user)
        else:
            alarm = 'error. please try again.'
            return render(request, 'registration/login.html', {'alarm': alarm})

    # logout
    if(request.method == 'POST' and request.POST.get(
      'submit_logout_page', '') == 'go_logout'):
        auth.logout(request)


      
    return render(request, 'home.html',{'movies':movies , 'movies_s':movies_s , 'str_f':str_f , 'search':search})


def edit_page(request, movie_id):
    movie_ = Movie.objects.get(id=movie_id)
  
    # แก้ไข รายละเอียดหนัง
    if (request.method == 'POST' and request.POST.get(
      'Update_send_Detail', '') == 'submit_send_update'):
        movie_ = Movie.objects.get(id=movie_id)
        if request.POST['name_text'] != '':
            movie_.name = request.POST['name_text']
        if request.POST['detail_text'] != '':
            movie_.detail = request.POST['detail_text']
        if request.POST['date_text'] != '':
            movie_.release_date = request.POST['date_text']
        if request.POST['actor_text'] != '':
            movie_.lead_actors = request.POST['actor_text']
        if request.POST['director_text'] != '':
            movie_.director = request.POST['director_text']
        if request.POST['genre_text'] != '':
            movie_.genre = request.POST['genre_text']
        if request.POST['clip_url'] != '':
            movie_.clip = request.POST['clip_url']
        if request.POST['poster_url'] != '':
            movie_.poster = request.POST['poster_url']
        if request.POST['pic_url'] != '':
            movie_.picture = request.POST['pic_url']
        movie_.add_date = movie_.add_date
        movie_.save()
        Movie_xml()
        return redirect('/movie_detail/%d' % int(movie_.id)) 
    return render(request, 'edit.html', {'movie_': movie_})


def add_page(request):
    if request.method == 'POST':
        return redirect('/add_movie')
    return render(request, 'add.html')


def movie_detail_page(request, movie_id):
    movie_ = Movie.objects.get(id=movie_id)
    picdet = []
    details = movie_.detail.split("\n")


    if movie_.picture != '':
       picdet=movie_.picture.split(" ")
       
    comments = Comment.objects.filter(movie=movie_)
    # rating
    if (request.method == 'POST' and request.POST.get(
      'send_rate', '') == 'send_rate'):
        star = float(request.POST.get('star', 0))
        point = int(movie_.viewer)*float(movie_.rate)
        movie_.viewer = int(movie_.viewer)+1
        movie_.rate = float(format(((point+star)/movie_.viewer), '.1f'))
        movie_.save()

    # กรณีใส่คอมเมนต์
    if (request.method == 'POST' and request.POST.get(
      'send_comment', '') == 'send_Comment'):
        if request.POST['user_name'] != '' and request.POST[
          'comment_text'] != '':
            Comment.objects.create(
                                      user=request.POST['user_name'],
                                      comment_text=request.POST[
                                        'comment_text'],
                                      date=datetime.now(),
                                      like=0,
                                      movie=movie_,)
            movie_.countcom = int(movie_.countcom)+1
            movie_.save()
            return redirect('/movie_detail/%d' % int(movie_id))
    # กรณีกดไลค์
    if(request.method == 'POST' and request.POST.get(
      'send_like', '') == 'submit_like'):
        id_comment = request.POST['id_send_like']
        comment_ = Comment.objects.get(id=id_comment)
        add_like = int(comment_.like) + 1
        comment_.like = add_like
        comment_.save()
        return redirect('/movie_detail/%d' % int(movie_id))

    if(request.method == 'POST' and request.POST.get(
      'send_unlike', '') == 'submit_unlike'):
        id_comment = request.POST['id_send_unlike']
        comment_ = Comment.objects.get(id=id_comment)
        add_unlike = int(comment_.unlike) + 1
        comment_.unlike = add_unlike
        comment_.save()
        return redirect('/movie_detail/%d' % int(movie_id))

    paginator = Paginator(comments, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages) 
    return render(request, 'detail.html', {
                  'movie_': movie_, 'comments': comments, 'picdet':picdet , 'details':details,'contacts':contacts})


def login_page(request):
    if(request.method == 'POST' and request.POST.get(
      'submit_login_page', '') == 'go_login'):
        return redirect('/accounts/login/')
    return render(request, 'registration/login.html')


def register_page(request):
    if(request.method == 'POST' and request.POST.get(
      'submit_regis_page', '') == 'go_regis'):
        return redirect('/accounts/registration/')
    return render(request, 'registration/registration_form.html')

def news1(request):
    return render(request, '1.html')

def news2(request):
    return render(request, '2.html')

def news3(request):
    return render(request, '3.html')

def news4(request):
    return render(request, '4.html')

def news5(request):
    return render(request, '5.html')

def news6(request):
    return render(request, '6.html')

def news7(request):
    return render(request, '7.html')

def news8(request):
    return render(request, '8.html')

def news9(request):
    return render(request, '9.html')

def news10(request):
    return render(request, '10.html')

def register_complete_page(request):
    # register
    alarm = ''
    if(request.method == 'POST' and request.POST.get(
      'send_register', '') == 'send'):
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        alarm = ''
        if (request.POST['password1'] == request.POST['password2'] and
           username != '' and request.POST['password1'] != ''):
            if User.objects.filter(username=username).count() == 0:
                new_user = User.objects.create_user(username, email, password)
                new_user.is_staff = True
                new_user.save()
                return redirect('/accounts/registration_complete/')
            else:
                alarm = "already have this username."
        else:
            alarm = "error. please try again"

        return render(request,
                      'registration/registration_form.html', {'alarm': alarm})
    return render(request, 'registration/registration_complete.html')


def movie_comming(request):
    movies = Movie.objects.all()
    Day = int(time.strftime("%Y%m%d"))
    IDcomming = []
    Datecomming = []
    if Movie.objects.count() != 0:
        for movie in movies:
            if str(movie.release_date) != "":
                date = str(movie.release_date).split("-")
                F = ""
                for j in range(len(date)):
                    F = F+str(date[j])
                dates = int(F)
            else:
                dates = Day
            if Day < dates:
                IDcomming.append(movie.id)
                Datecomming.append(dates)
                for i in range(len(Datecomming)):
                    for j in range(len(Datecomming)):
                        if Datecomming[i] <= Datecomming[j]:
                            tempd = Datecomming[j]
                            Datecomming[j] = Datecomming[i]
                            Datecomming[i] = tempd

                            temp = IDcomming[j]
                            IDcomming[j] = IDcomming[i]
                            IDcomming[i] = temp
    contact_list=[]
    for ids in IDcomming :   
        for movie in movies:
           if ids==movie.id :
                 contact_list.append(Movie.objects.get(id=ids))
        
    #contact_list = Movie.objects.all()
    paginator = Paginator(contact_list, 20) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)    
    return render(request, 'commingsoon.html', {
        'movies': movies, 'IDcomming': IDcomming ,'contacts':contacts
                  })


def movie_now(request):
    movies = Movie.objects.all()
    Day = int(time.strftime("%Y%m%d"))
    IDnow = []
    Date = []
    if Movie.objects.count() != 0:
        for movie in movies:
            if str(movie.release_date) != "":
                date = str(movie.release_date).split("-")
                F = ""
                for j in range(len(date)):
                    F = F+str(date[j])
                dates = int(F)
            else:
                dates = Day
            if Day >= dates:
                Date.append(dates)
                IDnow.append(movie.id)
                for i in range(len(Date)):
                    for j in range(len(Date)):
                        if Date[i] >= Date[j]:
                            tempd = Date[j]
                            Date[j] = Date[i]
                            Date[i] = tempd

                            temp = IDnow[j]
                            IDnow[j] = IDnow[i]
                            IDnow[i] = temp
    contact_list=[]
    for ids in IDnow :   
        for movie in movies:
           if ids==movie.id :
                 contact_list.append(Movie.objects.get(id=ids))
        
    #contact_list = Movie.objects.all()
    paginator = Paginator(contact_list, 20) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'movienow.html', {
        'movies': movies, 'IDnow': IDnow ,'contacts':contacts
                  })


def show_all(request):
    movies = Movie.objects.all()
    Day = int(time.strftime("%Y%m%d"))
    IDall = []
    Date = []
    if Movie.objects.count() != 0:
        for movie in movies:
            if str(movie.release_date) != "":
                date = str(movie.release_date).split("-")
                F = ""
                for j in range(len(date)):
                    F = F+str(date[j])
                dates = int(F)
            else:
                dates = Day
            Date.append(dates)
            IDall.append(movie.id)
            for i in range(len(Date)):
                for j in range(len(Date)):
                    if Date[i] >= Date[j]:
                        tempd = Date[j]
                        Date[j] = Date[i]
                        Date[i] = tempd

                        temp = IDall[j]
                        IDall[j] = IDall[i]
                        IDall[i] = temp
    contact_list=[]
    for ids in IDall :   
        for movie in movies:
           if ids==movie.id :
                 contact_list.append(Movie.objects.get(id=ids))
        
    #contact_list = Movie.objects.all()
    paginator = Paginator(contact_list, 20) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'showall.html', {
        'movies': movies, 'IDall': IDall ,'contacts':contacts
                  })


def last_movie(request):
    movies = Movie.objects.all()
    Day = int(time.strftime("%Y%m%d"))
    IDlast = []
    Date = []
    if Movie.objects.count() != 0:
        for movie in movies:
            if str(movie.release_date) != "":
                date = str(movie.release_date).split("-")
                F = ""
                for j in range(len(date)):
                    F = F+str(date[j])
                dates = int(F)
            else:
                dates = Day
            if Day < dates:
                IDlast.append(movie.id)
                Date.append(dates)
                for i in range(len(Date)):
                    for j in range(len(Date)):
                        if Date[i] <= Date[j]:
                            tempd = Date[j]
                            Date[j] = Date[i]
                            Date[i] = tempd

                            temp = IDlast[j]
                            IDlast[j] = IDlast[i]
                            IDlast[i] = temp
    return render(request, 'lastmovie.html', {
        'movies': movies, 'IDlast': IDlast
                  })


def top_rate(request):
    movies = Movie.objects.all()
    IDrate = []
    Rate = []
    if Movie.objects.count() != 0:
        for movie in movies:
            Rate.append(movie.rate)
            IDrate.append(movie.id)
            for i in range(len(Rate)):
                for j in range(len(Rate)):
                    if Rate[i] >= Rate[j]:
                        tempr = Rate[j]
                        Rate[j] = Rate[i]
                        Rate[i] = tempr

                        temp = IDrate[j]
                        IDrate[j] = IDrate[i]
                        IDrate[i] = temp
    contact_list=[]
    for ids in IDrate :   
        for movie in movies:
           if ids==movie.id :
                 contact_list.append(Movie.objects.get(id=ids))
        
    #contact_list = Movie.objects.all()
    paginator = Paginator(contact_list, 20) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'toprate.html', {
        'movies': movies, 'IDrate': IDrate ,'contacts':contacts
                  })


def most_comment(request):
    movies = Movie.objects.all()
    IDcomm = []
    Com = []
    if Movie.objects.count() != 0:
        for movie in movies:
            Com.append(movie.countcom)
            IDcomm.append(movie.id)
            for i in range(len(Com)):
                for j in range(len(Com)):
                    if Com[i] >= Com[j]:
                        tempc = Com[j]
                        Com[j] = Com[i]
                        Com[i] = tempc
                        temp = IDcomm[j]
                        IDcomm[j] = IDcomm[i]
                        IDcomm[i] = temp
    contact_list=[]
    for ids in IDcomm :   
        for movie in movies:
           if ids==movie.id :
                 contact_list.append(Movie.objects.get(id=ids))
        
    #contact_list = Movie.objects.all()
    paginator = Paginator(contact_list, 20) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'mostcomment.html', {
        'movies': movies, 'IDcomm': IDcomm , 'contacts':contacts
                  })
def listing(request,search):
    movies = Movie.objects.all()
    for movie in movies:
         if movie.name.lower().find(search.lower()) != -1:
                movies_s.append(movie.id)
                str_f=1
    if str_f != 1: str_f=2
    return render(request, 'list.html', {'str_f':str_f,'movies_s':movies_s,'movies':movies})

#def search_titles(request):
 #   if request.method == "POST" :
  #     search_text=request.POST['search_test']
   # else :
    #   search_text=''
   # movies= Movie.objects.filter(name__contains=search_text)
    #return render_to_response('ajax_search.html',{'movies':movies})
    

#def contact(request):
 #   if request.method == 'POST':
  #      return redirect('/contact')
   # return render(request, 'contact.html')
