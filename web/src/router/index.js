import { createRouter, createWebHashHistory } from 'vue-router'
import imgUp from "@/components/ImgUp";

const routes = [
  {
    path: '/',
    name: 'home',
    component: imgUp
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
