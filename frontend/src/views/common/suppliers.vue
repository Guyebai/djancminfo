<template>
  <div class="probleminfo">

     <!-- 添加记录-->
    <el-row :gutter="5" class="line-addproblem">
    <el-col :span="8">
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
            增加供应商</el-button>
      </el-col>
      <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>

    </el-row>

    <el-table
      ref="multipleTable"
      :data="data_names"
      tooltip-effect="dark"
      style="width: 95%"
      max-height="500"
      @selection-change="handleSelectionChange">
      <el-table-column
        type="selection"
        width="40">
      </el-table-column>
      <el-table-column type="index" :index="indexMethod">索引</el-table-column>
    
     <!--
      <el-table-column
        label="序号"
        width="80">
        <template slot-scope="scope">{{ scope.row.id }}</template>
      </el-table-column> -->


factory_name: "",
         factory_address: '0',
         factory_category:'',
         factory_leader:'',
         factory_leader_phone:'',

    <el-table-column
        prop="factory_name"
        label="供应商名称"
        width="180">
      </el-table-column>
     
      <el-table-column
        prop="factory_address"
        label="供应商地址"
        show-overflow-tooltip>
        </el-table-column>

        <el-table-column
        prop="factory_category"
        label="供应商类型"  :formatter="formatdata"
        show-overflow-tooltip>
        </el-table-column>
        <el-table-column
        prop="factory_leader"
        label="联系人"
        show-overflow-tooltip>
        </el-table-column>

        <el-table-column
        prop="factory_leader_phone"
        label="联系方式"
        width="180">
      </el-table-column>

        <el-table-column
        prop="factory_desc"
        label="描述"
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



  <!--增加供应商信息模态框-->
  <el-dialog title="增加供应商"   width="30%"  :visible.sync="dialogFormVisible">
    <el-form :model="addform"     :label-position="labelPosition"   >
      <el-form-item label="供应商名称"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="addform.factory_name"  autocomplete="off" ></el-input>
      </el-form-item>
       <el-form-item label="供应商负责人"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="addform.factory_leader"  autocomplete="off" ></el-input>
      </el-form-item>
      
      <el-form-item label="供应商类型" :label-width="formLabelWidth" >
        <el-radio-group v-model="addform.factory_category"  width='formrebootLabelWidth'  >
            <el-radio class="radio" :label="1">集成商/代理商</el-radio>
            <el-radio class="radio" :label="0">厂商</el-radio>
          </el-radio-group>
      </el-form-item>

       <el-form-item label="联系方式"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="addform.factory_leader_phone"  autocomplete="off" ></el-input>
      </el-form-item>
       <el-form-item label="供应商地址"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="addform.factory_address"  autocomplete="off" ></el-input>
      </el-form-item>
    
      <el-form-item label="供应商描述备注"  :label-width="formLabelWidth" >
        <el-input type="textarea"  size='mini'  v-model="addform.factory_desc" :autosize="{ minRows: 2, maxRows: 4}" ></el-input>
      </el-form-item>


    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="dialogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="addinfo(); dialogFormVisible = false">确 定</el-button> <!--绑定两个事件-->
    </div>
  </el-dialog>




    <!--编辑故障类型模态框-->

  <el-dialog title="编辑故障类型"    width="30%"   :visible.sync="editlogFormVisible">
    <el-form    :model="editform"  >
         <el-form-item label="机房名称"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="editform.idc_name"  autocomplete="off" ></el-input>
      </el-form-item>
       <el-form-item label="机房标识"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="editform.idc_tag"  autocomplete="off" ></el-input>
      </el-form-item>
       <el-form-item label="负责人"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="editform.idc_leader"  autocomplete="off" ></el-input>
      </el-form-item>
       <el-form-item label="联系方式"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="editform.idc_leader_phone"  autocomplete="off" ></el-input>
      </el-form-item>
       <el-form-item label="机房地址"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="editform.idc_address"  autocomplete="off" ></el-input>
      </el-form-item>
     <el-form-item label="机房描述"  :label-width="formLabelWidth" >
        <el-input type='text'  size='mini' v-model="editform.idc_desc"  autocomplete="off" ></el-input>
      </el-form-item>

    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="editlogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="ahandleEdit(editform.id);  editlogFormVisible = false">确 定</el-button> <!--绑定两个事件-->
    </div>
  </el-dialog>

  </div>

</template>

<script>
import   qs from 'qs'

  export default {
    name: "suppliers",
    data () {
      return {
        addform:{
         factory_name: "",
         factory_address: '',
         factory_category:'',
         factory_leader:'',
         factory_leader_phone:'',
         factory_desc:'',
        },
        data_names:[],
        dialogFormVisible: false,
        editlogFormVisible: false,
        labelPosition: 'left',
        formLabelWidth: '90px',
        formrebootLabelWidth:'30px',
       
        editform:{
          id:'',
         factory_name: "",
         factory_address: '0',
         factory_category:'',
         factory_leader:'',
         factory_leader_phone:'',
         factory_desc:'',
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
    //获取机房数据
      getproblemData(){
        if(this.page.currentPage >1);
         this.page.currentPage === 1
        this.$axios.get("http://127.0.0.1:8000/api/suppliers/",{
        params:{
        page:  this.page.currentPage,
        page_size: this.page.pageSize ,
        search: this.filters.name,
        }
        })
          .then(res => {
            this.filterData(res.data);

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
            id:data.results[i].id,
            factory_name:data.results[i].factory_name,
            factory_address:data.results[i].factory_address,
            factory_category:data.results[i].factory_category,
            factory_leader:data.results[i].factory_leader,
            factory_leader_phone:data.results[i].factory_leader_phone,
            factory_desc:data.results[i].factory_desc,

          }
          finaldata.push(dataobj);
        }
        this.data_names = finaldata;
      },

      formatdata: function (row, column) {
        return row.factory_category == 1 ? '集成商/代理商' : row.factory_category == 0 ? '厂商' : '未知';
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

      //添加机房信息
      addinfo(){
        this.$axios.post("http://127.0.0.1:8000/api/suppliers/", {
           idc_name:  this.addform.idc_name,
            idc_address:this.addform.idc_address,
            idc_tag:this.addform.idc_tag,
            idc_leader:this.addform.idc_leader,
            idc_leader_phone:this.addform.idc_leader_phone,
            idc_desc:this.addform.idc_desc,

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
        //删除故障记录
      deleteproblem(id) {
        this.$confirm("确认删除吗？",'提示',{type:'waring'}).then(()=>{
        this.$axios.delete("http://127.0.0.1:8000/api/suppliers/" + id +'/').then(res => {
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


      //供应商信息编辑
      editproblem(id) {
      this.$axios.get("http://127.0.0.1:8000/api/suppliers/" + id + '/').then(res => {
      if (res.status === 200 ) {
            // 删除成功
         this.editform ={
          id:res.data.id,
           idc_name:  res.data.idc_name,
            idc_address:res.data.idc_address,
            idc_tag:res.data.idc_tag,
            idc_leader:res.data.idc_leader,
            idc_leader_phone:res.data.idc_leader_phone,
            idc_desc:res.data.idc_desc,
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
        this.$axios.patch("http://127.0.0.1:8000/api/suppliers/" + id +'/', qs.stringify({
            idc_name:  this.editform.idc_name,
            idc_address:this.editform.idc_address,
            idc_tag:this.editform.idc_tag,
            idc_leader:this.editform.idc_leader,
            idc_leader_phone:this.editform.idc_leader_phone,
            idc_desc:this.editform.idc_desc,
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
