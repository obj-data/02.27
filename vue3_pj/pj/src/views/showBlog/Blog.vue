<template>
  <div class="max">
    <div class="blog">
        <!-- 如果当前用户与创建博客的用户一致，显示修改按钮 -->
      <h2 class="title">{{blog.title}} <el-button v-if="username==blog.username"><router-link :to="link">修改博客</router-link></el-button><el-button v-if="username==blog.username" @click="DeleteBlog">删除此博客</el-button></h2>
      <div class="msg">
        <span>用户：<span>{{blog.username}}</span></span><span>{{blog.date}}</span>
      </div>
      <div class="body" v-html="blog.body"></div>
    </div>
  </div>
</template>

<script>
import { reactive } from 'vue'
import { useRoute } from 'vue-router'
import { request } from '../../network/request'
export default {
  components:{
    
  },
  setup(props) {

    // 根据用户名是否存在决定能否修改
    const username = localStorage.getItem('username')
    const title = useRoute().query.title
    let blog = reactive({})
    const link = '/redact?title='+title
    request({
      url:'/blog/detail/'+title+'/',
      method:'get',
    }).then(res=>{
      // 解析时间戳
      let T = res.date.indexOf('T')
      let day = res.date.substr(0, T)
      let time = res.date.split(':')
      let t = time[0].substr(T+1,T+3)-16>=0 ? time[0].substr(T+1,T+3)-16 : (24+ (time[0].substr(T+1,T+3) -16))*-1
      res.date = '于' + day + '\t\t\t' + t + ':' + time[1] + ':' + time[2].substr(0,2) + '发布'
      Object.keys(res).forEach((key) =>{
        blog[key] = res[key]
      })
    })
    // 删除博客
    const DeleteBlog = () =>{
      request({
        method:"DELETE",
        url:'/blog/detail/'+title+'/',
      }).then(res=>{
        if(res.status==204){
          window.location.replace('/myblog')
        }
      })
    }
    
    return {
      blog,
      username,
      link,
      DeleteBlog
    }    
  }
}
</script>

<style lang="scss">
.max{
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.3);
  width: 100%;
  display: flex;
  justify-content: center;

  .blog{
    margin: 40px;
    width: 60%;
    background-color: #fff;
    .title{
      margin: 15px 0 15px 15px;
      display: flex;
      justify-content: space-between;
      .el-button{
        margin-right: 10px;
        padding: 0 10px;
        color: #000;

        a{
          color: #000;
          padding: 8px 15px;
        }
        a:hover{
            color: rgb(13, 189, 233);
          }
      }
    }
    .msg{
      height: 40px;
      background-color: rgb(214, 214, 214);
      span{
        margin: 20px 20px;
        color: #999aaa;
        font-size: 12px;
        span{
          color: rgb(75, 74, 74);
        }
      }
    }
    .body{
      margin: 40px;
      line-height: 3;
      text-align: left;
      font-size: 14px;
      a{
        color: #000;
      }
    }

  }
}
</style>