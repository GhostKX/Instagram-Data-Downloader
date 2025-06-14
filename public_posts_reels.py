import instaloader

L = instaloader.Instaloader()

url = 'https://www.instagram.com/p/shortcode/'

# Extract shortcode
shortcode = url.strip('/').split('/')[-1]

try:
    # Fetch post and download
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    L.download_post(post, target=post.owner_username)

    # Print metadatak
    print("📄 Title:", post.title)
    print("📝 Description:", post.caption)
    print("📷 Media URL:", post.url)
    print("🎥 Is Video:", post.is_video)
    print("❤️ Likes:", post.likes)
    print("💬 Comments:", post.comments)
    print("👤 Username:", post.owner_username)
    print("📍 Location:", post.location)
except Exception as e:
    print(f"❌ Error: {e}")