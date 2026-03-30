from django.shortcuts import render
from .forms import Registartion, Login

# Create your views here.

def registration(req):
    form = Registartion(field_order=['email','city'])
    return render(req, 'registration.html', {'form':form})

 
def login(req):
    # fm = Login(auto_id='sonam_%s') # FOR ID LOOK IN INSPECT
    # fm = Login(auto_id=True)
    # fm = Login(auto_id='sonam')
    # fm = Login(auto_id=False)

    # fm = Login(label_suffix='')
    # fm = Login(label_suffix='A')

    # fm = Login(initial={'email': 'johndoe@example.com', 'password': '********'})
    fm = Login()
    return render(req, 'login.html', {'form':fm})


