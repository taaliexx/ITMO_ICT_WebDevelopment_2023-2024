<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/rooms">Rooms</router-link> |
      <router-link to="/bookings">Bookings</router-link> |
      <router-link to="/check_availability">Check Availability</router-link> |
      <router-link to="/quarterly_report">Quarterly Report</router-link>


    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  font-family: Montserrat;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#button
nav {
  margin-bottom: 20px;
}
</style>
