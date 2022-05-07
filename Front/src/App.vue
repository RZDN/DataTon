<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-spacer></v-spacer>
      <h1>Espectadores</h1>
      <v-spacer></v-spacer>
      <!--<v-list-item-icon style="cursor: pointer" @click="navigateToStatistics">
          <v-icon class="mt-lg-n2 mr-3">mdi-chart-bar</v-icon>
          Estadisticas
      </v-list-item-icon>-->
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
  methods:{
    navigateToStatistics(){
      this.$router.push({name:'statistics'})
    }
  }
};
</script>
