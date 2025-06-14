import subprocess
import os

# 🎥 Instagram video URL to download
video_url = "https://www.instagram.com/p/shortcode/"

# 🗂️ Filenames for the original download and the re-encoded output
downloaded_file = "insta_video.mp4"
enhanced_file = "insta_video_enhanced.mp4"

try:
    # ⬇️ Download the best quality MP4 video + audio using yt-dlp
    download = subprocess.run([
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",
        "-o", downloaded_file,
        video_url
    ])

    # ❌ Check if download failed or file is missing
    if download.returncode != 0 or not os.path.exists(downloaded_file):
        print("❌ Download failed or file not found.")
        exit(1)

    # 🔄 Re-encode the downloaded video to H.264 (libx264) for compatibility
    re_encode = subprocess.run([
        "ffmpeg", "-y"  # Overwrite output file if it exists
        "-i", downloaded_file,
        "-c:v", "libx264",
        "-preset", "superfast",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "192k",
        enhanced_file,
    ])

    # ❌ Check if re-encoding failed or output file is missing
    if re_encode.returncode != 0 or not os.path.exists(enhanced_file):
        print("❌ Re-encoding failed.")
        exit(1)

    # 🧹 Clean up: remove the original downloaded file to save space
    os.remove(downloaded_file)

    # ✅ All done successfully!
    print('✅ Done')

except Exception as e:
    # ⚠️ Catch and print any unexpected errors
    print(f"⚠️ An error occurred: {e}")
