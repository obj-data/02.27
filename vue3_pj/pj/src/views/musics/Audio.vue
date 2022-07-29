<template>
  <div class="player">
    <div class="audio">
    <button class="operation"  @click="last"><img class="edit" src="../../assets/player/last.png" alt="" ></button> 
    <button class="operation" v-if="playBoo" @click="play"><img src="../../assets/player/play.png" alt="" ></button> 
    <button class="operation" v-else @click="stop"><img src="../../assets/player/stop.png" alt=""></button>
    <button class="operation"  @click="next"><img class="edit" src="../../assets/player/next.png" alt="" ></button> 
    </div>
    <span>{{name}}</span>
  </div>
</template>


<script>
import { ref } from 'vue'
export default {
  props:{
    name:String
  },
  setup(props,context) {
        // 创建audio实例
    let name = ref(props.name)
    let url = ref('http://127.0.0.1:8000/music/list/'+name.value)
    let playBoo = ref(false)
    const audio = new Audio(url.value) 
    audio.autoplay = true
    const play = () => {
      playBoo.value = !playBoo.value
      audio.play()
      localStorage.setItem('MusicName', name.value)
    }
    const stop = () =>{
      audio.pause()
      playBoo.value = !playBoo.value
    }
    // 下一首
    const next = () => {
      audio.pause()
      console.log('下一首');
      playBoo.value = !playBoo.value
      let nextName = null
      context.emit('eventEnd',(nextName)=>{
        name.value = nextName
        audio.src = 'http://127.0.0.1:8000/music/list/'+nextName
        audio.load()
        localStorage.setItem('MusicName', nextName)
      })
      audio.autoplay = true
      audio.play()
      playBoo.value = !playBoo.value
    }
    // 捕抓结束事件，结束后条用父组件的方法获取下一首歌名
    audio.addEventListener('ended',()=>{
      next()
    })
    // 上一首
    const last = () => {
      audio.pause()
      console.log('上一首');
      playBoo.value = !playBoo.value
      let lastName = null 
      context.emit('LastName', (lastName)=>{
        name.value = lastName
        audio.src = 'http://127.0.0.1:8000/music/list/'+lastName
        audio.load()
        localStorage.setItem('MusicName', lastName)
    })
      audio.autoplay = true
      audio.play()
      playBoo.value = !playBoo.value
    }

    return{
      name,
      playBoo,
      play,
      stop,
      last,
      next

    }
    
  },
}
</script>

<style lang="scss">
.player{
  width: 100%;
  height: 50px;
  color: #ffffff;
  // 透明效果
  opacity: 0.8;
  background-color: rgb(71, 70, 70);
  position: absolute;
  zoom: 1;
  .audio{
    position: relative;
    left: 2%;
  }
  span{
    position: relative;
    bottom: 40%;
    left: 40%;
  }
  .operation{
    background-color: rgb(71, 70, 70);
    border: 0;
    // width: 50px;
    margin-right: 10px;
    border-radius: 100%;
    border: 2px solid #FFF;
  }
  button:hover{
    cursor: pointer;
    img:hover{
    -webkit-filter: brightness(150%);
    filter: brightness(150%);

    }
  }
  .img{
    -webkit-filter: contrast(150%);
    width: 30px;
    margin-top: 20%;
    // border-radius: 100%;
    border: 2px solid #FFF;
    background-color: rgb(53, 52, 52);

  }
  .edit{
    width: 15px;
    margin-top: 3px;
  }
}
  
</style>