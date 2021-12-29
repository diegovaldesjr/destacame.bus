<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Reservas</h2>
                <div class=" container row">
                    <div class="col">
                        <div class="card">
                            <div class="card-body row">
                                <div class="col-md-6 form-group row">
                                    <label class="col-sm-3 col-form-label">Fecha</label>
                                    <div class="col-sm-9">
                                        <b-form-datepicker id="example-datepicker" size="sm" v-model="fecha"></b-form-datepicker>
                                    </div>
                                </div>

                                <div class="col-md-6 form-group row">
                                    <label for="trayecto" class="col-sm-3 col-form-label">Trayectos</label>
                                    <div class="col-sm-9">
                                        <select class="form-control" id="trayecto" v-model="trayecto">
                                            <option v-for="item in trayectos" :value="item.id" :key="item.id">{{item.origen_nombre}} -> {{item.destino_nombre}}</option>
                                        </select>
                                    </div>
                                </div>

                                <div class="col-md-4 form-group row">
                                    <label for="capacidad" class="col-sm-6 col-form-label">Capacidad Disponible</label>
                                    <div class="col-sm-6">
                                        <select class="form-control" id="capacidad" v-model="capacidad">
                                            <option v-for="item in capacidadOptions" :value="item" :key="item">{{item}}%</option>
                                        </select>
                                    </div>
                                </div>
                                
                                <div class="col-md-12 text-center">
                                    <b-button size="sm" variant="dark" v-on:click="buscarHorarios()">
                                        Buscar
                                    </b-button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-12" v-show="horarios.length > 0">
                    <b-table striped hover :items="horarios" :fields="fields">
                        <template v-slot:cell(action)="data">
                            <b-button size="sm" variant="dark" :to="{name: 'NewReserva', params: {horarioId: data.item.id, trayectoId: data.item.trayecto}}">
                                Reservar
                            </b-button>
                        </template>
                    </b-table>
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
            fields: [
                {key: 'fecha_format', label:'Hora Salida'},
                {key: 'action', label: ''}
            ],
            terminales: [],
            trayectos: [],
            horarios: [],
            trayecto: '',
            fecha: '',
            capacidadOptions: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            capacidad: ''
        }
    },
    methods: {
        getTerminales() {
            const path = 'http://localhost:8000/api/v1/terminales/'
            axios.get(path).then((response => {
                this.terminales = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        getTrayectos() {
            const path = 'http://localhost:8000/api/v1/trayectos/'
            axios.get(path).then((response => {
                this.trayectos = response.data

                for(let trayecto of this.trayectos){
                    let origen = this.terminales.find(elem => elem.id == trayecto.origen_id)
                    let destino = this.terminales.find(elem => elem.id == trayecto.destino_id)

                    trayecto.origen_nombre = origen.ciudad + ", " + origen.pais
                    trayecto.destino_nombre = destino.ciudad + ", " + destino.pais
                }
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        buscarHorarios() {
            if(!this.fecha){
                swal("Seleccione una fecha", "", "warning")
                return
            }
            else if(!this.trayecto){
                swal("Seleccione un trayecto", "", "warning")
                return
            }

            let fecha = new Date(this.fecha)

            const path = 'http://localhost:8000/api/v1/trayectos/'+this.trayecto+'/horarios/?day='+fecha.getUTCDate()+'&month='+(fecha.getUTCMonth()+1)+'&year='+fecha.getFullYear()+'&capacidad='+this.capacidad
            axios.get(path).then((response => {
                this.horarios = response.data

                for(let horario of this.horarios){
                    let fecha = new Date(horario.fecha)

                    horario.fecha_format = 
                        ("0" + fecha.getHours()).slice(-2) + ":" +
                        ("0" + fecha.getMinutes()).slice(-2)
                }
            }))
            .catch((error) => {
                console.log(error);
            })
        },
    },
    created() {
        this.getTerminales()
        this.getTrayectos()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>