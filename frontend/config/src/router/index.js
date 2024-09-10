import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import UserLogin from '../views/UserLogin.vue';
import ProductList from '../views/ProductList.vue';
import ProductCreate from '../views/ProductCreate.vue';
import ProductEdit from '../views/ProductEdit.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'UserLogin',
    component: UserLogin,
  },
  {
    path: '/products',
    name: 'ProductList',
    component: ProductList,
  },
  {
    path: '/products/create',
    name: 'CreateProduct',
    component: ProductCreate,
  },
  {
    path: '/products/:id/edit',
    name: 'EditProduct',
    component: ProductEdit,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
