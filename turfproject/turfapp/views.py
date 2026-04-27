from django.shortcuts import render, redirect
from .models import Slot, Booking

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
            slot=slot
        )

        slot.is_available = False
        slot.save()

        return redirect("index")

    return render(request, "index.html", {"slots": slots})

from django.shortcuts import render, redirect
from .models import Slot, Booking

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
            slot=slot
        )

        slot.is_available = False
        slot.save()

        return redirect("booking")

    return render(request, "book.html", {"slots": slots})