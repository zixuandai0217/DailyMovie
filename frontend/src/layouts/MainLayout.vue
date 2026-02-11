<template>
  <el-container class="layout-container">
    <Sidebar />
    <el-container class="main-container">
      <el-main class="main-content-area">
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup lang="ts">
import Sidebar from '@/components/Sidebar.vue'
</script>

<style scoped>
.layout-container {
  min-height: 100vh;
  background-color: #1a1a2e;
}

.main-container {
  margin-left: 240px;
  min-height: 100vh;
  transition: margin-left 0.3s;
}

.main-content-area {
  padding: 0;
  overflow-x: hidden;
  position: relative;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 768px) {
  .main-container {
    margin-left: 60px; /* Collapsed width */
  }
}
</style>
