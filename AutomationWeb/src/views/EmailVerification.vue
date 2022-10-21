<template>
    <n-space vertical justify="center">
      <n-card class="card" title="Email Verification">
        <h3 class="message">We have sent a verification link to the email you've provided. Please click on the link now to verify your email before moving forward. If you don't see it, make sure you check your spam folder.</h3>
      </n-card>
    </n-space>
  </template>
  
  <script setup lang="ts">
  import { NCard, NInput, NSpace, NButton, useNotification } from 'naive-ui';
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';

  const router = useRouter();
  const notif = useNotification();
  

  </script>
  
  <style scoped>
  .n-input {
    margin-top: 10px;
  }
  .submit {
    margin-top: 30px;
  }
  .outside {
    text-align: center;
    flex: 0;
  }
  .message {
    text-align: center;
    flex: 0;
    color: black;
    font-size: small;
  }
  .card {
    align-items: center;
    justify-content: center;
    height: 300px;
    width: 300px;
  }
  </style>