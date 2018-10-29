<template>
  <el-carousel indicator-position="outside" >
    <el-carousel-item v-for="item in images"><img v-bind:src="item.message">
    </el-carousel-item>
  </el-carousel>
</template>

<script>
	export default {
    name: "resetpasswd",
    data() {
      return {
        images: [
          {message: 'http://t2.hddhhn.com/uploads/tu/201707/9999/f608e5f329.jpg'},
          {message: 'http://t2.hddhhn.com/uploads/tu/201611/198/zorfiz0wta1.jpg'},
          {message: 'http://t2.hddhhn.com/uploads/tu/201611/198/zlez3axuowt.jpg'},
        ]
      }
    }
  }
</script>

<style >
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    width: 100%;
    padding: 0px;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
