<template>
    <div>
      <h1 v-if="isAuthenticated">Home</h1>
      <p v-else>Please log in to access Home.</p>
    </div>
  </template>
  
  <script>
  export default {
    computed: {
      isAuthenticated() {
        return this.$store.state.isAuthenticated;
      },
    },
  };
  </script>