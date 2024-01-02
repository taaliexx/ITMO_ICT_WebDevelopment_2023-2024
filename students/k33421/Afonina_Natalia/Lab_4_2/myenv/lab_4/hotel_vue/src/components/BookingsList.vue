<template>
  <div>
    <h2>Booking Management</h2>

    <!-- Отображение всех бронирований -->
    <div>
      <h3>All Bookings</h3>
      <ul>
        <li v-for="booking in bookings" :key="booking.id">
          <p>User: {{ booking.user.first_name }}</p>
          <p>Room: {{ booking.room.number }}</p>
          <p>Check In: {{ booking.check_in }}</p>
          <p>Check Out: {{ booking.check_out }}</p>
          <p>Check In Done: {{ booking.check_in_done }}</p>
          <p>Check Out Done: {{ booking.check_out_done }}</p>

          <!-- Галочки для check-in и check-out -->
          <label>
            Check In
            <input type="checkbox" v-model="booking.check_in_done" @change="updateCheckInOut(booking.id, 'check_in')">
          </label>

          <label>
            Check Out
            <input type="checkbox" v-model="booking.check_out_done" @change="updateCheckInOut(booking.id, 'check_out')">
          </label>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      bookings: [],
    };
  },
  methods: {
    async loadBookings() {
      try {
        const response = await this.$http.get(`http://127.0.0.1:8000/hotel/all_bookings/`);
        this.bookings = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async updateCheckInOut(bookingId, updateType) {
      try {
        const response = await this.$http.patch(`http://127.0.0.1:8000/hotel/all_bookings/${bookingId}/`, {
          update_type: updateType,
        });

        // Найти индекс обновленной записи в массиве
        const index = this.bookings.findIndex((b) => b.id === bookingId);

        // Обновить массив
        if (index !== -1) {
          this.bookings[index] = response.data;
          this.$forceUpdate(); // Принудительное обновление компонента
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.loadBookings();
  },
};
</script>

<style scoped>
/* Ваши стили для компонента (если нужны) */
</style>
