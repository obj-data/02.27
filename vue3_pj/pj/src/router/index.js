import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/home',
    name: 'index',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../User/login.vue')
  },
  {
    path: '/blog',
    name: 'Blog',
    component: () => import('../views/showBlog/Blog.vue')
  },
  {
    path: '/myblog',
    name: 'MyBlog',
    component: () => import('../views/MyBlog/Myblog.vue')
  },
  {
    path:'/redact',
    name: 'Redact',
    component: () => import('../views/MyBlog/Redact.vue')
  },
  {
    path:'/music',
    name:'Music',
    component: () => import('../views/musics/Music.vue')
  },
  {
    path:'/music/list',
    name:"MusicList",
    component: () => import("../views/musics/MusicList.vue")
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
