from items.views import ListItems
from django.urls import path


urlpatterns = [
    path("",ListItems.as_view(),name="items"),
    path("<int:key>",ListItems.as_view(),name="items_detail"),
]