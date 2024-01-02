import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import RoomList from './components/RoomList.vue';
import AvailabilityCheck from './components/AvailabilityCheck.vue';
import QuarterlyReport from './components/QuarterlyReport.vue';
import BookingsList from './components/BookingsList.vue';
import LoginView from './components/LoginView.vue';


const app = createApp(App);

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: "homepage", component: HomePage },
    { path: '/login', name: "login", component: LoginView },
    { path: '/rooms', component: RoomList, name: 'RoomList', meta: { requiresAuth: true } },
    { path: '/check_availability', component: AvailabilityCheck, meta: { requiresAuth: true } },
    { path: '/quarterly_report', component: QuarterlyReport, meta: { requiresAuth: true } },
    { path: '/bookings', component: BookingsList, meta: { requiresAuth: true } },

  ],
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('access_token');

  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    // Если маршрут требует аутентификации и пользователь не аутентифицирован,
    // вывести предупреждение и перенаправить на главную страницу
    alert('Please login');
    next('/');
  } else {
    // В противном случае продолжите нормальное выполнение навигации
    next();
  }
});

app.use(router);

app.config.globalProperties.$http = axios;

app.mount('#app');
