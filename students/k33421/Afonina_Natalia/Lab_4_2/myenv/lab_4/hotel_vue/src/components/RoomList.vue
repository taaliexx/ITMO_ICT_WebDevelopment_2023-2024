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

          <button type="submit">   Add Room</button>
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

<style scoped>
.rooms_container {
  width: 80%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

.rooms_content {
  text-align: center;
  width: 100%;
}

.add_room form {
  width: 80%;
  max-width: 400px; /* Ограничиваем максимальную ширину формы */
  margin: 0 auto; /* Центрируем форму в родительском контейнере */
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 20px;
}

.add_room label {
  display: block;
  margin-bottom: 5px;
}

.add_room select,
.add_room input {
  width: 100%; /* Занимает всю ширину доступного пространства */
  padding: 8px;
  margin-bottom: 10px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.add_room button[type="submit"] {
  cursor: pointer;
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 3px;
  transition: background-color 0.3s;
}

.add_room button[type="submit"]:hover {
  background-color: #1e6ea9;
}

.room_list {
  list-style-type: none;
  padding: 0;
  width: 100%;
}

.room_list li {
  width: 80%;
  max-width: 400px; /* Ограничиваем максимальную ширину списка комнат */
  align: center;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  margin: 0 auto; /* Центрируем элемент списка в родительском контейнере */
}

.room_list button {
  cursor: pointer;
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 5px 10px;
  border-radius: 3px;
  transition: background-color 0.3s;
}

.room_list button:hover {
  background-color: #1e6ea9;
}

.room_list p {
  margin: 5px 0;
}

.room_list h2 {
  margin-bottom: 10px;
}

.room_list div {
  margin-top: 20px;
}
</style>
