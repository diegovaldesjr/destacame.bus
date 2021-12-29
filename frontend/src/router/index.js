import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import Terminal from '@/components/Terminal/Terminal'
import EditTerminal from '@/components/Terminal/EditTerminal'
import NewTerminal from '@/components/Terminal/NewTerminal'
import Bus from '@/components/Bus/Bus'
import EditBus from '@/components/Bus/EditBus'
import NewBus from '@/components/Bus/NewBus'
import Chofer from '@/components/Chofer/Chofer'
import EditChofer from '@/components/Chofer/EditChofer'
import NewChofer from '@/components/Chofer/NewChofer'
import Trayecto from '@/components/Trayecto/Trayecto'
import EditTrayecto from '@/components/Trayecto/EditTrayecto'
import NewTrayecto from '@/components/Trayecto/NewTrayecto'
import Horario from '@/components/Trayecto/Horario/Horario'
import EditHorario from '@/components/Trayecto/Horario/EditHorario'
import NewHorario from '@/components/Trayecto/Horario/NewHorario'
import Pasajero from '@/components/Pasajero/Pasajero'
import EditPasajero from '@/components/Pasajero/EditPasajero'
import NewPasajero from '@/components/Pasajero/NewPasajero'
import Reserva from '@/components/Reserva/Reserva'
import NewReserva from '@/components/Reserva/NewReserva'
import PasajeroReserva from '@/components/Pasajero/PasajeroReserva'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Reserva',
      component: Reserva
    },
    {
      path: '/terminales',
      name: 'Terminal',
      component: Terminal
    },
    {
      path: '/terminales/:terminalId/edit',
      name: 'EditTerminal',
      component: EditTerminal
    },
    {
      path: '/terminales/new',
      name: 'NewTerminal',
      component: NewTerminal
    },
    {
      path: '/buses',
      name: 'Bus',
      component: Bus
    },
    {
      path: '/buses/:busId/edit',
      name: 'EditBus',
      component: EditBus
    },
    {
      path: '/buses/new',
      name: 'NewBus',
      component: NewBus
    },
    {
      path: '/choferes',
      name: 'Chofer',
      component: Chofer
    },
    {
      path: '/choferes/:choferId/edit',
      name: 'EditChofer',
      component: EditChofer
    },
    {
      path: '/choferes/new',
      name: 'NewChofer',
      component: NewChofer
    },
    {
      path: '/trayectos',
      name: 'Trayecto',
      component: Trayecto
    },
    {
      path: '/trayectos/:trayectoId/edit',
      name: 'EditTrayecto',
      component: EditTrayecto
    },
    {
      path: '/trayectos/new',
      name: 'NewTrayecto',
      component: NewTrayecto
    },
    {
      path: '/trayectos/:trayectoId/horarios',
      name: 'Horario',
      component: Horario
    },
    {
      path: '/trayectos/:trayectoId/horarios/:horarioId/edit',
      name: 'EditHorario',
      component: EditHorario
    },
    {
      path: '/trayectos/:trayectoId/horarios/new',
      name: 'NewHorario',
      component: NewHorario
    },
    {
      path: '/pasajeros/',
      name: 'Pasajero',
      component: Pasajero
    },
    {
      path: '/pasajeros/:pasajeroId/edit',
      name: 'EditPasajero',
      component: EditPasajero
    },
    {
      path: '/pasajeros/new',
      name: 'NewPasajero',
      component: NewPasajero
    },
    {
      path: 'horarios/:horarioId/reservas/new',
      name: 'NewReserva',
      component: NewReserva
    },
    {
      path: '/pasajeros/:pasajeroId/reservas',
      name: 'PasajeroReserva',
      component: PasajeroReserva
    },
  ]
})
