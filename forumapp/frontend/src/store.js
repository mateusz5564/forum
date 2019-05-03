import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accessToken: null,
    loggignIn: false,
    loginError: null,
  },
  mutations: {
    loginStart: state => state.loggingIn = true,
    loginStop: (state, errorMessage) => {
      state.loggignIn = false;
      state.loginError = errorMessage;
    },
    updateAccessToken: (state, accessToken) => {
      state.accessToken = accessToken;
    }
  },
  actions: {
    doLogin({ commit }, loginData) {
      commit('loginStart');

      axios.post('http://127.0.0.1:8000/api/auth/login', {
        ...loginData
      })
      .then(response => {
        console.log(response);
        localStorage.setItem('accessToken', response.data.token);
        commit('loginStop', null);
        commit('updateAccessToken', response.data.token);
      })
      .catch(error => {
        commit('loginStop', error.response.data.error);
        commit('updateAccessToken', null);
      })
    },
    fetchAccessToken({ commit }) {
      commit('updateAccessToken', localStorage.getItem('accessToken'));
    }
  }
})
