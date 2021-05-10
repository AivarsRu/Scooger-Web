from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class scgUserCountry(models.Model):
    country_ID = models.AutoField(primary_key=True)
    country_Name = models.CharField(max_length=50)
    countrycode = models.CharField(max_length=3, verbose_name=('ISO alpha-3'),
                                   help_text=("Enter Country Code. e.g. USA - ISO alpha-3"))
    country_Code = models.IntegerField()

    class Meta:
        ordering = ["country_Name"]
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.country_Name}"


class scgUserProfile (models.Model):
    uProfile_ID = models.AutoField(primary_key=True)
    uProfile_userID = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name="Profile")
    uProfile_Image = models.ImageField(
        default="defaultUserPic.jpg", upload_to="UserImages")
    uProfile_Address = models.CharField(blank=True, max_length=400)
    uProfile_Country = models.ForeignKey(
        scgUserCountry, blank=True, on_delete=models.PROTECT, related_name="FromCountry")
    uProfile_Phone = models.IntegerField(blank=True)
    uProfile_PhoneVerified = models.BooleanField(default=False)
    uProfile_Notes = models.CharField(blank=True, max_length=400)

    class Meta:
        indexes = [
            models.Index(fields=['uProfile_Phone'], name='user_phone_idx'),
        ]

    def __str__(self):
        return f"{self.uProfile_ID}"
