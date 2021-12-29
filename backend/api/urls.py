from django.urls import path
from rest_framework import routers

from .viewsets import BusViewSet, ChoferViewSet, PasajeroViewSet, TerminalViewSet, UserViewSet, ReservaReadViewSet
from . import views

router = routers.DefaultRouter()
router.register('terminales', TerminalViewSet, basename='Terminal')
router.register('buses', BusViewSet, basename='Buses')
router.register('choferes', ChoferViewSet, basename='Chofer')
router.register('pasajeros', PasajeroViewSet, basename='Pasajero')

router.register('usuarios', UserViewSet, basename='Usuario')

urlpatterns = router.urls

urlpatterns.append(path('trayectos/', views.TrayectoList.as_view()))
urlpatterns.append(path('trayectos/<int:pk>/', views.TrayectoDetail.as_view()))
urlpatterns.append(path('trayectos/<int:pk>/horarios/', views.HorarioList.as_view()))
urlpatterns.append(path('trayectos/<int:fk>/horarios/<int:pk>/', views.HorarioDetail.as_view()))
urlpatterns.append(path('horarios/<int:pk>/reservas/', views.HorarioReservaList.as_view()))
# urlpatterns.append(path('horarios/<int:pf>/reservas/<int:pk>/', views.HorarioDetail.as_view()))
urlpatterns.append(path('pasajeros/<int:pk>/reservas/', views.PasajeroReservaList.as_view()))
urlpatterns.append(path('pasajeros/<int:fk>/reservas/<int:pk>/', views.PasajeroReservaDetail.as_view()))