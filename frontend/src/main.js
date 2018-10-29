// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui';
import   "element-ui/lib/theme-chalk/index.css";
import   Axios  from "axios"
import store from 'store'
import VueRouter from 'vue-router'


Vue.use(VueRouter)



Vue.use(ElementUI);
Vue.prototype.$axios = Axios; //生成axios对象
Vue.config.productionTip = false

//axios.defaults.baseURL = 'https://127.0.0.1:8000/api/';
/*Axios.defaults.headers.common['Authorization'] = res.headers.authorization*/

Axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
