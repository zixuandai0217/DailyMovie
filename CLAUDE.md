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

---

# Agent 协作与上下文优化指南

本指南旨在规范 Agent 在开发过程中的技能激活行为，优化上下文消耗，提升任务执行效率。

## 1. 技能激活策略 (Skills Activation)

### 强制入口 (Mandatory Entry)
- **每次必触发**：任何用户输入/任务开始前，必须去你的技能清单，先调用 `using-superpowers`。
- **统一分派**：后续是否触发其他技能，由 `using-superpowers` 决定。
- **禁止例外**：不得以"简单问题""无需技能"等理由跳过。
- **可观测性**：必须明确输出"已触发 using-superpowers + 是否分派其他技能"的执行摘要。

### 精准唤醒词
- **分析/搜索**：优先调用 `search` 子代理进行 read-only 调研，避免主 Agent 陷入琐碎搜索。
- **重构/优化**：使用 `refactor` 或 `optimize` 明确意图。
- **验证/测试**：在修改后立即调用 `verify` 或 `test` 技能。

### 意图声明
Agent 在执行前应声明其"当前工作模式"：
- `[PLANNING]`：正在进行多步任务规划。
- `[EXECUTING]`：正在执行具体的代码修改。
- `[VERIFYING]`：正在运行测试验证结果。

## 2. 上下文节约 (Context Optimization)

### 任务拆解 (Plan-and-Execute)
- 严禁一次性执行超过 3 个不相关的子任务。
- 复杂任务必须先生成 `TODO.md` 或调用 `TodoWrite` 工具。
- 每个子任务完成后，应总结核心变化，并"清理"不需要的中间上下文。

### 外部记忆化 (Offloading)
- **大文件处理**：对于超过 500 行的文件，禁止全文 Read。应先用 `Grep` 定位，再进行局部读取。
- **中间状态**：将复杂的分析报告写入 `docs/notes/` 或 `tmp/`，Agent 仅在后续对话中引用其路径和摘要。

### 工具选择优化
- **搜索**：能用 `Glob` 找到的文件，不用 `Grep`；能用 `Grep` 找到的字符串，不用 `SearchCodebase`。
- **编辑**：优先使用 `SearchReplace` 进行精准修改，避免全量重写。

## 3. 技能控制 (Skills Control)

### 核心原则
- **按需加载**：只有在任务明确需要时才激活特定的 Skills。
- **反馈闭环**：每项技能执行后必须提供明确的执行结果摘要。
- **避免冗余**：如果一个任务可以通过标准 CLI 工具完成，则不应创建复杂的自定义 Skill。

### 变更注释规范 (Change Annotation)
- **强制要求**：每次对代码、路由、配置或文档进行修改后，必须在修改处添加简短注释，说明变更目的（Why）、影响范围（Scope）与验证方法（Verify）。
- **注释形式**：
  - 代码文件：在变更附近使用合适的行内/块级注释（JS/Vue 使用 `//` 或 `/* */`；模板遵循框架推荐方式）。
  - 文档文件：在调整段落紧邻位置添加 HTML 注释 `<!-- ... -->` 描述本次修改。
- **安全约束**：注释中不得包含密钥、访问令牌或私有链接等敏感信息。
- **与用户偏好冲突时**：若用户明确禁止添加注释，应遵循用户指令，记录在任务说明中。

---
*本文件由 Agent 自动维护，作为协作契约。*
