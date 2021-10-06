from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'booking/index.html')


def login(request):
    return render(request, 'booking/login.html', {'form': LoginForm})


def register(request):
    return render(request, 'booking/registration.html', {
        'form': RegistrationForm
    })


def registration(request):
    if request.method == 'POST':
        customerObj = Customer(name=request.POST['name'], contact=request.POST['contact'],
                               password=request.POST['password'], email=request.POST['email'],
                               address=request.POST['address'])

        customerObj.save()

    return render(request, 'booking/dashboard.html')

def dashboard(request):
    if
