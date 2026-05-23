from django import forms

from .models import TOPPING_CHOICES, Pizza


"""
class OrderForm(forms.Form): 
    name = forms.CharField(label='Your Name', max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})) 
    address = forms.CharField(label='Your Address', widget=forms.Textarea) 
    pizza_size = forms.ChoiceField(label='Pizza Size', choices=size.choices) 
    toppings = forms.MultipleChoiceField(label='Toppings', choices=[('pepperoni', 'Pepperoni'), ('mushrooms', 'Mushrooms'), ('onions', 'Onions')], widget=forms.CheckboxSelectMultiple) 
    """
class OrderForm(forms.ModelForm):
    toppings = forms.MultipleChoiceField(
        choices=TOPPING_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Pizza
        fields = ['name', 'description', 'size', 'price', 'toppings','image']
        #Customize form field labels and widgets if needed
        labels = {
            'name': 'Pizza Name',
            'description': 'Description',
            'size': 'Size',
            'price': 'Price',
            'toppings': 'Toppings',
            'image': 'Pizza Image',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter pizza name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter pizza description'}),
            'size': forms.Select(),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
            'toppings': forms.CheckboxSelectMultiple(),
            'image': forms.FileInput(),
        }