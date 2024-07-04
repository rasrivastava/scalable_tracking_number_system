from django.shortcuts import render, get_object_or_404, redirect
from .models import TrackedOrder
from .forms import TrackedOrderForm


def create_tracked_order(request):
    """
    Handle creation or update of a TrackedOrder based on form input.
    """
    if request.method == "POST":
        form = TrackedOrderForm(request.POST)
        if form.is_valid():
            order = form.cleaned_data['order']
            status = form.cleaned_data['status']
            
            # Check if an order with the same 'order' value exists
            existing_orders = TrackedOrder.objects.filter(order=order)
            
            if existing_orders.exists():
                # Update the status of the first found order
                tracked_order = existing_orders.first()
                tracked_order.status = status
                tracked_order.save()
            else:
                # Create a new TrackedOrder instance
                tracked_order = form.save()

            tracking_number = tracked_order.tracking_number
            return render(request, 'tracking/create_tracked_order.html', {'form': form, 'tracking_number': tracking_number})
    else:
        form = TrackedOrderForm()

    # Return an HttpResponse object for the GET request
    return render(request, 'tracking/create_tracked_order.html', {'form': form})


def track_order(request, tracking_number):
    """
    Render the 'tracking/track_order.html' template with the TrackedOrder instance identified by tracking_number.
    """
    order = get_object_or_404(TrackedOrder, tracking_number=tracking_number)
    return render(request, 'tracking/track_order.html', {'order': order})
