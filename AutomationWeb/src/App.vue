<template>
  <n-notification-provider>
    <RouterView />
  </n-notification-provider>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router'
import { NNotificationProvider } from 'naive-ui'
</script>