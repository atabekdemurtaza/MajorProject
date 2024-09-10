<template>
  <div class="product-create">
    <h1>Create New Product</h1>
    <form @submit.prevent="createProduct">
      <label for="name">Name:</label>
      <input v-model="name" type="text" required />

      <label for="description">Description:</label>
      <textarea v-model="description" required></textarea>

      <label for="price">Price:</label>
      <input v-model="price" type="number" step="0.01" required />

      <button type="submit">Create Product</button>
      <p v-if="error" style="color: red;">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      description: '',
      price: '',
      error: null,
    };
  },
  methods: {
    async createProduct() {
      try {
        await axios.post('http://localhost:8000/api/products/', {
          name: this.name,
          description: this.description,
          price: this.price
        });
        this.$router.push('/products');  // После успешного создания перенаправляем на список продуктов
      } catch (error) {
        console.error('Error creating product:', error);
        this.error = 'Error creating product. Please try again.';
      }
    }
  },
};
</script>

<style scoped>
.product-create {
  padding: 20px;
}

input,
textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
}

button {
  background-color: #28a745;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}

button:hover {
  background-color: #218838;
}

h1 {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}
</style>
