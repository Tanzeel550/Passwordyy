from django.shortcuts import render
import string
import random

def home(request):
    return render(request, 'gen_pass/home.html')

def password(request):
    arr = ''

    length = request.GET.get('length', '16')
    if request.GET.get('uppercase', 'on') == 'on':
        arr += string.ascii_uppercase
    if request.GET.get('lowercase', 'on') == 'on':
        arr += string.ascii_lowercase
    if request.GET.get('numbers', 'on') == 'on':
        arr += string.digits
    if request.GET.get('characters', 'on') == 'on':
        arr += string.punctuation
    
    # generating the password
    gen_password = ''
    for i in range(int(length)):
        gen_password += random.choice(arr)
    print(gen_password)

    return render(request, 'gen_pass/show_password.html', context={'password':gen_password})

def about(request):
    return render(request, 'gen_pass/about.html')