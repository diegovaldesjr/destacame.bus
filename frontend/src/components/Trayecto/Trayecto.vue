<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <div class="row">
                    <div class="col-sm-6">
                        <h2>Trayectos</h2>
                    </div>
                    <div class="col-sm-6">
                        <b-button size="sm" :to="{name: 'NewTrayecto'}" variant="primary" class="float-right">Nuevo Trayecto</b-button>
                    </div>
                </div>
                <div class="col-md-12">
                    <b-table striped hover :items="trayectos" :fields="fields">
                        <template v-slot:cell(action)="data">
                            <b-button size="sm" variant="secondary" :to="{name: 'Horario', params: {trayectoId: data.item.id}}">
                                Horarios
                            </b-button>
                            <b-button size="sm" variant="primary" :to="{name: 'EditTrayecto', params: {trayectoId: data.item.id}}">
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger" v-on:click="deleteTrayecto(data.item)">
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
            fields: [
                {key: 'origen_nombre', label:'Origen'},
                {key: 'destino_nombre', label:'Destino'},
                {key: 'promedio_reservas', label:'Promedio pasajeros'},
                {key: 'action', label: ''}
            ],
            trayectos: [],
            terminales: []
        }
    },
    methods: {
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
        deleteTrayecto(item) {
            const path = 'http://localhost:8000/api/v1/trayectos/'+item.id+'/'

            swal({
                title: "Estas seguro?",
                text: "Seguro de que quiere eliminar "+item.pais+"-"+item.ciudad+"?",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            }).then((willDelete) => {
                if (willDelete) {

                    axios.delete(path).then((response => {
                        swal("Trayecto eliminado", {
                            icon: "success",
                        });

                        this.getTrayectos()
                    }))
                    .catch((error) => {
                        console.log(error);
                        swal("No es posible eliminar trayecto", "", "error")
                    })
                }
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