<template>
  <div class="hello">
    <template>
      <el-table
        ref="multipleTable"
        :data="trouble_names"
        tooltip-effect="dark"
        style="width: 100%"
        @selection-change="handleSelectionChange">
        <el-table-column
          type="selection"
          width="40">
        </el-table-column>
        <el-table-column
          label="序号"
          width="100">
          <template slot-scope="scope">{{ scope.row.id }}</template>
        </el-table-column>
        <el-table-column
          prop="trouble_name"
          label="故障名稱"
          width="100">
        </el-table-column>
        <el-table-column
          prop="trouble_influence"
          label="故障是否需要重启"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="200">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">详情</el-button>
            <el-button type="text" size="small">编辑</el-button>
            <el-button type="text" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

    </template>


  </div>

</template>

<script>
import Tableselect from "./Tableselect";
export default {
  name: 'HelloWorld',
  components: {Tableselect},
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      trouble_names:[]
    }

  },
  created(){
    this.$axios.get("http://127.0.0.1:8000/api/troubles/")
      .then(res => {
        this.filterData(res.data);
      })
      .catch(error =>{
        console.log(error)
      })
  },
  methods:{
    filterData(data){
      var  finaldata = [];
      for (var i=0;i<data.results.length;i++){
        var dataobj ={
          id:data.results[i].id,
          trouble_name:data.results[i].trouble_name,
          trouble_influence:data.results[i].trouble_influence
        }
        finaldata.push(dataobj);
      }
       this.trouble_names = finaldata;
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    handleClick(row) {
      console.log(row);
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .hello{
    color: #42b983;
    font-weight: normal;
    margin-top:0px;
    margin-left: 0px;
    padding-top:0px ;
  }
  .el-table{
    height: 2em;
  }
</style>
