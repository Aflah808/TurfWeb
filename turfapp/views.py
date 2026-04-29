from django.shortcuts import render, redirect
from .models import Slot, Booking
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    slots = Slot.objects.filter(is_available=True)

    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        slot_id = request.POST.get("slot")

        if not slot_id:
            return render(request, "index.html", {
                "slots": slots,
                "error": "Select a slot"
            })

        slot = Slot.objects.get(id=slot_id)

        if not slot.is_available:
            return render(request, "index.html", {
                "slots": slots,
                "error": "Already booked"
            })

        Booking.objects.create(
            name=name,
            contact=contact,
            slot=slot,
            user=request.user   # ✅ THIS LINE
        )

        slot.is_available = False
        slot.save()

        return redirect("index")

    return render(request, "index.html", {"slots": slots})

from django.shortcuts import render, redirect
from .models import Slot, Booking

@login_required
def book(request):
    slots = Slot.objects.filter(is_available=True)

    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        slot_id = request.POST.get("slot")

        if not slot_id:
            return render(request, "book.html", {
                "slots": slots,
                "error": "Select a slot"
            })

        slot = Slot.objects.get(id=slot_id)

        if not slot.is_available:
            return render(request, "book.html", {
                "slots": slots,
                "error": "Already booked"
            })

        Booking.objects.create(
            name=name,
            contact=contact,
            slot=slot,
            user=request.user   # ✅ ADD THIS
        )

        slot.is_available = False
        slot.save()

        return redirect("booking")

    return render(request, "book.html", {"slots": slots})

@login_required
def book_slot(request):
    slots = Slot.objects.filter(is_available=True)

    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        slot_id = request.POST.get("slot")

        if not slot_id:
            return render(request, "book_slot.html", {
                "slots": slots,
                "error": "Please select a slot"
            })

        slot = Slot.objects.get(id=slot_id)

        if not slot.is_available:
            return render(request, "book_slot.html", {
                "slots": slots,
                "error": "Slot already booked"
            })

        Booking.objects.create(
            name=name,
            contact=contact,
            slot=slot,
            user=request.user   # ✅ ADD THIS
        )

        slot.is_available = False
        slot.save()

        messages.success(request, "Booking successful!")

        return redirect("history")

    return render(request, "book_slot.html", {"slots": slots})
@login_required
def history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "history.html", {"bookings": bookings})

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return render(request, "signup.html", {
                "error": "All fields are required"
            })

        if len(password) < 6:
            return render(request, "signup.html", {
                "error": "Password must be at least 6 characters"
            })

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {
                "error": "Username already exists"
            })

        user = User.objects.create_user(username=username, password=password)

        # ✅ AUTO LOGIN
        login(request, user)

        return redirect("index")

    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')   # ✅ THIS is what you want
        else:
            return render(request, "login.html", {
                "error": "Invalid credentials"
            })
        

    return render(request, "login.html")