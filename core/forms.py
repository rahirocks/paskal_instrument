from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=120)
    email = forms.EmailField()
    phone = forms.CharField(max_length=30,required=False)
    company = forms.CharField(max_length=120,required=False)
    address_line_1 = forms.CharField(max_length=120,required=False)
    address_line_2 = forms.CharField(max_length=120,required=False)
    city = forms.CharField(max_length=120,required=False)
    state= forms.CharField(max_length=120,required=False)
    country = forms.CharField(max_length=120,required=False)
    zipcode = forms.CharField(max_length=120,required=False)
    notes = forms.CharField(widget=forms.Textarea(attrs={"rows":4}),required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": (
                    "w-full rounded-xl "
                    "border border-gray-300 "
                    "bg-white px-3 py-2 "
                    "text-black outline-none "
                    "focus:ring-2 focus:ring-indigo-400/40"
                )
            })