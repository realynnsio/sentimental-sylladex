from django.test import TestCase, Client

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')

    def test_create_item_using_create_item(self):
        response = Client().get('/create-item/')
        self.assertTemplateUsed(response, 'create_item.html')