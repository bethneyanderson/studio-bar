from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .forms import ArtistForm
from .models import Artist

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def artists_list_view(request):
    artists = Artist.objects.all().order_by('name')
    return render(request, 'artists/artists.html', {'artists': artists})

@user_passes_test(is_admin)
def create_artist_view(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artist created successfully!')
            return redirect('artists_list')
    else:
        form = ArtistForm()
    return render(request, 'artists/create_artist.html', {'form': form})

@user_passes_test(is_admin)
def update_artist_view(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artist updated successfully!')
            return redirect('artists_list')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'artists/update_artist.html', {'form': form, 'artist': artist})

@user_passes_test(is_admin)
def delete_artist_view(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == 'POST':
        artist.delete()
        messages.success(request, 'Artist deleted successfully!')
        return redirect('artists_list')
    return render(request, 'artists/delete_artist.html', {'artist': artist})
