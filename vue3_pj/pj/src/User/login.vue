<template>

<div class="index">
  
<div class="login-win">
  <div class="nav">
    <el-button type="primary" id="signIn" :class="{checked:!navValue}" @click="navValue=true">注册</el-button>
    <el-button type="primary" :class="{checked:navValue}" @click="navValue=false">登录</el-button>
  </div>
  <sign-in v-if="navValue"></sign-in>
  <div class="login" v-else="navValue">
    <el-input v-model="user.username" placeholder="请输入用户名" clearable />
  <el-input
    v-model="user.password"
    type="password"
    placeholder="请输入密码"
    show-password
  />
  <span v-show="show" class="msg">{{massage}}</span>
  <el-button @click="login" type="success" plain class="success">登录</el-button>

  </div>
</div>
</div>
</template>

<script>
import { ref, watch, computed, onMounted, reactive } from 'vue'
import signIn from './signIn.vue'
import {Login} from '../network/login'
export default {
  components: { signIn },
  setup(){
    let show = ref(false)
    let massage = ref('')
    let user = reactive({
      username:'',
      password: ''
    })
    let navValue = ref(true)

    const login = () =>{
      //  提示信息
      for (let i in user){
        if (user[i] === ''){
          show.value = true
          massage.value = i+' 数据为空'
          setTimeout(()=>{
            show.value = false
            // 等待两秒自动关闭错误信息显示
          }, 2000)
          return 
        }
      }
      const err = Login(user)
      err.then(res =>{
        //登陆成功重定向到主页，密码/账号错误提示
        let data = Object.values(res)[0]
        if (data =='Unable to log in with provided credentials.'){
        massage.value = '账号或密码错误'
        show.value = true
      }else if(res){
        window.location.replace('home/')
      }
      }
      )
      
    }
    return {
      navValue,
      user,
      login,
      massage,
      show
    }
  }
  }


</script>

<style lang="scss" scoped>
.index{
  width: 100%;
  height: 700px;
}


.login-win{
  position: relative;
  top:100px;
  left:30%;
  width: 40%;
  height: 400px;
  border-radius: 4px;
  // background-color: rgb(214, 214, 214);
  background-color: #fff;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;

  // 导航栏
  .nav{
    display: flex;
    justify-content: space-between;
    width: 100%;
    height: 15%;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);

    .el-button{
      width: 50%;
      height: 100%;
      margin: 0px;
      border-radius: 0;
    }

  }
}
.checked{
  background-color: #fff;
  color: #000;
  border: #fff;
}

.login{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  .el-input{
    width: 80%;
    margin-top: 10%;

  }
  .el-button{
    margin: 10% 0;
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