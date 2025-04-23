from django import forms
from .models import Doctor, Department
from django.core.validators import RegexValidator

class DoctorForm(forms.ModelForm):
    # Additional fields or overrides
    mobile = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. +1234567890',
            'pattern': '^\+?1?\d{9,15}$'
        }),
        validators=[RegexValidator(
            regex='^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )
    
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    consultation_fee = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.01',
            'min': '0'
        })
    )
    
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['user', 'created_at', 'updated_at']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dr. Firstname Lastname',
                'required': True
            }),
            'gender': forms.Select(attrs={
                'class': 'form-select'
            }),
            'alternate_mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional alternate number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'doctor@example.com'
            }),
            'department': forms.Select(attrs={
                'class': 'form-select'
            }),
            'speciality': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Cardiology, Neurology',
                'required': True
            }),
            'qualification': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. MD, PhD, MBBS'
            }),
            'experience': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Years of experience'
            }),
            'available_days': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Monday-Friday'
            }),
            'available_time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 9:00 AM - 5:00 PM'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Clinic/Hospital address'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'pincode': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief professional bio'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize department queryset if needed
        self.fields['department'].queryset = Department.objects.all()
        
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                if isinstance(field.widget, forms.CheckboxInput):
                    field.widget.attrs['class'] = 'form-check-input'
                elif isinstance(field.widget, forms.Select):
                    field.widget.attrs['class'] = 'form-select'
                else:
                    field.widget.attrs['class'] = 'form-control'
            
            # Add placeholder if it doesn't exist
            if 'placeholder' not in field.widget.attrs and field_name != 'is_active':
                field.widget.attrs['placeholder'] = field.label

    def clean(self):
        cleaned_data = super().clean()
        # Add any custom validation here
        return cleaned_data