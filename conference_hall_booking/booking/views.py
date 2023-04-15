from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(status='Approved')
    return render(request, 'booking/home.html', {'bookings': bookings})


def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if Booking.objects.filter(start_date__lte=booking.start_date, end_date__gte=booking.start_date).exists() or Booking.objects.filter(start_date__lte=booking.end_date, end_date__gte=booking.end_date).exists():
                messages.error(
                    request, 'The selected dates are not available.')
                return redirect('book')
            booking.save()
            send_mail(
                'Conference Hall Booking',
                f'Thank you for booking the conference hall for {booking.programme_title} from {booking.start_date} to {booking.end_date}.',
                settings.EMAIL_HOST_USER,
                [booking.contact_email],
                fail_silently=False,
            )
            messages.success(request, 'Your booking has been submitted.')
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'booking/book.html', {'form': form})


def approve(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.status = 'Approved'
    booking.save()
    send_mail(
        'Conference Hall Booking',
        f'Your booking for {booking.programme_title} from {booking.start_date} to {booking.end_date} has been approved.',
        settings.EMAIL_HOST_USER,
        [booking.contact_email],
        fail_silently=False,
    )
    messages.success(request, 'The booking has been approved.')
    return redirect('home')


def reject(request, booking_id):
    if request.method == 'POST':
        booking = Booking.objects.get(id=booking_id)
        booking.status = 'Rejected'
        booking.reason = request.POST['reason']
        booking.save()
        send_mail('Conference Hall Booking',
                  f'Your booking for {booking.programme_title} from {booking.start_date} to {booking.end_date} has been rejected. Reason: {booking.reason}',
                  settings.EMAIL_HOST_USER,
                  [booking.contact_email],
                  fail_silently=False,
                  )
        messages.success(request, 'The booking has been rejected.')
        return redirect('home')
    return render(request, 'booking/reject.html', {'booking_id': booking_id})


def login(request):
    return render(request, 'booking/login.html')


def logout(request):
    return render(request, 'booking/logout.html')
