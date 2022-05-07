import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
      options: {
        customProperties: true,
      },
    themes: {
      light: {
        primary: '#174eb3',
        secondary: '#ffffff',
        accent: '#82B1FF',
        error: '#FF5252',
        info: '#150b7b',
        success: '#4CAF50',
        warning: '#FFC107'
      },
    },
  },
});
