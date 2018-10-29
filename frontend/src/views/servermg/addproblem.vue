<template>
  <div>
    <el-form ref="form" label-width="80px">
      <el-form-item label="故障名称">
        <el-input v-model="trouble_name"></el-input>
      </el-form-item>
      <el-form-item label="是否需要重启">
        <el-select v-model="trouble_influence" placeholder="请选择">
          <el-option label="否" value="0"></el-option>
          <el-option label="是" value="1"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="addinfo">立即添加</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
  export default {
    name:'addproblem',
    data() {
      return {
        trouble_name: "",
        trouble_influence: '0'
      };
    },
    methods:{
      addinfo(){
        this.$axios.post("troubles/", {
          trouble_name: this.trouble_name,
          trouble_influence: this.trouble_influence,
        })
          .then(res => {
            var res = res.body;
            if (result.code === 200){
              alert("添加成功！");
            }else{
              //失败
              alert("添失败！");
            }
          })
          .catch(error =>{
            console.log(error)
          })
      }
    }

  };
</script>
