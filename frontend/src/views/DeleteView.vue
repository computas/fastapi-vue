<template>
    <div>
      <input v-model="id" type="text" placeholder="Enter ID">
      <button @click="deletePerson">Delete Person</button>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script lang="ts">
  import { ref } from 'vue';
  import axios from 'axios';
  
  export default {
    setup() {
      const id = ref('');
      const message = ref('');
  
      const deletePerson = async () => {
        if (id.value) {
          await axios.delete(`/people/${id.value}`);
          message.value = 'Person deleted successfully.';
          id.value = '';
        } else {
          message.value = 'Please enter an ID.';
        }
      };
  
      return {
        id,
        deletePerson,
        message,
      };
    },
  };
  </script>
  