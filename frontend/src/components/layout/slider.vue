<template>


  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-row :gutter="20">
      <el-col :span="24" ><div class="grid-content web-logo" >
        <img src="../../assets/404_images/logo.png" class="image-style" >
      </div></el-col>
    </el-row>

    <el-menu unique-opened   router
             class="el-menu-vertical-demo"
             @open="handleOpen"
             @close="handleClose"
             background-color="#545c64"
             text-color="#fff"
             active-text-color="#ffd04b">
      <div  v-for="(route,index) in Routers">
      <el-submenu  :key="index" :index="route.path">
        <template slot="title"><i class="el-icon-message"></i>{{route.meta.name}}</template>
        <el-menu-item v-for="(cRoute,cIndex) in route.children" :key="cIndex" :index="cRoute.path" :router="cRoute.name">{{cRoute.meta.name}}

        </el-menu-item>

      </el-submenu>
      </div>
    </el-menu>
  </el-aside>
</template>

<script>
  import  sliderpath   from '@/router/silderPath.js'
	export default {
		data(){
		  return{
		    Routers: sliderpath
      }
    }
	}
</script>

<style>
  .el-aside {
    height: 100%;
    color: #333;
    overflow-y:auto;
  }

  .web-logo{
    color: #2c3e50;
    background: #545c64;
    width: 199px;

  }
  .image-style{
    width: 65px;
    height: 65px;
    margin-top: 10px;
  }

</style>
