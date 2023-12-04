from django import forms
from . import models
<<<<<<< HEAD
dj
class OrderForm(forms.ModelForm):
    email=forms.EmailField()
    date_of_birth = models.DateField()

    first_name = models.CharField(
         validators=[
            MaxLengthValidators(limit_value=30),
            RegexValidator(
                regex=r'^[a-zA-Z][a-zA-Z0-9_]{4-31}$'
                message="Введите правильно"
                code="invalid_first_number"
            )
            ]
    )

    last_name = models.CharField(
         validators=[
            MaxLengthValidators(limit_value=30),
            RegexValidator(
                regex=r'^[a-zA-Z][a-zA-Z0-9_]{4-31}$'
                message="Введите правильную фамлию"
                code="invalid_last_name"
            )]
    )

    phone_number = models.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+77\d{9}$'
                message="Введите номер телефона в формате +7хххххххххх"
                code="invalid_phone_number"
            )
        ]
    )
    housenumber = models.CharField(
        validators=[
            RegexValidator(
                message="Неправильно указанный номер дома"
                code="invalid_home_number"
            )
        ]
    )
    flatnumber = models.CharField(
        validators=[
            RegexValidator(
                message="Неправильно указанный номер дома"
                code="invalid_flat_number"
            )
        ]
    )
    class Meta:
        model = models.Order
        fields =['last_name','first_name' ,'phone_number','email' ,'housenumber' ,'flatnumber' ,'streetname']

=======

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields ='__all__'



        
>>>>>>> 049dd5a9771965afa8e66fc8d103aee34b35e5be
