<template>
  <div class="rooms_container">
    <div class="rooms_content">
      <h1>Rooms</h1>

      <!-- Форма для добавления новой комнаты -->
      <div class="add_room">
        <h2>Add a New Room</h2>
        <form @submit.prevent="addRoom">
          <label for="number">Number:</label>
          <input type="text" v-model="newRoom.number" required />

          <label for="category">Category:</label>
          <select v-model="newRoom.category" required>
            <option value="SINGLE">Single Room</option>
            <option value="DOUBLE">Double Room</option>
            <option value="TRIPLE">Triple Room</option>
          </select>

          <label for="cost">Cost:</label>
          <input type="text" v-model="newRoom.cost" required />

          <label for="phone">Phone:</label>
          <input type="text" v-model="newRoom.phone" required />

          <label for="floor">Floor:</label>
          <!-- Используйте элемент select для выбора этажа -->
          <select v-model="newRoom.floor" required>
            <option v-for="floor in availableFloors" :key="floor.id" :value="floor.id">{{ floor.floor }}</option>
          </select>

          <button type="submit">Add Room</button>
        </form>
      </div>

      <!-- Список комнат -->
      <ul class="room_list">
        <li v-for="room in rooms" :key="room.id">
          <h2>{{ room.number }}</h2>
          <p>Category: {{ room.category }}</p>
          <p>Cost: {{ room.cost }}</p>
          <p>Phone: {{ room.phone }}</p>
          <p>Floor: {{ room.floor }}</p>
          <button @click="deleteRoom(room)">Delete</button>
        </li>
      </ul>
      <div v-if="rooms.length === 0">No rooms available.</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rooms: [],
      newRoom: {
        number: "",
        category: "",
        cost: "",
        phone: "",
        floor: null,
      },
      availableFloors: [],
    };
  },
  methods: {
    async getData() {
      try {
        const responseFloors = await this.$http.get('http://127.0.0.1:8000/hotel/floors/');
        this.availableFloors = responseFloors.data;

        const responseRooms = await this.$http.get('http://127.0.0.1:8000/hotel/rooms/');
        this.rooms = responseRooms.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async addRoom() {
      try {
        const response = await this.$http.post('http://127.0.0.1:8000/hotel/rooms/', {
          ...this.newRoom,
        });

        this.rooms.push(response.data);
        this.newRoom = {
          number: "",
          category: "",
          cost: "",
          phone: "",
          floor: null,
        };
      } catch (error) {
        console.error('Error adding room:', error);
      }
    },
    async deleteRoom(room) {
      let confirmation = confirm("Do you want to delete this room?");

      if (confirmation) {
        try {
          await this.$http.delete(`http://127.0.0.1:8000/hotel/rooms/${room.id}`);

          this.getData();
        } catch (error) {
          console.error('Error deleting room:', error);
        }
      }
    },
  },
  created() {
    this.getData();
  },
};
</script>