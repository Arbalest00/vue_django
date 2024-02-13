// src/stores/devicesStore.ts
import { defineStore } from 'pinia';
import { api } from 'boot/axios';
import type {  DeviceData } from 'src/types/interface.ts';
export const useDevicesStore = defineStore('devices', {
  state: () => ({
    devices: {} as Record<string, DeviceData>, // 明确指定 devices 对象的类型
    q_count: 0,
    devices_count: 0,
    map:null,
    map_label_layer:null
  }),
  actions: {
    fetchDevices() {
      api.get('/usr_data')
        .then((response) => {
          const devicesData: DeviceData[] = response.data;
          devicesData.forEach((device: DeviceData) => {
            this.devices[device.device_id] = device;
          });
          this.devices_count = Object.keys(this.devices).length;
          this.q_count+=1;
        })
        .catch(error => {
          console.error('Error fetching devices data:', error);
        });
    }
  },
});
