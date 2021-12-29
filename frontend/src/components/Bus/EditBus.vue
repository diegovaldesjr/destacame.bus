<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Editar Bus</h2>
                <div class="row">
                    <div class="col">
                        <div class="card">
                            <div class="card-body">
                                <form @submit="onSubmit">
                                    <div class="form-group row">
                                        <label for="placa" class="col-sm-2 col-form-label">Placa</label>
                                        <div class="col-sm-6">
                                            <input type="text" placeholder="Placa" name="placa" class="form-control" v-model="form.placa">
                                        </div>
                                    </div>

                                    <div class="form-group row">
                                        <label for="chofer" class="col-sm-2 col-form-label">Chofer</label>
                                        <div class="col-sm-6">
                                            <select class="form-control" id="chofer" v-model="form.chofer">
                                                <option v-for="item in choferes" :value="item.rut" :key="item.rut">{{item.nombre}} {{item.apellido}}</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="rows">
                                        <div class="col text-left">
                                            <b-button type="submit" variant="primary">Editar</b-button>
                                            <b-button type="submit" variant="secondary" :to="{name:'Bus'}">Cancelar</b-button>
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
            busId: this.$route.params.busId,
            form: {
                placa: '',
                chofer: ''
            },
            choferes: []
        }
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()

            const path = 'http://localhost:8000/api/v1/buses/'+this.busId+'/'
            axios.put(path, this.form).then((response => {
                this.form.placa = response.data.placa
                this.form.chofer = response.data.chofer

                swal("Bus actualizado!", "", "success").then(()=> {
                    this.$router.push({ name: 'Bus' })
                })
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        getBus() {
            const path = 'http://localhost:8000/api/v1/buses/'+this.busId+'/'
            axios.get(path).then((response => {
                this.form.placa = response.data.placa
                this.form.chofer = response.data.chofer
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        getChoferes() {
            const path = 'http://localhost:8000/api/v1/choferes/'
            axios.get(path).then((response => {
                this.choferes = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        }
    },
    created() {
        this.getBus()
        this.getChoferes()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>