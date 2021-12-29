<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <div class="row">
                    <div class="col-sm-6">
                        <h2>Pasajeros</h2>
                    </div>
                    <div class="col-sm-6">
                        <b-button size="sm" :to="{name: 'NewPasajero'}" variant="primary" class="float-right">Nuevo Pasajero</b-button>
                    </div>
                </div>
                <div class="col-md-12">
                    <b-table striped hover :items="pasajeros" :fields="fields">
                        <template v-slot:cell(action)="data">
                            <b-button size="sm" variant="dark" :to="{name: 'PasajeroReserva', params: {pasajeroId: data.item.id}}">
                                Reservas
                            </b-button>
                            <b-button size="sm" variant="primary" :to="{name: 'EditPasajero', params: {pasajeroId: data.item.id}}">
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger" v-on:click="deletePasajero(data.item)">
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
                {key: 'email', label:'Email'},
                {key: 'nombre', label:'Nombre'},
                {key: 'apellido', label:'Apellido'},
                {key: 'action', label: ''}
            ],
            pasajeros: []
        }
    },
    methods: {
        getPasajeros() {
            const path = 'http://localhost:8000/api/v1/pasajeros/'
            axios.get(path).then((response => {
                this.pasajeros = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        deletePasajero(item) {
            const path = 'http://localhost:8000/api/v1/pasajeros/'+item.id+'/'

            swal({
                title: "Estas seguro?",
                text: "Seguro de que quiere eliminar a"+item.nombre+"?",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            }).then((willDelete) => {
                if (willDelete) {

                    axios.delete(path).then((response => {
                        swal("Pasajero eliminado", {
                            icon: "success",
                        });

                        this.getPasajeros()
                    }))
                    .catch((error) => {
                        console.log(error);
                        swal("No es posible eliminar al pasajero", "", "error")
                    })
                }
            });
        }
    },
    created() {
        this.getPasajeros()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>