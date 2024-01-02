import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import RoomList from './components/RoomList.vue';
import AvailabilityCheck from './components/AvailabilityCheck.vue';
import QuarterlyReport from './components/QuarterlyReport.vue';
import BookingsList from './components/BookingsList.vue';


const app = createApp(App);

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomePage },
    { path: '/rooms', component: RoomList },
    { path: '/check_availability', component: AvailabilityCheck },
    { path: '/quarterly_report', component: QuarterlyReport },
    { path: '/bookings', component: BookingsList },

  ],
});

app.use(router);

app.config.globalProperties.$http = axios;

app.mount('#app');
