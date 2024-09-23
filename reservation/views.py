from django.shortcuts import render , redirect
from .models import Reservation
from django.contrib import messages

def reservation_success(request):

    return render(request , 'success.html')


def reserve_table(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')


        if not fullname or not phone or not email or not date or not time or not guests:
            messages.error(request, "لطفاً تمام فیلدها را پر کنید")

            return render(request, 'reservation.html')

        try:
            guests = int(guests)

        except ValueError:
            messages.error(request , "تعداد مهمان‌ها باید یک عدد باشد")

            return render(request , 'reservation.html')


        reservation = Reservation(
            name = fullname,
            phone = phone,
            email = email,
            date = date,
            time = time,
            number_of_persons = guests,
        )
        reservation.save()

        return redirect('reservation:reservation_success')

    else:

        return render(request , 'reservation.html')
