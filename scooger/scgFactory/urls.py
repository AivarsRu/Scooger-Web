from django.urls import path
from . import views

urlpatterns = [
    path("", views.factoryFloor, name="factoryFloor"),
    path("floor", views.factoryFloor, name="factoryFloor"),
    path("rfidroom", views.rfidRoom, name="rfidRoom"),
    # # JSON API - atgriez transmitter un receiver
    # path("TxRx_Selector", views.TxRxSelector, name="TxRx_Selector"),

    # # tiek novirzīts uz tabulas izvēli
    # # path("WPT_measurements/<int:Batch_ID>", views.WPT_measurements_view, name="WPT_measurements"), # Padots mainīgais Deliverable_ID
]
