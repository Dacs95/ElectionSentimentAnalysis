import Vue from 'vue'
import Vuex from 'vuex'
import api from './modules/api'
import tuits from './modules/tuits'

Vue.use(Vuex)

export default new Vuex.Store({
  modules:{
    api,
    tuits
    }
})
