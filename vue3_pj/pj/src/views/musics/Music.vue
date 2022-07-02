<template>
  <div class="index">
    {{name}}
<audio id="myAudio"  @ended="overAudio"  controls>
  <source v-if="url"  :src='url'  type="audio/mpeg">
</audio>

  </div>
</template>

<script>
import { reactive, ref } from 'vue'
import { request } from '../../network/request'
import { useRoute} from 'vue-router'
const audio = new Audio()

export default {
  setup() {
    const name = useRoute().query.name
    console.log(useRoute().query);
    let url = ref(null)
    let tar = ref(true)
    let num = ref(1)
    let list = ref(null)
    let time = ref(null)
    let res = request({
    url:'/music/list/',
    method: 'get',
    }).then(res=>{
      list.value = res.names
    url.value = 'http://127.0.0.1:8000/music/list/' + res.names[0]

      })
    const test = () => {
      console.log('已执行test');
    }

    let overAudio = () =>
    {
    url = 'http://127.0.0.1:8000/music/list/' + list.value[num.value]
    num.value ++
    audio.src = url
    audio.load()
    console.log(url);
    tar.value = !tar.value
    // let state = audio.play()

    }
   
    return {
      url,
      overAudio,
      time,
      tar,
      test,
      name
}
  },
}

</script>


<style lang="scss">
.index{
  height: 900px;
  width: 100%;
  audio{
    margin: 450px 40%;
  }
}
  
</style>