
from .models import Product

# from django import forms
# class ProductCreateForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['owner', 'name', 'slug', 'category', 'description', 'price', 'image', 'rent_duration']

#         owner = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "value":"{{request.user}}", "disabled":"", "readonly":""}), required=True)
#         name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Name', 'class':'form-control'}), required=True)
#         slug = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Slug', 'class':'form-control'}), required=True)
#         category = forms.MultipleChoiceField(widget=forms.TextInput(attrs={'placeholder':'Product Slug', 'class':'form-control'}), required=True)