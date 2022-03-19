<template>
<div class="MyBlog">
<div class="index">
  <show-blog :data="blogs"></show-blog>
</div>
</div>
</template>

<script>
import {reactive} from 'vue'
import {request} from '../../network/request'
import showBlog from '../showBlog/ShowBlog.vue'
export default {
  components: { showBlog },
  comments:{showBlog},
  name: 'MyBlog',
  setup() {
    let blogs = reactive([])
    let res = request({
    url:'/blog/userblog/',
    method: 'get',
    }).then(res=>{
      for (let i in res){
        let T = res[i].date.indexOf('T')
        let date = res[i].date.substr(0, T)
        res[i].date = date
        blogs[i]=res[i]
      }   
    })

    return {
      blogs
    }
  }
}
</script>

<style lang="scss" scoped>
.MyBlog{
  // color: #fff;
  padding-bottom: 20%;
}

</style>