from django.contrib import messages
from django.shortcuts import render, redirect
from .froms import UserForm


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        username = request.POST.get('username')
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, f"{user.username} User yaratildi.")
            except Exception as e:
                messages.success(request, f"{username} oldin yaratilgan.")
                return redirect('home')
            return redirect('home')  # Agar muvaffaqiyatli bo'lsa, bosh sahifaga o'tkazamiz
    else:
        form = UserForm()
    return render(request, 'regist/register.html', {'form': form})

# Create your views here.
