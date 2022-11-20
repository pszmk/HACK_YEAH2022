from django.urls import path

from .views import RoutineCreate, RoutineList, RoutineRelationCreate, RoutineRelationList


urlpatterns = [
  path('', RoutineList.as_view(), name='routines'),
  path('routine-create/', RoutineCreate.as_view(), name='routine-create'),
  path('', RoutineRelationList.as_view(), name='routines-relation'),
  path('routine-create/', RoutineRelationCreate.as_view(), name='routine-relation-create'),
]