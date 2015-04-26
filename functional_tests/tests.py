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

    def check_for_row(self, row_text, idT, tag):
        table = self.browser.find_element_by_id(idT)
        rows = table.find_elements_by_tag_name(tag)
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
        inputURL.send_keys(
         'http://www.majorcineplex.com/uploads/movie/868/thumb_868.jpg')
        self.browser.find_element_by_id('submit_data').click()

        # back to homepage can see Fast And Furious 7
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Movie Rate', header_text)
        self.check_for_row('Fast And Furious 7\n0.0', 'id_list_table', 'td')

        # click at Fast And Furious 7 go to the movie's detail
        self.browser.find_element_by_id('view_detail_1').click()
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Detail of Fast And Furious 7', header_text)
        self.check_for_row('Name: Fast And Furious 7', 'id_list_table', 'tr')
        self.check_for_row('Release Date: 04/01/2015', 'id_list_table', 'tr')
        self.check_for_row('Detail: action', 'id_list_table', 'tr')

        # test edit detail of Fast 7 (action change to action and racing)
        self.browser.find_element_by_id('Edit').click()
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Edit Fast And Furious 7', header_text)
        inputdetail = self.browser.find_element_by_id('id_new_detail')
        self.assertEqual(
                inputdetail.get_attribute('placeholder'),
                'action'
        )
        inputdetail.send_keys('action and racing')
        self.browser.find_element_by_id('submit_update_data').click()

        # redirect to Fast And Furious 7's detail page after edit
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Detail of Fast And Furious 7', header_text)
        self.check_for_row('Detail: action and racing', 'id_list_table', 'tr')

        # test comment
        inputcomment_user = self.browser.find_element_by_id('id_user_name')
        inputcomment_text = self.browser.find_element_by_id('id_comment_text')
        self.assertEqual(
                inputcomment_user.get_attribute('placeholder'),
                'Your Name'
        )
        self.assertEqual(
                inputcomment_text.get_attribute('placeholder'),
                'Comment this movie'
        )
        inputcomment_user.send_keys('Alice')
        inputcomment_text.send_keys('this is the greatest movie forever.')
        self.browser.find_element_by_id('id_comment').click()

        comment = self.browser.find_element_by_id('comment_1').text
        self.assertIn('Name: Alice', comment)
        self.assertIn('comment: this is the greatest movie forever.', comment)
        self.assertIn('Like: 0', comment)

        # test click LIKE
        self.browser.find_element_by_id('submit_like_1').click()
        comment = self.browser.find_element_by_id('comment_1').text
        self.assertIn('Like: 1', comment)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
