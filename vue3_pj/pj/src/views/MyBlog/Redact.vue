<template>
  <div class="redact">
     <el-button type="primary" @click="RedactBlog">提交</el-button>
    <div class="title">
       <span>标题：</span> <el-input v-model="blog.title" placeholder="请输入标题" clearable />
    </div>
    <p class="body">内容:</p>
    <QuillEditor class="Quill" spellcheck="false" v-if="title" theme="snow"
     v-model:content="blog.body" contentType="html"/>
    <QuillEditor class="Quill" spellcheck="false" v-else theme="snow"
     v-model:content="blog.body" placeholder="请输入内容" contentType="html"/>
  </div>
</template>

<script>
import { reactive, ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import {request} from '../../network/request'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import { ElMessageBox, ElMessage, Action } from 'element-plus'

export default {
  name:'Redact',
  components: {
    QuillEditor
  },
  setup(){
    const route = useRoute()
    const title = route.query.title
    let blog = reactive({
      title:title,
      body: ''
    })
    if (title !=null){
      request({
        method:'get',
        url:'/blog/detail/'+title+'/',
      }).then(res=>{
        console.log('test1');

        blog.body = res.body
      }).catch(err=>{
        console.log(err);
      })
    }
    const RedactBlog = () =>{
      if (title){
        request({
          url:'/blog/detail/'+title+'/',
          method:'PUT',
          data: blog
        }).then(res=>{
          ElMessageBox.alert(res, 'Title',{
            confirmButtonText: '回到博客页面',
            callback:(Action)=>{
            const link = '/blog?title='+title
            window.location.replace(link)
            }
          })
        })
      }else{
        request({
          url:'/blog/userblog/',
          method:'POST',
          data: blog
        }).then(res=>{
          console.log(res['title'] == 'true');
          ElMessageBox.alert('创建博客成功',res, 'Title',{
            confirmButtonText: '回到首页',
            callback:(Action)=>{
            window.location.replace('/home')
            }
          })
        })
      }
    }

  return {
      title,
      blog,
      RedactBlog
    }
  }
}
</script>

<style lang="scss">
  .redact{
  top: 30px;
  left: 20%;
  // height: 100%;
  border-radius: 10px;
  position: relative;
  border: 1px solid #E4E7ED;
  width: 60%;
  color:#000;
  background-color: #fff;
  display: flex;
  justify-content: space-between;
  flex-direction: column;
  // line-height: 3;
  button{
    width: 30%;
    align-self: center;
    
  }
  .title{
    margin: 40px;
    display: flex;
    margin-left: 10px;
    margin-bottom: 10px;
    span{
      margin-top: 10px;
      width: 100px;
    }
    .el-input{
      width: 100%;
      margin-top: 5px;
    }
  }
  .body{
    margin-left: 10px;
  }
  .Quill{
    height: 400px;
    border: 0;
  }
  }
</style>