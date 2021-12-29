<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Agregar Pasajero</h2>
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

                                    <!-- <div class="form-group row">
                                        <label for="pass" class="col-sm-2 col-form-label">Contraseña</label>
                                        <div class="col-sm-6">
                                            <input type="password" placeholder="Contraseña" name="pass" class="form-control" v-model="form.password">
                                        </div>
                                    </div> -->

                                    <div class="rows">
                                        <div class="col text-left">
                                            <b-button type="submit" variant="primary">Crear</b-button>
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

            if(!this.validEmail(this.form.email)){
                swal("Correo invalido", "", "error")
                return
            }

            const path = 'http://localhost:8000/api/v1/pasajeros/'
            axios.post(path, this.form).then((response => {
                swal("Pasajero creado!", "", "success").then(()=> {
                    this.$router.push({ name: 'Pasajero' })
                })
            }))
            .catch((error) => {
                console.log(error);
                swal("El pasajero no pudo ser registrado", "", "error")
            })
        },
        validEmail: function (email) {
            var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(email);
        }
    },
    created() {
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>