<template>
<!-- 歌曲信息页面 -->
<h3 style="color:#FFF;margin: 0 40%;" :key="i" v-for="i in [...Array(50).keys()]">歌曲详情页面</h3>
<Player @eventEnd="endMusic" :name="name" class="player"/>

  <div class="index">

  </div>
</template>

<script>
import { reactive, ref } from 'vue'
import { request } from '../../network/request'
import { useRoute} from 'vue-router'
import  Player  from './Audio.vue'
import { isUndefined } from 'element-plus/es/utils'
// const audio = new Audio()

export default {
  components:{
    Player
  },
  setup() {
    let name =  isUndefined(localStorage.getItem('MusicName')) ? localStorage.getItem('MusicName') : useRoute().query.name
    const list = useRoute().query.list
    let url = ref('http://127.0.0.1:8000/music/list/'+name)
    let tar = ref(true)
    let num = ref(0)
    let time = ref(null)

    const endMusic = (back) =>{
      console.log(localStorage.getItem('MusicName'), '播放完毕后');
      if (list.indexOf(localStorage.getItem('MusicName'))+1 != list.lenth){
      back(list[list.indexOf(localStorage.getItem('MusicName'))+1])}else{useRoute.query.name}

    }
   
    return {
      name,
      endMusic
}
  },
}

</script>


<style lang="scss">
.index{
  color:#FFF;
  height: 900px;
  width: 100%;
  
  audio{
    margin: 450px 40%;
  }
}
.player{
  position: fixed;
  bottom: 0px;
  left: 0;
  }
  
</style>
