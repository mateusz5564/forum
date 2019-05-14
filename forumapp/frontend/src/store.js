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
    registerError: null,
    username: null,
    userId: null,
    userAvatar: null,
  },
  mutations: {
    loginStart: state => state.loggingIn = true,
    loginStop: (state, errorMessage) => {
      state.loggingIn = false;
      state.loginError = errorMessage;
    },
    registerStop: (state, errorMessage) => {
      state.registerError = errorMessage;
    },
    updateAccessToken: (state, accessToken) => {
      state.accessToken = accessToken;
    },
    updateUserUsername: (state, username) => {
      state.username = username;
    },
    updateUserId: (state, userId) => {
      state.userId = userId;
    },
    updateUserAvatar: (state, userAvatar) => {
      state.userAvatar = userAvatar;
    },
    logout: (state) => {
      state.accessToken = null;
      state.username = null;
      state.userId = null;
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
        localStorage.setItem('userId', response.data.user.id);
        localStorage.setItem('userAvatar', response.data.user.profil.avatar);
        commit('loginStop', null);
        commit('updateAccessToken', response.data.token);
        commit('updateUserUsername', response.data.user.username);  
        commit('updateUserId', response.data.user.id);
        commit('updateUserAvatar', response.data.user.profil.avatar);
        router.push('/home');
      })
      .catch(error => {
      commit('loginStop', "Nie udało się zalogować!");
      if(accessToken !== null) {
        commit('loginStop', "Nie udało się zalogować!");
        commit('updateAccessToken', null);
        commit('updateUserUsername', null);
        commit('updateUserId', null);
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
        localStorage.setItem('userId', response.data.user.id);
        localStorage.setItem('userAvatar', response.data.user.profil.avatar);
        commit('registerStop', null);
        commit('loginStop', null);
        commit('updateAccessToken', response.data.token);
        commit('updateUserUsername', response.data.user.username); 
        commit('updateUserId', response.data.user.id); 
        commit('updateUserAvatar', response.data.user.profil.avatar);
        router.push('/home');
      })
      .catch(error => {
        commit('registerStop', "Nie udało się zarejestrować!");
        commit('loginStop', "Nie udało się zalogować!");
        commit('updateAccessToken', null);
        commit('updateUserUsername', null);
        commit('updateUserId', null);
        commit('updateUserAvatar', null);
      })
    },
    fetchAccessToken({ commit }) {
      commit('updateAccessToken', localStorage.getItem('accessToken'));
    },
    fetchUserUsername({ commit }) {
      commit('updateUserUsername', localStorage.getItem('username'));
    },
    fetchUserId({ commit }) {
      commit('updateUserId', localStorage.getItem('userId'));
    },
    fetchUserAvatar({ commit }) {
      commit('updateUserAvatar', localStorage.getItem('userAvatar'));
    },
    logout( { commit }) {
      localStorage.removeItem('accessToken');
      localStorage.removeItem('username');
      localStorage.removeItem('userId');
      localStorage.removeItem('userAvatar');
      commit('logout');
      router.push('/login');
    }
  }
})




