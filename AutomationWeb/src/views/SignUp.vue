<template>
    <n-space vertical justify="center">
      <n-card style="height: 300px; width: 300px; justify-content: center; color: white" title="Account Information">
        <n-input v-model:value="email" placeholder="Email Address" size="large"/>
        <n-input
          v-model:value="password"
          placeholder="Password"
          type="password"
          show-password-on="click"
          size="large"
        />
        <br/>
        <n-input
          v-model:value="confirmPassword"
          placeholder="Confirm Password"
          type="password"
          show-password-on="click"
          size="large"
        />
        <br/>
        <n-button class="submit" @click="signUp">Sign Up</n-button>
      </n-card>
      <h3 class="outside">Already have an account?</h3>
      <n-button color="white" text-color="black" style="margin-left: 110px" size="large" @click="logIn">Log In</n-button>
  </n-space>
  </template>
  
  <script setup lang="ts">
  import { NCard, NInput, NSpace, NButton, useNotification } from 'naive-ui';
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { createUser } from '@/services/UserServices';

  const router = useRouter();
  const notif = useNotification();
  
  const email = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  
  const logIn = () => {
    router.push({ name: 'home' });
  }
  
  const signUp = async () => {
    var error = await createUser(email.value, password.value);
    if (error) {
        notif.error({ content: error, duration: 3000 });
    }
  }
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
  </style>