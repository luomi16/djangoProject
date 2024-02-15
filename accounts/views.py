from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from utils.exceptions.logger import get_logger
# from pswValidator import CustomPasswordValidator

logger = get_logger(__name__)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials, Please try again')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password is matched
        if password == password2:
            # Check if username is duplicate
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            # Check if username is duplicate
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Create a new user
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('index')
                    # user.save()
                    # messages.success(request, 'You are now register')
                    # return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def updatepsw(request):
    logger.error(
        "This is a error level log information. User try to update password.")
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(
                request, 'That username do not exist, please try again')
            return redirect('updatepsw')
        else:
            # todo: update user password
            user = User.objects.get(username=username)
            user.set_password(new_password)  # 更新密码
            user.save()
            # update_session_auth_hash(request, user)  # 重要：更新session以防止用户登出
            messages.success(
                request, 'Your password has been updated successfully!')
            return redirect('login')
    else:
        return render(request, 'accounts/updatepsw.html')
