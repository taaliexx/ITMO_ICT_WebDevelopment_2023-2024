<template>
  <div class="form-signin">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div class="form-floating mb-3">
        <input type="text" v-model="loginData.username" class="form-control" id="username" placeholder="Username" required>
        <label for="username">Username</label>
      </div>
      <div class="form-floating mb-3">
        <input type="password" v-model="loginData.password" class="form-control" id="password" placeholder="Password" required>
        <label for="password">Password</label>
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loginData: {
        username: '', // Обновлено с email на username
        password: '',
      },
    };
  },
  methods: {
    login() {
      axios.post('http://127.0.0.1:8000/hotel/api/v1/token/', this.loginData)
      .then(response => {
  if (response.data && response.data.access) {
    localStorage.setItem('accessToken', response.data.access);
    localStorage.setItem('refreshToken', response.data.refresh);
    console.log('Login successful. Access Token:', response.data.access);

    // Перенаправление на страницу Home
    this.$router.push({ name: 'Home' });
  } else {
    console.error('Invalid response format:', response);
  }
});
    },
  },
};
</script>
