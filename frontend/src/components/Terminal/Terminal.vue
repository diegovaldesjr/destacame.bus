<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <div class="row">
                    <div class="col-sm-6">
                        <h2>Terminales</h2>
                    </div>
                    <div class="col-sm-6">
                        <b-button size="sm" :to="{name: 'NewTerminal'}" variant="primary" class="float-right">Nuevo Terminal</b-button>
                    </div>
                </div>
                <div class="col-md-12">
                    <b-table striped hover :items="terminales" :fields="fields">
                        <template v-slot:cell(action)="data">
                            <b-button size="sm" variant="primary" :to="{name: 'EditTerminal', params: {terminalId: data.item.id}}">
                                Editar
                            </b-button>
                            <b-button size="sm" variant="danger" v-on:click="deleteTerminal(data.item)">
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
                {key: 'pais', label:'Pais'},
                {key: 'ciudad', label:'Ciudad'},
                {key: 'action', label: ''}
            ],
            terminales: []
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
        deleteTerminal(item) {
            const path = 'http://localhost:8000/api/v1/terminales/'+item.id+'/'

            swal({
                title: "Estas seguro?",
                text: "Seguro de que quiere eliminar "+item.pais+"-"+item.ciudad+"?",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            }).then((willDelete) => {
                if (willDelete) {

                    axios.delete(path).then((response => {
                        swal("Terminal eliminada", {
                            icon: "success",
                        });

                        this.getTerminales()
                    }))
                    .catch((error) => {
                        console.log(error);
                        swal("No es posible eliminar la terminal", "", "error")
                    })
                }
            });
        }
    },
    created() {
        this.getTerminales()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>