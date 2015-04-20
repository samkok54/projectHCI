from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_add_new_movie(self):
        # open browser
        self.browser.get('http://localhost:8000')
        self.assertIn('Movie Rate App', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Movie Rate', header_text)

        # click add movie and go to add page
        self.browser.find_element_by_id('add_data').click()
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Add New Movie', header_text)

        inputname = self.browser.find_element_by_id('id_new_name')
        self.assertEqual(
                inputname.get_attribute('placeholder'),
                'New Movie Name'
        )
        inputname.send_keys('movieA')

        self.browser.find_element_by_id('submit_data').click()

        # back to homepage
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Movie Rate', header_text)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('movieA\n0.0', [row.text for row in rows])

    def test_view_movie_detail_page(self):
        # open browser
        self.browser.get('http://localhost:8000')
        self.assertIn('Movie Rate App', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Movie Rate', header_text)

        # click more... of movieA
        self.browser.find_element_by_id('view_detail_1').click()
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Detail of movieA', header_text)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
