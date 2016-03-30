
		
from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page #use view function to display
from django.http import HttpRequest
from django.template.loader import render_to_string




class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # looking for "/" on the root site
        self.assertEqual(found.func, home_page)
		
		
    def test_home_page_returns_correct_html(self):
	
        request = HttpRequest()  # Creating a HttpRequest object

        response = home_page(request)  # Pass the request to home_page view and get a response
		
		self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string('home.html',{'new_item_text':  'A new list item'})

        self.assertEqual(response.content.decode(), expected_html)
		
	
	
	
	def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertIn('A new list item', response.content.decode())
		
		
        #self.assertTrue(response.content.startswith(b'<html>'))  # looking for HTML tag
        #self.assertIn(b'<title>To-Do lists</title>', response.content)  # Looking for a title tag with word "To-Do List"
        #self.assertTrue(response.content.strip().endswith(b'</html>'))  