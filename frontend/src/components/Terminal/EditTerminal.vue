<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Editar Terminal</h2>
                <div class="row">
                    <div class="col">
                        <div class="card">
                            <div class="card-body">
                                <form @submit="onSubmit">
                                    <div class="form-group row">
                                        <label for="pais" class="col-sm-2 col-form-label">Pais</label>
                                        <div class="col-sm-6">
                                            <input type="text" placeholder="Pais" name="pais" class="form-control" v-model="form.pais">
                                        </div>
                                    </div>

                                    <div class="form-group row">
                                        <label for="ciudad" class="col-sm-2 col-form-label">Ciudad</label>
                                        <div class="col-sm-6">
                                            <input type="text" placeholder="Ciudad" name="ciudad" class="form-control" v-model="form.ciudad">
                                        </div>
                                    </div>

                                    <div class="rows">
                                        <div class="col text-left">
                                            <b-button type="submit" variant="primary">Editar</b-button>
                                            <b-button type="submit" variant="secondary" :to="{name:'Terminal'}">Cancelar</b-button>
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
            terminalId: this.$route.params.terminalId,
            form: {
                pais: '',
                ciudad: ''
            }
        }
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()

            const path = 'http://localhost:8000/api/v1/terminales/'+this.terminalId+'/'
            axios.put(path, this.form).then((response => {
                this.form.pais = response.data.pais
                this.form.ciudad = response.data.ciudad

                swal("Terminal actualizado!", "", "success").then(()=> {
                    this.$router.push({ name: 'Terminal' })
                })
            }))
            .catch((error) => {
                console.log(error);
                swal("No se pudo actualizar informacion", "Verifique sus datos", "error")
            })
        },
        getTerminal() {
            const path = 'http://localhost:8000/api/v1/terminales/'+this.terminalId+'/'
            axios.get(path).then((response => {
                this.form.pais = response.data.pais
                this.form.ciudad = response.data.ciudad
            }))
            .catch((error) => {
                console.log(error);
            })
        },
    },
    created() {
        this.getTerminal()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>