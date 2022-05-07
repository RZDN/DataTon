<template>
  <v-container>
    <v-row>
      <v-col>
        <v-col class="text-center">
          <v-icon color="primary" size="180" class="mt-12">
            mdi-account-search
          </v-icon>
          <h1 class="mt-12 mb-6" style="color: #26292e;font-size: 36px">¡Hola Espectador!</h1>
        </v-col>
        <v-col cols="12" md="6" sm="8" class="mx-auto">
          <v-toolbar
              dark
              color="primary"
              class="mt-10"
          >
            <v-autocomplete
                v-model="supplier"
                :loading="loading"
                :items="items"
                :search-input.sync="search"
                class="mx-4"
                flat
                hide-no-data
                hide-details
                item-text="RUCPROVEEDOR"
                label="Buscar por RUC"
                solo-inverted
                return-object
            ></v-autocomplete>
            <v-btn  color="secondary" class="primary--text" depressed @click="saveRuc">Buscar</v-btn>
          </v-toolbar>
        </v-col>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
  import SupplierService from "@/services/supplier.service";

  export default {
    name: 'HelloWorld',
    data: () => ({
      loading: false,
      supplier: null,
      search: null,
      suppliers:[]
    }),
    computed:{
      items () {
        return this.suppliers.map(supplier => {
          return Object.assign({}, supplier)
        })
      },
    },
    watch: {
      search (val) {
        // Items have already been loaded
        if (this.items.length > 0) return

        // Items have already been requested
        if (this.loading) return

        this.loading = true

        // Lazily load input items
        fetch('http://127.0.0.1:4000/empresas')
            .then(response => response.json())
            .then(response => {
              console.log(response.empresas)
              this.suppliers = response.empresas
            })
            .catch(err => {
              console.log(err)
            })
            .finally(() => (this.loading = false))
      },
    },
    methods:{
      saveRuc(){
        localStorage.ruc = this.supplier.RUC_MIEMBRO
        this.$router.push({name:'supplier'})
      }
    }
  }
</script>
