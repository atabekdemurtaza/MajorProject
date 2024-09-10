<template>
  <div class="product-edit">
    <h1>Edit Product</h1>
    <form @submit.prevent="updateProduct">
      <label for="name">Name:</label>
      <input v-model="name" type="text" required />

      <label for="description">Description:</label>
      <textarea v-model="description" required></textarea>

      <label for="price">Price:</label>
      <input v-model="price" type="number" step="0.01" required />

      <button type="submit">Update Product</button>
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
  created() {
    this.fetchProduct();
  },
  methods: {
    async fetchProduct() {
      const productId = this.$route.params.id;
      try {
        const response = await axios.get(`http://localhost:8000/api/products/${productId}/`);
        this.name = response.data.name;
        this.description = response.data.description;
        this.price = response.data.price;
      } catch (error) {
        console.error('Error fetching product:', error);
      }
    },
    async updateProduct() {
      const productId = this.$route.params.id;
      try {
        await axios.put(`http://localhost:8000/api/products/${productId}/`, {
          name: this.name,
          description: this.description,
          price: this.price,
        });
        this.$router.push('/products');
      } catch (error) {
        console.error('Error updating product:', error);
        this.error = 'Failed to update product. Please try again.';
      }
    },
  },
};
</script>

<style scoped>
.product-edit {
  padding: 20px;
}

input,
textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
}
</style>
