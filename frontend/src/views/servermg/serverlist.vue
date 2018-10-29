<template>
  <div class="probleminfo">

     <!-- 添加记录与搜索-->
    <el-row :gutter="5" class="line-addproblem">
    <el-col :span="8">
     <!--搜索-->
     <el-row>
            <el-col :span="16"  :offset="2"class="grid">
                <el-input v-model="filters.name"  placeholder="请输入内容" size="mini" @keyup.enter.native="getproblemData()" ></el-input>
            </el-col>
            <el-col :span="4" class="grid">
                <el-button type="success" icon="el-icon-search"  v-on:click="getproblemData()" size="mini">搜索</el-button>
            </el-col>
     </el-row>

      </el-col>

      <el-col :span="8" class="line-addproblem-left">

          <el-button type="success"
                     icon="el-icon-circle-plus-outline"
                     size="mini"  @click="dialogFormVisible = true" >
            添加故障记录</el-button>
      </el-col>
      <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>

    </el-row>

    <el-table
      ref="multipleTable"
      :data="problems_names"
      tooltip-effect="dark"
      style="width: 95%"
      @selection-change="handleSelectionChange">
      <el-table-column
        type="selection"
        width="40">
      </el-table-column>
      <el-table-column type="index" :index="indexMethod">索引</el-table-column>
      
      <el-table-column
        prop="host_ip"
        label="主机IP"
        width="120">
      </el-table-column>
      <el-table-column
        prop="host_sn"
        label="SN编号" 
         width="100"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
        prop="idc_name"
        label="机房"
        width="100"
        show-overflow-tooltip>
      </el-table-column>

        <el-table-column
        prop="trouble_name"
        label="故障类型"
         width="100"
        show-overflow-tooltip>
      </el-table-column>
       <el-table-column
        prop="problem_desc"
        label="故障描述"
         width="100"
        show-overflow-tooltip>
      </el-table-column>
       <el-table-column
        prop="server_category"
        label="机型"
         width="100"
        show-overflow-tooltip>
      </el-table-column>
       <el-table-column
        prop="factory_name"
        label="厂商"
         width="100"
        show-overflow-tooltip>
      </el-table-column>
       <el-table-column
        prop="problem_info"
        label="备注"
         width="100"
        show-overflow-tooltip>
      </el-table-column>




      <el-table-column label="编辑" width="100">
        <template slot-scope="scope">
          <el-button type="primary" icon="el-icon-edit" size="mini" @click.prevent="editproblem(scope.row.id)">编辑</el-button>
        </template>
      </el-table-column>
      <el-table-column label="删除" width="100">
        <template slot-scope="scope">
          <el-button type="danger" icon="el-icon-delete"   size="mini"   @click.prevent="deleteproblem(scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>




    <!--分页条-->
<div class="block" style="float:right;margin-top:20px ;margin-right:280px" >
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="page.currentPage"
      :page-sizes="[5,8, 10, 100,200,500]"
      :page-size="page.pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="page.totalRecords">
    </el-pagination>
  </div>



  <!--增加故障类型模态框-->
  <el-dialog title="增加故障类型"   width="30%"  :visible.sync="dialogFormVisible">
    <el-form :model="editform"     :label-position="labelPosition"   >
      <el-form-item label="故障名称"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="editform.trouble_name"  autocomplete="off" ></el-input>
      </el-form-item>
      <el-form-item label="是否重启" :label-width="formLabelWidth" >
        <el-radio-group v-model="editform.trouble_influence"  width='formrebootLabelWidth'  >
            <el-radio class="radio" :label="1">是</el-radio>
            <el-radio class="radio" :label="0">否</el-radio>
          </el-radio-group>
      </el-form-item>
      <el-form-item label="故障描述"  :label-width="formLabelWidth" >
        <el-input    type="textarea"  v-model="editform.trouble_desc" :autosize="{ minRows: 2, maxRows: 4}"></el-input>
      </el-form-item>

    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="dialogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="addinfo(); dialogFormVisible = false">确 定</el-button> <!--绑定两个事件-->
    </div>
  </el-dialog>

    <!--编辑故障类型模态框-->

  <el-dialog title="编辑故障类型"    width="30%"   :visible.sync="editlogFormVisible">
    <el-form    :model="form"  >
      <el-form-item  label="故障名称"  :label-width="formLabelWidth" >
        <el-input v-model="form.trouble_name"  autocomplete="off" ></el-input>
      </el-form-item>
      <el-form-item label="是否重启" :label-width="formLabelWidth" >
           <el-radio-group v-model="form.trouble_influence">
            <el-radio class="radio" :label="1">是</el-radio>
            <el-radio class="radio" :label="0">否</el-radio>
          </el-radio-group>

      </el-form-item>
      <el-form-item label="故障描述"   :label-width="formLabelWidth">
        <el-input   type="textarea" v-model="form.trouble_desc"  :autosize="{ minRows: 2, maxRows: 4}"></el-input>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="editlogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="ahandleEdit(form.id);  editlogFormVisible = false">确 定</el-button> <!--绑定两个事件-->
    </div>
  </el-dialog>

  </div>

</template>

<script>
import   qs from 'qs'

  export default {
    name: "serverlist",
    data () {
      return {
        editform:{
         trouble_name: "",
         trouble_influence: '0',
         trouble_desc:'',
        },
        problems_names:[],
        dialogFormVisible: false,
        editlogFormVisible: false,
        labelPosition: 'left',
        formLabelWidth: '70px',
        formrebootLabelWidth:'30px',
       
        form:{
          id:'',
          trouble_name: '',
          trouble_influence: '',
          trouble_desc: '',
        },
        filters: {
        name: ""
      },page:{
        currentPage:1,
        pageSize:5,
        totalRecords: 0, //总条数
        totalPages: 0, //总页数
      }
      }

    },
    created(){
      this.getproblemData()  //页面渲染时调用获取数据的方法
    },
    methods:{
    //获取故障列表
      getproblemData(){
        if(this.page.currentPage >1);
         this.page.currentPage === 1
        this.$axios.get("http://127.0.0.1:8000/api/problems/",{
        params:{
        page:  this.page.currentPage,
        page_size: this.page.pageSize ,
        search: this.filters.name,
        }
        })
          .then(res => {
            console.log(res.data)
            this.filterData(res.data);
            console.log(id,host)

            this.page.totalRecords = res.data.count;//分页
            var newPageInfo = [];
            for (var i = 0; i < page.pagesize; i++) {
              var index =i+(page.pageCurrent-1)*page.pagesize;
              if(index>this.pagerData.page.totalCount-1)break;
                 newPageInfo[newPageInfo.length] = this.dataAll[index];
                    }
                this.pagerData.data = newPageInfo; // 修改分页数据
          })
          .catch(error =>{
            console.log(error)
          })
      },

      //数据展示筛选
      filterData(data){
        var  finaldata = [];
        for (var i=0;i<data.results.length;i++){
          var dataobj ={
            
            host_ip: data.results[i].host_ip,
            host_sn:data.results[i].host_sn,
            idc_name: data.results[i].idc_name,
            trouble_name:data.results[i].trouble_name,
            problem_time:data.results[i].problem_time,
            repair_time:data.results[i].repair_time,
            problem_desc: data.results[i].problem_desc,
            server_category: data.results[i].server_category,
            factory_name:data.results[i].factory_name,
            problem_info:data.results[i].problem_info

          }
          finaldata.push(dataobj);
        }
        this.problems_names = finaldata;
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
      },

      //格式化显示是否重启
      formatproble: function (row, column) {
        return row.trouble_influence == 1 ? '是' : row.trouble_influence == 0 ? '否' : '未知';
      },

      //添加故障信息
      addinfo(){
        this.$axios.post("http://127.0.0.1:8000/api/troubles/", {
          trouble_name: this.editform.trouble_name,
          trouble_influence: this.editform.trouble_influence,
          trouble_desc: this.editform.trouble_desc,
        })
          .then(res => {
            if (res.status === 201){

              this.$message({message:"添加成功",type:'success'});
              return  this.getproblemData()
            }else{
              //失败
              this.$message({message:"添加失败",type:'error'});
            }

          })
          .catch(error => {
            console.log(error)
          });
      },
        //删除故障信息
      deleteproblem(id) {
        this.$confirm("确认删除吗？",'提示',{type:'waring'}).then(()=>{
        this.$axios.delete("http://127.0.0.1:8000/api/troubles/" + id +'/').then(res => {
          if (res.status === 204 ) {
            // 删除成功
             this.$message({message:"删除成功",type:'success'});
            return  this.getproblemData()
          } else {
            this.$message({message:"删除失败",type:'success'});
          }
        });
        })
      },


      //故障编辑类型
      editproblem(id) {
      this.$axios.get("http://127.0.0.1:8000/api/troubles/" + id + '/').then(res => {
      if (res.status === 200 ) {
            // 删除成功
         this.form ={
          id:res.data.id,
          trouble_name:res.data.trouble_name ,
          trouble_influence:res.data.trouble_influence,
          trouble_desc:res.data.trouble_desc
           };
        this.editlogFormVisible = true

        }

         else {
                  this.$message({message:"数据不存在",type:'error'});
            }
            });

      },
      //编辑后提交
      ahandleEdit(id){
        this.$axios.patch("http://127.0.0.1:8000/api/troubles/" + id +'/', qs.stringify({
          trouble_name: this.form.trouble_name,
          trouble_influence: this.form.trouble_influence,
          trouble_desc: this.form.trouble_desc,
        }))
          .then(res => {
            if (res.status === 200){

              this.$message({message:"编辑成功",type:'success'});
            

            }else{
              //失败
              this.$message({message:"编辑失败",type:'error'});
              
              
            }
            return  this.getproblemData()

          })
          .catch(error => {
            console.log(error)
          });


      },
      handleSizeChange(pageSize) {
         

         this.page.pageSize= pageSize;
         this.getproblemData()

      },
      handleCurrentChange(page) {
        this.page.currentPage= page;
        
         this.getproblemData()
      
      }
    },

  }



 


</script>

<style scoped>
  .probleminfo{
    color: #42b983;
    font-weight: normal;
    margin-top:0px;
    margin-left: 0px;
    padding-top:0px ;
  }
  .el-table{
    line-height: 2em;
  }
  .line-addproblem{
    line-height: 30px;
    margin-top: 10px;
    margin-left: 10px;
  }
  .line-addproblem-left{
    padding-left: 0px;
    margin-left: 10px;
    text-align: left;
  }
</style>
