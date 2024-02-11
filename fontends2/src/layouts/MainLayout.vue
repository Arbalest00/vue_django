<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar class="toolbar_top">
        
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />
        <q-toolbar-title>
          Drone WEBUI
        </q-toolbar-title>
        <q-btn dense flat round icon="menu" @click="toggleRightDrawer" />
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered class="drawer_left">
      <q-scroll-area class="fit">
        <q-list padding class="menu-list">
          <router-link to="/main" custom v-slot="{navigate}">
            <q-item clickable v-ripple @click="navigate">
              <q-item-section avatar>
                <q-icon name="inbox" />
              </q-item-section>

              <q-item-section>
                Main
              </q-item-section>
            </q-item>
          </router-link>
          <router-link to="/side0" custom v-slot="{navigate}">
            <q-item clickable v-ripple @click="navigate">
              <q-item-section avatar>
                <q-icon name="drafts" />
              </q-item-section>

              <q-item-section>
                Map
              </q-item-section>
            </q-item>
          </router-link>
        </q-list>
      </q-scroll-area>
    </q-drawer>


    <q-drawer show-if-above v-model="rightDrawerOpen" side="right" bordered class="drawer_right">
      <q-card flat bordered class="col-sm-6 col-lg-3 mb-5">
        <q-card-section :class="`text-white ${devicesStore.q_count !== 0 ? 'bg-green' : 'bg-red'}`" style="display: flex;justify-content: center;
    align-items: center">
          <div class="text-h6">{{ devicesStore.q_count !== 0 ? '后端已连接' : '后端未连接' }}</div>
        </q-card-section>
      </q-card>
      <q-separator />
      <q-scroll-area class="fit">
  <q-card flat bordered class="col-sm-6 col-lg-3 mb-5 card_right" v-for="device in sortedData" :key="device.device_id" style="display: flex;justify-content: center;
    align-items: center">
          <q-card-section :style="{ backgroundColor: getColorById(device.device_id), color: 'white' }">
            <div class="text-h6">Device_ID: {{ device.device_id }}</div>
          </q-card-section>
          <q-separator />
          <q-card-section class="flex flex-center q-pa-md">
            经度: {{ device.x }} <br/> 纬度: {{ device.y }}
          </q-card-section>
          <q-separator />
          <q-card-section class="flex flex-center q-pa-md">
            {{ timeSince(device.time) }}更新
          </q-card-section>
        </q-card>
      </q-scroll-area>
    </q-drawer>


    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar class="toolbar_foot">
        <q-toolbar-title>
          <div>Drone WEBUI</div>
        </q-toolbar-title>
        <div style="font-size: 26px;">
            <p>当前时间：{{ currentTime }}</p>
        </div>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useDevicesStore } from 'src/stores/global_var.ts'; // 引入 Pinia 存储

const devicesStore = useDevicesStore(); // 使用 Pinia 存储
const data = computed(() => Object.values(devicesStore.devices));
const leftDrawerOpen = ref(false);
const rightDrawerOpen = ref(false);
const currentTime = ref(formatTime());
function getColorById(id) {
  let hash = 0;
  for (let i = 0; i < id.length; i++) {
    hash = id.charCodeAt(i) + ((hash << 5) - hash);
  }
  const color = (hash & 0x00FFFFFF)
    .toString(16)
    .toUpperCase();
  return "#" + "00000".substring(0, 6 - color.length) + color;
}
function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}

function toggleRightDrawer() {
  rightDrawerOpen.value = !rightDrawerOpen.value;
}

function formatTime() {
  const now = new Date();
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  const seconds = now.getSeconds().toString().padStart(2, '0');
  return `${hours}:${minutes}:${seconds}`;
}
const sortedData = computed(() => {
  const devicesArray = Object.values(devicesStore.devices);
  const sorted = devicesArray.sort((a, b) => {
    const timeA = new Date(a.time).getTime();
    const timeB = new Date(b.time).getTime();
    return timeB - timeA; // 升序排序
  });
  //console.log(devicesArray);
  //console.log(sorted);
  return sorted;
});
function timeSince(dateString) {
  const date = new Date(dateString);
  const seconds = Math.floor((new Date() - date) / 1000);

  let interval = seconds / 31536000;
  if (interval > 1) {
    return Math.floor(interval) + " 年前";
  }
  interval = seconds / 2592000;
  if (interval > 1) {
    return Math.floor(interval) + " 个月前";
  }
  interval = seconds / 86400;
  if (interval > 1) {
    return Math.floor(interval) + " 天前";
  }
  interval = seconds / 3600;
  if (interval > 1) {
    return Math.floor(interval) + " 小时前";
  }
  interval = seconds / 60;
  if (interval > 1) {
    return Math.floor(interval) + " 分钟前";
  }
  return Math.floor(seconds) + " 秒前";
}

onMounted(() => {
  setInterval(() => {
    currentTime.value = formatTime();
  }, 1000);
});
</script>

<style lang="scss">
  .toolbar_top{
    background: #0F2027;  /* fallback for old browsers */
    background: -webkit-linear-gradient(to right, #2C5364, #203A43, #0F2027);  /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(to right, #2C5364, #203A43, #0F2027); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  }
  .toolbar_foot {
    background: #0F2027;  /* fallback for old browsers */
    background: -webkit-linear-gradient(to left, #2C5364, #203A43, #0F2027);  /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(to left, #2C5364, #203A43, #0F2027); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  }
  .drawer_left {
    background: #FFFFFF;  /* fallback for old browsers */
  }
  .drawer_right {
    background: #FFFFFF;  /* fallback for old browsers */
  }
  .card_right{
    margin-bottom: 10px;
  }
</style>
