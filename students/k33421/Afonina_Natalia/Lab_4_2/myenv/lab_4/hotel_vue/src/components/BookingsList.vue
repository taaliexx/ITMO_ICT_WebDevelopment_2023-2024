<template>
  <div>
    <h2>Booking Management</h2>
    <!-- Форма для добавления нового бронирования -->
    <h3>Add New Booking</h3>
    <form @submit.prevent="addNewBooking">
      <!-- Ваши поля для ввода информации о бронировании -->
      <label for="user">User:</label>
      <select v-model="newBooking.user" required>
        <option v-for="user in users" :key="user.id" :value="user.id">{{ user.first_name }} {{ user.last_name }}</option>
      </select>

      <label for="room">Room:</label>
      <select v-model="newBooking.room" required>
        <option v-for="room in rooms" :key="room.id" :value="room.id">{{ room.number }} {{ room.category }}</option>
      </select>

      <label for="checkIn">Check In:</label>
      <input type="date" v-model="newBooking.check_in" required />

      <label for="checkOut">Check Out:</label>
      <input type="date" v-model="newBooking.check_out" required />

      <!-- Кнопка для отправки формы -->
      <button type="submit">Add Booking</button>
    </form>

    <!-- Отображение всех бронирований -->
    <div>
      <h3>All Bookings</h3>
      <ul>
        <li v-for="booking in bookings" :key="booking.id">
          <p>User: {{ getUserById(booking.user).first_name }} {{ getUserById(booking.user).last_name }}</p>
          <p>Room: {{ getRoomById(booking.room).number }} {{ getRoomById(booking.room).category }}</p>
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
      newBooking: {
        user: "",
        room: "",
        check_in: "",
        check_out: "",
      },
      users: [],
      rooms: [],
    };
  },
  methods: {
    // Вспомогательные методы для получения данных по id
    getUserById(userId) {
      return this.users.find(user => user.id === userId) || {};
    },
    getRoomById(roomId) {
      return this.rooms.find(room => room.id === roomId) || {};
    },
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
    async addNewBooking() {
      try {
        const isBookingConflict = await this.checkBookingConflict();

        if (isBookingConflict) {
          alert("This room is already booked for the selected period.");
          return;
        }

        const response = await this.$http.post(`http://127.0.0.1:8000/hotel/all_bookings/`, this.newBooking);

        // Очищаем поля ввода после успешного добавления
        this.newBooking = {
          user: "",
          room: "",
          check_in: "",
          check_out: "",
        };

        // Добавляем новое бронирование в массив
        this.bookings.push(response.data);
      } catch (error) {
        console.log(error);
      }
    },
    async checkBookingConflict() {
      const { room, check_in, check_out } = this.newBooking;

      try {
        const response = await this.$http.post(`http://127.0.0.1:8000/hotel/check_booking_conflict/`, {
          room,
          check_in,
          check_out,
        });

        return response.data.conflict;
      } catch (error) {
        console.log(error);
        return false;
      }
    },
    async loadUsersAndRooms() {
      try {
        const usersResponse = await this.$http.get(`http://127.0.0.1:8000/hotel/users/`);
        const roomsResponse = await this.$http.get(`http://127.0.0.1:8000/hotel/rooms/`);

        this.users = usersResponse.data;
        this.rooms = roomsResponse.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
  created() {
    this.loadBookings();
    this.loadUsersAndRooms();
  },
};
</script>



<style scoped>
.bookings_container {
  width: 100%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

h2, h3 {
  text-align: center;
}

form {
  width: 80%;
  max-width: 400px;
  margin: 0 auto;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
}

select, input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 3px;
}

button[type="submit"] {
  cursor: pointer;
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 3px;
  transition: background-color 0.3s;
}

button[type="submit"]:hover {
  background-color: #1e6ea9;
}

ul {
  list-style-type: none;
  padding: 0;
  width: 100%;
}

li {
  width: 80%;
  max-width: 400px;
  align: center;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  margin: 0 auto;
}

p {
  margin: 5px 0;
}

label {
  display: block;
  margin-bottom: 5px;
}

.checkbox-label {
  display: flex;
  align-items: center;
}

.checkbox-label input {
  margin-left: 5px;
}

</style>
