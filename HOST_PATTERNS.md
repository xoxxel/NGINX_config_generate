# 🌐 Host & Port Patterns Dictionary

Complete reference for different hosting patterns and proxy configurations

---

## 📝 What is `proxy_pass`?

The `proxy_pass` tells NGINX where to send requests. Different technologies and hosting environments use different patterns.

**Format**: `proxy_pass http://HOST:PORT;`

---

## 🚢 CapRover Pattern (srv-captain--)

**Most Common**: When using CapRover (Docker hosting platform)

### Pattern: `srv-captain--{service-name}`

| Service Name | Framework | proxy_pass URL |
|-------------|-----------|----------------|
| `blog` | WordPress | `http://srv-captain--blog` |
| `shop` | WooCommerce | `http://srv-captain--shop` |
| `api` | Express.js | `http://srv-captain--api` |
| `frontend` | React | `http://srv-captain--frontend` |
| `dashboard` | Vue.js | `http://srv-captain--dashboard` |
| `backend` | Django | `http://srv-captain--backend` |
| `docs` | Hugo | `http://srv-captain--docs` |
| `chat` | Socket.io | `http://srv-captain--chat` |

**Why**: CapRover automatically creates internal network names

---

## 🐳 Docker Compose Pattern

**When**: Using docker-compose.yml with custom service names

### Pattern: `http://{service-name}:{port}`

| Framework | Service Name Example | proxy_pass URL | Port |
|-----------|---------------------|----------------|------|
| **React/Vue SPA** | `frontend` | `http://frontend:3000` | 3000 |
| **Next.js** | `nextjs-app` | `http://nextjs-app:3000` | 3000 |
| **Express API** | `api-server` | `http://api-server:3000` | 3000 |
| **Django** | `django-web` | `http://django-web:8000` | 8000 |
| **Laravel** | `laravel-app` | `http://laravel-app:9000` | 9000 |
| **WordPress** | `wordpress` | `http://wordpress:80` | 80 |
| **Socket.io** | `realtime-server` | `http://realtime-server:3001` | 3001 |

---

## 🖥️ Localhost Development Pattern

**When**: Running services on same machine during development

### Pattern: `http://localhost:{port}` or `http://127.0.0.1:{port}`

| Framework | Default Port | proxy_pass URL | Alternative |
|-----------|-------------|----------------|-------------|
| **React (Vite)** | 5173 | `http://localhost:5173` | `http://127.0.0.1:5173` |
| **React (CRA)** | 3000 | `http://localhost:3000` | `http://127.0.0.1:3000` |
| **Vue (Vite)** | 5173 | `http://localhost:5173` | `http://127.0.0.1:5173` |
| **Next.js** | 3000 | `http://localhost:3000` | `http://127.0.0.1:3000` |
| **Express** | 3000 | `http://localhost:3000` | `http://127.0.0.1:3000` |
| **Django** | 8000 | `http://localhost:8000` | `http://127.0.0.1:8000` |
| **Laravel** | 8000 | `http://localhost:8000` | `http://127.0.0.1:8000` |
| **WordPress** | 8080 | `http://localhost:8080` | `http://127.0.0.1:8080` |
| **Hugo** | 1313 | `http://localhost:1313` | `http://127.0.0.1:1313` |

---

## 🌍 External Server Pattern

**When**: Services running on different servers

### Pattern: `http://{ip-address}:{port}` or `http://{domain}:{port}`

| Scenario | Example | proxy_pass URL |
|----------|---------|----------------|
| **Internal Network** | Server IP | `http://192.168.1.100:3000` |
| **VPS/Cloud** | Server IP | `http://10.0.0.5:8000` |
| **Subdomain** | API subdomain | `http://api.mysite.com:3000` |
| **Different Port** | Custom port | `http://myserver.com:8080` |

---

## 🔗 Production Patterns

### 1. Load Balancer Pattern
```nginx
upstream backend {
    server srv-captain--api-1;
    server srv-captain--api-2;
    server srv-captain--api-3;
}

location /api/ {
    proxy_pass http://backend;
}
```

### 2. SSL Internal Pattern
```nginx
location / {
    proxy_pass https://internal-server:443;
    proxy_ssl_verify off;
}
```

### 3. Unix Socket Pattern (PHP-FPM)
```nginx
location ~ \.php$ {
    fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
}
```

---

## 📋 Quick Reference Table

| Environment | Pattern | Example | Use Case |
|-------------|---------|---------|----------|
| **CapRover** | `srv-captain--{name}` | `srv-captain--blog` | Docker containers |
| **Docker Compose** | `{service}:{port}` | `frontend:3000` | Local containers |
| **Development** | `localhost:{port}` | `localhost:3000` | Local development |
| **Production** | `{ip}:{port}` | `192.168.1.10:8000` | Server deployment |
| **Subdomain** | `{subdomain}.{domain}` | `api.mysite.com` | Microservices |

---

## 🎯 How to Choose the Right Pattern

### Step 1: Identify Your Environment
- **CapRover**: Use `srv-captain--{name}`
- **Docker Compose**: Use `{service-name}:{port}`
- **Local Dev**: Use `localhost:{port}`
- **VPS/Cloud**: Use `{server-ip}:{port}`

### Step 2: Find Your Framework's Default Port
| Framework Type | Common Ports |
|----------------|-------------|
| **React/Vue** | 3000, 5173 |
| **Node.js** | 3000, 8000 |
| **Python** | 8000, 5000 |
| **PHP** | 8080, 9000 |
| **Static** | 8080, 3000 |

### Step 3: Test the Connection
```bash
# Test if service is reachable
curl http://your-proxy-pass-url
```

---

## 🛠️ Common Examples

### WordPress Blog Example
```nginx
# CapRover
proxy_pass http://srv-captain--blog;

# Docker Compose
proxy_pass http://wordpress:80;

# Local Development
proxy_pass http://localhost:8080;
```

### React Frontend Example
```nginx
# CapRover
proxy_pass http://srv-captain--frontend;

# Docker Compose
proxy_pass http://react-app:3000;

# Local Development (Vite)
proxy_pass http://localhost:5173;
```

### Express API Example
```nginx
# CapRover
proxy_pass http://srv-captain--api;

# Docker Compose
proxy_pass http://api-server:3000;

# Local Development
proxy_pass http://localhost:3000;
```

---

## ⚠️ Troubleshooting

### 1. Connection Refused
**Problem**: `proxy_pass` URL not reachable
**Solutions**:
- Check if service is running
- Verify port number
- Test with `curl` or browser

### 2. Wrong Service Name
**Problem**: Service name doesn't match
**Solutions**:
- Check docker container names: `docker ps`
- Verify CapRover service names
- Check docker-compose.yml service names

### 3. Port Conflicts
**Problem**: Multiple services on same port
**Solutions**:
- Use different ports for each service
- Use service names instead of localhost
- Check `netstat -tulpn` for used ports

---

## 💡 Best Practices

1. **Use Service Names**: Prefer `srv-captain--name` over IP addresses
2. **Document Your Patterns**: Keep track of your service naming convention
3. **Test Connectivity**: Always test `proxy_pass` URLs before deployment
4. **Environment Variables**: Use env vars for different environments
5. **Health Checks**: Implement health check endpoints

---

*This file helps you choose the correct `proxy_pass` pattern based on your hosting environment and framework.*
