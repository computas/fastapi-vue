<template>
    <div>
      <input v-model="person.name" type="text" placeholder="Enter Name">
      <input v-model="person.age" type="number" placeholder="Enter Age">
      <input v-model="person.gender" type="text" placeholder="Enter Gender">
      <button @click="savePerson">Save Person</button>
    </div>
  </template>
  
  <script lang="ts">
  import { ref } from 'vue';
  import axios from 'axios';
  
  export default {
    setup() {
      const person = ref({
        name: '',
        age: '',
        gender: '',
      });
  
      const savePerson = () => {
        axios.post('/people', person.value);
        
        person.value = {
          name: '',
          age: '',
          gender: '',
        };
      };
  
      return {
        person,
        savePerson,
      };
    },
  };
  </script>
  