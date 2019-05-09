import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from './router';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    loggingIn: false,
    register: false,
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
    updateUserUsername: (state, username) => {
      state.username = username;
    },
    updateUserAvatar: (state, userAvatar) => {
      state.userAvatar = userAvatar;
    },
    logout: (state) => {
      state.accessToken = null;
      state.username = null;
      state.userAvatar = null;
      state.loginError = null;
    }
  },
  actions: {
    //logowanie
    doLogin({ commit }, loginData) {
      commit('loginStart');

      axios.post('http://127.0.0.1:8000/api/auth/login', {
        ...loginData
      })
      .then(response => {
        localStorage.setItem('accessToken', response.data.token);
        localStorage.setItem('username', response.data.user.username);
        localStorage.setItem('userAvatar', response.data.user.profil.avatar);
        commit('loginStop', null);
        commit('updateAccessToken', response.data.token);
        commit('updateUserUsername', response.data.user.username);  
        commit('updateUserAvatar', response.data.user.profil.avatar);
        router.push('/home');
      })
      .catch(error => {
      commit('loginStop', "Nie udało się zalogować!");
      if(accessToken !== null) {
        commit('loginStop', "Nie udało się zalogować!");
        commit('updateAccessToken', null);
        commit('updateUserUsername', null);
        commit('updateUserAvatar', null);
      };
      })
    },
    //rejestracja
    doRegister({ commit }, registerData) {
      commit('loginStart');

      axios.post('http://127.0.0.1:8000/api/auth/register', {
        ...registerData
      })
      .then(response => {
        localStorage.setItem('accessToken', response.data.token);
        localStorage.setItem('username', response.data.user.username);
        localStorage.setItem('userAvatar', response.data.user.profil.avatar);
        commit('loginStop', null);
        commit('updateAccessToken', response.data.token);
        commit('updateUserUsername', response.data.user.username);  
        commit('updateUserAvatar', response.data.user.profil.avatar);
        router.push('/home');
      })
      .catch(error => {
        commit('loginStop', "Nie udało się zalogować!");
        commit('updateAccessToken', null);
        commit('updateUserUsername', null);
        commit('updateUserAvatar', null);
      })
    },
    fetchAccessToken({ commit }) {
      commit('updateAccessToken', localStorage.getItem('accessToken'));
    },
    fetchUserUsername({ commit }) {
      commit('updateUserUsername', localStorage.getItem('username'));
    },
    fetchUserAvatar({ commit }) {
      commit('updateUserAvatar', localStorage.getItem('userAvatar'));
    },
    logout( { commit }) {
      localStorage.removeItem('accessToken');
      localStorage.removeItem('username');
      localStorage.removeItem('userAvatar');
      commit('logout');
      router.push('/posts');
    }
  }
})




