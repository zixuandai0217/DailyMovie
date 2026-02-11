<template>
  <div class="list-page">
    <div class="list-header">
      <h1>{{ title }}</h1>
    </div>
    
    <div class="loading-state" v-if="loading">
      <el-icon class="is-loading" :size="40"><Loading /></el-icon>
    </div>
    
    <div class="movies-grid" v-else>
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
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { Loading, StarFilled } from '@element-plus/icons-vue'
import { movieApi, type Movie } from '@/api/movie'

const route = useRoute()
const router = useRouter()
const movies = ref<Movie[]>([])
const loading = ref(true)
const title = ref('')

async function fetchData() {
  loading.value = true
  movies.value = []
  
  try {
    if (route.name === 'GenreList') {
      const genreId = Number(route.params.id)
      title.value = "分类浏览" 
      const res = await movieApi.getMoviesByGenre(genreId)
      movies.value = res.movies
      
      const genres = await movieApi.getGenres()
      const g = genres.find(g => g.id === genreId)
      if (g) title.value = g.name
      
    } else if (route.name === 'MovieList') {
      const type = route.params.type as string
      const titleMap: Record<string, string> = {
        popular: '热门电影',
        top_rated: '高分经典',
        upcoming: '即将上映'
      }
      title.value = titleMap[type] || '电影列表'
      const res = await movieApi.getMovieList(type)
      movies.value = res.movies
    }
  } catch (e) {
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

onMounted(fetchData)
watch(() => route.fullPath, fetchData)
</script>

<style scoped>
.list-page {
  padding: 40px;
  max-width: 1200px;
  margin: 0 auto;
  color: #fff;
}

.list-header {
  margin-bottom: 30px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 15px;
}

.list-header h1 {
  font-size: 28px;
  color: #fff;
}

.loading-state {
  display: flex;
  justify-content: center;
  padding: 100px 0;
  color: #fff;
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
