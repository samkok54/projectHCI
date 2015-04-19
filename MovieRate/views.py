from django.shortcuts import redirect, render
from MovieRate.models import Movie

def home_page(request):
    if request.method == 'POST':
        if request.POST['name_text'] != '' :
            Movie.objects.create(name=request.POST['name_text'],
                             detail=request.POST['detail_text'],
                             release_date=request.POST['date_text'],
                             rate=0,
                             viewer=0,
                             poster=request.POST['poster_url'],
                             add_date='',
                              )
        return redirect('/')
    movies = Movie.objects.all()
    return render(request, 'home.html', {
        'movies': movies,
                  })

def add_page(request):

    if request.method == 'POST':
        return redirect('/add_movie')
    return render(request, 'add.html',)
