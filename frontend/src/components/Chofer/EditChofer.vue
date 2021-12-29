<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Editar Chofer</h2>
                <div class="row">
                    <div class="col">
                        <div class="card">
                            <div class="card-body">
                                <form @submit="onSubmit">
                                    <div class="form-group row">
                                        <label for="rut" class="col-sm-2 col-form-label">RUT</label>
                                        <div class="col-sm-6">
                                            <input type="text" placeholder="xxxxxxxx-x" name="rut" class="form-control" v-model="form.rut">
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
                                            <input type="text" placeholder="Apellido" name="apellido" class="form-control" v-model="form.apellido">
                                        </div>
                                    </div>

                                    <div class="rows">
                                        <div class="col text-left">
                                            <b-button type="submit" variant="primary">Editar</b-button>
                                            <b-button type="submit" variant="secondary" :to="{name:'Chofer'}">Cancelar</b-button>
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
            choferId: this.$route.params.choferId,
            form: {
                rut: '',
                nombre: '',
                apellido: ''
            }
        }
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()

            if(!this.validarRut(this.form.rut)) {
                swal("Rut invalido", "", "warning")
                return
            }

            const path = 'http://localhost:8000/api/v1/choferes/'+this.choferId+'/'
            axios.put(path, this.form).then((response => {
                this.form.rut = response.data.rut
                this.form.nombre = response.data.nombre
                this.form.apellido = response.data.apellido

                swal("Chofer actualizado!", "", "success").then(()=> {
                    this.$router.push({ name: 'Chofer' })
                })
            }))
            .catch((error) => {
                console.log(error);
                swal("No se pudo actualizar informacion", "Verifique sus datos", "error")
            })
        },
        getChofer() {
            const path = 'http://localhost:8000/api/v1/choferes/'+this.choferId+'/'
            axios.get(path).then((response => {
                this.form.rut = response.data.rut
                this.form.nombre = response.data.nombre
                this.form.apellido = response.data.apellido
            }))
            .catch((error) => {
                console.log(error);
            })
        },
        validarRut(rutCompleto) {
            if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
                return false;
            var tmp 	= rutCompleto.split('-');
            var digv	= tmp[1]; 
            var rut 	= tmp[0];
            if ( digv == 'K' ) digv = 'k' ;
            return (this.dv(rut) == digv );
        },
        dv(T){
            var M=0,S=1;
            for(;T;T=Math.floor(T/10))
                S=(S+T%10*(9-M++%6))%11;
            return S?S-1:'k';
        }
    },
    created() {
        this.getChofer()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>