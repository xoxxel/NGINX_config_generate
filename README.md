# 🚀 NGINX Location Generator

Simple CLI tool to generate NGINX location blocks for microservices with step-by-step selection.

## ✨ Features

- **🎯 Simple Selection**: Choose technology and host pattern with numbers
- **⚡ Quick CLI**: Generate configs with single command
- **📖 Complete Guide**: Automatic installation guide generation
- **🔧 Multiple Technologies**: Support for 10+ popular frameworks
- **🌐 Flexible Hosting**: CapRover, Docker, localhost, custom hosts
- **📁 Clean Output**: Ready-to-use configuration files

## 🚀 Quick Start

### Interactive Mode
```bash
python nginx_gen.py
```

### Quick CLI Mode
```bash
# WordPress blog with CapRover
python nginx_gen.py --tech 7 --service blog --host-pattern 1

# React dashboard with Docker Compose
python nginx_gen.py --tech 1 --service dashboard --host-pattern 2

# Django API with custom host
python nginx_gen.py --tech 5 --service api --host-pattern 4 --custom-host "192.168.1.100:8000"
```

## 📋 Supported Technologies

| # | Technology | Type | Default Port |
|---|------------|------|--------------|
| 1 | React SPA | Frontend | 3000 |
| 2 | Vue.js SPA | Frontend | 5173 |
| 3 | Next.js | Full-stack | 3000 |
| 4 | Express API | Backend | 3000 |
| 5 | Django | Backend | 8000 |
| 6 | Laravel | Backend | 9000 |
| 7 | WordPress | CMS | 80 |
| 8 | Socket.io | WebSocket | 3001 |
| 9 | Hugo Static | Static | 1313 |
| 10 | Custom API | Backend | 8000 |

## � Host Patterns

| # | Pattern | Example | Use Case |
|---|---------|---------|----------|
| 1 | CapRover | `srv-captain--blog` | Docker containers |
| 2 | Docker Compose | `frontend:3000` | Local containers |
| 3 | Localhost | `localhost:3000` | Development |
| 4 | Custom Host | `192.168.1.100:8000` | Production servers |

## 📁 Output Files

### `location_block.conf`
Ready-to-use NGINX location block:
```nginx
# blog - WordPress
location /blog/ {
    proxy_pass http://srv-captain--blog/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

### `install_guide.txt`
Complete installation instructions with:
- File locations
- Step-by-step commands
- Testing procedures
- Troubleshooting tips

## �️ CLI Reference

### Commands
```bash
python nginx_gen.py                    # Interactive mode
python nginx_gen.py --list             # Show technologies
python nginx_gen.py --patterns         # Show host patterns
python nginx_gen.py --help             # Show help
```

### Parameters
```bash
--tech, -t        Technology number (1-10)
--service, -s     Service name
--host-pattern    Host pattern (1-4)
--custom-host     Custom address for pattern 4
```

### Examples
```bash
# WordPress blog
python nginx_gen.py -t 7 -s blog --host-pattern 1

# React SPA
python nginx_gen.py -t 1 -s frontend --host-pattern 2

# Custom API server
python nginx_gen.py -t 10 -s api --host-pattern 4 --custom-host "server:8080"
```

## 📖 Documentation

- **[NGINX_EXAMPLES.md](NGINX_EXAMPLES.md)** - Complete configuration examples
- **[HOST_PATTERNS.md](HOST_PATTERNS.md)** - Host pattern reference
- **[FRAMEWORK_TEMPLATES.md](FRAMEWORK_TEMPLATES.md)** - Technical templates
- **[TECHNOLOGY_GUIDE.md](TECHNOLOGY_GUIDE.md)** - Simple technology guide

## 🎯 Use Cases

### Microservices Routing
Convert subdomains to paths:
- `blog.example.com` → `example.com/blog/`
- `shop.example.com` → `example.com/shop/`
- `api.example.com` → `example.com/api/`

### Development Setup
Quick NGINX configuration for local development with multiple services.

### Production Deployment
Generate production-ready configurations for CapRover, Docker, or custom servers.

## 🔧 Installation

1. **Clone or download** the `nginx_gen.py` file
2. **Run directly** with Python 3.6+:
   ```bash
   python nginx_gen.py
   ```

No dependencies required! Pure Python standard library.

## 🌟 Examples

### WordPress Blog
```bash
$ python nginx_gen.py --tech 7 --service blog --host-pattern 1
Generated NGINX configuration:
============================================================
    # blog - WordPress
    location /blog/ {
        proxy_pass http://srv-captain--blog/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

Files saved: location_block.conf, install_guide.txt
```

### React Dashboard
```bash
$ python nginx_gen.py --tech 1 --service dashboard --host-pattern 2
Generated NGINX configuration:
============================================================
    # dashboard - React SPA
    location /dashboard/ {
        proxy_pass http://dashboard:3000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # SPA routing support
        try_files $uri $uri/ /dashboard/index.html;
    }

Files saved: location_block.conf, install_guide.txt
```

## 🤝 Contributing

This is a simple, focused tool. Contributions welcome for:
- New technology templates
- Host pattern improvements
- Documentation enhancements

## 📄 License

MIT License - Feel free to use in your projects!

## 🎉 Credits

Created for simplifying microservice NGINX configuration. Perfect for developers who want quick, reliable NGINX location blocks without memorizing syntax.

---

**Happy configuring!** 🚀

## ✅ Advantages

- **Fewer SSL Certificates**: Only one main domain
- **Simpler DNS Management**: Fewer subdomains
- **Easier Management**: All services under one domain
- **Lower Cost**: Fewer domains and certificates

## 🚧 Next Phase (Roadmap)

### Phase 2: Convert to API + Modular
- Convert to Flask/FastAPI
- Create REST API
- Modular structure
- Web Interface
- Configuration storage

## 🧪 Testing

```bash
# Quick test
python template_manager.py
```

## 📞 Support

This tool is in MVP stage and designed for microservice simplification.
