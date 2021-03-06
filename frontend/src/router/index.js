import Vue from 'vue'
import Router from 'vue-router'
import MapComponent from '../components/MapComponent'
import HomeComponent from '../components/HomeComponent'
import AnalysisComponent from '../components/AnalysisComponent'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HomeComponent',
      component: HomeComponent
    },
    {
      path: '/map',
      name: 'MapComponent',
      component: MapComponent
    },
    {
      path: '/analysis',
      name: 'AnalysisComponent',
      component: AnalysisComponent
    }
  ]
})
