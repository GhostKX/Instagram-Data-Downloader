import instaloader

# 📦 Create an Instaloader instance (used for downloading & context)
L = instaloader.Instaloader()

# 🔗 Instagram post URL (make sure it's a public post or you're logged in for private ones)
url = 'https://www.instagram.com/p/shortcode/'

# 🧩 Extract the shortcode from the URL (the unique part of the post URL)
shortcode = url.strip('/').split('/')[-1]

try:
    # 📥 Fetch the post using the shortcode
    post = instaloader.Post.from_shortcode(L.context, shortcode)

    # 💾 Download the post content into a folder named after the user
    L.download_post(post, target=post.owner_username)

    # 📄 Print metadata from the post
    print("📄 Title:       ", post.title)
    print("📝 Description: ", post.caption)
    print("📷 Media URL:   ", post.url)
    print("🎥 Is Video:    ", post.is_video)
    print("❤️ Likes:       ", post.likes)
    print("💬 Comments:    ", post.comments)
    print("👤 Username:    ", post.owner_username)
    print("📍 Location:    ", post.location)

except Exception as e:
    # ⚠️ Catch and display any errors (e.g., private post, bad shortcode, rate limit)
    print(f"❌ Error: {e}")
