from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('', index),
    path('signup_page/', signup_page,  name='signup_page'),
    path('otp_page/', otp_page,  name='otp_page'),
    path('profile_page/', profile_page,  name='profile_page'),
    path('my_collections/', my_collections,  name='my_collections'),
    path('payment/', payment,  name='payment'),
    path('security/', security,  name='security'),
    path('favourite/', favourite,  name='favourite'),

    path('signup/', signup,  name='signup'),
    path('verify_otp/', verify_otp, name="verify_otp"),
    path('signin/', signin,  name='signin'),
    path('signout/', signout, name='signout'),
    path('update_profile/', update_profile, name='update_profile'),
    path('change_password/', change_password, name='change_password'),

]
