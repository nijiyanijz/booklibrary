from django.shortcuts import render,redirect
from customer.forms import UserRegistrationForm,LoginForm,OrderCreateForm,ReviewForm
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from owner.models import Books
from django.views.generic import View,ListView,CreateView
from django.contrib.auth import authenticate,login,logout
from customer.decorators import sign_in_required
from customer.models import Carts,Orders,Reviews
from django.db.models import Sum
from django.contrib import messages
from customer.filters import BookFilter

@method_decorator(sign_in_required,name='dispatch')
class ListAllView(View):

    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        f=BookFilter(request.GET,queryset=Books.objects.all())
        context={"books":qs,"filter":f}
        return render(request,"listallbooks.html",context)

class SingUpView(View):
    def get(self,request):
        form=UserRegistrationForm
        context={"form":form}
        return render(request,"signup.html",context)
    def post(self,request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'signup.html')

        else:
            context={'form':form}
            return render(request,'signup.html',context)

class SinginView(View):
    def get(self,request):
        form=LoginForm
        context={"form":form}
        return render(request,"signin.html",context)

    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.is_superuser:
                    return redirect("allbooks")
                else:
                    context={"form":form}
                    return render(request,'signin.html',context)

def sign_out(request):
    logout(request)
    return redirect('signin')

class AddToCartView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        book=Books.objects.get(id=id)
        user=request.user
        cart=Carts(user=user,item=book)
        cart.save()
        messages.success(request,"item as been added to cart")
        return redirect('cartitems')


class CartItem(ListView):
    model=Carts
    template_name = 'cartitem.html'
    context_object_name = 'items'
    def get(self,request,*args,**kwargs):
        qs= self.model.objects.filter(user=self.request.user,status="incart")
        total=qs.aggregate(Sum('item__price'))

        print(total)
        sum=total['item__price__sum']
        context = {'items': qs,'sum':sum}
        return render(request,self.template_name,context)

class RemoveCartitem(View):
    def get(self,request,*args,**kwargs):
        id=kwargs['id']
        cart=Carts.objects.get(id=id)
        cart.status='cancelled'
        cart.save()
        messages.success(request,"item as been removed")
        return redirect('allbooks')

class OrderView(CreateView):
    model = Orders
    form_class = OrderCreateForm
    template_name = "order_create.html"

    def post(self,request,*args,**kwargs):
        print(kwargs)
        form=self.form_class(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            book=Books.objects.get(id=kwargs["p_id"])
            order.item=book
            order.save()
            cid=kwargs.get("c_id")
            cart=Carts.objects.get(id=cid)
            cart.status="order_placed"
            cart.save()
            messages.success(request,"order as been placed")
            return redirect('allbooks')
        else:
            return render(request,self.template_name,{'form':form})

class MyOrders(ListView):
    model=Orders
    template_name = "myorders.html"
    context_object_name = "orders"
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).exclude(status='cancelled').order_by("-date")


class RemoveOrderitem(View):
    def get(self,request,*args,**kwargs):
        id=kwargs['id']
        order=Orders.objects.get(id=id)
        order.status='cancelled'
        order.save()
        messages.success(request,"your order as been cancelled")
        return redirect('allbooks')

class FilterView(View):

    def get(self,request,*args,**kwargs):
        qs = Books.objects.all()
        f=BookFilter(request.GET,queryset=Books.objects.all())
        context={"filter":f}
        return render(request,"filter.html",context)


class ReviewsView(CreateView):
    model=Reviews
    form_class =ReviewForm

    template_name = "review.html"
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            id=kwargs['r_id']
            reviews=form.save(commit=False)
            reviews.user=request.user
            order=Orders.objects.get(id=id)
            reviews.item=order.item
            reviews.save()
            messages.success(request,"your review has been posted")
            return redirect('allbooks')
        else:
            return render(request,self.template_name,{"form":form})

class ListReviewsView(ListView):
    model=Reviews
    template_name = "listreview.html"
    context_object_name = 'reviews'







