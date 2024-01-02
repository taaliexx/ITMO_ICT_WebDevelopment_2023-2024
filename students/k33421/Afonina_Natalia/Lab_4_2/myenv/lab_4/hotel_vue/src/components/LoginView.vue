<template>
  <div>
    <input v-model="login" type="text" placeholder="Username"/>
    <input v-model="password" type="password" placeholder="Password"/>
    <button @click="setLogin">Login</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginView',
  data() {
    return {
      login: '',
      password: '',
    };
  },
  methods: {
    async setLogin() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/hotel/token/', {
          username: this.login,
          password: this.password,
        });

        // При успешном получении токена сохраняем его в localStorage
        localStorage.setItem('access_token', response.data.access);

        // Перенаправляем на домашнюю страницу
        this.$router.push({ name: 'homepage' });
      } catch (error) {
        console.error(error);

        // При ошибке 401 (неверные учетные данные), выводим сообщение
        if (error.response && error.response.status === 401) {
          alert('Invalid username or password');
        }
      }
    },
  },
};
</script>
