from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row(self, row_text, idT):
        table = self.browser.find_element_by_id(idT)
        rows = table.find_elements_by_tag_name('td')
        self.assertIn(row_text, [row.text for row in rows])

    def test_add_new_movie_and_view_movie_detail_page(self):
        # open browser
        self.browser.get(self.live_server_url)
        self.assertIn('Movie Rate App', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Movie Rate', header_text)

        # click add movie and go to add page(add.html)
        self.browser.find_element_by_id('add_data').click()
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Add New Movie', header_text)

        inputname = self.browser.find_element_by_id('id_new_name')
        inputdate = self.browser.find_element_by_id('id_new_date')
        inputdetail = self.browser.find_element_by_id('id_new_detail')
        inputURL = self.browser.find_element_by_id('id_new_pic')
        # check placeholder of input tab
        self.assertEqual(
                inputname.get_attribute('placeholder'),
                'New Movie Name'
        )
        self.assertEqual(
                inputdate.get_attribute('placeholder'),
                'Add Release Date'
        )
        self.assertEqual(
                inputdetail.get_attribute('placeholder'),
                'Add Details'
        )
        self.assertEqual(
                inputURL.get_attribute('placeholder'),
                'Add Poster URL'
        )
        # input data of movie Fast And Furious 7
        inputname.send_keys('Fast And Furious 7')
        inputdate.click()
        inputdate.send_keys(Keys.ESCAPE)
        inputdate.send_keys('04/01/2015')
        inputdetail.send_keys('action')
        inputURL.send_keys('http://www.majorcineplex.com/uploads/movie/868/thumb_868.jpg')
        self.browser.find_element_by_id('submit_data').click()

        # back to homepage
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Movie Rate', header_text)
        self.check_for_row('Fast And Furious 7\n0.0', 'id_list_table')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
