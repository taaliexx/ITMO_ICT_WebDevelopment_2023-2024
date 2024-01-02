import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    dark: false, // или true, если вы хотите темный режим
    themes: {
      light: {
        primary: '#1976D2', // цвет основных элементов
        secondary: '#424242', // цвет второстепенных элементов
        accent: '#82B1FF', // цвет акцента
      },
      dark: {
        primary: '#2196F3',
        secondary: '#212121',
        accent: '#FF4081',
      },
    },
  },
});