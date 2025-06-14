# <a href="https://instagram.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="28" valign="middle"/></a> Instagram Content Downloader


<div align="center">

[![Instagram Downloader](https://img.shields.io/badge/Instagram-Downloader-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)](https://creativecommons.org/licenses/by-nd/4.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=black)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)](https://github.com/GhostKX/Instagram-Data-Downloader)


**Professional-Grade Instagram Content Downloading Toolkit**

*A comprehensive collection of 6 specialized Python scripts for downloading Instagram posts, reels, stories, and highlights with enterprise-level reliability and HD quality optimization.*

[🚀 Quick Start](#-quick-start) • [📱 Scripts Overview](#-scripts-overview) • [🛠️ Installation](#-installation) • [📖 Usage Guide](#-usage-guide) • [🔐 Authentication](#-authentication-setup)

---

</div>

## ✨ Key Features

<table>
<tr>
<th width="25%">🎯 Feature</th>
<th width="25%">🌐 Public Content</th>
<th width="25%">🔐 Private Content</th>
<th width="25%">🎵 Audio Extraction</th>
</tr>
<tr>
<td><strong>Content Types</strong></td>
<td>Posts, Reels, IGTV</td>
<td>Stories, Highlights, Private Posts</td>
<td>MP3 from any video</td>
</tr>
<tr>
<td><strong>Quality</strong></td>
<td>HD, 4K, Original</td>
<td>Maximum Available</td>
<td>192kbps MP3</td>
</tr>
<tr>
<td><strong>Authentication</strong></td>
<td>❌ None Required</td>
<td>✅ Cookies/Login</td>
<td>❌ None Required</td>
</tr>
<tr>
<td><strong>Special Features</strong></td>
<td>Metadata Extraction</td>
<td>Anti-Detection</td>
<td>Auto Cleanup</td>
</tr>
</table>

### 📂 **What's Inside this Toolkit?**
- **6 Specialized Scripts** - Each optimized for specific scenarios
- **Military-Grade Reliability** - Robust error handling and retry mechanisms
- **HD Quality Processing** - Automatic codec optimization with FFmpeg
- **Zero Configuration** - Works out of the box with minimal setup
- **Privacy Focused** - Secure authentication with no data collection

---

## 🚀 Quick Start

### ⚡ **30-Second Setup**

```bash
# 1. Clone and navigate
git clone https://github.com/your-repo/instagram-downloader.git
cd instagram-downloader

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start downloading
python public_posts_reels.py
```

### 🎯 **Choose Your Script**

| Script | Perfect For | Speed | Quality |
|--------|-------------|--------|---------|
| **`public_posts_reels.py`** | Quick public downloads | ⚡⚡⚡ | Standard |
| **`public_video_post_reels_HD.py`** | HD video content | ⚡⚡ | HD/4K |
| **`public_audio_file.py`** | Music extraction | ⚡⚡⚡ | 192kbps |
| **`private_posts_reels.py`** | Private content with login | ⚡⚡ | Standard |
| **`private_video_content_HD.py`** | Premium private HD | ⚡ | Maximum |
| **`public_private_data_HD.py`** | Universal downloader | ⚡ | Ultimate |

---

## 📱 Scripts Overview

### 🌐 **Public Content Scripts**

<details>
<summary><strong>📱 public_posts_reels.py</strong> - Essential Public Downloader</summary>

**🎯 Perfect for**: Beginners, quick downloads, metadata extraction

**✨ Key Features**:
- ⚡ Lightning-fast downloads
- 📊 Complete metadata extraction (likes, comments, captions)
- 🔄 Automatic retry mechanisms
- 📁 Organized file structure

**Usage**:
```python
# Edit the script
url = 'https://www.instagram.com/p/YOUR_POST_ID/'
python public_posts_reels.py
```

**Output Example**:
```
📄 Title: Amazing sunset photo
👤 Username: @photographer_pro
❤️ Likes: 1,234 • 💬 Comments: 56
✅ Downloaded: photographer_pro/2024-12-14_sunset.jpg
```

</details>

<details>
<summary><strong>🎬 public_video_post_reels_HD.py</strong> - HD Video Specialist</summary>

**🎯 Perfect for**: High-quality video content, professional use

**✨ Key Features**:
- 🎬 4K/HD video downloads
- 🔧 Automatic H.264 codec optimization
- 📱 Mobile-friendly format conversion
- 💾 Efficient storage management

**Processing Pipeline**:
```
📥 Downloading best quality...
🔄 Optimizing codec (H.264)...
📱 Ensuring mobile compatibility...
✅ HD video ready: insta_video_enhanced.mp4
```

</details>

<details>
<summary><strong>🎵 public_audio_file.py</strong> - Audio Extraction Master</summary>

**🎯 Perfect for**: Music lovers, podcast creators

**✨ Key Features**:
- 🎵 High-quality MP3 extraction (192kbps)
- 🔄 Interactive URL input
- 🧹 Automatic cleanup

**Interactive Flow**:
```bash
python public_audio_file.py
📥 Paste Instagram URL: [your_url_here]
🎧 Extracting audio and converting to MP3...
✅ Success! MP3 saved as: Instagram_audio/insta_audio_xyz789.mp3
```

</details>

### 🔐 **Private Content Scripts**

<details>
<summary><strong>🔒 private_posts_reels.py</strong> - Authenticated Downloader</summary>

**🎯 Perfect for**: Private accounts, exclusive content

**✨ Key Features**:
- 🔐 Secure login authentication
- 🛡️ Advanced anti-detection
- 📱 Private stories and highlights access

**Setup**:
```python
username = 'your_instagram_username'
password = 'your_secure_password'
url = 'https://www.instagram.com/p/PRIVATE_POST_ID/'
```

</details>

<details>
<summary><strong>🏆 private_video_content_HD.py</strong> - Premium Private HD</summary>

**🎯 Perfect for**: Maximum quality private content

**✨ Key Features**:
- 🍪 Cookie-based authentication (most secure)
- 🎬 4K/8K video support
- 📁 Professional output organization

</details>

<details>
<summary><strong>🌟 public_private_data_HD.py</strong> - Universal Master Tool</summary>

**🎯 Perfect for**: Power users, mixed content types

**✨ Key Features**:
- 🌐 Handles ALL Instagram content types
- 🤖 Intelligent codec detection
- 📊 Comprehensive logging

</details>

---

## 🛠️ Installation

### 📋 **Requirements**

| Component | Minimum | Recommended |
|-----------|---------|------------|
| **Python** | 3.8+ | 3.10+ |
| **RAM** | 2GB | 4GB+ |
| **Storage** | 1GB | 5GB+ |
| **Internet** | 5 Mbps | 25+ Mbps |

### 🔧 **Step-by-Step Installation**

#### **1. Environment Setup**
```bash
# Create virtual environment (recommended)
python -m venv instagram_downloader
source instagram_downloader/bin/activate  # Linux/Mac
instagram_downloader\Scripts\activate     # Windows
```

#### **2. Install Dependencies**
```bash
# Install Python packages
pip install -r requirements.txt

# Verify installation
python -c "import instaloader, yt_dlp; print('✅ All packages ready!')"
```

#### **3. System Dependencies**

**Windows:**
```powershell
# Install FFmpeg via Chocolatey
choco install ffmpeg
```

**macOS:**
```bash
# Install FFmpeg via Homebrew
brew install ffmpeg
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg
```

#### **4. Verify Installation**
```bash
python -c "
import sys, yt_dlp, instaloader, subprocess
print('✅ Python:', sys.version[:5])
print('✅ yt-dlp:', yt_dlp.version.__version__)
print('✅ instaloader: Ready')
subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
print('✅ FFmpeg: Ready')
print('🎉 Installation Complete!')
"
```

---

## 📖 Usage Guide

### 🎯 **Common Scenarios**

#### **Scenario 1: Download Public Reel**
```bash
# 1. Copy Instagram reel URL
# 2. Edit public_video_post_reels_HD.py:
video_url = "https://www.instagram.com/reel/ABC123/"

# 3. Run script
python public_video_post_reels_HD.py
```

#### **Scenario 2: Extract Audio**
```bash
# Interactive audio extraction
python public_audio_file.py
# Paste URL when prompted
```

#### **Scenario 3: Private Content**
```bash
# 1. Setup authentication (see below)
# 2. Configure private script
# 3. Run with authentication
python private_posts_reels.py
```

### 📁 **File Organization**

```
Instagram-Downloads/
├── Instagram/                    # Main downloads
│   ├── 20241214_abc123/         # Date-organized
│   │   ├── video1.mp4
│   │   └── image1.jpg
├── Instagram_audio/             # Audio extractions
│   └── insta_audio_xyz789.mp3
└── [username]/                  # User-specific
    ├── 2024-12-14_post.jpg
    └── 2024-12-14_reel.mp4
```

---

## 🔐 Authentication Setup

### 🍪 **Method 1: Cookie Authentication (Recommended)**

1. **Install Browser Extension**:
   - Chrome: [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt)
   - Firefox: [cookies.txt](https://addons.mozilla.org/firefox/addon/cookies-txt)

2. **Export Cookies**:
   - Login to Instagram in browser
   - Click extension → Export for instagram.com
   - Save as `cookies.txt` in script directory

3. **Use in Scripts**:
   ```python
   cookies_path = "cookies.txt"
   ```

### 🔑 **Method 2: Username/Password**

```python
# Secure credential setup
username = 'your_instagram_username'
password = 'your_secure_password'
```

⚠️ **Security Note**: Use app-specific passwords and store credentials securely.

---

## 🛠️ Advanced Configuration

### 🎬 **Video Quality Settings**

```python
# Maximum Quality
"-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best"

# Codec-Specific
"-f", "best[vcodec*=h264]"

# Mobile Compatible
"-f", "best[height<=1080]"
```

### 🎵 **Audio Quality Options**

```python
# High-Quality MP3
"-acodec", "libmp3lame"
"-ab", "192k"  # 192 kbps bitrate
```

### 📊 **Performance Benchmarks**

| Content Type | File Size | Processing Time |
|-------------|-----------|-----------------|
| Image Post | 1-5 MB | 3-6 seconds     |
| Video Reel | 10-50 MB | 5-20 seconds    |
| HD Video | 25-100 MB | 10-25 seconds   |
| Audio Extract | 5-15 MB | 5-15 seconds    |

---

## 🔍 Troubleshooting

### ❌ **Common Issues**

**Authentication Failed:**
```bash
# Solution: Update cookies or check credentials
# Re-export cookies from browser
```

**Download Failed:**
```bash
# Solution: Update yt-dlp
pip install --upgrade yt-dlp
```

**FFmpeg Not Found:**
```bash
# Solution: Verify FFmpeg installation
ffmpeg -version
```

**Private Content Access:**
```bash
# Solution: Ensure you have viewing permissions
# Check if content is still available
```

---

## 📊 Dependencies

### **Core Requirements**
(`requirements.txt`)
```
annotated-types==0.7.0
certifi==2025.4.26
charset-normalizer==3.4.2
gallery_dl==1.29.7
idna==3.10
instaloader==4.14.1
pillow==11.2.1
pycryptodomex==3.23.0
pydantic==2.11.5
pydantic_core==2.33.2
PySocks==1.7.1
requests==2.32.3
typing-inspection==0.4.1
typing_extensions==4.14.0
urllib3==2.4.0
yt-dlp==2025.5.22
```

### **System Dependencies**
- **Python 3.8+**: Core runtime
- **FFmpeg**: Video/audio processing
- **Stable Internet**: Download reliability

---

## 🔒 Privacy & Legal

### **Best Practices**
- ✅ Only download content you have permission to access
- ✅ Respect Instagram's Terms of Service
- ✅ Use for personal purposes only
- ✅ Keep credentials secure

### **Security**
- 🔐 Never share Instagram credentials
- 🍪 Use cookie authentication when possible
- 🔄 Regularly update authentication tokens
- 🛡️ No data collection by scripts

---

## 📜 License

This project is for **educational purposes only**. Please respect Instagram's Terms of Service and only download content you have permission to access.

---

<div align="center">

## 👨‍💻 Author

Developed by **GhostKX**

[![GitHub](https://img.shields.io/badge/GitHub-@GhostKX-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GhostKX)

</div>