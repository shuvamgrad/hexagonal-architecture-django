from typing import cast

from django.apps import apps as django_anapp
from django.urls import path

from anapp.apps import AnappConfig

app_config: AnappConfig = cast(
    AnappConfig,
    django_anapp.get_containing_app_config('anapp')
)

transaction_view = app_config.container['transaction_view']

urlpatterns = [
    path('transaction', transaction_view)
]
