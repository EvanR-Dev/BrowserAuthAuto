import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { initializeApp } from 'firebase/app'

import App from './App.vue'
import router from './router'

import './assets/main.css'

const firebaseConfig = {
    apiKey: "AIzaSyB1mWGGgltQb_g9Phh1V-qeIzHZ6y8wXD8",
    authDomain: "browserauthauto.firebaseapp.com",
    projectId: "browserauthauto",
    storageBucket: "browserauthauto.appspot.com",
    messagingSenderId: "153868310004",
    appId: "1:153868310004:web:ae7f8095f6cc9045d3d5a1"
};
  
// Initialize Firebase
initializeApp(firebaseConfig);

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
