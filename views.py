def check_change_password(request):

    if request.user.is_authenticated:
        if customer.objects.filter(email=request.user.email):



            return render(request, 'change_password.html')

        else:
            po = pharmacyowner.objects.get(email=request.user.email)


            return render(request, 'change_password.html')





def change_password(request):
    if request.method=="POST":
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            u=User.objects.get(email=request.user.email)
            u.set_password(password2)
            u.save()
            return render(request,'commonloginpage.html')

        else:

            messages.info(request,"Passwords didnot match")

    else:
        return render(request,'changepassword.html')
		


def logout(request):
    auth.logout(request)
    return redirect('homepage.html')
