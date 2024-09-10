<template>
  <div class="register">
    <form @submit.prevent="register">
      <label for="username">Username:</label>
      <input v-model="username" type="text" required />

      <label for="email">Email:</label>
      <input v-model="email" type="email" required />

      <label for="password">Password:</label>
      <input v-model="password" type="password" required />

      <label for="password2">Confirm Password:</label>
      <input v-model="password2" type="password" required />

      <button type="submit">Register</button>

      <p v-if="error" style="color: red;">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios'; // Используем axios для запросов

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      password2: '',
      error: null, // Добавляем поле для обработки ошибок
    };
  },
  methods: {
    async register() {
      if (this.password !== this.password2) {
        this.error = 'Passwords do not match.';
        return;
      }

      try {
        const response = await axios.post('http://localhost:8000/api/auth/register/', {
          username: this.username,
          email: this.email,
          password: this.password,
        });

        console.log('Register response:', response);

        if (response.data && response.data.access) {
          // Сохраняем токен и перенаправляем пользователя
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);

          this.$router.push('/');
        } else {
          throw new Error('Invalid registration response');
        }
      } catch (error) {
        console.error('Register error:', error);
        this.error = 'Registration failed. Please try again.';
      }
    },
  },
};
</script>

<style src="@/assets/styles/register.css"></style>
