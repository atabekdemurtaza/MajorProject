<template>
  <div class="login">
    <form @submit.prevent="login">
      <label for="email">Email:</label>
      <input v-model="email" type="email" required />

      <label for="password">Password:</label>
      <input v-model="password" type="password" required />

      <button type="submit">Login</button>

      <p v-if="error" style="color: red;">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8000/api/auth/login/', {
          email: this.email,
          password: this.password,
        });

        if (response.data && response.data.access) {
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);
          localStorage.setItem('username', response.data.user.username);

          // Перенаправляем на домашнюю страницу
          this.$router.push('/');
        } else {
          throw new Error('Invalid login response');
        }
      } catch (error) {
        console.error('Login error:', error);
        this.error = 'Login failed. Please check your email and password.';
      }
    },
  },
};
</script>

<style src="@/assets/styles/login.css"></style>
