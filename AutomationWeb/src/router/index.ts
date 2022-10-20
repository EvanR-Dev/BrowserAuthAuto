import { createRouter, createWebHistory } from 'vue-router'
import LogIn from '@/views/LogIn.vue'
import SignUp from '@/views/SignUp.vue'
import Recovery from '@/views/Recovery.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LogIn
    },
    {
      path: '/sign_up',
      name: 'signUp',
      component: SignUp
    },
    {
      path: '/recover',
      name: 'recoverAccount',
      component: Recovery
    }
  ]
})

export default router
