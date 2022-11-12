from django.urls import path
from .  import views


urlpatterns = [
path('',views.index,name="drone"),
path('check-drone-status',views.check_drone_status,name="check-drone-status")

]
