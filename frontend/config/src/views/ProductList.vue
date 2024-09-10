<template>
  <div class="product-list">
    <h1>Products</h1>
    <div v-if="products.length">
      <ul>
        <li v-for="product in products" :key="product.id">
          <h3>{{ product.name }}</h3>
          <p>{{ product.description }}</p>
          <p>Price: ${{ product.price }}</p>
          <button @click="editProduct(product)">Edit</button>
          <button @click="deleteProduct(product.id)">Delete</button>
        </li>
      </ul>
    </div>
    <p v-else>No products available.</p>
    <button @click="createProduct">Add New Product</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      products: [],
    };
  },
  created() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('http://localhost:8000/api/products/');
        this.products = response.data;
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    },
    editProduct(product) {
      this.$router.push({ name: 'EditProduct', params: { id: product.id } });
    },
    async deleteProduct(productId) {
      try {
        await axios.delete(`http://localhost:8000/api/products/${productId}/`);
        this.fetchProducts(); // Обновляем список после удаления
      } catch (error) {
        console.error('Error deleting product:', error);
      }
    },
    createProduct() {
      this.$router.push({ name: 'CreateProduct' });
    },
  },
};
</script>

<style scoped>
.product-list {
  padding: 20px;
}

h3 {
  margin: 0;
}

button {
  margin-right: 10px;
}
</style>
