import Vue from 'vue'
import Vuex from 'vuex'
import api from './modules/api'
import tuits from './modules/tuits'
import tuitsAmlo from './modules/tuitsAmlo'


Vue.use(Vuex)

export default new Vuex.Store({
  modules:{
    api,
    tuits,
    tuitsAmlo
    }
})
