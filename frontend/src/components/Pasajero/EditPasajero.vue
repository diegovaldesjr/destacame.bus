<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Editar Pasajero</h2>
                <div class="row">
                    <div class="col">
                        <div class="card">
                            <div class="card-body">
                                <form @submit="onSubmit">
                                    <div class="form-group row">
                                        <label for="email" class="col-sm-2 col-form-label">Email</label>
                                        <div class="col-sm-6">
                                            <input type="email" placeholder="email" name="pais" class="form-control" v-model="form.email">
                                        </div>
                                    </div>

                                    <div class="form-group row">
                                        <label for="nombre" class="col-sm-2 col-form-label">Nombre</label>
                                        <div class="col-sm-6">
                                            <input type="text" placeholder="Nombre" name="nombre" class="form-control" v-model="form.nombre">
                                        </div>
                                    </div>

                                    <div class="form-group row">
                                        <label for="apellido" class="col-sm-2 col-form-label">Apellido</label>
                                        <div class="col-sm-6">
                                            <input type="text" placeholder="apellido" name="apellido" class="form-control" v-model="form.apellido">
                                        </div>
                                    </div>

                                    <div class="rows">
                                        <div class="col text-left">
                                            <b-button type="submit" variant="primary">Editar</b-button>
                                            <b-button type="submit" variant="secondary" :to="{name:'Pasajero'}">Cancelar</b-button>
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
            pasajeroId: this.$route.params.pasajeroId,
            form: {
                email: '',
                nombre: '',
                apellido: ''
            }
        }
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()

            const path = 'http://localhost:8000/api/v1/pasajeros/'+this.pasajeroId+'/'
            axios.put(path, this.form).then((response => {
                swal("Pasajero actualizado!", "", "success").then(()=> {
                    this.$router.push({ name: 'Pasajero' })
                })
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        getPasajero() {
            const path = 'http://localhost:8000/api/v1/pasajeros/'+this.pasajeroId+'/'
            axios.get(path).then((response => {
                this.form.email = response.data.email
                this.form.nombre = response.data.nombre
                this.form.apellido = response.data.apellido
            }))
            .catch((error) => {
                console.log(error);
            })
        },
    },
    created() {
        this.getPasajero()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>