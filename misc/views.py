from django.shortcuts import render

from auth.helpers import auth_required
from landing.models import GodSettings
from users.models.achievements import Achievement


@auth_required
def achievements(request):
    achievements = Achievement.objects.filter(is_visible=True)
    return render(request, "pages/achievements.html", {
        "achievements": achievements
    })


@auth_required
def network(request):
    secret_page_html = GodSettings.objects.first().network_page
    return render(request, "pages/network.html", {
        "page_html": secret_page_html,
    })
