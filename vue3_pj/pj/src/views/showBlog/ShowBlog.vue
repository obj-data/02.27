<template>
  <div class="index">
    <div class="blog-list" v-if="data.length!=0">
      <div class="blog" v-for="i in data" :key="i.title">
        <h2 @click="getKey(i.title)">{{i.title}}</h2>
        <div class="body">{{i.body}}</div>
        <span class="user">{{i.username}}</span>
        <span class="date">{{i.date}}</span>
      </div>
    </div>
    <div v-else style="background-color: #fff;">
      <h1 style="margin:50%;">空空如也</h1>
    </div>
  </div>
</template>

<script>
import { reactive, ref, toRaw } from 'vue'
import { useRoute, useRouter} from 'vue-router'
export default {
  name: 'ShowBlog',
  props:{
    data:{
      type:Object,
      default:''
    }
  },
  setup(props){
      const router = useRouter()  // 跳转
      const route = useRoute() //获取到值

    const getKey = (key) => {
      // 监视点击的博客标题，携带标题进行请求
      router.push({
        path:'/blog',
        query:{
          title:key,        
          }
      })
        
    }
    
    return {
      getKey,
    }
  }
}
</script>

<style lang="scss" scoped>
.index{
  top: 30px;
  left: 20%;
  position: relative;
  border: 1px solid #E4E7ED;
  

  width: 60%;
  color:#000;
  background-color: #fff;

  .blog-list{

    .blog{
      position: relative;
      width: 100%;
      height: 150px;
      // background-color: pink;
      border-bottom: 1px solid #f2f2f2;
      h2 ,.body{
        margin-left: 20px;
      }
      h2:hover{
        color: red;
        cursor: pointer
      }
      .body{
        font-size: 14px;
        color: #999aaa;
      }
      .user{
        position: absolute;
        right: 100px;
      }
      .date{
        position: absolute;
        right: 10px;
      }
      .date,.user{
        bottom: 10%;
        color: #999aaa;
        font-size: 12px;
      }
    }
  }
}
</style>