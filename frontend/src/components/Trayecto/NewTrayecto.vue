<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Agregar Trayecto</h2>
                <div class="row">
                    <div class="col">
                        <div class="card">
                            <div class="card-body">
                                <form @submit="onSubmit">
                                    <div class="form-group row">
                                        <label for="origen" class="col-sm-2 col-form-label">Origen</label>
                                        <div class="col-sm-6">
                                            <select class="form-control" id="origen" v-model="form.origen">
                                                <option v-for="item in terminales" :value="item.id" :key="item.id">{{item.ciudad}}, {{item.pais}}</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="form-group row">
                                        <label for="destino" class="col-sm-2 col-form-label">Destino</label>
                                        <div class="col-sm-6">
                                            <select class="form-control" id="destino" v-model="form.destino">
                                                <option v-for="item in terminales" :value="item.id" :key="item.id">{{item.ciudad}}, {{item.pais}}</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="rows">
                                        <div class="col text-left">
                                            <b-button type="submit" variant="primary">Crear</b-button>
                                            <b-button type="submit" variant="secondary" :to="{name:'Trayecto'}">Cancelar</b-button>
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
                origen: '',
                destino: ''
            },
            terminales: []
        }
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()

            if(this.form.origen == this.form.destino){
                swal("El origen y destino no pueden ser el mismo terminal", "", "error")
                return
            }

            const path = 'http://localhost:8000/api/v1/trayectos/'
            axios.post(path, this.form).then((response => {
                swal("Trayecto creado!", "", "success").then(()=> {
                    this.$router.push({ name: 'Trayecto' })
                })
            }))
            .catch((error) => {
                console.log(error);
                swal("El trayecto no pudo ser registrado", "Verifique sus datos", "error")
            })
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
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>