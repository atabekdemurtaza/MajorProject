<template>
  <nav class="navbar">
    <a class="navbar-brand" href="#">Recommender System</a>
    <ul>
      <li><router-link to="/" active-class="active">Home</router-link></li>
      <li v-if="!isAuthenticated"><router-link to="/login" active-class="active">Login</router-link></li>
      <li v-if="!isAuthenticated"><router-link to="/register" active-class="active">Register</router-link></li>
      <li v-if="isAuthenticated"><button @click="logout">Logout</button></li>
    </ul>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      isAuthenticated: !!localStorage.getItem('access_token'),
    };
  },
  methods: {
    logout() {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      localStorage.removeItem('username');
      this.isAuthenticated = false;
      this.$router.push('/login');
    }
  }
};
</script>

<style src="@/assets/styles/navbar.css"></style>
