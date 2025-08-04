from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .models import About
from .forms import AboutForm


def about_page_view(request):
    # Get the About content (create default if none exists)
    about_content, created = About.objects.get_or_create(
        id=1,
        defaults={
            'story_lead': 'Studio Bar is Penzance\'s premier live music venue, bringing together the best local and touring artists in an intimate setting that celebrates the power of live performance.',
            'story_content': 'Located in the heart of Penzance at 71 Bread St, our venue has been a cornerstone of the local music scene, providing a platform for emerging artists and established acts alike. From indie rock to jazz, electronic to folk, we showcase diverse musical genres that reflect the vibrant cultural landscape of Cornwall.',
            'mission_content': 'We believe in the transformative power of live music. Our mission is to create unforgettable experiences that connect artists with audiences in meaningful ways. Studio Bar is more than just a venue – it\'s a community space where music lovers gather to discover new sounds and celebrate established favorites.',
            'space_content': 'Our intimate venue features state-of-the-art sound equipment and lighting, ensuring every performance sounds and looks incredible. With a capacity that allows for up-close and personal shows, every seat in the house offers an exceptional view of the stage.',
            'programming_content': 'Studio Bar is programmed and produced by LNZRT, ensuring a carefully curated selection of artists and events that maintain the highest standards of quality and artistic integrity.',
            'community_content': 'We\'re proud to support local initiatives and festivals, including our partnership with the Golowan Festival. We also participate in community programs and support emerging artists through our platform.'
        }
    )
    
    return render(request, 'about/about.html', {'about': about_content})


@staff_member_required
def edit_about_view(request):
    about_content, created = About.objects.get_or_create(id=1)
    
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about_content)
        if form.is_valid():
            about_obj = form.save(commit=False)
            about_obj.updated_by = request.user
            about_obj.save()
            messages.success(request, 'About page content updated successfully!')
            return redirect('about')
    else:
        form = AboutForm(instance=about_content)
    
    return render(request, 'about/edit_about.html', {'form': form, 'about': about_content})
