import axios from 'axios'
import router from '../../router'
let apiTuit = 'http://192.168.1.78:8080/api'
const getters = {}

const actions = {
  getAllTuits({commit}, candId){
    return axios.get(`${apiTuit}/toptweets/${candId}`).then((res) =>{
      return res.data
    })
  },
  getAllTuitsResp({commit}, candId){
    return axios.get(`${apiTuit}/topuserstweets/${candId}`).then((res) =>{
      return res.data
    })
  }
}


export default {
  getters,
  actions,
}
