<template>
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="row">
          <div class="col-md-12" style="margin-bottom: 10px">
              <b-button size="sm" :to="{name: 'Pasajero'}" variant="secondary" class="float-right">Volver</b-button>
          </div>
          <h2>Reservas de {{pasajero.nombre}} {{pasajero.apellido}}</h2>
        </div>
        <div class="col-md-12">
          <b-table striped hover :items="reservas" :fields="fields">
            <template v-slot:cell(action)="data">
              <b-button
                size="sm"
                variant="primary"
                v-on:click="mostrarDetalles(data.item)"
              >
                Ver detalles
              </b-button>
            </template>
          </b-table>
        </div>
      </div>
    </div>
    <div>
      <b-modal ok-only id="modal-1" title="Detalles reserva">
        <div class="row">
          <div class="col-md-8">
            <label class="col">Fecha y hora: <strong>{{reservaSelect.horario.fecha_format}}</strong></label>
            <label class="col">Trayecto: <strong>{{reservaSelect.trayecto.origen_nombre}} -> {{reservaSelect.trayecto.destino_nombre}}</strong></label>
            <label class="col">Bus: <strong>{{reservaSelect.horario.bus}}</strong></label>
            <label class="col">Asiento: <strong>{{reservaSelect.asiento.n_asiento}}</strong></label>
          </div>
          <div class="col-md-4">
            <b-button
              size="sm"
              variant="danger"
              v-on:click="deleteReserva(reservaSelect)"
            >
              Cancelar Reserva
            </b-button>
          </div>
        </div>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import swal from "sweetalert";

export default {
  data() {
    return {
      fields: [
        { key: "horario.fecha_format", label: "Fecha y hora" },
        { key: "trayecto.origen_nombre", label: "Origen" },
        { key: "trayecto.destino_nombre", label: "Destino" },
        { key: "horario.bus", label: "Bus" },
        { key: "action", label: "" },
      ],
      terminales: [],
      reservas: [],
      pasajeroId: this.$route.params.pasajeroId,
      pasajero: {},
      reservaSelect: {
        asiento: {
          n_asiento: ''
        },
        horario: {
          fecha_format: '',
          bus: ''
        },
        trayecto: {
          origen_nombre: '',
          destino_nombre: ''
        }
      }
    };
  },
  methods: {
    getReservas() {
      const path =
        "http://localhost:8000/api/v1/pasajeros/" + this.pasajeroId + "/reservas/";
      axios.get(path).then((response) => {
          this.reservas = response.data;

          for(let reserva of this.reservas){
            let origen = this.terminales.find(elem => elem.id == reserva.trayecto.origen)
            let destino = this.terminales.find(elem => elem.id == reserva.trayecto.destino)

            reserva.trayecto.origen_nombre = origen.ciudad + ", " + origen.pais
            reserva.trayecto.destino_nombre = destino.ciudad + ", " + destino.pais

            let fecha = new Date(reserva.horario.fecha)

            reserva.horario.fecha_format = fecha.getFullYear() + "/" +
              ("0" + (fecha.getMonth()+1)).slice(-2) + "/" +
              ("0" + fecha.getDate()).slice(-2) + " " +
              ("0" + fecha.getHours()).slice(-2) + ":" +
              ("0" + fecha.getMinutes()).slice(-2)
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteReserva(item) {
      const path = "http://localhost:8000/api/v1/pasajeros/"+this.pasajeroId+"/reservas/" + item.id + "/";

      swal({
        title: "Estas seguro?",
        text: "Seguro de que quiere cancelar reserva?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      }).then((willDelete) => {
        if (willDelete) {
          axios.delete(path).then((response) => {
              swal("Reserva cancelada", {
                icon: "success",
              });

              this.$bvModal.hide("modal-1")
              this.getReservas();
            })
            .catch((error) => {
              console.log(error);
              swal("No es posible cancelar reserva", "", "error");
            });
        }
      });
    },
    getPasajero() {
      const path =
        "http://localhost:8000/api/v1/pasajeros/" + this.pasajeroId + "/";
      axios.get(path).then((response) => {
          this.pasajero = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getTerminales() {
      const path = 'http://localhost:8000/api/v1/terminales/'
      axios.get(path).then((response => {
          this.terminales = response.data
      }))
      .catch((error) => {
          console.log(error);
      })
    },
    mostrarDetalles(reserva) {
      this.reservaSelect = reserva
      this.$bvModal.show("modal-1")
    }
  },
  created() {
    this.getTerminales()
    this.getPasajero()
    this.getReservas()
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>