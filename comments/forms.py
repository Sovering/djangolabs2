class ReviewForm(forms.ModelForm):
    """Форма отзыва"""

    captcha = ReCaptchaField()


    class Meta:
        model = Reviews
        fields = ("name", "email", "text", "captcha")
        widget ={
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.Textarea(attrs={"class": "form-control border"}),
        }
