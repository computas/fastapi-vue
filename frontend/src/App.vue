<template>
  <div id="app">
    <header>
      <nav>
        <router-link to="/people">People View</router-link> |
        <router-link to="/add">Add View</router-link> |
        <router-link to="/update">Update View</router-link> |
        <router-link to="/delete">Delete View</router-link>
      </nav>
    </header>
    <main>
      <router-view/>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
});
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.main {
  padding-top: 1em;
}

</style>
