# DNS Resolver

A fast, multi-service DNS resolver with intelligent caching and TTL-based cache expiration built with Go, Python, and vanilla JavaScript.

## Features

- **DNS Resolution:** Resolves domain names to IP addresses using Go's native `net` package
- **Smart Caching with TTL:** Python Flask service with SQLite backend caches results with configurable time-to-live
- **Cache Expiration:** Automatic cache invalidation after 1 day to ensure fresh results
- **Clean UI:** Minimalist dark-themed frontend for easy domain resolution
- **Multi-Service Architecture:** Go backend communicates with Python cache service

## Tech Stack

- **Backend API:** Go
- **Cache Service:** Python (Flask + SQLite)
- **Frontend:** HTML, CSS, JavaScript
- **Build Scripts:** Bash/Batch

## Architecture
```
Frontend (HTML/JS)
    ↓
Go Backend (port 8080)
    ↓
Python Cache Service (port 5050) + TTL validation
    ↓
SQLite Database
```

## Installation

### Prerequisites
- Go 1.20+
- Python 3.10+

### Build

**Linux/Mac:**
```bash
chmod +x scripts/build.sh
./scripts/build.sh
```

**Windows:**
```bat
scripts\build.bat
```

## Usage

**Linux/Mac:**
```bash
./scripts/run.sh
```

**Windows:**
```bat
scripts\run.bat
```

Then open `frontend/index.html` in your browser and start resolving domains.

## How It Works

1. User enters domain in frontend
2. Frontend calls Go API at `localhost:8080/lookup`
3. Go checks Python cache service at `localhost:5050`
4. Cache service validates TTL—if expired, returns cache miss
5. On cache miss, Go performs DNS lookup and stores result with timestamp
6. IP address returned to frontend and displayed

## Cache Behavior

- **TTL:** 1 hour (3600 seconds)
- **Expired entries:** Treated as cache misses, triggering fresh DNS lookup
- **Storage:** Domain, IP, and timestamp stored in SQLite

## Project Structure
```
dns-resolver/
├── backend/
│   ├── api/           # Go backend
│   ├── flask-server/  # Python cache service
│   ├── log/           # Logging utilities
│   ├── resources/     # SQLite database
├── frontend/          # HTML/CSS/JS
└── scripts/           # Build and run scripts
```

## License

MIT

## Author

Muhammad Hasan - [GitHub](https://github.com/mhaxanali)