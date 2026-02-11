import apiClient from './index'

export interface Movie {
  id: number
  tmdb_id: number
  title: string
  title_en: string | null
  original_title: string | null
  overview: string | null
  overview_en: string | null
  poster_path: string | null
  backdrop_path: string | null
  release_date: string | null
  vote_average: number
  genres: string[]
  director: string | null
  cast: string[]
  runtime: number | null
  tagline: string | null
  is_favorite: boolean
}

export interface RandomMovieResponse {
  movie: Movie
  message: string
}

export interface MovieListResponse {
  movies: Movie[]
  total: number
  page: number
  page_size: number
}

export const movieApi = {
  getRandomMovie(): Promise<RandomMovieResponse> {
    return apiClient.get('/movies/random')
  },
  getMovieDetail(movieId: number): Promise<Movie> {
    return apiClient.get(`/movies/${movieId}`)
  },
  searchMovies(query: string, page: number = 1): Promise<MovieListResponse> {
    return apiClient.get('/movies/search', { params: { query, page } })
  },
}