<template>
  <div class="quarterly-report">
    <h2>Generate Quarterly Report</h2>
    <form @submit.prevent="generateReport">
      <label for="quarter">Select Quarter:</label>
      <select v-model="selectedQuarter" required>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
      </select>

      <label for="year">Enter Year:</label>
      <input type="number" v-model="selectedYear" required />

      <button type="submit">Generate Report</button>
    </form>

    <!-- Отображение результатов -->
    <div v-if="reportData">
      <h3>Quarterly Report</h3>

      <!-- Отображение room_client_reports -->
      <div v-if="reportData.room_client_reports.length > 0">
        <h4>Room Client Reports</h4>
        <ul>
          <li v-for="(report, index) in reportData.room_client_reports" :key="index">
            Room {{ report.room__number }}: {{ report.num_clients }} clients
          </li>
        </ul>
      </div>

      <!-- Отображение floor_reports -->
      <div v-if="reportData.floor_reports.length > 0">
        <h4>Floor Reports</h4>
        <ul>
          <li v-for="(report, index) in reportData.floor_reports" :key="index">
            Floor {{ report.floor }}: {{ report.num_rooms }} rooms
          </li>
        </ul>
      </div>

      <!-- Отображение total_income_for_room -->
      <div v-if="reportData.total_income_for_room.length > 0">
        <h4>Total Income for Each Room</h4>
        <ul>
          <li v-for="(report, index) in reportData.total_income_for_room" :key="index">
            Room {{ report.room__number }}: {{ report.total_income_for_room }}
          </li>
        </ul>
      </div>

      <!-- Отображение total_income_for_hotel -->
      <div v-if="reportData.total_income_for_hotel !== null">
        <h4>Total Income for Hotel</h4>
        <p>{{ reportData.total_income_for_hotel }}</p>
      </div>
    </div>
    <div v-else>
      <p>No report generated yet.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedQuarter: '',
      selectedYear: '',
      reportData: null,
    };
  },
  methods: {
    async generateReport() {
      try {
        const response = await this.$http.get(`http://127.0.0.1:8000/hotel/quarterly_report/${this.selectedQuarter}/${this.selectedYear}/`);
        this.reportData = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
.quarterly-report {
  width: 80%;
  margin: 0 auto;
  text-align: center;
}

.quarterly-report form {
  margin-bottom: 20px;
}

.quarterly-report label {
  display: block;
  margin-bottom: 5px;
}

.quarterly-report select,
.quarterly-report input {
  width: calc(100% - 12px);
  padding: 8px;
  margin-bottom: 10px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.quarterly-report button[type="submit"] {
  cursor: pointer;
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 3px;
  transition: background-color 0.3s;
}

.quarterly-report button[type="submit"]:hover {
  background-color: #1e6ea9;
}

.quarterly-report h3,
.quarterly-report h4 {
  margin-top: 20px;
}
</style>