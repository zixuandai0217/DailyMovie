<template>
  <div class="ai-page">
    <div class="ai-header">
      <h1>AI 智能选片</h1>
      <p>告诉我你想看什么，AI 为你推荐</p>
    </div>
    
    <div class="ai-input-container">
      <el-input
        v-model="prompt"
        type="textarea"
        :rows="3"
        placeholder="例如：我想看一部 90 年代的悲伤爱情电影..."
        class="ai-input"
        @keydown.enter.ctrl="handleSearch"
      />
      <el-button 
        type="primary" 
        size="large" 
        class="ai-btn" 
        :loading="loading"
        @click="handleSearch"
      >
        <el-icon><MagicStick /></el-icon>
        生成推荐
      </el-button>
    </div>
    
    <div class="results-container" v-if="movies.length > 0">
      <div class="movies-grid">
        <div 
          v-for="movie in movies" 
          :key="movie.id" 
          class="movie-card"
          @click="goToDetail(movie.tmdb_id)"
        >
          <img :src="getImageUrl(movie.poster_path)" class="card-poster" />
          <div class="card-info">
            <div class="card-rating">
              <el-icon><StarFilled /></el-icon>
              {{ movie.vote_average.toFixed(1) }}
            </div>
            <h3 class="card-title">{{ movie.title }}</h3>
          </div>
        </div>
      </div>
    </div>
    
    <div v-else-if="searched && !loading" class="empty-state">
      <el-empty description="未找到相关电影，换个说法试试？" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { MagicStick, StarFilled } from '@element-plus/icons-vue'
import { movieApi, type Movie } from '@/api/movie'
import { ElMessage } from 'element-plus'

const router = useRouter()
const prompt = ref('')
const loading = ref(false)
const movies = ref<Movie[]>([])
const searched = ref(false)

async function handleSearch() {
  if (!prompt.value.trim()) return
  
  loading.value = true
  searched.value = true
  movies.value = []
  
  try {
    const res = await movieApi.aiRecommend(prompt.value)
    movies.value = res.movies
  } catch (e) {
    ElMessage.error('AI 推荐失败，请稍后重试')
    console.error(e)
  } finally {
    loading.value = false
  }
}

function getImageUrl(path: string | null) {
  return path ? `https://image.tmdb.org/t/p/w500${path}` : 'https://via.placeholder.com/300x450?text=No+Poster'
}

function goToDetail(id: number) {
  router.push(`/movie/${id}`)
}
</script>

<style scoped>
.ai-page {
  padding: 40px;
  max-width: 1200px;
  margin: 0 auto;
  color: #fff;
}

.ai-header {
  text-align: center;
  margin-bottom: 40px;
}

.ai-header h1 {
  font-size: 36px;
  margin-bottom: 10px;
  background: linear-gradient(45deg, #e50914, #ff6b6b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.ai-input-container {
  max-width: 800px;
  margin: 0 auto 60px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.ai-input :deep(.el-textarea__inner) {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #fff;
  font-size: 16px;
  border-radius: 12px;
  padding: 15px;
}

.ai-input :deep(.el-textarea__inner:focus) {
  border-color: #e50914;
  box-shadow: 0 0 0 1px #e50914;
}

.ai-btn {
  align-self: flex-end;
  background: #e50914;
  border: none;
  border-radius: 8px;
  padding: 12px 30px;
  font-weight: bold;
}

.ai-btn:hover {
  background: #f40612;
}

.movies-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 30px;
}

.movie-card {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.3s;
  aspect-ratio: 2/3;
}

.movie-card:hover {
  transform: scale(1.05);
  z-index: 10;
}

.card-poster {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-info {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 20px 10px 10px;
  background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
  opacity: 0;
  transition: opacity 0.3s;
}

.movie-card:hover .card-info {
  opacity: 1;
}

.card-title {
  font-size: 14px;
  margin: 5px 0 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-rating {
  color: #fbbf24;
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-weight: bold;
}
</style>
