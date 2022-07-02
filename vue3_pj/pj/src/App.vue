<template>
  <!-- <router-view/> -->
  <div class="app">
    <!-- <button @click="rmToken">删除token</button> -->
  <el-menu
    class="el-menu-demo"
    mode="horizontal"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
  >
    <el-menu-item index="0"><router-link to="/"  class="index">首页</router-link></el-menu-item>
    <el-menu-item index="1" v-if="userState"><router-link to="/login"  class="index">用户</router-link></el-menu-item>
    <el-sub-menu index="2" v-else>
      <template #title><router-link to="#"  class="index">{{username}}</router-link></template>
      <el-menu-item index="2-1" ><router-link to="/myblog" class="index">我的博客</router-link></el-menu-item>
      <!-- <el-menu-item index="2-2">用户信息</el-menu-item> -->
      <el-menu-item index="2-3" @click="rmToken">退出登录</el-menu-item>
    </el-sub-menu>
    <!-- <el-menu-item index="3" disabled>Info</el-menu-item> -->
    <el-menu-item index="4" v-if="!userState"><router-link to="/redact" >新建博客</router-link></el-menu-item>
    <el-menu-item index="4" v-else disabled>新建博客</el-menu-item>
    <el-menu-item index="5"><router-link to="/music/list"  class="index">音乐</router-link></el-menu-item>
  </el-menu>
    <router-view/>
  </div>
</template>

<script>
import {computed, onMounted, reactive, ref, watch} from 'vue'
import {request} from './network/request'
export default {
  setup(){
    // 获取用户名到导航栏
    let username = ref(localStorage.getItem('username'))
    let userState = ref(true)
    const rmToken = () => {
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      userState.value = true
    }
    return {
      rmToken,
      username,
      userState
    }
  },
  beforeCreate() {
    // 检测是否登录， 已登录用户关闭登录接口
    if (localStorage.getItem('username')){
        this.userState = false
    }
  }
  }


</script>

<style lang="scss">
.app{
  width: 100%;
  
  background-image: url('./assets/bg.jpg');
  padding-bottom: 100px;
  li{
    padding: 0;
  }
  .index{
    width: 100%;
    height: 100%;
    padding: 0 20px;
    
    // color: #FFF;
  }
  .el-menu-demo{
    display: flex;
    justify-content: space-around;
  }

}
 a{
    width: 100%;
    text-decoration: none;
    color: #FFF;
  }

</style>