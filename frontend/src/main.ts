import './assets/main.css'

import { createApp } from 'vue';

import App from './App.vue';
import router from './router';
import axios from 'axios';

// Set up axios defaults
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000';


createApp(App)
  .use(router)
  .mount('#app');

