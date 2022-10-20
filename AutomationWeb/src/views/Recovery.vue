<template>
    <n-space vertical justify="center">
      <n-card style="height: 300px; width: 300px; justify-content: center; color: white" title="Recover Account">
        <n-input v-model:value="email" placeholder="Email Address" size="large" @input="print"/>
        
        <n-button class="text-button" text @click="sendEmail">
          Send eMail
        </n-button>
        <br/>
      </n-card>
      <h3 class="outside">outside</h3>
      
  </n-space>
  </template>


<script setup lang="ts">

import { NCard, NInput, NSpace, NButton, useNotification } from 'naive-ui';
// import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();


const sendEmail = () => {
  // do something with firebase
  // also validate email exists for an account?
};

</script>



<style scoped>
.n-input {
  margin-top: 10px;
}
.text-button {
  margin-top: 20px;
  margin-bottom: 30px;
  justify-self: center;
}
.outside {
  text-align: center;
  flex: 0;
}
</style>