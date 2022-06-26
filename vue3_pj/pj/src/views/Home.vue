<template>
  <div class="home">
    <show-blog :data = blogs v-if="boo"></show-blog>
    <err v-else></err>
  </div>
</template>

<script>
// @ is an alias to /src
import { reactive, ref } from 'vue'
import { request } from '../network/request'
import ShowBlog from './showBlog/ShowBlog.vue'
import Err from './Err.vue'
export default {
  components: { ShowBlog , Err},
  name: 'Home',
  comments:{
    ShowBlog,
  },
  setup(){

    let boo = ref(true)
    let blogs = reactive([])
    let res = request({
    url:'blog/list/',
    method: 'get',
    }).then(res=>{
      if (res){
        // 去html标签
        for (let n in res){
          res[n].body = res[n].body.replace(/<[^>]+>/g, '')
        }
       // 解析时间戳
      for (let i in res){
        let T = res[i].date.indexOf('T')
        let date = res[i].date.substr(0, T)
        res[i].date = date
        blogs[i]=res[i]
      }   
      }
      else{
        boo.value = false
      }
    })

    return {
      blogs,
      boo
    }
  }

}
</script>

<style lang="scss" scoped>
.home{
  color: #fff;
  padding-bottom: 20%;
}
</style>