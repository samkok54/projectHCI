from django.core.urlresolvers import resolve
from django.test import TestCase
from MovieRate.views import home_page
import pep8


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


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
