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
/* Ваши стили для компонента (если нужны) */
</style>
