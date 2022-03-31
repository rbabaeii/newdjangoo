
from django.urls import path , include
from .views import landing_page , Update
urlpatterns = [
    path("" , landing_page.as_view() ),
    path('<slug:todo_id>/', Update.as_view() )
]
