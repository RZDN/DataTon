<template>
  <v-container>
    <v-toolbar flat>
      <v-toolbar-title style="color: #174eb3" >Proveedores</v-toolbar-title>
      <v-divider
          class="ml-2 info"
          inset
          vertical
      ></v-divider>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-card-title>
      <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
          class="mb-0"
      ></v-text-field>
    </v-card-title>
    <v-data-table
        :headers="headers"
        :items="suppliers"
        :search="search"
    >
      <template v-slot:top>
        <v-dialog
            v-model="dialog"
        >
          <template v-slot:activator="{ on, attrs }">
          </template>
          <v-row class="pt-10 pb-10">
            <v-col col="12" md="6">
              <v-card>
                <v-card-title>
                  <span class="text-h5" style="color: #FFC107">Penalidades</span>
                </v-card-title>
                <v-card-title>
                  <v-text-field
                      v-model="search1"
                      append-icon="mdi-magnify"
                      label="Search"
                      single-line
                      hide-details
                      color="#FFC107"
                  ></v-text-field>
                </v-card-title>
                <v-data-table
                    :headers="headers1"
                    :items="penalties"
                    :search="search1"
                ></v-data-table>
              </v-card>
            </v-col>
            <v-col col="12" md="6">
              <v-card>
                <v-card-title>
                  <span class="text-h5" style="color: #FF5252">Sanciones</span>
                </v-card-title>
                <v-card-title>
                  <v-text-field
                      v-model="search2"
                      append-icon="mdi-magnify"
                      label="Search"
                      single-line
                      hide-details
                  ></v-text-field>
                </v-card-title>
                <v-data-table
                    :headers="headers2"
                    :items="sanctions"
                    :search="search2"
                ></v-data-table>
              </v-card>
            </v-col>
          </v-row>
        </v-dialog>
        <v-dialog
            v-model="dialog2"
            max-width="1200px"
        >
          <template v-slot:activator="{ on, attrs }">
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5" style="color: #174eb3">Adjudicaciones</span>
            </v-card-title>
            <v-card-title>
              <v-text-field
                  v-model="search3"
                  append-icon="mdi-magnify"
                  label="Search"
                  single-line
                  hide-details
              ></v-text-field>
            </v-card-title>
            <v-data-table
                :headers="headers3"
                :items="allotments"
                :search="search3"
            ></v-data-table>
          </v-card>
        </v-dialog>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon
            color="#1e82ce"
            small
            class="mr-2"
            @click="viewPenalties(item)"
        >
          mdi-gavel
        </v-icon>
        <v-icon
            color="#1e82ce"
            small
            @click="viewSanctions(item)"
        >
          mdi-file-document
        </v-icon>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import SupplierService from "@/services/supplier.service";
import PenaltyService from "@/services/penalty.service";
import SanctionService from "@/services/sanction.service";
import AllotmentService from "@/services/allotment.service";

export default {
  name: "StatisticsView",
  data: () => ({
    search: '',
    search1: '',
    search2: '',
    search3: '',
    headers: [
      {
        text: 'RUC',
        align: 'start',
        value: 'ruc',
        sortable: false
      },
      { text: 'Proveedor', value: 'name', sortable: false},
      { text: 'País', value: 'country',filterable: false, sortable: false },
      { text: 'Departamento', value: 'departament', sortable: false},
      { text: 'Provincia', value: 'province',filterable: false, sortable: false },
      { text: 'Distrito', value: 'district',filterable: false, sortable: false },
      { text: 'Accciones', value: 'actions', sortable: false },
    ],
    suppliers: [],
    editedIndex: -1,
    dialog: false,
    headers1: [
      {text: 'Fecha', value:'date',},
      { text: 'Descripción', value: 'description',filterable: false, sortable: false},
      { text: 'Entidad contratante', value: 'contractor',filterable: false, sortable: false },
      { text: 'Id Contrato', value: 'contract_id',filterable: false, sortable: false},
      { text: 'Monto', value: 'amount',filterable: false, sortable: false },
      { text: 'Tipo de Penalidad', value: 'type', sortable: false  },
    ],
    penalties:[],
    dialog1: false,
    headers2: [

      {text: 'Fecha inicio',  value:'start_date',filterable: false, sortable: false},
      { text: 'Fecha fin', value: 'end_date',filterable: false, sortable: false},
      { text: 'Resolución', value: 'resolution',sortable: false },
      { text: 'Motivo', value: 'reason', sortable: false},
    ],
    sanctions:[],
    dialog2: false,
    headers3: [

      {text: 'Código Convocatoria',  value:'code',filterable: false, sortable: false},
      { text: 'Descripcion', value: 'description',filterable: false, sortable: false},
      { text: 'Entidad RUC', value: 'entity_ruc',sortable: false },
      { text: 'Fecha Buena Pro', value: 'date_1',filterable: false, sortable: false},
      { text: 'Fecha Concentimiento', value: 'date_2',filterable: false, sortable: false},
      { text: 'Fecha Convocatoria', value: 'date_3',filterable: false, sortable: false},
      { text: 'Moneda', value: 'currency',filterable: false, sortable: false},
      { text: 'Monto', value: 'amount',filterable: false, sortable: false},
    ],
    allotments:[]
  }),
  created() {
    this.retrieveAllSuppliers()
  },
  methods:{
    getDisplaySupplier(supplier){
      return{
        ruc:supplier.RUCPROVEEDOR,
        name:supplier.PROVEEDOR,
        country:supplier.ORIGEN,
        departament:supplier.DEPARTAMENTO,
        province:supplier.PROVINCIA,
        district:supplier.DISTRITO,
      };
    },
    getDisplayPenalty(penalty){
      return{
        description:penalty.DESCRIPCION,
        date:penalty.FECHA_PENALIDAD,
        contractor:penalty.ENTIDAD_CONTRATANTE,
        contract_id:penalty.ID_CONTRATO,
        amount:penalty.MONTO,
        object:penalty.OBJETO_CONTRATO,
        type:penalty.TIPO_PENALIDAD,
      };
    },
    getDisplaySanction(sanction){
      return{
        start_date:sanction.FECHA_INICIO,
        end_date:sanction.FECHA_FIN,
        resolution:sanction.NUMERO_RESOLUCION,
        reason:sanction.MOTIVO_DE_INFRACCION,
      }
    },
    getDisplayAllotment(allotment){
      return{
        code:allotment.CODIGOCONVOCATORIA,
        description:allotment.DESCRIPCION_ITEM,
        entity_ruc:allotment.ENTIDAD_RUC,
        date_1:allotment.FECHA_BUENAPRO,
        date_2:allotment.FECHA_CONSENTIMIENTO_BP,
        date_3:allotment.FECHA_CONVOCATORIA,
        currency:allotment.MONEDA,
        amount:allotment.MONTO_ADJUDICADO_ITEM,
      };
    },
    //---
    retrieveAllSuppliers(){
      SupplierService.getAllSuppliers()
          .then(response => {
            this.suppliers=response.data.empresas.map(this.getDisplaySupplier)
          }).catch(e => {
        console.log(e);
      })
    },
    retrieveAllPenalties(ruc){
      PenaltyService.getAllPenaltiesByRuc(ruc)
          .then(response => {
            this.penalties=response.data.penalidades.map(this.getDisplayPenalty)
          }).catch(e => {
        console.log(e);
      })
    },
    retrieveAllSanctions(ruc){
      SanctionService.getAllSanctionsByRuc(ruc)
          .then(response => {
            this.sanctions=response.data.penalidades.map(this.getDisplaySanction)
          }).catch(e => {
        console.log(e);
      })
    },
    retrieveAllAllotments(ruc){
      AllotmentService.getAllAllotmentsByRuc(ruc)
          .then(response => {
            this.allotments=response.data.adjudicaciones.map(this.getDisplayAllotment)
            console.log(this.allotments)
          }).catch(e => {
        console.log(e);
      })
    },
    //--
    viewPenalties(item) {
      this.retrieveAllPenalties(item.ruc)
      this.retrieveAllSanctions(item.ruc)
      this.dialog = true
    },
    viewSanctions(item) {
      this.retrieveAllAllotments(item.ruc)
      this.dialog2 = true
    }
  }
}
</script>

<style scoped>

</style>
