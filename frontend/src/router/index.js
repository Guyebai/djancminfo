import Vue from 'vue'
import Router from 'vue-router'
import   sliderpath  from './silderPath.js'
import  home  from '@/views/home'
Vue.use(Router)

export const constantRouterMap = [
  {
    path: '/404',
    component: () => import('@/views/errorPage/404'),
    hidden: true
  },
  {
    path: '/401',
    component: () => import('@/views/errorPage/401'),
    hidden: true
  },
]

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      redirect: '/servers/probleminfo',
      meta:{
        name:'首页',
        auth:false
      },
      component: home,
      children:sliderpath
      }
    ]
})




