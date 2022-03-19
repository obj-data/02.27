<template>
<div class="signIn">
  <el-input v-model="user.username" placeholder="请输入用户名" clearable />
  <el-input
    v-model="user.password"
    type="password"
    placeholder="请输入密码"
    show-password
  />
  <el-input
    v-model="user.password2"
    type="password2"
    placeholder="请再次输入密码"
    show-password
  />
  <el-input v-model="user.email" placeholder="请输入邮箱号" clearable style="margin-bottom:0;"/>
  <span v-show="show" class="msg">{{massage}}</span>

  <el-button @click="success" type="success" plain class="success">注册</el-button>

</div>
</template>



<script>
import { defineComponent, reactive, ref} from 'vue'
import {request} from '../network/request'
import { Login } from '../network/login'
import loginVue from './login.vue'

export default defineComponent({
  name:'signIn',
  setup() {
    let show = ref(false)
    let massage = ref('')
    let user = reactive({
      username: '',
      password: '',
      password2: '',
      email: ''
    })
    const success = () => {
      for (let i in user){
        if (user[i] === ''){
          show.value = true
          massage.value = i+' 数据为空'
          setTimeout(()=>{
            show.value = false
          }, 2000)
          return 
        }
      }
      request({
        method: 'post',
        url: 'registered/',
        data: user
      }).then(res=>{
        if (res){
          
        }
        massage.value = res
        show.value = true
      })
      // 注册成功自动登录，登陆成功重定向到主页
      const loginUser = {'username':user.username,'password': user.password }
      Login(loginUser).then(res=>{
        if (Object.values(res)[0] == 'True'){
          window.location.replace('home/')
        }
      })
      
    }
   
   return {
     user,
     success,
     show,
     massage
   }
  }
})
</script>

<style lang="scss" scoped>
.signIn{
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  .el-input{
    margin: 15px 10%;
    height: 32px;
    width: 80%;

  }
  .success{
    margin: 5% 25% 0;
    width: 50%;
    height: 40px;
  }
  .msg{
    width: 50%;
    height: 20px;
    text-align: center;
    background-color: rgb(219, 24, 24);
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.3);
    border-radius: 20px;
    color: #fff;
    margin: 5% auto 0;
    font-size: 12px;
    padding: 0 20px;
  }
}


</style>