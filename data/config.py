from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
CHANNELS = ['@super_bot_chanel']
GROUPS = [-1001624989323]
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
ADMIN_PASSWORD = 'admin123'