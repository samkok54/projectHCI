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


class TestCodeFormat(TestCase):

    def test_functional_test(self):
        pep8style = pep8.StyleGuide(show_source=True)
        result = pep8style.check_files([
                 '/home/poo/assignment_ii/functional_tests/tests.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_test(self):
        pep8style = pep8.StyleGuide(show_source=True)
        result = pep8style.check_files([
                 '/home/poo/assignment_ii/MovieRate/tests.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_view(self):
        pep8style = pep8.StyleGuide(show_source=True)
        result = pep8style.check_files([
                 '/home/poo/assignment_ii/MovieRate/views.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_model(self):
        pep8style = pep8.StyleGuide(show_source=True)
        result = pep8style.check_files([
                 '/home/poo/assignment_ii/MovieRate/models.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
