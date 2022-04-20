from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from owner.forms import BookForm,OrderProcessForm
from django.views.generic import View,ListView,DetailView,DeleteView,CreateView,UpdateView
from owner.models import Books
from owner.decorators import book_user
from django.utils.decorators import method_decorator
from customer.models import Orders
from django.core.mail import send_mail

class AddBookView(CreateView):
    model=Books
    form_class = BookForm
    template_name = 'addbook.html'
    success_url = reverse_lazy('booklist')

class BookListView(ListView):
    model=Books
    context_object_name = 'books'
    template_name = 'viewbook.html'


class BookDetailView(DetailView):
    model=Books
    context_object_name = "book"
    template_name = 'bookdetails.html'
    pk_url_kwarg = 'id'

@method_decorator(book_user,name='dispatch')
class BookEditView(UpdateView):
    model = Books
    template_name = 'book_edit.html'
    form_class = BookForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('allbook')


class BookDeleteView(DeleteView):
    def get(self,request,**kwargs):
        id=kwargs.get('id')
        qs=Books.objects.get(id=id)
        qs.delete()
        books=Books.objects.all()

        context={"book":qs,"books":books}
        return render(request,"viewbook.html",context)
        # return redirect("booklist")



class  DashboardView(ListView):
    model = Orders
    template_name = "admin_dashboard.html"
    context_object_name = "orders"
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(object_list=None,**kwargs)
        qs=Orders.objects.all()
        new_orders=qs.filter(status="order_placed")
        context["new_orders"]=new_orders
        delivered_orders=qs.filter(status="delivered")
        context["delivered_orders"]=delivered_orders
        intransit_orders = qs.filter(status="intransit")
        context["intransit_orders"] = intransit_orders
        cancelled_orders = qs.filter(status="cancelled")
        context["cancelled_orders"] = cancelled_orders
        return context

class OrderProcess(UpdateView):
    model=Orders
    form_class = OrderProcessForm
    template_name = "orderprocess.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("dashview")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["order"]=self.object
        return context
    def form_valid(self, form):
        self.object=form.save()
        delivery_date=form.cleaned_data.get('expected_delivery_date')
        message='your order will delivered on'+str(delivery_date)
        send_mail(
            'Order Notification',
            message,
            'nijiyanijzz@gmail.com',
            ['nazznamol@gmail.com'],
            fail_silently=False,
        )

        return super().form_valid(form)






































# from django.http import HttpResponse
# from owner.models import books
# # Create your views here.
#
# #class based and function based
#
# def owner_home(request):
#     return render(request,"c_base.html")
#
# def add_book(request):
#     if request.method=="GET":
#         print("inside get")
#         return render(request,"addbook.html")
#     else:
#
#         print(request.method)
#         return render(request,"addbook.html")
#
# def list_books(request):
#     context={"books":books}
#     return render(request,"viewtbook.html",context)
#
#
# def book_detail(request,id):
#     book=[book for book in books if book["id"]==id]
#     context={"book":book}
#     return render(request,"bookdetails.html",context)
#
#
