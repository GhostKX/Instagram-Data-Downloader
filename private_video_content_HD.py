import subprocess
import os
import datetime

# 🔗 Instagram URL: Can be a post, reel, story, or highlight
url = "https://www.instagram.com/link/"  # Replace with actual URL

# 🍪 Cookies file path (must be logged-in Instagram cookies)
cookies_path = "cookies.txt"

# 📁 Output file naming (use playlist index if available)
output_template = "Instagram/%(playlist_index)03d_%(title)s_%(id)s.%(ext)s"

print("📅", datetime.datetime.now())
print("📥 Starting download from Instagram...")

try:
    result = subprocess.run([
        "yt-dlp",
        "--cookies", cookies_path,                             # Authenticate via cookies
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",    # Best video+audio combo, fallback if needed
        "--merge-output-format", "mp4",                        # Final format: .mp4
        "--postprocessor", "FFmpegVideoConvertor",             # Trigger ffmpeg to re-encode
        "--postprocessor-args", (                              # 🔧 Re-encode settings for compatibility
            "-c:v libx264 -preset superfast -crf 23 "
            "-c:a aac -b:a 192k -movflags +faststart"
        ),
        "-o", output_template,                                 # Output filename structure
        url
    ])

    if result.returncode == 0:
        print("✅ Download completed successfully!")
    else:
        print("❌ Download failed with code:", result.returncode)




except Exception as e:
    print("🚨 An error occurred during download:")
    print(e)
