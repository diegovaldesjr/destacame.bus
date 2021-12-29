<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <div class="row">
                    <div class="col-md-12" style="margin-bottom: 10px">
                        <b-button size="sm" :to="{name: 'Trayecto'}" variant="secondary" class="float-left">Volver</b-button>
                    </div>
                    <div class="col-md-6">
                        <!-- <h2>{{origen_nombre}} - {{destino_nombre}}</h2> -->
                        <h3>Horarios</h3>
                    </div>
                    <div class="col-md-6">
                        <b-button size="sm" :to="{name: 'NewHorario', params: {trayectoId: trayectoId}}" variant="primary" class="float-right">Nuevo Horario</b-button>
                    </div>
                </div>
                <div class="col-md-12">
                    <b-table striped hover :items="horarios" :fields="fields">
                        <template v-slot:cell(action)="data">
                            <b-button size="sm" variant="primary" :to="{name: 'EditHorario', params: {horarioId: data.item.id}}">
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger" v-on:click="deleteHorario(data.item)">
                                Eliminar
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
            trayectoId: this.$route.params.trayectoId,
            fields: [
                {key: 'fecha_format', label:'Horario'},
                {key: 'bus', label:'Placa bus'},
                {key: 'action', label: ''}
            ],
            horarios: [],
            trayecto: {}
        }
    },
    methods: {
        getHorarios() {
            const path = 'http://localhost:8000/api/v1/trayectos/'+this.trayectoId+'/horarios/'
            axios.get(path).then((response => {
                this.horarios = response.data
                
                for(let horario of this.horarios){
                    let fecha = new Date(horario.fecha)

                    horario.fecha_format = fecha.getFullYear() + "/" +
                        ("0" + (fecha.getMonth()+1)).slice(-2) + "/" +
                        ("0" + fecha.getDate()).slice(-2) + " " +
                        ("0" + fecha.getHours()).slice(-2) + ":" +
                        ("0" + fecha.getMinutes()).slice(-2)
                }
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        deleteHorario(item) {
            const path = 'http://localhost:8000/api/v1/trayectos/'+this.trayectoId+'/horarios/'+item.id+'/'

            swal({
                title: "Estas seguro?",
                text: "Seguro de que quiere eliminar el horario seleccionado?",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            }).then((willDelete) => {
                if (willDelete) {

                    axios.delete(path).then((response => {
                        swal("Horario eliminado", {
                            icon: "success",
                        });

                        this.getHorarios()
                    }))
                    .catch((error) => {
                        console.log(error);
                        swal("No es posible eliminar horario", "", "error")
                    })
                }
            });
        },
        getTrayecto() {
            const path = 'http://localhost:8000/api/v1/trayectos/'+this.trayectoId+'/'
            axios.get(path).then((response => {
                this.trayecto = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        getTerminal(id, terminal) {
            const path = 'http://localhost:8000/api/v1/terminales/'+id
            axios.get(path).then((response => {
                terminal = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        },
    },
    created() {
        this.getTrayecto()
        // this.getTerminal(this.trayecto.origen, this.origen)
        // this.getTerminal(this.trayecto.destino, this.destino)
        this.getHorarios()
        
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>