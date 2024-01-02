<template>
  <div>
    <h1>Welcome to the Home Page</h1>
    <button @click="goAuth">{{ isAuthenticated ? 'Logout' : 'Login' }}</button>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      isAuthenticated: false, // Изначально пользователь не залогинен
    };
  },
  methods: {
    goAuth() {
      if (this.isAuthenticated) {
        // Если пользователь залогинен, то делаем logout
        localStorage.removeItem('access_token');
        this.isAuthenticated = false;
      } else {
        // Если пользователь не залогинен, то переходим на страницу login
        this.$router.push({ name: 'login' });
      }
    },
  },
  created() {
    // Проверяем, есть ли токен в localStorage при создании компонента
    const accessToken = localStorage.getItem('access_token');
    this.isAuthenticated = !!accessToken;
  },
};
</script>
