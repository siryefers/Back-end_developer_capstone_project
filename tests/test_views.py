from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def test_get_menu(self):
        item = Menu.objects.create(title="IceCream",price=80,inventory=100)
        self.assertEqual(str(item),"IceCream : 80")
        # Note that I can use str to get item in the right format from the Menu model
        # becuse we defined the method in the model:
        #     def __str__(self):
        # return f'{self.title} : {str(self.price)}'

    def setUp(self):
        Menu.objects.create(title="Apple",price=50,inventory=500)
        Menu.objects.create(title="Banana",price=60,inventory=600)
        Menu.objects.create(title="Cherry",price=70,inventory=700)

    def test_getall(self):
        data = Menu.objects.all()
        serializer= MenuSerializer(data,many=True)
        # Create a list of strings from the serialized data for comparison
        serialized_data = [f"{item['title']} : {round(float(item['price']))}" for item in serializer.data]
        expected_data = ["Apple : 50", "Banana : 60", "Cherry : 70"]
        self.assertEqual(serialized_data,expected_data)
