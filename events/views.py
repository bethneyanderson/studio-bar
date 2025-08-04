from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from index.models import Event
from .forms import EventForm

def is_admin(user):
    return user.is_authenticated and user.is_staff

# Test view to debug template rendering
def test_template_view(request):
    return render(request, 'events/simple_test.html')

# Create your views here.
def events_page_view(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/events.html', {'events': events})

def event_detail_view(request, event_id):
    event = get_object_or_404(Event.objects.select_related('artist'), id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@user_passes_test(is_admin)
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('events')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@user_passes_test(is_admin)
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('events')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/update_event.html', {'form': form, 'event': event})

@user_passes_test(is_admin)
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('events')
    return render(request, 'events/delete_event.html', {'event': event})
