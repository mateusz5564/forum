import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from './router';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    loggingIn: false,
    loginError: null,
    username: null,
    userAvatar: null,
  },
  mutations: {
    loginStart: state => state.loggingIn = true,
    loginStop: (state, errorMessage) => {
      state.loggingIn = false;
      state.loginError = errorMessage;
    },
    updateAccessToken: (state, accessToken) => {
      state.accessToken = accessToken;
    },
    updateUserDetails: (state, username) => {
      state.username = username;
      // state.userAvatar = userAvatar;
    },
    logout: (state) => {
      state.accessToken = null;
      state.username = null;
    }
  },
  actions: {
    doLogin({ commit }, loginData) {
      commit('loginStart');

      axios.post('http://127.0.0.1:8000/api/auth/login', {
        ...loginData
      })
      .then(response => {
        localStorage.setItem('accessToken', response.data.token);
        localStorage.setItem('username', response.data.user.username);
        commit('loginStop', null);
        commit('updateAccessToken', response.data.token);
        commit('updateUserDetails', response.data.user.username, null);  //trzeba dodać avatar do API
        router.push('/home');
      })
      .catch(error => {
        commit('loginStop', error.response.data.error);
        commit('updateAccessToken', null);
      })
    },
    fetchAccessToken({ commit }) {
      commit('updateAccessToken', localStorage.getItem('accessToken'));
    },
    fetchUserDetails({ commit }) {
      commit('updateUserDetails', localStorage.getItem('username'));
    },
    logout( { commit }) {
      localStorage.removeItem('accessToken');
      localStorage.removeItem('username');
      commit('logout');
      router.push('/posts');
    }
  }
})




