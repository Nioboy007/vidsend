from pyrogram import Client, filters
import os

# Function to send video files from folder to user
def send_videos(client, folder_path, chat_id):
    try:
        total_videos = len([filename for filename in os.listdir(folder_path) if filename.endswith((".mp4", ".avi", ".mkv"))])
        sent_videos = 0
        
        for filename in os.listdir(folder_path):
            if filename.endswith((".mp4", ".avi", ".mkv")):
                video_path = os.path.join(folder_path, filename)
                client.send_video(chat_id, video_path)
                sent_videos += 1
                print(f"Sent {sent_videos}/{total_videos} videos.")
    
    except Exception as e:
        print(f"An error occurred while sending videos: {e}")

# Your bot API token
api_id = "10471716"
api_hash = "f8a1b21a13af154596e2ff5bed164860"
bot_token = "6680585225:AAEXQVe8voeIvCJ6ebzVN8cGdi4hmzKkkq4"

# Create Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Folder path where videos are stored
folder_path = "X-Vid"

# Handler for /begin command
@app.on_message(filters.command("begin") & filters.private)
def begin_command_handler(client, message):
    chat_id = message.chat.id
    send_videos(client, folder_path, chat_id)

# Handler for /start command
@app.on_message(filters.command("start") & filters.private)
def start_command_handler(client, message):
    message.reply_text("Hello! Send me the command /begin to start sending videos to you.")

with app:
    # Start the bot
    try:
        app.run()
    except Exception as e:
        print(f"An error occurred while running the bot: {e}")
