<template>
    <div class="rooms_container">
        <div class="rooms_content">
            <h1>Rooms</h1>
            <ul class="room_list">
                <li v-for="room in rooms" :key="room.id">
                    <h2>Number: {{ room.number }}</h2>
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
            rooms: ['']
        };
    },
    methods: {
        async getData() {
            try {
                const response = await this.$http.get('http://127.0.0.1:8000/hotel/all_rooms/');
                console.log("API Response:", response.data);
                this.rooms = response.data;
            } catch (error) {
                console.error("Error fetching room data:", error.message);
            }
        },
        async deleteRoom(room) {
            try {
                // Implement the logic to delete a room
                await this.$http.delete(`http://127.0.0.1:8000/hotel/all_rooms/${room.id}/`);
                // Refresh room data after deletion
                this.getData();
            } catch (error) {
                console.error("Error deleting room:", error.message);
            }
        },
    },
    mounted() {
        this.getData();
    }
};
</script>
