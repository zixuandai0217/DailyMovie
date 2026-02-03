# DailyMovie 项目配置

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
