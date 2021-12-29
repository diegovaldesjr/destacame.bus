<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Agregar Horario</h2>
                <div class="row">
                    <div class="col">
                        <div class="card">
                            <div class="card-body">
                                <form @submit="onSubmit">
                                    <div class="form-group row">
                                        <label class="col-sm-2 col-form-label">Fecha</label>
                                        <div class="col-sm-6">
                                            <b-form-datepicker id="example-datepicker" v-model="form.fecha" class="mb-2"></b-form-datepicker>
                                        </div>
                                    </div>

                                    <div class="form-group row">
                                        <label class="col-sm-2 col-form-label">Hora</label>
                                        <div class="col-sm-6">
                                            <b-time v-model="form.hora" locale="en"></b-time>
                                        </div>
                                    </div>

                                    <div class="form-group row">
                                        <label for="bus" class="col-sm-2 col-form-label">Bus</label>
                                        <div class="col-sm-6">
                                            <select class="form-control" id="bus" v-model="form.bus">
                                                <option v-for="item in buses" :value="item.placa" :key="item.placa">{{item.placa}}</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div class="rows">
                                        <div class="col text-left">
                                            <b-button type="submit" variant="primary">Crear</b-button>
                                            <b-button type="submit" variant="secondary" :to="{name:'Horario', params: {trayectoId: trayectoId}}">Cancelar</b-button>
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
                fecha: '',
                hora: '',
                bus: ''
            },
            trayectoId: this.$route.params.trayectoId,
            buses: []
        }
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()

            let horario = {
                fecha: this.form.fecha + " " + this.form.hora,
                bus: this.form.bus,
                trayecto: this.trayectoId
            }

            const path = 'http://localhost:8000/api/v1/trayectos/'+this.trayectoId+'/horarios/'
            axios.post(path, horario).then((response => {
                swal("Horario creado!", "", "success").then(()=> {
                    this.$router.push({ name: 'Horario' , params: {trayectoId: this.trayectoId}})
                })
            }))
            .catch((error) => {
                console.log(error);
                swal("El horario no pudo ser registrado", "", "error")
            })
        },
        getBuses() {
            const path = 'http://localhost:8000/api/v1/buses/'
            axios.get(path).then((response => {
                this.buses = response.data
            }))
            .catch((error) => {
                console.log(error);
            })
        },
    },
    created() {
        this.getBuses()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>