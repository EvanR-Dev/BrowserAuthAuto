<template>
  <n-space vertical justify="center">
    <n-card style="height: 300px; width: 300px; justify-content: center; color: white" title="Welcome">
      <n-input v-model:value="email" placeholder="Email Address" size="large" @input="print"/>
      <n-input
        v-model:value="password"
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
import { NCard, NInput, NSpace, NButton, useNotification } from 'naive-ui';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { logInUser } from '@/services/UserServices';

const router = useRouter();
const notif = useNotification();

const email = ref('');
const password = ref('');

const print = (input: string) => {
  console.log(email.value);
}

const forgotPassword = () => {
  //do something
};

const logIn = async () => {
  console.log(email.value);
  var error = await logInUser(email.value, password.value);
    if (error) {
        notif.error({ content: error, duration: 3000 });
    }
};

const signUp = () => {
  router.push({ name: 'signUp'});
};

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