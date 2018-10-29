import Vue from 'vue'
import Router from 'vue-router'
import   baseinfo  from  '@/views/common/baseinfo'
import   servercategory from '@/views/setting/servercategory'
import   goodList from   '@/views/servers/goods-list'
import   server_category from  '@/views/setting/server_category'
import  probleminfo  from '@/views/servermg/probleminfo'
import  serverlist from '@/views/servermg/serverlist'
import   addproblem  from  '@/views/servermg/addproblem'
import   idcinfo   from  '@/views/setting/idcinfo'


export  default [
    {
      path: '/setting',
      name: 'setting',
      redirect: '/setting/',
      meta:{
        name:'基础管理',
        auth:false,
        icon:'el-icon-menu',
      },
      component:baseinfo,
      children:[
        {
          path: '/setting/category',
          name: 'category',
          meta: {
            name: '机型管理',
            auth: false,
            icon: 'el-icon-edit-outline',
          },
          component: servercategory,
         },{
          path: '/setting/apps',
          name: 'server_category',
          meta: {
            name: '应用管理',
            auth: false,
            icon: 'el-icon-edit-outline',
          },
          component: server_category,
        },
        {
          path: '/setting/idcroom',
          name: 'room',
          meta: {
            name: '机房管理',
            auth: false,
            icon: 'el-icon-edit-outline',
          },
          component: idcinfo,
         },
          ]
        },
        {
          path:'/servers',
          name:'servers',
          meta:{
            name: '主机管理',
            auth: false,
            icon: 'el-icon-message',
          },
          component:baseinfo,
          children:[
            {
              path: '/servers/list',
              name: 'goodlist',
              meta: {
                name: '主机管理',
                auth: false,
                icon: 'el-icon-tickets',
              },
              component: goodList,
            }
          ]
        },
  {
    path:'/servers',
    name:'servers',
    meta:{
      name: '故障管理',
      auth: false,
      icon: 'el-icon-message',
    },
    component:baseinfo,
    children:[
      {
        path: '/servers/probleminfo',
        name: 'probleminfo',
        meta: {
          name: '故障类型',
          auth: false,
          icon: 'el-icon-tickets',
        },
        component: probleminfo,
      },
      {
        path: '/servers/serverlist',
        name: 'serverlist',
        hidden: true,
        meta: {
          name: '故障记录',
          auth: false,
          icon: 'el-icon-tickets',

        },
        component: serverlist,
      },

    ]
  },

  ]




