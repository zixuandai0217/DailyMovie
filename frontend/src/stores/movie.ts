import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { movieApi, type Movie } from '@/api/movie'

export const useMovieStore = defineStore('movie', () => {
  const currentMovie = ref<Movie | null>(null)
  const isLoading = ref(false)
  const error = ref<string | null>(null)

  const posterUrl = computed(() => {
    if (currentMovie.value?.poster_path) {
      return `https://image.tmdb.org/t/p/w500${currentMovie.value.poster_path}`
    }
    return undefined
  })

  const backdropUrl = computed(() => {
    if (currentMovie.value?.backdrop_path) {
      return `https://image.tmdb.org/t/p/original${currentMovie.value.backdrop_path}`
    }
    return undefined
  })

  async function fetchRandomMovie() {
    isLoading.value = true
    error.value = null
    try {
      const response = await movieApi.getRandomMovie()
      currentMovie.value = response.movie
    } catch (e: any) {
      // Why: Capture detailed error message for UI display
      let msg = e.response?.data?.detail || e.message || '未知错误'
      if (e.code === 'ERR_NETWORK') {
        msg = '无法连接到服务器，请检查后端服务是否启动 (Network Error)'
      }
      error.value = `获取电影失败: ${msg}`
      console.error(e)
    } finally {
      isLoading.value = false
    }
  }

  async function fetchMovieDetail(movieId: number) {
    isLoading.value = true
    error.value = null
    try {
      currentMovie.value = await movieApi.getMovieDetail(movieId)
    } catch (e: any) {
      let msg = e.response?.data?.detail || e.message || '未知错误'
      if (e.code === 'ERR_NETWORK') {
        msg = '无法连接到服务器，请检查后端服务是否启动 (Network Error)'
      }
      error.value = `获取电影详情失败: ${msg}`
      console.error(e)
    } finally {
      isLoading.value = false
    }
  }

  return {
    currentMovie,
    isLoading,
    error,
    posterUrl,
    backdropUrl,
    fetchRandomMovie,
    fetchMovieDetail,
  }
})