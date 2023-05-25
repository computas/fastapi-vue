<template>
  <div>
    <input v-model="person.id" type="text" placeholder="Enter ID">
    <input v-model="person.name" type="text" placeholder="Enter Name">
    <input v-model="person.age" type="number" placeholder="Enter Age">
    <input v-model="person.gender" type="text" placeholder="Enter Gender">
    <button @click="updatePerson">Update Person</button>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const person = ref({
      id: '',
      name: '',
      age: '',
      gender: '',
    });

    const updatePerson = () => {
      if (person.value.id)
        axios.put(`/people/${person.value.id}`, person.value);
    
      person.value = {
        id: '',
        name: '',
        age: '',
        gender: '',
      };
    };

    return {
      person,
      updatePerson,
    };
  },
};
</script>
