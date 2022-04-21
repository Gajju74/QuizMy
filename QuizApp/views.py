from doctest import master
from django.shortcuts import redirect, render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from random import randint

# Create your views here.


defulat_data ={
    'app_name': 'Quiz'
}

def index(request):
    return render(request, "signin_page.html")
    
def signup_page(request):
    return render(request, "signup_page.html")

def my_collections(request):
    load_quizes(request)
    return render(request, "my_collections.html", defulat_data)

def payment(request):
    return render(request, "payment.html", defulat_data)

def security(request):
    return render(request, "security.html", defulat_data)

def otp_page(request):
    return render(request, "otp_page.html", defulat_data)

def favourite(request):
    return render(request, "favourite.html", defulat_data)

def profile_page(request):
    profile_data(request)
    return render(request, "profile_page.html", defulat_data)

def load_quizes(request):
    # master = Master.objects.get(Email = request.session['email'])
    quesets = QuesSet.objects.all()
    # option = OptionSet.objects.all()
    q_sets = []
    for ques in quesets:
        op_set = OptionSet.objects.filter(QuesSet=ques)
        point = 0
        for op in op_set:
            point += op.Point

        q_sets.append(
            {'quesset': ques, 'questions': op_set, 'total': len(op_set), 'points': point}
        )

    print('question sets', q_sets)
    defulat_data['all_quizes'] = q_sets
    #defulat_data['all_quizes'] = quesets

def profile_data(request):
    master = Master.objects.get(Email = request.session['email'])

    profile = Profile.objects.get(Master = master)

    defulat_data['profile_data'] = profile

def update_profile(request):
    master = Master.objects.get(Email = request.session['email'])

    profile = Profile.objects.get(Master = master)

    print('update data:', request.POST['address'])

    profile.FullName = request.POST['full_name']
    profile.Mobile = request.POST['mobile']
    profile.City = request.POST['city']
    profile.State = request.POST['state']
    profile.AdderssLine = request.POST['address']

    profile.save() 

    return redirect(profile_page)

def change_password(request):
    master = Master.objects.get(Email = request.session['email'])
    if master.Password == request.POST['old_password']:
        if request.POST['new_password'] == request.POST['confirm_password']:
            master.Password = request.POST['new_password']
            master.save()
            print('password change sucessfully.')
        else:
            print('password are deffrent')
    else:
        print('invalid current password')

    return redirect(security)


# generate otp
# otp
def create_otp(request):
    email_to_list = [request.session['reg_data']['email'],]
    
    subject = 'OTP for NMS Registration'

    otp = randint(1000,9999)

    print('OTP is: ', otp)

    request.session['otp'] = otp

    message = f"Your One Time Password for verification is: {otp}"
    
    email_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, email_from, email_to_list)

# verify otp
def verify_otp(request):
    if request.method == 'POST':
        otp = int(request.POST['otp'])

        if otp == request.session['otp']:
            master = Master.objects.create(
                Email = request.session['reg_data']['email'],
                Password = request.session['reg_data']['password'],
                IsActive = True,
            )
            Profile.objects.create(
                Master = master,
            )

            del request.session['otp']
            del request.session['reg_data']

            print('otp verify success!')

        else:
            print('invalid otp')
            return redirect(otp_page)

        return redirect(signup_page)
    else:
        pass

def signup(request):
    print(request.POST)
    request.session['reg_data'] = {
        'email': request.POST['email'],
        'password': request.POST['password'],

    }
    
    create_otp(request)

    

    return redirect(otp_page)

def signin(request):
    try:
        master = Master.objects.get(Email = request.POST['email'])

        if master.Password == request.POST['password']:
            #create a session for current login
            request.session['email'] = master.Email

            return redirect(profile_page)
        else:
            print('incurrect password')

    except Master.DoesNotExist as err:
        print('record not found.', err)

    return redirect(index)

def signout(request):
    if 'email' in request.session:
        del request.session['email']

    return redirect(index)
