<template>
  <el-aside width="240px" class="sidebar">
    <div class="logo">
      <el-icon :size="24" color="#e50914"><Film /></el-icon>
      <span>DailyMovie</span>
    </div>
    
    <el-menu
      router
      :default-active="activeMenu"
      background-color="transparent"
      text-color="#ccc"
      active-text-color="#e50914"
      class="sidebar-menu"
    >
      <el-menu-item index="/">
        <el-icon><Compass /></el-icon>
        <span>每日推荐</span>
      </el-menu-item>
      
      <el-menu-item index="/ai">
        <el-icon><MagicStick /></el-icon>
        <span>AI 选片</span>
      </el-menu-item>
      
      <el-sub-menu index="lists">
        <template #title>
          <el-icon><Trophy /></el-icon>
          <span>精选榜单</span>
        </template>
        <el-menu-item index="/list/popular">热门电影</el-menu-item>
        <el-menu-item index="/list/top_rated">高分经典</el-menu-item>
        <el-menu-item index="/list/upcoming">即将上映</el-menu-item>
      </el-sub-menu>
      
      <el-sub-menu index="genres">
        <template #title>
          <el-icon><Menu /></el-icon>
          <span>分类浏览</span>
        </template>
        <el-menu-item 
          v-for="genre in genres" 
          :key="genre.id" 
          :index="`/genre/${genre.id}`"
        >
          {{ genre.name }}
        </el-menu-item>
      </el-sub-menu>
    </el-menu>
  </el-aside>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { movieApi } from '@/api/movie'

const route = useRoute()
const activeMenu = computed(() => route.path)
const genres = ref<{id: number, name: string}[]>([])

onMounted(async () => {
  try {
    const res = await movieApi.getGenres()
    genres.value = res
  } catch (e) {
    console.error(e)
  }
})
</script>

<style scoped>
.sidebar {
  background-color: #0f0f1a;
  border-right: 1px solid rgba(255, 255, 255, 0.05);
  height: 100vh;
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 1000;
  transition: width 0.3s;
}

.logo {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  font-size: 20px;
  font-weight: 800;
  color: #fff;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  letter-spacing: 1px;
}

.sidebar-menu {
  border-right: none;
  flex: 1;
  overflow-y: auto;
  padding-top: 10px;
}

:deep(.el-menu-item) {
  height: 50px;
  line-height: 50px;
  margin: 4px 0;
}

:deep(.el-menu-item:hover), :deep(.el-sub-menu__title:hover) {
  background-color: rgba(255, 255, 255, 0.05) !important;
}

:deep(.el-menu-item.is-active) {
  background-color: rgba(229, 9, 20, 0.1) !important;
  border-right: 3px solid #e50914;
}

/* Scrollbar */
.sidebar-menu::-webkit-scrollbar {
  width: 4px;
}
.sidebar-menu::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 2px;
}
</style>
