# 🚀 Framework Templates & Documentation

Comprehensive guide for NGINX templates for different frameworks in Microservice Router

---

## 📋 Supported Frameworks List (Phase 1)

### ⭐ High Priority - Popular Frameworks

| Framework | Execution Type | Popularity | Status |
|-----------|---------------|------------|--------|
| **React** | SPA | ⭐⭐⭐⭐⭐ | ✅ Full Support |
| **Vue.js** | SPA | ⭐⭐⭐⭐⭐ | ✅ Full Support |
| **Next.js** | SSR/SPA | ⭐⭐⭐⭐⭐ | ✅ Full Support |
| **Angular** | SPA | ⭐⭐⭐⭐ | ✅ Full Support |
| **Express.js** | API | ⭐⭐⭐⭐⭐ | ✅ Full Support |
| **Django** | API/SSR | ⭐⭐⭐⭐ | ✅ Full Support |
| **Laravel** | PHP | ⭐⭐⭐⭐ | ✅ Full Support |
| **WordPress** | PHP | ⭐⭐⭐⭐⭐ | ✅ Full Support |

---

## 🔧 Proxy Headers Reference

### 🚨 Essential Headers (Always Included)

These headers are critical for basic proxy functionality and are included in all templates:

| Header | Purpose | When Required |
|--------|---------|---------------|
| `proxy_set_header Host $host` | **Critical** - Preserves original host for backend | Always |
| `proxy_pass http://{PROXY_HOST}/` | **Core** - Defines backend target | Always |

### 🔄 Standard Headers (Included by Default)

Commonly needed headers included in most scenarios:

| Header | Purpose | Use Case |
|--------|---------|----------|
| `proxy_set_header X-Forwarded-Proto $scheme` | HTTPS/HTTP detection | SSL termination, security |
| `proxy_set_header X-Real-IP $remote_addr` | Client IP preservation | Logging, rate limiting |
| `proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for` | Client IP chain | Load balancers, CDN |

### ⚡ WebSocket Headers (SSR/Real-time Only)

Required for WebSocket connections and hot reload:

| Header | Purpose | Framework |
|--------|---------|-----------|
| `proxy_set_header Upgrade $http_upgrade` | WebSocket upgrade | Next.js, Socket.io |
| `proxy_set_header Connection "upgrade"` | Connection upgrade | SSR frameworks |
| `proxy_http_version 1.1` | HTTP version for WS | WebSocket apps |
| `proxy_cache_bypass $http_upgrade` | Bypass cache for WS | Development mode |

### 📡 Optional Headers (User Selectable)

Advanced headers that can be added based on specific needs:

| Header | Purpose | When to Use |
|--------|---------|-------------|
| `proxy_set_header X-Forwarded-Host $host` | Original host forwarding | Multi-tenant apps |
| `proxy_set_header X-Forwarded-Port $server_port` | Original port info | Port-sensitive apps |
| `proxy_set_header Content-Type $content_type` | Content type preservation | API gateways |
| `proxy_set_header Accept $http_accept` | Accept header forwarding | Content negotiation |
| `proxy_set_header Authorization $http_authorization` | Auth token forwarding | Secured APIs |
| `proxy_set_header User-Agent $http_user_agent` | Client info preservation | Analytics, logging |
| `proxy_set_header Referer $http_referer` | Referrer preservation | Analytics |
| `proxy_set_header X-Requested-With $http_x_requested_with` | AJAX detection | API behavior |

### 🔒 Security Headers (Framework Specific)

| Header | Purpose | Framework |
|--------|---------|-----------|
| `fastcgi_param HTTP_PROXY ""` | HTTP Proxy vulnerability | PHP applications |
| `proxy_set_header X-Forwarded-Ssl on` | SSL indicator | HTTPS-only apps |

### ⏱️ Timeout Settings (Optional)

| Setting | Purpose | Default | When to Customize |
|---------|---------|---------|-------------------|
| `proxy_connect_timeout` | Connection timeout | 60s | Slow backends |
| `proxy_send_timeout` | Send timeout | 60s | Large uploads |
| `proxy_read_timeout` | Read timeout | 60s | Long processing |
| `proxy_buffering` | Response buffering | on | Streaming apps |

---

## 🎯 Execution Types (Streamlined Templates)

### 1. 📱 SPA (Single Page Application)

**Suitable for**: React, Vue, Angular, Vite

#### Features:
- ✅ Static file serving
- ✅ History API routing
- ✅ API proxy separation
- ✅ Build output optimization

#### Template:
```nginx
# {SERVICE_NAME} - SPA Application
location /{SERVICE_NAME}/ {
    alias /var/www/{SERVICE_NAME}/;
    try_files $uri $uri/ /{SERVICE_NAME}/index.html;
    index index.html;
    
    # Cache static assets
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}

# API routes for SPA
location /{SERVICE_NAME}/api/ {
    rewrite ^/{SERVICE_NAME}/api(/.*)$ $1 break;
    proxy_pass http://{PROXY_HOST}/;
    proxy_set_header Host $host;
}
```

---

### 2. 🔄 SSR (Server Side Rendering)

**Suitable for**: Next.js, Nuxt.js, SvelteKit

#### Features:
- ✅ Server-side rendering
- ✅ WebSocket support
- ✅ Hot reload support
- ✅ API routes integration

#### Template:
```nginx
# {SERVICE_NAME} - SSR Application
location /{SERVICE_NAME}/ {
    rewrite ^/{SERVICE_NAME}(/.*)$ $1 break;
    proxy_pass http://{PROXY_HOST}/;
    proxy_set_header Host $host;
    
    # WebSocket support for hot reload
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_http_version 1.1;
    proxy_cache_bypass $http_upgrade;
}
```

---

### 3. 🔌 API (Backend Services)

**Suitable for**: Express, Django, FastAPI, Flask

#### Features:
- ✅ REST API routing
- ✅ JSON response handling
- ✅ CORS support
- ✅ Rate limiting ready

#### Template:
```nginx
# {SERVICE_NAME} - API Service
location /{SERVICE_NAME}/ {
    rewrite ^/{SERVICE_NAME}(/.*)$ $1 break;
    proxy_pass http://{PROXY_HOST}/;
    proxy_set_header Host $host;
}
```

---

### 4. 🐘 PHP (PHP Applications)

**Suitable for**: Laravel, WordPress, Symfony

#### Features:
- ✅ PHP-FPM integration
- ✅ Static asset handling
- ✅ URL rewriting
- ✅ Security headers

#### Template:
```nginx
# {SERVICE_NAME} - PHP Application
location /{SERVICE_NAME}/ {
    alias /var/www/{SERVICE_NAME}/;
    index index.php index.html;
    try_files $uri $uri/ /{SERVICE_NAME}/index.php?$query_string;
    
    # Security - deny access to sensitive files
    location ~ /\.(ht|git|env) {
        deny all;
    }
    
    # PHP file processing
    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $request_filename;
        include fastcgi_params;
    }
}
```

---

### 5. 🔌 WebSocket (Real-time Applications)

**Suitable for**: Socket.io, Phoenix, SignalR

#### Features:
- ✅ WebSocket upgrade handling
- ✅ Connection persistence
- ✅ Fallback to polling
- ✅ Load balancing support

#### Template:
```nginx
# {SERVICE_NAME} - WebSocket Application
location /{SERVICE_NAME}/ {
    rewrite ^/{SERVICE_NAME}(/.*)$ $1 break;
    proxy_pass http://{PROXY_HOST}/;
    proxy_set_header Host $host;
    
    # WebSocket specific
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_http_version 1.1;
    proxy_cache_bypass $http_upgrade;
}
```

---

### 6. 📄 Static (Static Site Generators)

**Suitable for**: Hugo, Jekyll, Gatsby

#### Features:
- ✅ High-performance static serving
- ✅ Asset optimization
- ✅ Compression
- ✅ Browser caching

#### Template:
```nginx
# {SERVICE_NAME} - Static Site
location /{SERVICE_NAME}/ {
    alias /var/www/{SERVICE_NAME}/;
    index index.html;
    try_files $uri $uri/ =404;
    
    # Compression
    gzip_static on;
}
```

---

## 🔧 Optional Headers Configuration

### Usage in CLI Tool:

The tool can prompt users for additional headers based on their specific needs:

```bash
# Example CLI interaction
Do you need additional headers? (y/n): y

Available options:
1. Standard proxy headers (X-Real-IP, X-Forwarded-For, X-Forwarded-Proto)
2. CORS headers (for API services)
3. Security headers (for production)
4. Timeout settings (for slow backends)
5. Caching headers (for static assets)

Select options (comma-separated): 1,3
```

### Pre-built Header Sets:

#### Basic Set (Default):
```nginx
proxy_set_header Host $host;
```

#### Standard Set (+Standard Headers):
```nginx
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

#### Production Set (+Security):
```nginx
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Host $host;
```

#### API Set (+Content Headers):
```nginx
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header Content-Type $content_type;
proxy_set_header Accept $http_accept;
```

---

## 🎪 Framework-Specific Configurations

### React (Create React App)
```yaml
Framework: React
Type: SPA
Detection: package.json contains "react-scripts"
Proxy Host: Usually port 3000
Special Notes: 
  - Needs history API fallback
  - Static build deployment
  - Development proxy for API calls
```

### Next.js
```yaml
Framework: Next.js
Type: SSR/SPA (Hybrid)
Detection: package.json contains "next"
Proxy Host: Usually port 3000
Special Notes:
  - Server-side rendering
  - API routes built-in
  - Image optimization
  - WebSocket for dev mode
```

### Vue.js (Vite)
```yaml
Framework: Vue + Vite
Type: SPA
Detection: package.json contains "vue" and "vite"
Proxy Host: Usually port 5173
Special Notes:
  - Fast dev server
  - ES modules support
  - Hot module replacement
```

### Laravel
```yaml
Framework: Laravel
Type: PHP
Detection: composer.json contains "laravel/framework"
Proxy Host: PHP-FPM socket or port 8000
Special Notes:
  - Artisan serve for development
  - Public folder for assets
  - Route caching
```

### Express.js
```yaml
Framework: Express
Type: API
Detection: package.json contains "express"
Proxy Host: Usually port 3000 or 8000
Special Notes:
  - RESTful API design
  - Middleware support
  - CORS handling
```

### WordPress
```yaml
Framework: WordPress
Type: PHP
Detection: wp-config.php exists
Proxy Host: PHP-FPM socket
Special Notes:
  - Permalink structure
  - Plugin compatibility
  - Media uploads handling
  - wp-admin security
```

---

## 🔧 Template Variables

### Replaceable Variables:

- `{SERVICE_NAME}`: Service name (e.g., shop, blog, api)
- `{PROXY_HOST}`: Proxy address (e.g., srv-captain--shop)
- `{DOMAIN}`: Main domain (e.g., example.com)
- `{PORT}`: Service port (e.g., 3000, 8000)

### Usage in Code:
```python
template = template.replace('{SERVICE_NAME}', service_name)
template = template.replace('{PROXY_HOST}', proxy_host)
```

---

## 🚀 Next Phase - Additional Frameworks

### In Development:
- **Nuxt.js** (Vue SSR)
- **SvelteKit** (Svelte SSR)
- **Astro** (Static + Island Architecture)
- **Remix** (React SSR)
- **FastAPI** (Python API)
- **NestJS** (Node.js API)
- **Ruby on Rails** (Ruby)
- **Phoenix** (Elixir)

### Development Priority:
1. ⭐ Nuxt.js (Vue ecosystem)
2. ⭐ FastAPI (Python API)
3. ⭐ NestJS (Enterprise Node.js)
4. SvelteKit (Growing popularity)
5. Astro (Modern static)

---

## 📖 Practical Examples

### Example 1: E-commerce Platform
```
Frontend: React SPA (shop.example.com → example.com/shop/)
Backend: Express API (api-shop.example.com → example.com/shop/api/)
Admin: Laravel (admin.example.com → example.com/admin/)
```

### Example 2: Blog & Portal
```
Blog: Next.js SSR (blog.example.com → example.com/blog/)
CMS: WordPress (cms.example.com → example.com/cms/)
API: Django (api.example.com → example.com/api/)
```

### Example 3: Real-time Application
```
Frontend: Vue SPA (app.example.com → example.com/app/)
WebSocket: Socket.io (ws.example.com → example.com/ws/)
API: NestJS (api.example.com → example.com/api/)
```

---

## 🔍 Automatic Framework Detection

### Based on Detection Files:

```python
FRAMEWORK_DETECTION = {
    'package.json': {
        'react-scripts': 'react-spa',
        'next': 'nextjs-ssr',
        'vue': 'vue-spa',
        'vite': 'vite-spa',
        'express': 'express-api',
        'nestjs': 'nestjs-api'
    },
    'composer.json': {
        'laravel/framework': 'laravel-php',
        'wordpress': 'wordpress-php'
    },
    'requirements.txt': {
        'django': 'django-api',
        'fastapi': 'fastapi-api',
        'flask': 'flask-api'
    },
    'files': {
        'wp-config.php': 'wordpress-php',
        'artisan': 'laravel-php',
        'manage.py': 'django-api'
    }
}
```

---

## 💡 Optimization Tips

### Performance:
- ✅ Static asset caching
- ✅ Gzip compression
- ✅ Browser caching headers
- ✅ CDN ready configuration

### Security:
- ✅ Security headers
- ✅ File access restrictions
- ✅ CORS configuration
- ✅ Rate limiting ready

### DevOps:
- ✅ Health check endpoints
- ✅ Logging configuration
- ✅ Error page handling
- ✅ SSL/TLS ready

---

*This template file will be updated and expanded in future versions.*
