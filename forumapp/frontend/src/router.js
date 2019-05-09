import Vue from 'vue';
import Router from 'vue-router';
import { directives } from 'vuetify/lib';
import Home from './views/Home.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '*',
      name: 'home',
      component: () => import('./views/Posts.vue')
    },
    {
      path: '/posts',
      name: 'posts',
      component: () => import('./views/Posts.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./components/Login.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('./components/Register.vue')
    },
    {
      path: '/profile',
      nane: 'profile',
      component: () => import('./views/Profile.vue')
    }
  ],
});

