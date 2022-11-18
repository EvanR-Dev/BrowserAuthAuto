<template>
  <n-space vertical justify="center">
    <n-card style="height: 300px; width: 300px; justify-content: center; color: white" title="Welcome">
      <n-input v-model:value="email" placeholder="Email Address" size="large"/>
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
import { getAuth, deleteUser, onAuthStateChanged } from 'firebase/auth';

const router = useRouter();
const notif = useNotification();

const email = ref('');
const password = ref('');

const forgotPassword = () => {
  router.push({name: 'recoverAccount'});
};

const logIn = async () => {
  var error = await logInUser(email.value, password.value);
  
  if (error) {
      notif.error({ content: error, duration: 3000 });
  } else {
    // once they're logged in, check if they've verified their email
    const auth = getAuth();

    if (auth.currentUser.emailVerified) {
      router.push({name: 'webList'});
    } else {
      // not verified -> delete their account and have them sign up again
      deleteUser(auth.currentUser).then(() => {
        notif.error({ content: "Account deleted because email is not verified. Please sign up again and verify your email before attempting to log in.", duration: 10000 });
        router.push({name: 'signUp'});
      }).catch((error) => {
        notif.error({ content: error, duration: 3000 });
      });
    }
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