# Django 练手 - 手机管理 (前后端分离)

一个基于 Django + Django REST Framework 的前后端分离练手项目，实现手机型号的增删改查管理。

## 项目结构

```
my_django_site/
├── manage.py                        # Django 管理入口
├── README.md                        # 项目说明
├── requirements.txt                 # Python 依赖
├── my_django_site/                  # 项目配置
│   ├── settings.py                  # Django 配置（含 DRF、CORS）
│   ├── urls.py                      # URL 路由（API + 前端页面）
│   └── wsgi.py
├── web/                             # 主应用
│   ├── models.py                    # 数据模型（Phone）
│   ├── serializers.py               # DRF 序列化器
│   ├── api_views.py                 # REST API 视图
│   ├── views.py                     # 页面视图
│   ├── admin.py                     # 后台管理
│   └── templates/web/
│       └── index.html               # 前端 SPA 页面
└── templates/                       # 全局模板
```

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端框架 | Django 4.2 |
| REST API | Django REST Framework 3.17 |
| 跨域 | django-cors-headers |
| 数据库 | SQLite |
| 前端 | 原生 HTML/CSS/JS（SPA 风格） |

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 数据库迁移

```bash
python manage.py migrate
```

### 3. 创建超级管理员（可选，用于后台管理）

```bash
python manage.py createsuperuser
```

### 4. 启动开发服务器

```bash
python manage.py runserver
```

### 5. 访问页面

| 地址 | 说明 |
|------|------|
| http://127.0.0.1:8000/ | 前端 SPA 页面（手机管理） |
| http://127.0.0.1:8000/api/ | API 总览 |
| http://127.0.0.1:8000/api/phones/ | 手机 REST API |
| http://127.0.0.1:8000/admin/ | Django 后台管理 |
| http://127.0.0.1:8000/phone_list/ | 原有模板渲染页面 |

## API 接口

### 手机管理

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/api/phones/` | 获取手机列表 |
| `POST` | `/api/phones/` | 新增手机 |
| `GET` | `/api/phones/{id}/` | 获取手机详情 |
| `PUT` | `/api/phones/{id}/` | 修改手机 |
| `DELETE` | `/api/phones/{id}/` | 删除手机 |

### 请求/响应示例

**新增手机**
```json
POST /api/phones/
{
    "brand": "Apple",
    "name": "iPhone 16",
    "price": "8999.00",
    "description": "最新款"
}
```

**响应**
```json
{
    "id": 1,
    "brand": "Apple",
    "name": "iPhone 16",
    "price": "8999.00",
    "description": "最新款",
    "created_at": "2026-06-28T21:00:00Z"
}
```

## 前后端分离说明

- **后端**：Django 仅提供 REST API，返回 JSON 数据，不参与页面渲染
- **前端**：纯 HTML/CSS/JS 页面，通过 `fetch` 调用后端 API，实现数据展示和交互
- **跨域**：使用 `django-cors-headers` 允许前端独立开发和部署
- **架构优势**：前后端解耦，前端可独立部署到 Nginx/CDN，后端专注 API 逻辑
