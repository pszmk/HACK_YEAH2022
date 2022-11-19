from django.urls import path

from .views import RoutineCreate, RoutineList


urlpatterns = [
  path('', RoutineList.as_view(), name='routines'),
  path('routine-create/', RoutineCreate.as_view(), name='routine-create'),
]