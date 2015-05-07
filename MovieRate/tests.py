from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from MovieRate.models import Movie, Comment
from MovieRate.views import home_page, edit_page, add_page, movie_detail_page
from MovieRate.views import login_page, register_page, movie_comming, movie_now
import pep8


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_root_url_resolves_to_add_page_view(self):
        found = resolve('/add_movie')
        self.assertEqual(found.func, add_page)

    def test_add_movie_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['name_text'] = 'X-men'
        request.POST['actor_text'] = ''
        request.POST['director_text'] = ''
        request.POST['genre_text'] = ''
        request.POST['clip_url'] = ''
        request.POST['detail_text'] = '3D/IMAX'
        request.POST['date_text'] = '2015-04-21'
        request.POST['poster_url'] = (
         'https://siam-movie.com/wp-content/uploads/2014/05/1395818775261.jpg')
        request.POST['Add_send_Detail'] = 'submit_send_data'

        response = home_page(request)

        new_movie = Movie.objects.first()
        self.assertEqual(new_movie.name, 'X-men')
        self.assertEqual(new_movie.release_date, '2015-04-21')
        self.assertEqual(new_movie.detail, '3D/IMAX')
        self.assertEqual(new_movie.poster, (
         'https://siam-movie.com/wp-content/uploads/2014/05/1395818775261.jpg')
                         )

    def test_home_page_only_saves_movie_when_necessary(self):
        request = HttpRequest()
        home_page(request)

    def test_home_page_displays_all_list_movies(self):
        Movie.objects.create(name='X-men 2')
        Movie.objects.create(name='Captian America')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('X-men 2', response.content.decode())
        self.assertIn('Captian America', response.content.decode())

    def test_edit_movie(self):
        movie_ = Movie()
        movie_.name = 'X-men'
        movie_.detail = ''
        movie_.release_date = '2015-04-21'
        movie_.poster = 'http://upic.me/i/6r/wallpaper3.jpg'
        movie_.lead_actors = ''
        movie_.director = ''
        movie_.genre = ''
        movie_.clip = ''
        movie_.save()
        movie = Movie.objects.first()
        movie_id = movie.id
        request = HttpRequest()
        request.method = 'POST'
        request.POST['name_text'] = 'Kamenraider'
        request.POST['detail_text'] = '3D/IMAX'
        request.POST['date_text'] = '2015-04-01'
        request.POST['poster_url'] = (
         'http://upic.me/i/6r/wallpaper3.jpg')
        request.POST['actor_text'] = ''
        request.POST['director_text'] = ''
        request.POST['genre_text'] = ''
        request.POST['clip_url'] = ''
        request.POST['Update_send_Detail'] = 'submit_send_update'

        response = edit_page(request, movie_id)

        edit_movie = Movie.objects.first()
        self.assertEqual(edit_movie.name, 'Kamenraider')
        self.assertEqual(edit_movie.release_date, '2015-04-01')
        self.assertEqual(edit_movie.detail, '3D/IMAX')
        self.assertEqual(edit_movie.poster, (
         'http://upic.me/i/6r/wallpaper3.jpg')
                         )

    def test_root_url_resolves_to_detail_page_view(self):
        movie_ = Movie()
        movie_.name = 'Kamenraider'
        movie_.detail = ''
        movie_.release_date = '2015-04-21'
        movie_.poster = 'http://upic.me/i/6r/wallpaper3.jpg'
        movie_.save()
        movie = Movie.objects.first()
        movie_id = movie.id
        request = HttpRequest()

        response = movie_detail_page(request, movie_id)

        found = resolve('/movie_detail/1/')
        self.assertEqual(found.func, movie_detail_page)

    def test_rating_movie(self):
        movie_ = Movie()
        movie_.name = 'X-men'
        movie_.detail = ''
        movie_.release_date = '2015-04-21'
        movie_.poster = 'http://upic.me/i/6r/wallpaper3.jpg'
        movie_.save()
        movie = Movie.objects.first()
        movie_id = movie.id
        request = HttpRequest()
        request.method = 'POST'
        request.POST['star'] = '3'
        request.POST['send_rate'] = 'send_rate'

        response = movie_detail_page(request, movie_id)

        edit_movie = Movie.objects.first()
        self.assertEqual(edit_movie.rate, 3.0)

    def test_comment_movie(self):
        movie_ = Movie()
        movie_.name = 'X-men'
        movie_.detail = ''
        movie_.release_date = '2015-04-21'
        movie_.poster = 'http://upic.me/i/6r/wallpaper3.jpg'
        movie_.save()
        movie = Movie.objects.first()
        movie_id = movie.id
        request = HttpRequest()
        request.method = 'POST'
        request.POST['user_name'] = 'Poowapong'
        request.POST['comment_text'] = 'Perfect'
        request.POST['send_comment'] = 'send_Comment'

        response = movie_detail_page(request, movie_id)

        comment_movie = Comment.objects.first()
        self.assertEqual(comment_movie.user, 'Poowapong')
        self.assertEqual(comment_movie.comment_text, 'Perfect')

    def test_like_comment_movie(self):
        movie_ = Movie()
        movie_.name = 'X-men'
        movie_.detail = ''
        movie_.release_date = '2015-04-21'
        movie_.poster = 'http://upic.me/i/6r/wallpaper3.jpg'
        movie_.save()
        movie = Movie.objects.first()
        movie_id = movie.id
        comment_ = Comment()
        comment_.movie = movie
        comment_.user = 'Poo'
        comment_.comment_text = 'Great'
        comment_.save()
        request = HttpRequest()
        request.method = 'POST'
        request.POST['like'] = '1'
        request.POST['id_send_like'] = '1'
        request.POST['send_like'] = 'submit_like'

        response = movie_detail_page(request, movie_id)

        comment_movie = Comment.objects.first()
        self.assertEqual(comment_movie.like, 1)

    def test_delete_movie(self):
        movie_ = Movie()
        movie_.name = 'X-men'
        movie_.detail = ''
        movie_.release_date = '2015-04-21'
        movie_.poster = 'http://upic.me/i/6r/wallpaper3.jpg'
        movie_.save()
        request = HttpRequest()
        request.method = 'POST'
        request.POST['id_delete'] = '1'
        request.POST['delete'] = 'delete'

        response = home_page(request)

        self.assertEqual(Movie.objects.count(), 0)


class MovieModelTest(TestCase):

    def test_saving_and_retrieving_movies(self):
        first_movie = Movie()
        first_movie.name = 'The first (ever) list movie'
        first_movie.save()

        second_movie = Movie()
        second_movie.name = 'The second movie'
        second_movie.save()

        saved_movies = Movie.objects.all()
        self.assertEqual(saved_movies.count(), 2)

        first_saved_movie = saved_movies[0]
        second_saved_movie = saved_movies[1]
        self.assertEqual(first_saved_movie.name, 'The first (ever) list movie')
        self.assertEqual(second_saved_movie.name, 'The second movie')


class TestCodeFormat(TestCase):

    def test_functional_test(self):
        pep8style = pep8.StyleGuide(show_source=True)
        result = pep8style.check_files([
                 'functional_tests/tests.py'])
        self.assertEqual(result.total_errors, 0,
                         "FT found code style errors (and warnings).")

    def test_test(self):
        pep8style = pep8.StyleGuide(show_source=True)
        result = pep8style.check_files([
                 'MovieRate/tests.py'])
        self.assertEqual(result.total_errors, 0,
                         "UT found code style errors (and warnings).")

    def test_view(self):
        pep8style = pep8.StyleGuide(show_source=True)
        result = pep8style.check_files([
                 'MovieRate/views.py'])
        self.assertEqual(result.total_errors, 0,
                         "views found code style errors (and warnings).")

    def test_model(self):
        pep8style = pep8.StyleGuide(show_source=True)
        result = pep8style.check_files([
                 'MovieRate/models.py'])
        self.assertEqual(result.total_errors, 0,
                         "models found code style errors (and warnings).")
