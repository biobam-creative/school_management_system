from django.shortcuts import render

from .forms import StudentPaymentInfoForm


def student_payment_info(request):
    if request.method == "POST":
        customer_form = StudentPaymentInfoForm(request.POST)
        if customer_form.is_valid()and customer_form.cleaned_data:
            email = customer_form.cleaned_data['email']
            customer_form.save()
            print(email)
            return render(request, "finance/payment.html", {'email': email})
        else:
            message = 'Invalid input try again!!!'
            return render(request, "finance/payment.html", {'message': message})
    else:
        customer_form = StudentPaymentInfoForm()
    return render(request, "finance/customer_info.html", {'customer_form': customer_form})
