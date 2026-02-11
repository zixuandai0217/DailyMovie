<template>
  <div class="home-page">
    <!-- 背景 -->
    <div class="background" :style="backgroundStyle"></div>

    <!-- 主要内容 -->
    <div class="main-content" v-if="currentMovie">
      <!-- 海报 -->
      <div class="poster-section">
        <img :src="posterUrl" :alt="currentMovie?.title" class="poster" />
      </div>

      <!-- 电影信息 -->
      <div class="info-section">
        <h1 class="movie-title">{{ currentMovie.title }}</h1>
        <h2 class="movie-title-en" v-if="currentMovie.title_en">{{ currentMovie.title_en }}</h2>

        <div class="movie-meta">
          <span v-if="currentMovie.release_date">{{ currentMovie.release_date.slice(0, 4) }}</span>
          <span v-if="currentMovie.runtime">{{ currentMovie.runtime }}分钟</span>
          <span class="rating">★ {{ currentMovie.vote_average.toFixed(1) }}</span>
        </div>

        <div class="genres" v-if="currentMovie.genres?.length">
          <span v-for="genre in currentMovie.genres" :key="genre" class="genre-tag">
            {{ genre }}
          </span>
        </div>

        <p v-if="currentMovie.tagline" class="tagline">{{ currentMovie.tagline }}</p>

        <div class="overview-section">
          <h3>剧情简介</h3>
          <p class="overview-zh">{{ currentMovie.overview }}</p>
          <p class="overview-en" v-if="currentMovie.overview_en">{{ currentMovie.overview_en }}</p>
        </div>

        <div class="buttons">
          <button class="btn-primary" @click="goToDetail">立即观看</button>
          <button class="btn-secondary" @click="refreshMovie">换一个</button>
        </div>
      </div>
    </div>

    <!-- 加载中 -->
    <div class="loading" v-else-if="isLoading">
      <p>正在为您推荐电影...</p>
    </div>

    <!-- 错误 -->
    <div class="error" v-else-if="error">
      <p>{{ error }}</p>
      <button @click="refreshMovie">重试</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { storeToRefs } from 'pinia'
import { useMovieStore } from '@/stores/movie'

const router = useRouter()
const store = useMovieStore()

// Why: Ensure reactivity for destructured store state
const { currentMovie, isLoading, error } = storeToRefs(store)
const { fetchRandomMovie } = store

const backgroundStyle = computed(() => {
  const url = store.backdropUrl
  if (url) {
    return { backgroundImage: `url(${url})` }
  }
  return { backgroundColor: '#1a1a2e' }
})

const posterUrl = computed(() => store.posterUrl || '')

function goToDetail() {
  if (currentMovie.value) {
    router.push(`/movie/${currentMovie.value.tmdb_id}`)
  }
}

function refreshMovie() {
  fetchRandomMovie()
}

onMounted(() => {
  fetchRandomMovie()
})
</script>

<style>
.home-page {
  min-height: 100vh;
  position: relative;
  color: #ffffff;
  padding: 40px;
}

.background {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-size: cover;
  background-position: center;
  z-index: -1;
}

.background::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(to right, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 50%, rgba(0,0,0,0.3) 100%);
}

.main-content {
  display: flex;
  gap: 50px;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.poster-section {
  flex-shrink: 0;
}

.poster {
  width: 300px;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}

.info-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.movie-title {
  font-family: 'Noto Sans SC', sans-serif;
  font-size: 42px;
  font-weight: bold;
  margin: 0 0 10px 0;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

.movie-title-en {
  font-family: 'Montserrat', sans-serif;
  font-size: 24px;
  font-weight: 400;
  color: #e0e0e0;
  margin: 0 0 25px 0;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}

.movie-meta {
  display: flex;
  gap: 20px;
  color: #aaa;
  font-size: 16px;
  margin-bottom: 20px;
}

.rating {
  color: #fbbf24;
  font-weight: bold;
}

.genres {
  display: flex;
  gap: 10px;
  margin-bottom: 25px;
  flex-wrap: wrap;
}

.genre-tag {
  background: rgba(255,255,255,0.15);
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 14px;
}

.tagline {
  font-style: italic;
  color: #aaa;
  margin-bottom: 25px;
  font-size: 16px;
}

.overview-section {
  margin-bottom: 30px;
}

.overview-section h3 {
  font-size: 14px;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 10px;
}

.overview-section p {
  font-size: 16px;
  line-height: 1.8;
  color: #ddd;
}

.overview-zh {
  font-family: 'Noto Sans SC', sans-serif;
  margin-bottom: 15px;
}

.overview-en {
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
  color: #bbb;
  font-style: italic;
}

.buttons {
  display: flex;
  gap: 15px;
}

.btn-primary {
  background: #e50914;
  color: white;
  border: none;
  padding: 14px 32px;
  font-size: 16px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
}

.btn-primary:hover {
  background: #f40612;
}

.btn-secondary {
  background: rgba(255,255,255,0.2);
  color: white;
  border: 1px solid rgba(255,255,255,0.3);
  padding: 14px 32px;
  font-size: 16px;
  border-radius: 8px;
  cursor: pointer;
}

.btn-secondary:hover {
  background: rgba(255,255,255,0.3);
}

.loading, .error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  position: relative;
  z-index: 1;
  text-align: center;
}

.error p {
  color: #ff6b6b;
  font-size: 18px;
  margin-bottom: 20px;
  max-width: 600px;
  line-height: 1.6;
}

@media (max-width: 768px) {
  .main-content {
    flex-direction: column;
    align-items: center;
  }

  .poster {
    width: 200px;
  }

  .movie-title {
    font-size: 28px;
    text-align: center;
  }

  .movie-meta {
    justify-content: center;
  }

  .genres {
    justify-content: center;
  }

  .buttons {
    justify-content: center;
  }
}
</style>