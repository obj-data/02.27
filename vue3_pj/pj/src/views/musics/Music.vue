<template>
  <div class="index">
<audio id="myAudio" @ended="overAudio" @timeupdate="" controls>
  <source v-if="url"  :src='url'  type="audio/mpeg">
  <!-- <source v-if="url" type="audio/mpeg"> -->
</audio>
  </div>
</template>

<script>
import { reactive, ref } from 'vue'
import { request } from '../../network/request'
const audio = new Audio()

export default {
  setup() {
    let url = ref(null)
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

    let overAudio = () =>
    {
    url = 'http://127.0.0.1:8000/music/list/' + list.value[num.value]
    num.value ++
    audio.src = url
    audio.load()
    audio.oncanplay = () =>{
      time.value = audio.duration 
      setTimeout(()=>{
        console.log(audio.ended);
      }, 1000)
      let state = audio.play()
      
      
    }

    }
   
    return {
      url,
      overAudio,
      time
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