<template>
  <div id="container"></div>
</template>
<script setup>
import { onMounted, onUnmounted } from "vue";
import AMapLoader from "@amap/amap-jsapi-loader";
import { useDevicesStore } from 'src/stores/global_var.ts'; // 引入 Pinia 存储
const devicesStore = useDevicesStore(); // 使用 Pinia 存储
onMounted(() => {
  AMapLoader.load({
    key: "", // 申请好的Web端开发者Key，首次调用 load 时必填
    version: "2.0", // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
    plugins: [
      "AMap.HawkEye", //鹰眼，显示缩略图
      "AMap.MapType", //图层切换，用于几个常用图层切换显示
      "AMap.LabelMarker",
      "AMap.Polyline",
    ], // 需要使用的的插件列表
  })
    .then((AMap) => {
      devicesStore.map = new AMap.Map("container", {
        viewMode: "3D", // 是否为3D地图模式
        zoom: 1, // 初始化地图级别
        center: [0, 0], // 初始化地图中心点位置
      });

      devicesStore.map.addControl(new AMap.HawkEye());
      devicesStore.map.addControl(new AMap.MapType());
      devicesStore.map_label_layer = new AMap.LabelsLayer({
        zooms: [3, 20],
        zIndex: 1000,
        collision: true, //该层内标注是否避让
        allowCollision: true, //不同标注层之间是否避让  
      });
      devicesStore.map.add(devicesStore.map_label_layer);
    })
    .catch((e) => {
      console.log(e);
    });
});

onUnmounted(() => {
  devicesStore.map?.destroy();
  devicesStore.map_label_layer?.destroy();
});
</script>
<style  scoped>
#container {
  padding: 0px;
  margin: 0px;
  width: 100%;
  height: 100%;
}
</style>