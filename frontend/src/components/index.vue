<template>
  <el-container>
    <el-header  >
      <el-row>
        <el-col :span="4"><div class="grid-content bg-purple-dark"><i class="el-icon-menu"></i>CMDB故障管理</div></el-col>
        <el-col :span="8"><div class="grid-content bg-purple-dark">
          <el-input
            placeholder="请输入搜索内容！"
            v-model="input10"
            clearable>
          </el-input>
         </div>
        </el-col>
        <el-col :span="8"><div class="grid-content bg-purple-dark"> &nbsp;


        </div></el-col>
        <el-col :span="4"><div class="grid-content bg-purple-dark">

          <el-button type="text" size="small">登录</el-button>
          <el-button type="text" size="small">注册</el-button>
        </div>
        </el-col>
      </el-row>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <hostinfo></hostinfo>
        <router-view>
        </router-view>
      </el-aside>
      <el-container>
        <el-main >


        </el-main>
        <el-footer height="120px">@同普科技</el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
	import Tableselect from "./Tableselect";
  import Menu from "./Menucores";
  import Hostinfo from "./Hostinfo";
  import HelloWorld from "./HelloWorld"
  export default {
		name: "index",
    components: {HelloWorld, Hostinfo, Menu, Tableselect}
  }
</script>

<style scoped>
  .el-header, .el-footer {
    background-color:  #545c64;
    text-align: center;
    line-height: 60px;
    font-family: PingFang SC;
    font-size: 30px Extra large;
    color: #42b983;
    margin-top: 0px;
  }

  .el-aside {
    background-color: #545c64;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
    margin-top: 0px;
    padding-top:2px ;
    padding-left:2px;
    padding-right: 2px;
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
  .el-container{
    background-color: #ffffff;
  }
</style>

