import { createRouter, createWebHistory } from 'vue-router';
import PeopleView from '../views/PeopleView.vue';
import AddView from '../views/AddView.vue';
import UpdateView from '../views/UpdateView.vue';
import DeleteView from '../views/DeleteView.vue';

const routes = [
  {
    path: '/people',
    name: 'PeopleView',
    component: PeopleView,
  },
  {
    path: '/add',
    name: 'AddView',
    component: AddView,
  },
  {
    path: '/update',
    name: 'UpdateView',
    component: UpdateView,
  },
  {
    path: '/delete',
    name: 'DeleteView',
    component: DeleteView,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
