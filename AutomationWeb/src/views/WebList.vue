<template>
  <div>
    <n-space justify="end">
      <n-button
        color="white"
        text-color="black"
        style="margin-left: 110px; margin-bottom: 10px"
        size="large"
        @click="logOut"
      >
        Log Out
      </n-button>
    </n-space>
    <n-space vertical justify="center">
      <n-card
        style="
          height: 500px;
          width: 700px;
          justify-content: center;
          color: white;
        "
      >
        <n-table style="color: black" :bordered="true" :single-line="false">
          <thead style="color: white">
            Blank space
          </thead>
          <tbody>
            <tr class="rowStyle" v-for="website in websites" :key="website.id">
              <td
                class="dataStyle"
                style="width: 350px; display: flex; align-items: center"
              >
                <div
                  style="
                    height: 70px;
                    width: 70px;
                    display: flex;
                    align-items: center;
                  "
                >
                  <img style="object-fit: cover; max-width : 100%" :src="website.logo" />
                </div>
                <div
                  style="
                    font-size: x-large;
                    padding-left: 25px;
                    padding-bottom: 10px;
                  "
                >
                  {{ website.name }}
                </div>
              </td>
              <td>
                <n-button class="dataStyle" @click="login"> Login </n-button>
              </td>
            </tr>
          </tbody>
        </n-table>
      </n-card>
    </n-space>
  </div>
</template>
<script setup lang="ts">
import { NCard, NInput, NSpace, NButton, useNotification } from "naive-ui";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const logOut = () => {
  router.push({ name: "home" });
};

const login = () => {};

const websites = [
  {
    id: 1,
    name: "Inzernet",
    link: "",
    logo: "/Logo/Inzernet.png",
  },
  {
    id: 2,
    name: "Amazon",
    link: "",
    logo: "/Logo/Amazon.png",
  },
  {
    id: 3,
    name: "Azure",
    link: "",
    logo: "/Logo/Azure.png",
  },
];
</script>

<style scoped>
tr.rowStyle {
  border: 2px solid black;
  display: flex;
  justify-content: space-between;
  width: 650px;
  margin-bottom: 20px;
  padding: 10px;
  align-items: center;
}
.dataStyle {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>
