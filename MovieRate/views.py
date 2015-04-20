from django.shortcuts import redirect, render
from MovieRate.models import Movie

def home_page(request):
    if (request.method == 'POST' and request.POST.get('Add_send_Detail','') == 'submit_send_data'):
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
    if (request.method == 'POST' and request.POST.get('back_send','') == 'Back_send' ):
        return redirect('/')
    if (request.method == 'POST' and request.POST.get('send_add_data','') == 'send_Add Movie' ):
        return redirect('/')
    if(request.method == 'POST' and request.POST.get(
                                    'delete', '') == 'delete'):
        id_data = request.POST['id_delete']
        Movie.objects.get(pk=id_data).delete()
        return redirect('/')
    movies = Movie.objects.all()
    return render(request, 'home.html', {
        'movies': movies,
                  })

def add_page(request):

    if request.method == 'POST':
        return redirect('/add_movie')
    return render(request, 'add.html',)

def movie_detail_page(request, movie_id):
    movie_ = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie_': movie_})

