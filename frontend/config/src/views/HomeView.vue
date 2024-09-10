<template>
  <div id="home">
    <h1>Get Product Recommendations</h1>
    <input v-model="reviewText" placeholder="Enter your review..." />
    <button @click="getRecommendation">Get Recommendation</button>
    <div v-if="recommendation" :class="['notification', notificationColor]">
      Recommended Rating: {{ recommendation }}
    </div>
    <p v-if="apiError" style="color: red">{{ apiError }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      reviewText: '',
      recommendation: null,
      apiError: null,
    };
  },
  computed: {
    notificationColor() {
      if (this.recommendation <= 2) {
        return 'red';
      } else if (this.recommendation <= 4) {
        return 'yellow';
      } else {
        return 'green';
      }
    }
  },
  methods: {
    async getRecommendation() {
      try {
        const response = await axios.get(`http://localhost:8000/recommendations/1/?features=${encodeURIComponent(this.reviewText)}`);

        if (response.data && response.data.prediction !== undefined) {
          this.recommendation = response.data.prediction;
          this.apiError = null;
        } else {
          throw new Error('Prediction not found in response');
        }
      } catch (error) {
        this.apiError = 'Error fetching recommendation. Please try again.';
        this.recommendation = null;
      }
    },
  },
};
</script>

<style src="@/assets/styles/home.css"></style>
