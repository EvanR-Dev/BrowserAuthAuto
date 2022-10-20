<template>
  <n-space vertical justify="center">
    <n-card style="height: 200px; width: 300px; justify-content: center; color: white" title="Recover Account">
      <n-input v-model:value="email" placeholder="Email Address" size="large" @input="print" />
      <br/>
      <br/>
      <n-button id='send' @click="sendEmail">
        Send Email
      </n-button>
    </n-card>

    <h3 class="outside">BrowserAuthAuto</h3>

  </n-space>
</template>


<script setup lang="ts">

import { NCard, NInput, NSpace, NButton, useNotification } from 'naive-ui';
//import { getAuth } from "firebase/auth";
import { recoverUser } from '@/services/UserServices';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const router = useRouter();
const notif = useNotification();
const email = ref('');

const print = (input: string) => {
  console.log(email.value);
}

const sendEmail = async () => {

  console.log(email.value);
  var error = await recoverUser(email.value);
  if (error) {
    notif.error({ content: error, duration: 3000 });
  }
};

</script>


<style scoped>
.n-input {
  margin-top: 10px;
}

#send {
  
}

.outside {
  text-align: center;
  flex: 0;
}
</style>