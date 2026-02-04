import { describe, it, expect, vi, beforeEach } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { useMovieStore } from './movie'
import { movieApi } from '@/api/movie'

// Mock the API module
vi.mock('@/api/movie', () => ({
  movieApi: {
    getRandomMovie: vi.fn(),
    getMovieDetail: vi.fn()
  }
}))

describe('Movie Store', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
    vi.clearAllMocks()
  })

  it('should display specific error message when API fails', async () => {
    const store = useMovieStore()
    const errorMessage = 'Network Error'
    
    // Mock API failure
    vi.mocked(movieApi.getRandomMovie).mockRejectedValue(new Error(errorMessage))

    await store.fetchRandomMovie()

    // EXPECT FAILURE: Current implementation hardcodes '获取电影失败'
    expect(store.error).toContain(errorMessage)
    // Or at least shouldn't be just generic
    expect(store.error).not.toBe('获取电影失败') 
  })
})
