<template>
  <n-space vertical justify="center">
    <n-card style="height: 300px; width: 300px; justify-content: center; color: white" title="Welcome">
      <n-input v-model="email" placeholder="Email" size="large"/>
      <n-input
        v-model="password"
        placeholder="Password"
        type="password"
        show-password-on="click"
        size="large"
      />
      <n-button class="text-button" text @click="forgotPassword">
        Forgot Password
      </n-button>
      <br/>
      <n-button @click="logIn">Log In</n-button>
    </n-card>
    <h3 class="outside">Don't have an account?</h3>
    <n-button color="white" text-color="black" style="margin-left: 110px" size="large" @click="signUp">Sign Up</n-button>
</n-space>
</template>

<script setup lang="ts">
import { NCard, NInput, NSpace, NButton } from 'naive-ui';
import { ref } from 'vue';

const email = ref('');
const password = ref('');

const forgotPassword = () => {
  //do something
}

const logIn = () => {
  //do something
}

const signUp = () => {
  //do something
}
</script>

<style scoped>
.n-input {
  margin-top: 10px;
}
.text-button {
  margin-top: 20px;
  margin-bottom: 30px;
}
.outside {
  text-align: center;
  flex: 0;
}
</style>