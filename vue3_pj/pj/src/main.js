import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import {QuillEditor} from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'


const app = createApp(App)
const Vue = app.use(router).use(ElementPlus)
Vue.mount('#app')
app.component('QuillEditor', QuillEditor)