<template>
  <div>
    <input v-model="id" type="text" placeholder="Enter ID">
    <button @click="getPeople">Get People</button>
    <div v-if="people.length">
      <div v-for="person in people" :key="person._id">
        <p>ID: {{ person._id }}</p>
        <p>Name: {{ person.name }}</p>
        <p>Age: {{ person.age }}</p>
        <p>Gender: {{ person.gender }}</p>
      </div>
    </div>
    <div v-else>
      <p>No people found.</p>
    </div>
  </div>
</template>


<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const id = ref('');
    const people = ref<Array<{_id: string, name: string, age: number, gender: string}>>([]);

    const getPeople = async () => {
      let response;
      if (id.value) {
        response = await axios.get(`/people/${id.value}`);
        people.value = [response.data];
      } else {
        response = await axios.get('/people');
        people.value = response.data;
        console.log(response.data);
        
      }
    };

    return {
      id,
      people,
      getPeople,
    };
  },
};
</script>
