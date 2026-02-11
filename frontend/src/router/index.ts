import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('@/layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import('@/views/HomeView.vue'),
      },
      {
        path: 'ai',
        name: 'AIRecommend',
        component: () => import('@/views/AIRecommendView.vue'),
      },
      {
        path: 'list/:type',
        name: 'MovieList',
        component: () => import('@/views/MovieListView.vue'),
      },
      {
        path: 'genre/:id',
        name: 'GenreList',
        component: () => import('@/views/MovieListView.vue'),
      },
      {
        path: 'movie/:id',
        name: 'MovieDetail',
        component: () => import('@/views/MovieDetailView.vue'),
        props: true,
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router