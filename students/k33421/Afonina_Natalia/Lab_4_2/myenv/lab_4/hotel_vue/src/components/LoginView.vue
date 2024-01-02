<template>
  <div class="login-container">
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

<style scoped>
.login-container {
  width: 80%;
  max-width: 400px; /* Ограничиваем максимальную ширину контейнера */
  margin: 0 auto; /* Центрируем контейнер на странице */
  text-align: center;
}

.login-container input {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.login-container button {
  cursor: pointer;
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 10px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.login-container button:hover {
  background-color: #1e6ea9;
}
</style>
