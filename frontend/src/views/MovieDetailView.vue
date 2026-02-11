<template>
  <div class="detail-container">
    <el-button class="back-btn" circle @click="router.back()">
      <el-icon><ArrowLeft /></el-icon>
    </el-button>

    <template v-if="currentMovie">
      <div class="backdrop" :style="backdropStyle">
        <div class="overlay"></div>
      </div>

      <div class="content">
        <div class="movie-info">
          <img :src="posterUrl" :alt="currentMovie.title" class="poster" />

          <div class="info">
            <h1 class="title">{{ currentMovie.title }}</h1>

            <div class="meta">
              <span v-if="currentMovie.release_date" class="year">
                {{ currentMovie.release_date.slice(0, 4) }}
              </span>
              <span v-if="currentMovie.runtime" class="runtime">
                {{ currentMovie.runtime }} 分钟
              </span>
              <span class="rating">
                <el-icon><Star /></el-icon>
                {{ currentMovie.vote_average.toFixed(1) }}
              </span>
            </div>

            <div class="genres">
              <el-tag
                v-for="genre in currentMovie.genres"
                :key="genre"
                type="info"
                effect="dark"
              >
                {{ genre }}
              </el-tag>
            </div>

            <p v-if="currentMovie.tagline" class="tagline">
              "{{ currentMovie.tagline }}"
            </p>

            <div class="section">
              <h3>剧情简介</h3>
              <p>{{ currentMovie.overview }}</p>
            </div>

            <div v-if="currentMovie.director" class="section">
              <h3>导演</h3>
              <p>{{ currentMovie.director }}</p>
            </div>

            <div v-if="currentMovie.cast.length" class="section">
              <h3>主演</h3>
              <p>{{ currentMovie.cast.join(", ") }}</p>
            </div>

            <div class="actions">
              <el-button type="primary" size="large" @click="watchMovie">
                <el-icon><VideoPlay /></el-icon>
                立即观看
              </el-button>
              <el-button size="large" @click="shareMovie">
                <el-icon><Share /></el-icon>
                分享
              </el-button>
            </div>
          </div>
        </div>
      </div>
    </template>

    <div v-else-if="isLoading" class="loading">
      <el-icon class="is-loading" :size="64"><Loading /></el-icon>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import { storeToRefs } from "pinia";
import { useMovieStore } from "@/stores/movie";
import {
  ArrowLeft,
  Star,
  VideoPlay,
  Share,
  Loading,
} from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";

const route = useRoute();
const router = useRouter();
const store = useMovieStore();

const { currentMovie, isLoading } = storeToRefs(store);
const { fetchMovieDetail } = store;

const posterUrl = computed(() => store.posterUrl);

const backdropStyle = computed(() => {
  const url = store.backdropUrl;
  if (url) {
    return { backgroundImage: `url(${url})` };
  }
  return { backgroundColor: "#1a1a2e" };
});

async function loadMovie() {
  const movieId = Number(route.params.id);
  if (movieId) {
    await fetchMovieDetail(movieId);
  }
}

function watchMovie() {
  if (!currentMovie.value) return;

  const movie = currentMovie.value;
  // 如果有官方主页，优先跳转
  if (movie.homepage) {
    window.open(movie.homepage, "_blank");
  } else {
    // 否则跳转到 TMDB 页面
    window.open(`https://www.themoviedb.org/movie/${movie.tmdb_id}`, "_blank");
  }
}

function shareMovie() {
  const url = window.location.href;
  if (navigator.share) {
    navigator.share({
      title: currentMovie.value?.title || "",
      text: currentMovie.value?.overview || "",
      url: url,
    });
  } else {
    navigator.clipboard.writeText(url);
    ElMessage.success("链接已复制到剪贴板");
  }
}

onMounted(loadMovie);

watch(() => route.params.id, loadMovie);
</script>

<style scoped lang="scss">
.detail-container {
  position: relative;
  min-height: 100vh;
  color: #fff;
}

.backdrop {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 60vh;
  background-size: cover;
  background-position: center top;
  z-index: 0;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.3) 0%,
    rgba(0, 0, 0, 0.8) 100%
  );
}

.back-btn {
  position: fixed;
  top: 20px;
  left: 20px;
  z-index: 100;
  background: rgba(0, 0, 0, 0.5);
  color: #fff;
}

.content {
  position: relative;
  z-index: 1;
  padding-top: 40vh;
}

.movie-info {
  display: flex;
  gap: 40px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px;
  background: linear-gradient(to bottom, transparent, #0f0f1a);
}

.poster {
  width: 300px;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
}

.info {
  flex: 1;
}

.title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 15px;
}

.meta {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  color: #9ca3af;
}

.rating {
  display: flex;
  align-items: center;
  gap: 5px;
  color: #fbbf24;
}

.genres {
  display: flex;
  gap: 10px;
  margin-bottom: 25px;
}

.tagline {
  font-style: italic;
  color: #9ca3af;
  margin-bottom: 25px;
}

.section {
  margin-bottom: 20px;

  h3 {
    font-size: 1.1rem;
    margin-bottom: 8px;
    color: #9ca3af;
  }

  p {
    line-height: 1.6;
  }
}

.actions {
  display: flex;
  gap: 15px;
  margin-top: 30px;
}

.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: #fff;
}
</style>
