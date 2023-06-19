from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password", "email"]


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    print(instance)
    email_plaintext_message = "{}?token={}".format(
        reverse("password_reset:reset-password-request"), reset_password_token.key
    )
    print(reset_password_token.user.email)

    res = send_mail(
        "Password Reset for {title}".format(title="Some website title"),
        email_plaintext_message,
        settings.EMAIL_HOST_USER,
        [reset_password_token.user.email],
        fail_silently=False,
    )
