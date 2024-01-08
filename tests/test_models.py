from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_menu(self):
        item = Menu.objects.create(title="IceCream",price=80,inventory=100)
        self.assertEqual(str(item),"IceCream : 80")
        # Note that I can use str to get item in the right format from the Menu model
        # becuse we defined the method in the model:
        #     def __str__(self):
        # return f'{self.title} : {str(self.price)}'