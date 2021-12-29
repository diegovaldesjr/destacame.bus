<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <div class="row">
                    <div class="col-md-6">
                        <h2>Buses</h2>
                    </div>
                    <div class="col-md-6">
                        <b-button size="sm" :to="{name: 'NewBus'}" variant="primary" class="float-right">Nuevo Bus</b-button>
                    </div>
                </div>
                <div class="col-md-12">
                    <b-table striped hover :items="buses" :fields="fields">
                        <template v-slot:cell(action)="data">
                            <b-button size="sm" variant="primary" :to="{name: 'EditBus', params: {busId: data.item.placa}}">
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger" v-on:click="deleteBus(data.item)">
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
                {key: 'placa', label:'Placa'},
                {key: 'chofer', label:'Chofer'},
                {key: 'action', label: ''}
            ],
            buses: []
        }
    },
    methods: {
        getBuses() {
            const path = 'http://localhost:8000/api/v1/buses/'
            axios.get(path).then((response => {
                this.buses = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        deleteBus(item) {
            const path = 'http://localhost:8000/api/v1/buses/'+item.placa+'/'

            swal({
                title: "Estas seguro?",
                text: "Seguro de que quiere eliminar bus con placa "+item.placa+"?",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            }).then((willDelete) => {
                if (willDelete) {

                    axios.delete(path).then((response => {
                        swal("Bus eliminado", {
                            icon: "success",
                        });

                        this.getBuses()
                    }))
                    .catch((error) => {
                        console.log(error);
                        swal("No es posible eliminar bus", "", "error")
                    })
                }
            });
        }
    },
    created() {
        this.getBuses()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>