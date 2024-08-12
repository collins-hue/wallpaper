from django.db import models

class WallpaperInfo(models.Model):
    image = models.ImageField(upload_to='media/')
    owner = models.TextField(max_length=200)
    contact = models.URLField(blank=False)
    description = models.TextField(max_length=500)
    upload_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.owner
    
    class Meta:
        ordering = ["-upload_date"]
        verbose_name_plural = "1 Wallpaper_Info"
        
class TermsConditions(models.Model):
    article = models.TextField(max_length=2000)
    
    class Meta:
        verbose_name_plural = "2 Terms & Condition"
        
class About(models.Model):
    about_us = models.TextField(max_length=5000)
    
    class Meta:
        verbose_name_plural = "3 About Us"
        