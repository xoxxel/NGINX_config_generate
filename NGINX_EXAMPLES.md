# 🧾 Technology NGINX Examples

Simple NGINX configuration examples for different technologies

---

## 📝 WordPress (Content Management)

**What it is**: Blog and content website platform
**Why special config**: Needs PHP processing and pretty URLs

```nginx
# WordPress Configuration
location / {
    try_files $uri $uri/ /index.php?$query_string;
    index index.php index.html;
}

location ~ \.php$ {
    fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
    fastcgi_index index.php;
    include fastcgi_params;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
}

# Security - block sensitive files
location ~ /\.(ht|git|env) {
    deny all;
}
```

**Key point**: Handles WordPress permalinks and PHP execution

---

## 🔴 Laravel (PHP Framework)

**What it is**: Modern PHP framework for custom web applications
**Why special config**: Routes everything through index.php

```nginx
# Laravel Configuration
location / {
    try_files $uri $uri/ /index.php?$query_string;
    index index.php;
}

location ~ \.php$ {
    fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
    fastcgi_index index.php;
    include fastcgi_params;
    fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
    fastcgi_param DOCUMENT_ROOT $realpath_root;
}

# Block access to Laravel files
location ~ /\.(env|git) {
    deny all;
}
```

**Key point**: All requests go to Laravel's routing system

---

## ⚛️ React SPA (Interactive Web App)

**What it is**: JavaScript framework for modern web applications
**Why special config**: History API routing (no page refresh)

```nginx
# React SPA Configuration
location / {
    try_files $uri $uri/ /index.html;
    root /var/www/app;
    index index.html;
}

# Cache JavaScript and CSS files
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

**Key point**: Without this, refreshing `/dashboard` gives 404 error

---

## 💚 Vue.js SPA (with Vite)

**What it is**: JavaScript framework, easier than React
**Why special config**: Same as React - needs fallback to index.html

```nginx
# Vue SPA Configuration
location / {
    try_files $uri $uri/ /index.html;
    root /var/www/app;
    index index.html;
}

# Static assets caching
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2)$ {
    expires 1y;
    add_header Cache-Control "public";
}
```

**Key point**: Same principle as React - all routes handled by JavaScript

---

## ⚡ Next.js (React with SSR)

**What it is**: React framework with server-side rendering
**Why special config**: Acts like a backend server

```nginx
# Next.js Configuration
location / {
    proxy_pass http://nextjs-app:3000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    
    # WebSocket support for development
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_http_version 1.1;
    proxy_cache_bypass $http_upgrade;
}
```

**Key point**: Proxies to Node.js server, includes WebSocket for hot reload

---

## 🟢 Node.js API (Express)

**What it is**: JavaScript server for APIs and backends
**Why special config**: Simple proxy to Node.js server

```nginx
# Node.js API Configuration
location / {
    proxy_pass http://node-api:3000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

# For JSON APIs
location /api/ {
    proxy_pass http://node-api:3000/api/;
    proxy_set_header Host $host;
    proxy_set_header Content-Type application/json;
}
```

**Key point**: Simple proxy, good for REST APIs

---

## 🔌 Node.js with WebSocket (Socket.io)

**What it is**: Real-time applications (chat, live updates)
**Why special config**: Needs WebSocket upgrade support

```nginx
# WebSocket Configuration
location / {
    proxy_pass http://node-app:3000;
    proxy_set_header Host $host;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    
    # Prevent timeouts
    proxy_read_timeout 86400;
}
```

**Key point**: WebSocket headers are essential for real-time features

---

## 🐍 Django (Python Web Framework)

**What it is**: Python framework for web applications and APIs
**Why special config**: Python server proxy

```nginx
# Django Configuration
location / {
    proxy_pass http://django-app:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

# Static files (CSS, JS, images)
location /static/ {
    alias /var/www/static/;
    expires 1M;
}

# Media uploads
location /media/ {
    alias /var/www/media/;
}
```

**Key point**: Separate handling for static files and media uploads

---

## ⚡ Hugo (Static Site Generator)

**What it is**: Super fast static websites (no database)
**Why special config**: Just serve static files

```nginx
# Hugo Static Site Configuration
location / {
    root /var/www/hugo;
    index index.html;
    try_files $uri $uri/ =404;
}

# Long caching for assets
location ~* \.(css|js|png|jpg|jpeg|gif|ico|svg)$ {
    root /var/www/hugo;
    expires 1y;
    add_header Cache-Control "public, immutable";
}

# Enable gzip compression
gzip on;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml text/javascript;
```

**Key point**: No backend needed, maximum caching for speed

---

## 🛒 WooCommerce (WordPress E-commerce)

**What it is**: WordPress with e-commerce features
**Why special config**: Same as WordPress but with file upload support

```nginx
# WooCommerce Configuration
location / {
    try_files $uri $uri/ /index.php?$query_string;
    index index.php;
}

location ~ \.php$ {
    fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
    fastcgi_index index.php;
    include fastcgi_params;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    
    # Increase limits for file uploads
    client_max_body_size 100M;
    fastcgi_read_timeout 300;
}

# Block xmlrpc.php (security)
location = /xmlrpc.php {
    deny all;
}
```

**Key point**: Higher upload limits for product images

---

## 🎯 Technology Quick Reference

| Technology | Type | Config Style | Key Feature |
|------------|------|--------------|-------------|
| **WordPress** | PHP CMS | `try_files` + PHP | Pretty URLs |
| **Laravel** | PHP Framework | `try_files` + PHP | Route all to index.php |
| **React SPA** | Frontend JS | `try_files` fallback | History API support |
| **Vue SPA** | Frontend JS | `try_files` fallback | Same as React |
| **Next.js** | Full-stack JS | `proxy_pass` | Server-side rendering |
| **Express API** | Backend JS | `proxy_pass` | Simple API proxy |
| **Socket.io** | Real-time JS | `proxy_pass` + WebSocket | Real-time features |
| **Django** | Python Web | `proxy_pass` | Python server |
| **Hugo** | Static | Direct file serving | Maximum speed |

---

## 🔍 Common Issues and Solutions

### 1. SPA 404 Errors
**Problem**: React/Vue routes show 404 on refresh
**Solution**: Use `try_files $uri $uri/ /index.html;`

### 2. WebSocket Not Working
**Problem**: Real-time features broken
**Solution**: Add `proxy_set_header Upgrade $http_upgrade;`

### 3. PHP Files Download Instead of Execute
**Problem**: PHP files download as text
**Solution**: Ensure `fastcgi_pass` is correctly configured

### 4. Large File Upload Fails
**Problem**: Can't upload big images/files
**Solution**: Increase `client_max_body_size`

### 5. CSS/JS Not Loading
**Problem**: Static assets give 404
**Solution**: Check `root` path and file permissions

---

## 💡 Quick Decision Helper

**Choose configuration based on:**

- **WordPress/WooCommerce**: If you want easy content management
- **Laravel**: If you need custom PHP application
- **React/Vue SPA**: If you want modern interactive frontend
- **Next.js**: If you need SEO-friendly React
- **Express API**: If you need JavaScript backend
- **Socket.io**: If you need real-time features
- **Django**: If you prefer Python
- **Hugo**: If you want maximum speed

---

*This file serves as a quick reference for NGINX configurations. Copy the relevant section for your technology.*
