from django.test import TestCase
from .forms import ItemForm

class TestItemForm(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
	    form = ItemForm()
	    self.assertEqual(form.Meta.fields, ['name','done'])