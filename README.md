# DailyMovie 🎬

DailyMovie 是一个基于 FastAPI 和 Vue 3 的全栈电影推荐应用。它能为你随机推荐一部高质量电影，并展示详细信息，帮助你发现下一部想看的佳作。

## 🛠 技术栈

### Backend (后端)
- **Language**: Python 3.12+
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **API Integration**: TMDB (The Movie Database) API

### Frontend (前端)
- **Framework**: [Vue 3](https://vuejs.org/)
- **Build Tool**: [Vite](https://vitejs.dev/)
- **Language**: TypeScript
- **State Management**: [Pinia](https://pinia.vuejs.org/)
- **UI Library**: [Element Plus](https://element-plus.org/)
- **CSS**: SCSS / CSS Variables

## 📂 项目结构

```
DailyMovie/
├── backend/            # FastAPI 后端服务
│   ├── app/            # 应用源码
│   │   ├── api/        # API 路由
│   │   ├── models/     # 数据模型
│   │   └── services/   # 业务逻辑 (如 TMDB 服务)
│   └── ...
├── frontend/           # Vue 3 前端应用
│   ├── src/            # 源码
│   │   ├── api/        # 前端 API 封装
│   │   ├── stores/     # Pinia 状态管理
│   │   └── views/      # 页面视图
│   └── ...
├── .env.example        # 环境变量模板
└── ...
```

## 🚀 快速开始

### 前置要求
- Node.js (v18+)
- Python (v3.12+)
- uv (推荐的 Python 包管理器)

### 1. 配置环境变量

复制环境变量模板文件，并填入你的 TMDB API 密钥：

```bash
cp .env.example .env
```

编辑 `.env` 文件：
```ini
TMDB_API_KEY=你的_api_key
TMDB_ACCESS_TOKEN=你的_read_access_token
```

> **注意**: 你需要从 [The Movie Database (TMDB)](https://www.themoviedb.org/settings/api) 申请 API Key。

### 2. 启动后端服务

进入项目根目录：

```bash
# 安装依赖
uv sync

# 启动开发服务器
uv run uvicorn app.main:app --reload
```

后端服务将在 `http://localhost:8000` 启动。
API 文档地址: `http://localhost:8000/docs`

### 3. 启动前端应用

进入 `frontend` 目录：

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端应用将在 `http://localhost:5173` 启动。

## ✅ 测试

项目包含单元测试以确保功能稳定性。

**运行前端测试**:
```bash
cd frontend
npm test
```

## ✨ 功能特性

- **随机推荐**: 每次刷新都能获得一部随机的高分电影推荐。
- **详细信息**: 查看电影海报、评分、简介、上映日期等详细信息。
- **错误处理**: 友好的 UI 提示，处理网络断开或 API 限制等异常情况。
- **响应式设计**: 适配桌面端和移动端设备。

## 📝 License

[MIT](LICENSE)
