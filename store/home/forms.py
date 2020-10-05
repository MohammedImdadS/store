from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
	
	Full_Name = forms.CharField(
		required=True,
	    max_length=30,
	    widget=forms.TextInput(
	        attrs={
	            'class': 'form-control',
	            'class': 'col-lg-12 form-group',
	            'placeholder': 'Your Full Name',
	            'name':'name',
	        }
	    )
	)
	Phone_Number = forms.IntegerField(
		 required=True,
		 widget=forms.TextInput(
	        attrs={
	            'class': 'form-control',
	            'class': 'col-lg-12 form-group',
	            'placeholder': 'Your Phone Number',
	            'type':'tel',
	            'pattern':'[0-9]{10}',
	            'name':'phone',
	        }
	    )
	)
	Email_Address = forms.EmailField(
	    max_length=254,
	    required=True,
	    widget=forms.TextInput(
	    	attrs={'class': 'form-control',
	    		   'class': 'col-lg-12 form-group',
	    		   'placeholder': 'Your Email Address',
	    		   'type': 'email',
	    		   'name':'email',
	    	})
	)
	Subject = forms.CharField(
	    max_length=64,
	    widget=forms.TextInput(
	    	attrs={'class': 'form-control',
	    		   'class': 'col-lg-12 form-group',
	    		   'placeholder': 'Subject',
	    		   'name':'submatter',
	    	})
	)
	Message = forms.CharField(
		required=True,
		max_length=1000,
		widget=forms.Textarea(
			attrs={
			'class': 'form-control',
			'class': 'col-lg-12 form-group',
			'rows':'3',
			'placeholder':'Type Your Message',
			'name':'msg'}),
		
		)
	class Meta():
		model = Contact
		fields = '__all__'
