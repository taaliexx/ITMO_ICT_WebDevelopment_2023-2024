import Vue from 'vue';
import App from './App.vue';
import axios from 'axios';

Vue.config.productionTip = false;
Vue.prototype.$http = axios;  // Установка Axios в качестве глобальной переменной

new Vue({
  render: h => h(App),
}).$mount('#app');