#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 NGINX Location Generator - Simple CLI Tool
Generate NGINX location blocks with numbered selection
"""

import argparse
import sys

# Supported technologies
TECHNOLOGIES = {
    1: {"name": "React SPA", "type": "spa", "port": "3000"},
    2: {"name": "Vue.js SPA", "type": "spa", "port": "5173"},
    3: {"name": "Next.js", "type": "ssr", "port": "3000"},
    4: {"name": "Express API", "type": "api", "port": "3000"},
    5: {"name": "Django", "type": "api", "port": "8000"},
    6: {"name": "Laravel", "type": "php", "port": "9000"},
    7: {"name": "WordPress", "type": "php", "port": "80"},
    8: {"name": "Socket.io", "type": "websocket", "port": "3001"},
    9: {"name": "Hugo Static", "type": "static", "port": "1313"},
    10: {"name": "Custom API", "type": "api", "port": "8000"}
}

# Host patterns
HOST_PATTERNS = {
    1: {"name": "CapRover", "pattern": "srv-captain--{service}"},
    2: {"name": "Docker Compose", "pattern": "{service}:{port}"},
    3: {"name": "Localhost", "pattern": "localhost:{port}"},
    4: {"name": "Custom Host", "pattern": "custom"}
}

# NGINX location templates
TEMPLATES = {
    'spa': """    # {service_name} - {tech_name}
    location /{service_name}/ {{
        proxy_pass http://{proxy_host}/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # SPA routing support
        try_files $uri $uri/ /{service_name}/index.html;
    }}""",
    
    'ssr': """    # {service_name} - {tech_name}
    location /{service_name}/ {{
        proxy_pass http://{proxy_host}/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
    }}""",
    
    'api': """    # {service_name} - {tech_name}
    location /{service_name}/ {{
        proxy_pass http://{proxy_host}/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}""",
    
    'php': """    # {service_name} - {tech_name}
    location /{service_name}/ {{
        proxy_pass http://{proxy_host}/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}""",
    
    'websocket': """    # {service_name} - {tech_name}
    location /{service_name}/ {{
        proxy_pass http://{proxy_host}/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }}""",
    
    'static': """    # {service_name} - {tech_name}
    location /{service_name}/ {{
        alias /var/www/{service_name}/;
        try_files $uri $uri/ =404;
        index index.html;
    }}"""
}

def show_help():
    """Display help information"""
    print("""
🚀 NGINX Location Generator - Usage Guide

Usage:
  python nginx_gen.py                    # Interactive mode
  python nginx_gen.py --list             # Show technologies
  python nginx_gen.py --patterns         # Show host patterns
  python nginx_gen.py --help             # This help

Quick CLI mode:
  python nginx_gen.py --tech 7 --service blog --host-pattern 1
  python nginx_gen.py -t 1 -s dashboard --host-pattern 2
  python nginx_gen.py -t 5 -s api --host-pattern 4 --custom-host "192.168.1.100:8000"

Parameters:
  --tech, -t        Technology number (1-10)
  --service, -s     Service name
  --host-pattern    Host pattern (1-4)
  --custom-host     Custom address for pattern 4

How it works:
1. Choose technology (number)
2. Enter service name
3. Select host pattern
4. NGINX config is generated

Examples:
  WordPress Blog:     --tech 7 --service blog --host-pattern 1
  React Dashboard:    --tech 1 --service dashboard --host-pattern 2
  Django API:         --tech 5 --service api --host-pattern 4 --custom-host "server:8000"

Output files:
  - location_block.conf   (location block)
  - install_guide.txt     (installation guide)
""")

def list_technologies():
    """Display supported technologies"""
    print("\n📋 Supported Technologies:")
    print("="*50)
    for num, tech in TECHNOLOGIES.items():
        print(f"{num:2d}. {tech['name']:<15} (Port: {tech['port']})")
    print()

def list_host_patterns():
    """Display host patterns"""
    print("\n🌐 Host Patterns:")
    print("="*40)
    for num, pattern in HOST_PATTERNS.items():
        print(f"{num}. {pattern['name']:<15} → {pattern['pattern']}")
    print("\nExamples:")
    print("1. srv-captain--blog     (CapRover)")
    print("2. frontend:3000         (Docker)")
    print("3. localhost:3000        (Local)")
    print("4. 192.168.1.100:8000    (Custom)")
    print()

def get_user_choice(prompt, options, allow_empty=False):
    """Get user choice with validation"""
    while True:
        try:
            choice = input(prompt).strip()
            if not choice and allow_empty:
                return None
            choice = int(choice)
            if choice in options:
                return choice
            print(f"Invalid choice {choice}! Please enter ({min(options)}-{max(options)})")
        except ValueError:
            print("Please enter a number!")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

def generate_proxy_host(pattern_choice, service_name, port):
    """Generate proxy host based on pattern"""
    pattern_info = HOST_PATTERNS[pattern_choice]
    
    if pattern_choice == 1:  # CapRover
        return f"srv-captain--{service_name}"
    elif pattern_choice == 2:  # Docker Compose
        return f"{service_name}:{port}"
    elif pattern_choice == 3:  # Localhost
        return f"localhost:{port}"
    elif pattern_choice == 4:  # Custom
        return input("Enter custom host address: ").strip()

def generate_location_block(service_name, tech_info, proxy_host):
    """Generate NGINX location block"""
    template = TEMPLATES[tech_info['type']]
    
    return template.format(
        service_name=service_name,
        tech_name=tech_info['name'],
        proxy_host=proxy_host
    )

def create_install_guide(service_name, tech_info, proxy_host, location_block):
    """Create installation guide"""
    guide = f"""
# 📖 NGINX Configuration Installation Guide

## Service Information:
- Service name: {service_name}
- Technology: {tech_info['name']}
- Internal address: {proxy_host}
- Access path: https://yourdomain.com/{service_name}/

## Installation Steps:

### 1. Find nginx.conf file
```bash
# Usually located in one of these paths:
/etc/nginx/nginx.conf
/etc/nginx/sites-available/default
/usr/local/nginx/conf/nginx.conf
```

### 2. Edit the file
```bash
sudo nano /etc/nginx/sites-available/default
```

### 3. Add location block
Inside the `server {{` section, add this code:

{location_block}

### 4. Test configuration
```bash
sudo nginx -t
```

### 5. Apply changes
```bash
sudo systemctl reload nginx
```

## Final test:
- Browser: https://yourdomain.com/{service_name}/
- cURL: curl https://yourdomain.com/{service_name}/

## Important notes:
- Make sure {service_name} service is running on {proxy_host}
- If using SSL, additional configuration may be required
- For local testing, you can use localhost

## Support:
- Documentation: HOST_PATTERNS.md
- Examples: NGINX_EXAMPLES.md
"""
    return guide

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='🚀 NGINX Generator', add_help=False)
    parser.add_argument('--help', '-h', action='store_true', help='Show help')
    parser.add_argument('--list', '-l', action='store_true', help='Show technologies')
    parser.add_argument('--patterns', '-p', action='store_true', help='Show host patterns')
    parser.add_argument('--tech', '-t', type=int, help='Technology number (1-10)')
    parser.add_argument('--service', '-s', type=str, help='Service name')
    parser.add_argument('--host-pattern', type=int, choices=[1,2,3,4], help='Host pattern (1-4)')
    parser.add_argument('--custom-host', type=str, help='Custom address for pattern 4')
    
    args = parser.parse_args()
    
    if args.help:
        show_help()
        return
    
    if args.list:
        list_technologies()
        return
        
    if args.patterns:
        list_host_patterns()
        return
    
    # Quick CLI mode
    if args.tech and args.service and args.host_pattern:
        tech_info = TECHNOLOGIES[args.tech]
        service_name = args.service
        
        if args.host_pattern == 4 and not args.custom_host:
            print("Error: Custom host pattern requires --custom-host parameter")
            return
            
        if args.host_pattern == 4:
            proxy_host = args.custom_host
        else:
            proxy_host = generate_proxy_host(args.host_pattern, service_name, tech_info['port'])
            
        # Generate and save
        location_block = generate_location_block(service_name, tech_info, proxy_host)
        
        print("Generated NGINX configuration:")
        print("="*60)
        print(location_block)
        
        # Save to files
        with open('location_block.conf', 'w', encoding='utf-8') as f:
            f.write(location_block)
        
        install_guide = create_install_guide(service_name, tech_info, proxy_host, location_block)
        with open('install_guide.txt', 'w', encoding='utf-8') as f:
            f.write(install_guide)
        
        print(f"\nFiles saved: location_block.conf, install_guide.txt")
        return
    
    # Interactive mode
    print("🚀 NGINX Location Generator")
    print("="*40)
    
    # Choose technology
    list_technologies()
    tech_choice = get_user_choice(
        "Choose technology (1-10): ",
        TECHNOLOGIES.keys()
    )
    tech_info = TECHNOLOGIES[tech_choice]
    
    # Get service name
    while True:
        service_name = input(f"\nEnter service name (e.g. blog, shop, api): ").strip()
        if service_name and service_name.replace('-', '').replace('_', '').isalnum():
            break
        print("Service name must contain only letters, numbers, - or _")
    
    # Choose host pattern
    list_host_patterns()
    host_choice = get_user_choice(
        "Choose host pattern (1-4): ",
        HOST_PATTERNS.keys()
    )
    
    # Generate proxy host
    proxy_host = generate_proxy_host(host_choice, service_name, tech_info['port'])
    
    # Generate location block
    location_block = generate_location_block(service_name, tech_info, proxy_host)
    
    # Display result
    print("\n" + "="*60)
    print("Generated NGINX configuration:")
    print("="*60)
    print(location_block)
    
    # Save to files
    with open('location_block.conf', 'w', encoding='utf-8') as f:
        f.write(location_block)
    
    # Create installation guide
    install_guide = create_install_guide(service_name, tech_info, proxy_host, location_block)
    with open('install_guide.txt', 'w', encoding='utf-8') as f:
        f.write(install_guide)
    
    print(f"\nFiles saved:")
    print(f"   📄 location_block.conf  - Configuration block")
    print(f"   📖 install_guide.txt    - Installation guide")
    
    print(f"\nSummary:")
    print(f"   Service: {service_name}")
    print(f"   Technology: {tech_info['name']}")
    print(f"   Host: {proxy_host}")
    print(f"   Path: https://yourdomain.com/{service_name}/")

if __name__ == "__main__":
    main()
