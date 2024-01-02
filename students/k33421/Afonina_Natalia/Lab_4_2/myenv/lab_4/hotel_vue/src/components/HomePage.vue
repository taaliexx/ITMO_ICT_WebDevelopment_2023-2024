<template>
  <div>
    <h1>Welcome to the Natasha's Hotel Managment System</h1>
    <button @click="goAuth" class="login-button bold-text">
      {{ isAuthenticated ? 'Logout' : 'Login' }}
    </button>
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

<style>
.bold-text {
  font-weight: bold;
}

.login-button {
  border: 2px solid #3498db; /* Цвет обводки кнопки */
  border-radius: 5px; /* Закругление углов */
  padding: 5px 10px; /* Внутренний отступ кнопки */
  margin: 10px; /* Внешний отступ кнопки */
  cursor: pointer; /* Задаем курсор */
  transition: background-color 0.3s; /* Плавный переход цвета фона */
}

.login-button:hover {
  background-color: #3498db; /* Изменяем цвет фона при наведении */
  color: #ffffff; /* Изменяем цвет текста при наведении */
}
</style>
