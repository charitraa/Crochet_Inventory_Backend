# views.py

from django.core.mail import send_mail
from django.contrib.auth import  get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PasswordResetRequest
from django.utils import timezone
from django.conf import settings

User = get_user_model()
@api_view(['POST'])
def forgot_password(request):
    email = request.data.get("email")

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"detail": "Email does not exist"}, status=404)

    # Generate and save reset code
    reset_request = PasswordResetRequest.objects.create(email=email)

    # Send the reset code to the email
    send_mail(
        "Password Reset Code",
        f"Your password reset code is {reset_request.reset_code}",
        settings.DEFAULT_FROM_EMAIL,
        [email],
    )

    return Response({"detail": "Password reset code sent to email."}, status=200)

# Step 2: Verify Code and Update Password
@api_view(['POST'])
def reset_password(request):
    email = request.data.get("email")
    reset_code = request.data.get("reset_code")
    new_password = request.data.get("new_password")

    try:
        reset_request = PasswordResetRequest.objects.get(email=email, reset_code=reset_code)
    except PasswordResetRequest.DoesNotExist:
        return Response({"detail": "Invalid code or email"}, status=400)

    # Check if the code is expired
    if reset_request.expires_at < timezone.now():
        return Response({"detail": "Code has expired"}, status=400)

    # Update the user's password
    try:
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.save()
        reset_request.delete()  # Optional: Delete the reset code after use
    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=404)

    return Response({"detail": "Password updated successfully."}, status=200)
