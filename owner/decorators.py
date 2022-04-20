from django.shortcuts import redirect
def book_user(fun):
    def wrapper(request,*args,**kwars):
        if request.user.is_superuser:
            return fun(request,*args,**kwars)
        else:
            return redirect('signin')
    return wrapper
