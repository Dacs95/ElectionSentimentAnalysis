// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader
import Vue from 'vue'
import App from './App'
import store from './store/index'
import router from './router'

import Vuetify from 'vuetify'
// import { Tweet, Moment, Timeline } from 'vue-tweet-embed'
import VueCharts from 'vue-chartjs'
import { Bar, Line } from 'vue-chartjs'


Vue.use(Vuetify)

Vue.config.productionTip = false
console.log(store)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store: store,
  components: { App },
  template: '<App/>'
})
