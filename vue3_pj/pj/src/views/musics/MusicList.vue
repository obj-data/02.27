<template>
  <div class="index">
    
    <div class="list">
      <div class="music" v-for=" i in list" v-bind:key="i" @click="getName(i)"><img src="../../assets/play.png" alt=""><span>{{i}}</span></div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { request } from '../../network/request'
import { useRoute, useRouter} from 'vue-router'

export default {
  setup() {
    const router = useRouter()  // 跳转
    const route = useRoute() //获取到值
    let list = ref()
    let res = request({
    url:'/music/list/',
    method: 'get',
    }).then(res=>{
      list.value = res.names

      })
      const getName = (key) => {
        console.log(key);
      // 监视点击的歌曲名称，携带名称进行请求
      router.push({
        path:'/music',
        query:{
          name:key,
          list:list.value        
          }
      })
        
    }

    return {
      list,
      getName
    }
    
  },
}
</script>

<style lang="scss">
  .index{
    
  .list{
    margin-top: 50px;
    // padding-top: 20px;
    width: 50%;
    padding-bottom: 30px;
    margin-left: 25%;
    background-color: rgb(117, 88, 88);
    border: rgb(170, 145, 153) solid 3px;
    border-radius: 10px;
  }
  .music{
    margin-top: 10px;
    width: 100%;
    height: 30px;
    color: rgb(247, 248, 248);
    // text-align: center;
    // background-color: rgb(117, 88, 88);
    border-radius: 3px;
    border-bottom: 2px solid #FFF;
    img{
      position: relative;
      top: 3px;
      width: 20px;
    }
    span{
      position: relative;
      bottom: 1px;
      left: 5px;
    }
  }
  .music:hover{
    background-color: rgb(158, 115, 115);
    cursor: pointer;
    span:hover{
      border-bottom: 1px solid #000;
    }
  }

  }
  
</style>
