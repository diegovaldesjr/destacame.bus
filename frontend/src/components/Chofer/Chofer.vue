<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <div class="row">
                    <div class="col-md-6">
                        <h2>Choferes</h2>
                    </div>
                    <div class="col-md-6">
                        <b-button size="sm" :to="{name: 'NewChofer'}" variant="primary" class="float-right">Nuevo Chofer</b-button>
                    </div>
                </div>
                <div class="col-md-12">
                    <b-table striped hover :items="choferes" :fields="fields">
                        <template v-slot:cell(action)="data">
                            <b-button size="sm" variant="primary" :to="{name: 'EditChofer', params: {choferId: data.item.rut}}">
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger" v-on:click="deleteChofer(data.item)">
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
                {key: 'rut', label:'RUT'},
                {key: 'nombre', label:'Nombre'},
                {key: 'apellido', label:'Apellido'},
                {key: 'action', label: ''}
            ],
            choferes: []
        }
    },
    methods: {
        getChoferes() {
            const path = 'http://localhost:8000/api/v1/choferes/'
            axios.get(path).then((response => {
                this.choferes = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        deleteChofer(item) {
            const path = 'http://localhost:8000/api/v1/choferes/'+item.rut+'/'

            swal({
                title: "Estas seguro?",
                text: "Seguro de que quiere eliminar a "+item.nombre+" "+item.apellido+"?",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            }).then((willDelete) => {
                if (willDelete) {

                    axios.delete(path).then((response => {
                        swal("Chofer eliminada", {
                            icon: "success",
                        });

                        this.getChoferes()
                    }))
                    .catch((error) => {
                        console.log(error);
                        swal("No es posible eliminar chofer", "", "error")
                    })
                }
            });
        }
    },
    created() {
        this.getChoferes()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>