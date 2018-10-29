<el-dialog title="增加服务器故障类型" :visible.sync="dialogFormVisible">
  <el-form :model="form">
    <el-form-item label="故障名称">
      <el-input v-model="trouble_name"></el-input>
    </el-form-item>
    <el-form-item label="是否需要重启" :label-width="formLabelWidth">
      <el-select v-model="trouble_influence" placeholder="请选择">
        <el-option label="不需要" value="0"></el-option>
        <el-option label="需要" value="1"></el-option>
      </el-select>
    </el-form-item>
  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">取 消</el-button>
    <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
  </div>
</el-dialog>
