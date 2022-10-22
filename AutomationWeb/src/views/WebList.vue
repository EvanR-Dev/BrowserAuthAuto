<template>
    <div>
        
    <n-space justify="end">
        <n-button color="white" text-color="black" style="margin-left: 110px; margin-bottom: 10px" size="large" @click="logOut">Log Out</n-button>
    </n-space>
    <n-space vertical justify="center">
    <n-card style="height: 500px; width: 400px; justify-content: center; color: white" title="Website Lists">
        <n-table style = "color: black" :bordered="true" :single-line="false">   
            <tbody>
      <tr class = "border_bottom" >
        <td style = "padding-right: 229px">1. Azure</td>
        <td><n-button style="margin-bottom: 10px">Login</n-button></td>
      </tr>
      
    </tbody>
  </n-table>

    </n-card>
    </n-space>
</div>
</template>

<script setup lang="ts">
import { NCard, NInput, NSpace, NButton, useNotification } from 'naive-ui';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();


const logOut = () => {
  router.push({ name: 'home'});
};
</script>

<style scoped>

tr.border_bottom td {
  border-bottom: 1px solid black;
}
</style>
