<template>
  <div class="q-pa-md row items-start q-gutter-md">

    <q-card flat bordered class="col-sm-6 col-lg-3 mb-3 mb-lg-5">
      <q-card-section class="bg-primary text-white my_card">
        <div class="text-h6">当前已连接设备数</div>
      </q-card-section>

      <q-separator />

      <q-card-section class="flex flex-center q-pa-md">
        <div class="text-h6">{{ devicesStore.devices_count }}</div>
      </q-card-section>
    </q-card>
    <q-card flat bordered class="col-sm-6 col-lg-3 mb-3 mb-lg-5">
      <q-card-section class="bg-purple text-white my_card">
        <div class="text-h6">数据请求成功次数</div>
      </q-card-section>

      <q-separator />

      <q-card-section class="flex flex-center q-pa-md">
        <div class="text-h6">{{devicesStore.q_count}}</div>
      </q-card-section>

    </q-card>

  </div>
</template>

<script setup>
import { useDevicesStore } from 'src/stores/global_var.ts'; // 引入 Pinia 存储
const devicesStore = useDevicesStore();
</script>

<style lang="scss" >
  .my_card {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
