<template>
  <v-container>
    <v-row justify="space-between">
      <v-col cols="12" sm="8" md="6"  class="mx-auto">
        <v-card
            class="mx-auto"
            max-width="700"
            style="border-top: #bf0909 4px solid"
        >
          <v-card-text>
            <p class="text-h4 text--primary text-center mt-5 mb-8">
              AUTONORT NOR ORIENTE S.A.C.
            </p>
            <v-row class="text-center">
              <v-col cols="12" md="3" class="mx-auto ml-10" style="display: flex" >
                <v-icon size="10" class="mb-5 mr-4">mdi-checkbox-blank-circle</v-icon>
                <p class="font-weight-bold" style="font-size: 16px" >RUC:</p>
              </v-col>
              <v-col cols="12" md="7" class="mx-auto ml-0">
                <p style="font-size: 16px">20450384322</p>
              </v-col>
            </v-row>
            <v-row class="text-center">
              <v-col cols="12" md="3" class="mx-auto mx-auto ml-10" style="display: flex" >
                <v-icon size="10" class="mb-5 mr-4">mdi-checkbox-blank-circle</v-icon>
                <p class="font-weight-bold" style="font-size: 16px" >Miembro:</p>
              </v-col>
              <v-col cols="12" md="7" class="mx-auto ml-0">
                <p style="font-size: 16px">MATRIXCONSULTING S.A.C.</p>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
        <v-card
            class="mx-auto mt-10"
            max-width="700"
            style="border: #FFC107 2px solid"
        >
          <v-card-text>
            <p class="text-h4 text--primary text-center mt-5 mb-5">
              AUTONORT NOR ORIENTE S.A.C.
            </p>
            <div class="text--primary">
              relating to or dependent on charity; charitable.<br>
              "an eleemosynary educational institution."
            </div>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="5" class="mx-auto">
        <v-card
            class="mx-auto"
            max-width="450"
        >
          <v-card
              dark
              flat
          >
            <v-card-title class="pa-2 info lighten-3">
              <h3 class="text-h6 font-weight-light text-center grow">
                Antecedentes
              </h3>
            </v-card-title>
          </v-card>
          <v-card-text class="py-0">
            <v-timeline
                align-top
                dense
            >
              <v-timeline-item
                  color="pink"
                  small
              >
                <v-row class="pt-1">
                  <v-col cols="4">
                    <strong>05/05/2022</strong>
                  </v-col>
                  <v-col>
                    <strong>New Icon New Icon New Icon New Icon New Icon New Icon</strong>
                    <div class="text-caption">
                      Mobile App
                    </div>
                    <div class="text-caption">
                      Mobile App
                    </div>
                    <div class="text-caption">
                      Mobile App
                    </div>
                  </v-col>
                </v-row>
              </v-timeline-item>
              <v-timeline-item
                  color="teal lighten-3"
                  small
              >
                <v-row class="pt-1">
                  <v-col cols="5">
                    <strong>3-4pm</strong>
                  </v-col>
                  <v-col>
                    <strong>Design Stand Up</strong>
                    <div class="text-caption mb-2">
                      Hangouts
                    </div>
                  </v-col>
                </v-row>
              </v-timeline-item>

              <v-timeline-item
                  color="pink"
                  small
              >
                <v-row class="pt-1">
                  <v-col cols="3">
                    <strong>12pm</strong>
                  </v-col>
                  <v-col>
                    <strong>Lunch break</strong>
                  </v-col>
                </v-row>
              </v-timeline-item>

              <v-timeline-item
                  color="teal lighten-3"
                  small
              >
                <v-row class="pt-1">
                  <v-col cols="3">
                    <strong>9-11am</strong>
                  </v-col>
                  <v-col>
                    <strong>Finish Home Screen</strong>
                    <div class="text-caption">
                      Web App
                    </div>
                  </v-col>
                </v-row>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export  default {
    name:'SupplierView',
    data: () => ({
      years: [
        {
          color: 'cyan',
          year: '1960',
        },
        {
          color: 'green',
          year: '1970',
        },
        {
          color: 'pink',
          year: '1980',
        },
        {
          color: 'amber',
          year: '1990',
        },
        {
          color: 'orange',
          year: '2000',
        },
      ],
    }),
    created() {
      console.log(localStorage.getItem('ruc'))
    }
  }
</script>
