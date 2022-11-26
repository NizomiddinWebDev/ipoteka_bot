from datetime import datetime, timedelta
from utils.db_api.model import getUserList, unban_user
import asyncio
import aioschedule


async def unban_user_month():
    today_date = datetime.now().date()
    users = await getUserList()
    for user in users:
        if user.ban and user.date_ban == str(today_date):
            try:
                await unban_user(user.tg_user_id)
            except:
                pass


async def scheduler():
    aioschedule.every().day.at("22:00").do(unban_user_month)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
