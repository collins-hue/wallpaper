from django.contrib import admin

from wallpaper_app.models import About, TermsConditions, WallpaperInfo

# Register your models here.

admin.site.register(WallpaperInfo)
admin.site.register(TermsConditions)
admin.site.register(About)