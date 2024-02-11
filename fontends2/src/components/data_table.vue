<template>
  <div class="q-pa-md">
    <q-table
      title="Received data"
      :rows="deviceRows"
      :columns="columns"
      row-key="device_id"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useDevicesStore } from 'src/stores/global_var.ts'; // 引入 Pinia 存储

// 定义响应式数据
const columns = ref([
  { name: 'device_id', required: true, label: 'Device id', align: 'left', field: 'device_id', sortable: true },
  { name: 'x', align: 'center', label: 'Latitude', field: 'x' },
  { name: 'y', align: 'center', label: 'Longitude', field: 'y' },
  { name: 'altitude', align: 'center', label: 'Altitude', field: 'altitude' },
  { name: 'speed_x', align: 'center', label: 'Speed x', field: 'speed_x' },
  { name: 'speed_y', align: 'center', label: 'Speed y', field: 'speed_y' },
  { name: 'speed_z', align: 'center', label: 'Speed z', field: 'speed_z' },
  { name: 'posture', align: 'center', label: 'Posture', field: 'posture' },
  { name: 'time', align: 'center', label: 'Last Update Time', field: 'time' }
]);

const devicesStore = useDevicesStore(); // 使用 Pinia 存储

// 计算属性，将 devices 对象转换为数组形式，以便 q-table 使用
const deviceRows = computed(() => Object.values(devicesStore.devices));

// 生命周期钩子
onMounted(() => {
  devicesStore.fetchDevices(); // 从 Pinia 存储获取设备数据
  setInterval(() => {
    devicesStore.fetchDevices(); // 定期获取设备数据
  }, 100); // 每0.1秒更新一次
});
</script>
