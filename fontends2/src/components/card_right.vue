<template>
    <q-card flat bordered class="col-sm-6 col-lg-3 mb-5">
        <q-card-section :class="`text-white ${devicesStore.q_count !== 0 ? 'bg-green' : 'bg-red'}`" style="display: flex;justify-content: center;
    align-items: center">
            <div class="text-h6">{{ devicesStore.q_count !== 0 ? '后端已连接' : '后端未连接' }}</div>
        </q-card-section>
    </q-card>
    <q-separator />
    <q-scroll-area class="fit">
        <q-card flat bordered class="col-sm-6 col-lg-3 mb-5 card_right " v-for="device in sortedData"
            :key="device.device_id">
            <q-card-section :style="{ backgroundColor: deviceColors[device.device_id], color: 'white' }">
                <div class="text-h6">Device_ID: {{ device.device_id }}</div>
            </q-card-section>
            <q-separator />
            <q-card-section class="flex flex-center q-pa-md">
                经度: {{ device.x }} <br /> 纬度: {{ device.y }}
                <q-btn class="btn-fixed-width" color="primary" label="定位到此设备"
                    @click="setMapCenter([device.x, device.y])"></q-btn>
            </q-card-section>
            <q-separator />
            <q-card-section class="flex flex-center q-pa-md">
                {{ timeSince(device.time) }}更新
            </q-card-section>
        </q-card>
    </q-scroll-area>
</template>
<script setup>
import { computed, watchEffect, ref, reactive } from 'vue';
import { useDevicesStore } from 'src/stores/global_var.ts'; // 引入 Pinia 存储
const devicesStore = useDevicesStore(); // 使用 Pinia 存储
const data = computed(() => Object.values(devicesStore.devices));
const sortedData = computed(() => {
    const devicesArray = Object.values(devicesStore.devices);
    const sorted = devicesArray.sort((a, b) => {
        const timeA = new Date(a.time).getTime();
        const timeB = new Date(b.time).getTime();
        return timeB - timeA;
    });
    //console.log(devicesArray);
    //console.log(sorted);
    return sorted;
});
const deviceColors = ref({});
const lastDeviceCoordinates = reactive({});
const deviceUpdateCount = reactive({}); // 存储每个设备的更新计数
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
watchEffect(() => {
    const devices = Object.values(devicesStore.devices);
    devices.forEach(device => {
        deviceColors.value[device.device_id] = getColorById(device.device_id);
        const lastCoords = lastDeviceCoordinates[device.device_id];
        const currentCoords = [device.x, device.y];
        if (!deviceUpdateCount[device.device_id]) {
            deviceUpdateCount[device.device_id] = 0; // 初始化计数器
        }
        if ((!lastCoords || lastCoords[0] !== currentCoords[0] || lastCoords[1] !== currentCoords[1]) && devicesStore.map_label_layer != null) {
            deviceUpdateCount[device.device_id] += 1; // 更新计数器
            const icon = {
                type: 'image',
                image: 'https://webapi.amap.com/theme/v1.3/markers/n/mark_b.png',
                size: [6, 9],
                anchor: 'bottom-center',
            };
            const text = {
                content: device.device_id + " (" + deviceUpdateCount[device.device_id] + "号轨迹)", //要展示的文字内容
                direction: "right", //文字方向，有 icon 时为围绕文字的方向，没有 icon 时，则为相对 position 的位置
                offset: [-20, -5], //在 direction 基础上的偏移量
                //文字样式
                style: {
                    fontSize: 22, //字体大小
                    fillColor: deviceColors.value[device.device_id], //字体颜色
                    strokeColor: deviceColors.value[device.device_id], //描边颜色
                    strokeWidth: 2, //描边宽度
                },
            };
            const labelMarker = new AMap.LabelMarker({
                name: "标注", //此属性非绘制文字内容，仅为标识使用
                position: [device.x, device.y],
                zIndex: device.altitude,
                rank: 1, //避让优先级
                text: text, //标注文本，将 text 对象传给 text 属性
                icon: icon
            });
            devicesStore.map_label_layer.add(labelMarker);
            lastDeviceCoordinates[device.device_id] = currentCoords;
            console.log("label_add");
        }
    });

});
function setMapCenter(coordinates) {
    if (devicesStore.map) {
        devicesStore.map.setZoomAndCenter(12, coordinates);
    }
}
function timeSince(dateString) {
    const date = new Date(dateString);
    const seconds = Math.floor((new Date() - date) / 1000);

    let interval = seconds / 31536000;
    if (interval > 1) {
        return Math.floor(Math.max(interval, 0)) + " 年前";
    }
    interval = seconds / 2592000;
    if (interval > 1) {
        return Math.floor(Math.max(interval, 0)) + " 个月前";
    }
    interval = seconds / 86400;
    if (interval > 1) {
        return Math.floor(Math.max(interval, 0)) + " 天前";
    }
    interval = seconds / 3600;
    if (interval > 1) {
        return Math.floor(Math.max(interval, 0)) + " 小时前";
    }
    interval = seconds / 60;
    if (interval > 1) {
        return Math.floor(Math.max(interval, 0)) + " 分钟前";
    }
    // 直接使用Math.max确保秒数不会小于0
    return Math.floor(Math.max(seconds, 0)) + " 秒前";
}

</script>
<style lang="scss">
.card_right {
    margin-bottom: 10px;
}
</style>