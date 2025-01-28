from django.urls import path
from api.HappyMarineShipping import views


urlpatterns = [
 path('RegShipForSale',views.AddShip),
 path('viewShip',views.AllShips)
]

