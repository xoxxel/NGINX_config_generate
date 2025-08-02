# 🚀 NGINX Location Generator

**Simple CLI tool that converts complex NGINX location configurations into easy numbered selections**

> 💡 **What it does**: Generate production-ready NGINX location blocks in seconds instead of hours of manual configuration  
> 🎯 **Perfect for**: DevOps engineers, Full-stack developers, System administrators, and anyone managing microservices  
> ⚡ **Why use it**: No more memorizing NGINX syntax, copying configs from StackOverflow, or debugging proxy headers

---

## 🌟 Why This Tool Exists

Managing multiple microservices with NGINX can be overwhelming:
- ❌ **Before**: Manually writing location blocks, remembering proxy headers, debugging routing issues
- ✅ **After**: Pick technology (1-10), enter service name, get perfect config instantly

**Perfect for developers who want to focus on building, not configuring.**

---

## 🎓 Learning Resources

📚 **New to NGINX?** Start here:
- [NGINX Beginner's Guide](https://nginx.org/en/docs/beginners_guide.html)
- [Understanding Proxy Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [Microservices Architecture](https://microservices.io/)

📖 **Included Documentation**:
- **[TECHNOLOGY_GUIDE.md](TECHNOLOGY_GUIDE.md)** - Simple explanations of each technology
- **[NGINX_EXAMPLES.md](NGINX_EXAMPLES.md)** - Complete real-world configurations
- **[HOST_PATTERNS.md](HOST_PATTERNS.md)** - Understanding different hosting patterns

---

## 🚀 Quick Start

### 📥 Installation

```bash
# Clone the repository
git clone https://github.com/xoxxel/NGINX_config_generate.git

# Navigate to project directory
cd NGINX_config_generate

# Run the tool (Python 3.6+ required)
python nginx_gen.py
```

### ⚡ Instant Usage

```bash
# Interactive mode - guided setup
python nginx_gen.py

# Quick CLI - for experienced users
python nginx_gen.py --tech 7 --service blog --host-pattern 1
```

---

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

## 🔧 Installation & Setup

### 📋 Requirements
- 🐍 Python 3.6 or higher
- 💻 Any operating system (Windows, macOS, Linux)
- 🌐 No additional dependencies required!

### 📥 Clone & Install

```bash
# Method 1: HTTPS
git clone https://github.com/xoxxel/NGINX_config_generate.git

# Method 2: SSH (if you have SSH keys)
git clone git@github.com:xoxxel/NGINX_config_generate.git

# Navigate to directory
cd NGINX_config_generate

# Test installation
python nginx_gen.py --help
```

### 🚀 First Run

```bash
# Start with interactive mode
python nginx_gen.py

# Follow the prompts:
# 1. Choose technology (1-10)
# 2. Enter service name
# 3. Select host pattern
# 4. Get your configuration!
```

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

## 🤝 Contributing & Development

### 👨‍💻 Created by **[@xoxxel](https://github.com/xoxxel)**

**🎯 Join the development!** This tool is actively maintained and welcomes contributions.

### 🌟 How to Contribute

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/NGINX_config_generate.git

# 3. Create a feature branch
git checkout -b feature/your-awesome-feature

# 4. Make your changes and test
python nginx_gen.py --help

# 5. Commit and push
git commit -m "Add: your awesome feature"
git push origin feature/your-awesome-feature

# 6. Create a Pull Request
```

### 🚀 Contribution Ideas
- 🔧 **New Technology Templates**: Add support for new frameworks
- 🌐 **Host Pattern Improvements**: Better hosting environment support  
- 📖 **Documentation**: Improve guides and examples
- 🐛 **Bug Fixes**: Report and fix issues
- ✨ **Feature Requests**: Suggest new functionality

### 💡 Development Roadmap
- 🔄 **Phase 2**: Convert to REST API with Flask/FastAPI
- 🖥️ **Phase 3**: Web interface for non-technical users
- 📊 **Phase 4**: Configuration management dashboard
- 🔌 **Phase 5**: Integration with popular deployment tools

---

## 📞 Support & Community

- 🐛 **Issues**: [GitHub Issues](https://github.com/xoxxel/NGINX_config_generate/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/xoxxel/NGINX_config_generate/discussions)
- ⭐ **Star the repo** if this tool helped you!
- 🔄 **Share with colleagues** who struggle with NGINX configs

---

## 📄 License

📝 **MIT License** - Free to use in personal and commercial projects!

## 🎉 Credits & Acknowledgments

### 👨‍💻 **Creator**: [@xoxxel](https://github.com/xoxxel)
**Mission**: Simplifying microservice NGINX configuration for developers worldwide

### 🙏 **Special Thanks**
- 🌟 **Early contributors** who provided feedback and testing
- 📚 **NGINX community** for excellent documentation
- 🚀 **DevOps engineers** who inspired this tool's creation

### 💪 **Built for Developers**
Perfect for developers who want quick, reliable NGINX location blocks without memorizing complex syntax.

---

<div align="center">

## 🌟 **Star this repo if it helped you!** ⭐

**Made with ❤️ by [@xoxxel](https://github.com/xoxxel) for the developer community**

[![GitHub stars](https://img.shields.io/github/stars/xoxxel/NGINX_config_generate?style=social)](https://github.com/xoxxel/NGINX_config_generate/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/xoxxel/NGINX_config_generate?style=social)](https://github.com/xoxxel/NGINX_config_generate/network)
[![GitHub issues](https://img.shields.io/github/issues/xoxxel/NGINX_config_generate)](https://github.com/xoxxel/NGINX_config_generate/issues)

**🚀 Happy configuring! 🚀**

</div>

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
