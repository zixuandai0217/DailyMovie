# DailyMovie 项目配置

## 项目概述

DailyMovie 是一个基于 TMDB API 的每日电影推荐应用，提供随机电影推荐、电影详情查询和电影搜索功能。

## 技术栈

- **后端**: FastAPI + Python 3.12+ + SQLAlchemy (异步) + SQLite
- **前端**: Vue 3 + TypeScript + Vite + Element Plus + Pinia
- **数据源**: TMDB (The Movie Database) API

## 项目架构

```
DailyMovie/
├── backend/                 # 后端服务
│   └── app/
│       ├── main.py         # FastAPI 应用入口
│       ├── config.py       # 配置管理 (Pydantic Settings)
│       ├── api/            # API 路由层
│       │   ├── routes_health.py  # 健康检查路由
│       │   └── routes_movies.py # 电影相关路由
│       ├── models/         # 数据模型层
│       │   ├── database.py # 数据库引擎和会话管理
│       │   └── schemas.py  # Pydantic 响应模型
│       ├── services/       # 业务服务层
│       │   └── tmdb_service.py  # TMDB API 服务封装
│       └── utils/          # 工具函数
├── frontend/               # 前端应用
│   └── src/
│       ├── views/         # 页面视图
│       ├── components/    # 公共组件
│       ├── api/           # API 调用封装
│       ├── stores/        # Pinia 状态管理
│       ├── router/        # Vue Router 路由配置
│       └── layouts/       # 布局组件
└── data/                  # 数据存储 (SQLite 数据库)
```

## 后端文件说明

| 文件路径 | 功能说明 |
|---------|---------|
| [backend/app/main.py](backend/app/main.py) | FastAPI 应用入口，配置 CORS 中间件，注册路由 |
| [backend/app/config.py](backend/app/config.py) | 配置管理，使用 Pydantic Settings 加载 .env 环境变量 |
| [backend/app/api/routes_health.py](backend/app/api/routes_health.py) | 健康检查路由，提供 `/api/v1/health` 端点 |
| [backend/app/api/routes_movies.py](backend/app/api/routes_movies.py) | 电影相关路由，包括随机推荐、详情查询、搜索功能 |
| [backend/app/models/database.py](backend/app/models/database.py) | SQLAlchemy 异步数据库引擎和会话管理 |
| [backend/app/models/schemas.py](backend/app/models/schemas.py) | Pydantic 数据模型，定义 API 响应数据结构 |
| [backend/app/services/tmdb_service.py](backend/app/services/tmdb_service.py) | TMDB API 服务封装，处理电影数据获取和转换 |

## API 端点

### 健康检查
- `GET /api/v1/health` - 检查服务状态

### 电影接口
- `GET /api/v1/movies/random` - 获取随机推荐电影
- `GET /api/v1/movies/{movie_id}` - 获取电影详情
- `GET /api/v1/movies/search?query=xxx` - 搜索电影

## 环境变量配置

项目使用 `.env` 文件管理敏感配置（API 密钥、令牌等），避免硬编码在代码中。

### 配置方式

- **`.env`** - 本地开发环境变量（已加入 `.gitignore`，不会提交到仓库）
- **`.env.example`** - 环境变量模板，仅包含变量名不含实际值

### 变量列表

| 变量名 | 说明 |
|-------|------|
| `TMDB_API_KEY` | TMDB API 密钥 |
| `TMDB_ACCESS_TOKEN` | TMDB API 读访问令牌 |

### 申请方式

1. 访问 [TMDB API 申请页面](https://www.themoviedb.org/settings/api)
2. 按指引填写信息并获取 API Key 和 Access Token
3. 将获取的凭证填入 `.env` 文件

## 开发命令

### 后端服务

```bash
# 初始化项目（仅首次）
cd backend
uv init
uv add fastapi uvicorn pydantic pydantic-settings httpx sqlalchemy aiosqlite python-dotenv

# 同步依赖
uv sync

# 启动开发服务器
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 前端服务

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build
```
