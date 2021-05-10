from django.urls import path
from . import views

urlpatterns = [
    path("", views.scootersHome, name="scootersHome"),
    # # JSON API - atgriez transmitter un receiver
    # path("TxRx_Selector", views.TxRxSelector, name="TxRx_Selector"),

    # # tiek novirzīts uz tabulas izvēli
    # # path("WPT_measurements/<int:Batch_ID>", views.WPT_measurements_view, name="WPT_measurements"), # Padots mainīgais Deliverable_ID
]
