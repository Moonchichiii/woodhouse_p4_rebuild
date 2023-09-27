class BookingsForm(forms.ModelForm):
   date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))    
   class Meta:
        model = Bookings
        fields = [
            'number_of_guests',
            'date',
            'time',
            'first_name',
            'last_name',
            'address',
            'email',
            'phone_number',
            'comment']


def clean(self):
    cleaned_data = super().clean()
    date = cleaned_data.get("date")
    time = cleaned_data.get("time")
    
    existing = Bookings.objects.filter(date=date, time=time).exists()
    
    if existing:
        raise forms.ValidationError("Sorry, choose another date or time!")
            