<template>
  <div id="navbar">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#" :to="{name: 'Reserva'}">Destacame.bus</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#" :to="{name: 'Terminal'}">Terminales</b-nav-item>
          <b-nav-item href="#" :to="{name: 'Trayecto'}">Trayectos</b-nav-item>
          <b-nav-item href="#" :to="{name: 'Chofer'}">Choferes</b-nav-item>
          <b-nav-item href="#" :to="{name: 'Bus'}">Buses</b-nav-item>
          <b-nav-item href="#" :to="{name: 'Pasajero'}">Pasajeros</b-nav-item>
          <b-nav-item href="#" :to="{name: 'Reserva'}">Reservas</b-nav-item>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>

export default {
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #navbar{
    margin-bottom: 40px;
  }
</style>