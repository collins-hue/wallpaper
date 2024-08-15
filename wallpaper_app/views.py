from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from wallpaper_app.models import About, TermsConditions, WallpaperInfo
import stripe

# Stripe API key
stripe.api_key = 'your-stripe-secret-key'
# Create your views here.
def home(request):
    all_wallpapers = WallpaperInfo.objects.all()
    return render(request, 'index.html', {"all_wallpapers": all_wallpapers})

def wallpaper_info(request, id):
    wallpaper = get_object_or_404(WallpaperInfo, id=id)
    
    if request.GET.get('download'):
        file_path = wallpaper.image.path
        try:
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/force-download')
                response['Content-Disposition'] = f'attachment; filename="{wallpaper.image.name}"'
                return response
        except FileNotFoundError:
            raise Http404("File not found")
    return render(request, 'wallpaper.html', {'wallpaper': wallpaper})


def about_us(request):
    about = About.objects.all()
    return render (request, 'about.html', {"about": about})

def terms_condition(request):
    our_terms = TermsConditions.objects.all()
    return render(request, 'terms.html', {"our_terms":our_terms})

def contact_us(request):
    return render(request, 'contact.html')


def buy_us_coffee(request):
    if request.method == 'POST':
        amount = int(request.POST['amount']) * 100  # Stripe uses cents
        try:
            # Create a charge: this will charge the user's card
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                description="Donation",
                source=request.POST['stripeToken']
            )
            return render(request, 'donate_success.html')
        except stripe.error.StripeError:
            return render(request, 'donate_failed.html')

    return render(request, 'donate.html')