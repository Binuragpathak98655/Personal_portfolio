from django.urls import path,include
from home  import views


urlpatterns = [
    path('',views.portfolio,name='portfolio'),
    path('Projects/',views.Projects,name='Projects'),
    path('contact/',views.contact,name='contact'),
]

