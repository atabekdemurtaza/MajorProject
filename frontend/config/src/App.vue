<template>
  <div id="app">
    <MainNavbar />
    <router-view />
  </div>
</template>

<script>
import MainNavbar from './components/MainNavbar.vue';

export default {
  components: {
    MainNavbar,
  },
};
</script>
