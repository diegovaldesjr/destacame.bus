<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Registrar Reserva</h2>
                <div class="row">
                    <div class="col">
                        <div class="card">
                            <div class="card-body">
                                <form @submit="onSubmit">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label>Bus: <strong>{{horario.bus}}</strong></label>
                                            <div class="form-group row">
                                                <label for="asiento" class="col-sm-8 col-form-label">Asientos disponibles</label>
                                                <div class="col-sm-4">
                                                    <select class="form-control" id="asiento" v-model="form.asiento">
                                                        <option v-for="item in asientosDisponibles" :value="item.n" :key="item.n" :disabled="!item.disponible">{{item.n}}</option>
                                                    </select>
                                                </div>
                                            </div>
                                            <div class="form-group row">
                                                <label for="pasajero" class="col-sm-8 col-form-label">Pasajero</label>
                                                <div class="col-sm-4">
                                                    <select class="form-control" id="pasajero" v-model="form.pasajero">
                                                        <option v-for="item in pasajeros" :value="item.id" :key="item.id">{{item.nombre}} {{item.apellido}}</option>
                                                    </select>
                                                </div>
                                            </div>

                                        </div>
                                        <div class="col-md-6">
                                            <div class="bus-map text-center">
                                                <label>Mapa del bus</label>
                                                <img src="@/assets/bus-map.png"/>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="rows">
                                        <div class="col text-left">
                                            <b-button type="submit" variant="primary">Crear</b-button>
                                            <b-button type="submit" variant="secondary" :to="{name:'Reserva'}">Cancelar</b-button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
    data () {
        return {
            form: {
                asiento: '',
                pasajero: ''
            },
            horario: {},
            horarioId: this.$route.params.horarioId,
            trayectoId: this.$route.params.trayectoId,
            asientosDisponibles: [
                {n: 1, disponible:true},
                {n: 2, disponible:true},
                {n: 3, disponible:true},
                {n: 4, disponible:true},
                {n: 5, disponible:true},
                {n: 6, disponible:true},
                {n: 7, disponible:true},
                {n: 8, disponible:true},
                {n: 9, disponible:true},
                {n: 10, disponible:true}
            ],
            pasajeros: []
        }
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()

            if(!this.form.asiento){
                swal("Seleccione asiento", "", "warning")
                return
            }

            let reserva = {
                asiento: this.form.asiento,
                bus: this.horario.bus,
                horario: this.horario.id,
                trayecto: this.horario.trayecto,
                pasajero: this.form.pasajero
            }

            const path = 'http://localhost:8000/api/v1/horarios/'+this.horarioId+'/reservas/'
            axios.post(path, reserva).then((response => {
                swal("Reserva realizada!", "", "success").then(()=> {
                    this.$router.push({ name: 'Reserva' })
                })
            }))
            .catch((error) => {
                console.log(error);
                swal("No se pudo realizar la reserva", "", "error")
            })
        },
        getHorario() {
            const path = 'http://localhost:8000/api/v1/trayectos/'+this.trayectoId+'/horarios/'+this.horarioId+'/'
            axios.get(path).then((response => {
                this.horario = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        getPasajeros() {
            const path = 'http://localhost:8000/api/v1/pasajeros/'
            axios.get(path).then((response => {
                this.pasajeros = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        getReservas() {
            const path = 'http://localhost:8000/api/v1/horarios/'+this.horarioId+'/reservas/'
            axios.get(path).then((response => {
                this.reservas = response.data

                for(let reserva of this.reservas){
                    this.asientosDisponibles.find(elem => {
                        if(reserva.asiento.n_asiento == elem.n) {
                            elem.disponible = false
                        }
                    })
                }
            }))
            .catch((error) => {
                console.log(error);
            })
        },
    },
    created() {
        this.getPasajeros()
        this.getHorario()
        this.getReservas()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .bus-map img{
        width: 50%;
        height: auto;
        margin: auto;
        display: block;
    }
</style>