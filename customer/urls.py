from django.urls import path
from customer import views


urlpatterns=[
   path('all/',views.ListAllView.as_view(),name='allbooks'),
   path('accounts/signup/',views.SingUpView.as_view(),name='signup'),
   path('',views.SinginView.as_view(),name='signin'),
   path('accounts/signout/',views.sign_out,name='signout'),
   path('customers/carts/add/<int:id>',views.AddToCartView.as_view(),name='addtocart'),
   path('customers/carts/items/',views.CartItem.as_view(),name='cartitems'),
   path('customer/carts/item/remove/<int:id>',views.RemoveCartitem.as_view(),name='removecartitem'),
   path('customer/order/add/<int:p_id>/<int:c_id>',views.OrderView.as_view(),name='ordercreate'),
   path('customer/order/',views.MyOrders.as_view(),name='myorders'),
   path('customer/order/remove/<int:id>',views.RemoveOrderitem.as_view(),name='removeorderitem'),
   path('customer/carts/filter/',views.FilterView.as_view(),name='filtereditems'),
   path('customer/orders/reviews/',views.ListReviewsView.as_view(),name='reviews')
]