<template>
<el-container style="height: 780px; border: 1px solid #eee">
  <div  class="left-silder">
  <my-slider></my-slider>
  </div>

  <div  class="right-main">
    <my-header> </my-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </div>

</el-container>

</template>
<style>
  .el-container{
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    overflow: hidden;
    display: flex;
    .left-silder{
      width: auto;
    }
  }
  .right-main{
    flex: 1;
    position: relative;

  }
  .el-main{
    height: 100;
    overflow-y: auto;
    padding: 0px;
  }

</style>

<script>
  import  MyHeader from '@/components/layout/header';
  import MySlider from "../components/layout/slider";
  export default {
    components: {MySlider,MyHeader},
    data() {
      const item = {
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      };
      return {
        tableData: Array(12).fill(item)
      }
    },
    comments:{
      MyHeader,MySlider
    }
  };
</script>
