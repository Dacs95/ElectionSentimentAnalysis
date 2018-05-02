import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home/Home'
import Tuits from '@/components/Tuits/Tuits'
import TuitsAmlo from '@/components/TuitsAmlo/TuitsAmlo'
import TuitsAnaya from '@/components/TuitsAnaya/TuitsAnaya'
import TuitsBronco from '@/components/TuitsBronco/TuitsBronco'
import TuitsMeade from '@/components/TuitsMeade/TuitsMeade'
import TuitsAmloResp from '@/components/TuitsAmloResp/TuitsAmloResp'




Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/tuits',
      name: 'Tuits',
      component: Tuits
    },
    {
      path: '/tuitsAmlo',
      name: 'TuitsAmlo',
      component: TuitsAmlo
    },
    {
      path: '/tuitsAnaya',
      name: 'TuitsAnaya',
      component: TuitsAnaya
    },
    {
      path: '/tuitsBronco',
      name: 'TuitsBronco',
      component: TuitsBronco
    },
    {
      path: '/tuitsMeade',
      name: 'TuitsMeade',
      component: TuitsMeade
    },
    {
      path: '/tuitsAmloResp',
      name: 'TuitsAmloResp',
      component: TuitsAmloResp
    }
  ]
})
