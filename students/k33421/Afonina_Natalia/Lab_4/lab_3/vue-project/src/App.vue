<template>
  <div id="app">
    <Rooms />
  </div>
</template>

<script>
import Rooms from './components/Rooms.vue';

export default {
    name: "Hotel",
  components: {
    Rooms
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.rooms_container {
  max-width: 800px;
  margin: 0 auto;
}

.rooms_content {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
}

.room_list {
  list-style: none;
  padding: 0;
}

.room_list li {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: #e74c3c;
  color: #fff;
  border: none;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #c0392b;
}
</style>
