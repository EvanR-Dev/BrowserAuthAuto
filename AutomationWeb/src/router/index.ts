import { createRouter, createWebHistory } from 'vue-router'
import LogIn from '@/views/LogIn.vue'
import SignUp from '@/views/SignUp.vue'
import Recovery from '@/views/Recovery.vue'
import EmailVerification from '@/views/EmailVerification.vue'

import { sendEmailVerification } from 'firebase/auth'

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
    },
    {
      path: '/email_verification',
      name: 'emailVerification',
      component: EmailVerification
    }
    {
      path: '/web-list',
      name: 'webList',
      component: WebList
    }
  ]
})

export default router
