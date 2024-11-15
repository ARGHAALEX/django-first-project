from.import views
from django.urls import path
urlpatterns = [
  
    path("",views.index,name="shopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("productview/",views.prodeView,name="ProductView"),
    path("cheackout/",views.checkout,name="Checkout"),
    
]
