from django.urls import path
from owner import views


urlpatterns=[
   path('books/add',views.AddBookView.as_view(),name='addbook'),
   path('books/all',views.BookListView.as_view(),name='booklist'),
   path('book/<int:id>',views.BookDetailView.as_view(),name='bookdetail'),
   path('book/change/<int:id>',views.BookEditView.as_view(),name='bookedit'),
   path('book/remove/<int:id>',views.BookDeleteView.as_view(),name='bookremove'),
   path('orders/all',views.DashboardView.as_view(),name='dashview'),
   path('order/process/<int:id>',views.OrderProcess.as_view(),name='orderprocess')
]