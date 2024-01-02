<template>
  <div class="availability_check">
    <h2>Check Room Availability</h2>
    <form @submit.prevent="checkAvailability">
      <label for="checkInDate">Check In Date:</label>
      <input type="date" v-model="checkInDate" required />

      <label for="checkOutDate">Check Out Date:</label>
      <input type="date" v-model="checkOutDate" required />

      <button type="submit">Check Availability</button>
    </form>

    <!-- Отображение результатов -->
    <div v-if="availableRooms.length > 0">
      <h3>Available Rooms:</h3>
      <ul>
        <li v-for="room in availableRooms" :key="room.id">{{ room.number }}</li>
      </ul>
    </div>
    <div v-else>
      <p>No available rooms for the selected dates.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      checkInDate: '',
      checkOutDate: '',
      availableRooms: [],
    };
  },
  methods: {
    async checkAvailability() {
      try {
        const response = await this.$http.get(`http://127.0.0.1:8000/hotel/free_rooms/${this.checkInDate}/${this.checkOutDate}/`);

        this.availableRooms = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
.availability_check {
  width: 80%;
  max-width: 600px; /* Ограничиваем максимальную ширину контейнера */
  margin: 0 auto; /* Центрируем контейнер на странице */
  text-align: center;
}

.availability_check form {
  margin-top: 20px;
}

.availability_check label {
  display: block;
  margin-bottom: 5px;
}

.availability_check input {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.availability_check button {
  cursor: pointer;
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 10px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.availability_check button:hover {
  background-color: #1e6ea9;
}

.availability_check ul {
  list-style: none;
  padding: 0;
}

.availability_check li {
  background-color: #f1f1f1;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 5px;
  border-radius: 5px;
}
</style>
