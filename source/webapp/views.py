from django.shortcuts import render

# Create your views here.


def home_view(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        first_number = int(request.POST.get('first_number'))
        second_number = int(request.POST.get('second_number'))
        if request.POST.get('action') == '+':
            message = f"{first_number}+{second_number}={first_number+second_number}"

        elif request.POST.get('action') == '-':
            message = f"{first_number}-{second_number}={first_number-second_number}"

        elif request.POST.get('action') == '*':
            message = f"{first_number}*{second_number}={first_number*second_number}"

        elif request.POST.get('action') == '/':
            if second_number == 0:
                message = 'You can`t divide by 0'
            else:
                message = f"{first_number}/{second_number}={first_number/second_number}"


        context = {"result":message}
        return render(request,'home.html',context)