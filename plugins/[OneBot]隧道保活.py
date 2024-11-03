import asyncio
import imgkit
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message, MessageSegment
from nonebot import on_command, require, on
from nonebot.log import logger
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.exception import FinishedException
import CMCBot.LCAU as LCAU
import CMCBot.WebView as WebView
from CMCBot.Hitokoto import get_yiyan

# 插件元数据
__plugin_meta__ = PluginMetadata(
    name="定时发送语录",
    description="定时向指定用户发送语录",
    usage="/baohuo.gbot",
    type="application",
    homepage="https://example.com",
    config=None,
    supported_adapters={"~onebot.v11"},
    extra={}
)

# 定义命令处理器
GetBot = on_command("baohuo.gbot", aliases={"baohuo.gbot"}, priority=5)

# 初始化定时任务
scheduler = require("nonebot_plugin_apscheduler").scheduler

# 命令处理函数
@GetBot.handle()
async def handle_command(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    global bot_1
    bot_1 = bot
    user_id = 1280993766

    try:
        await bot.send_private_msg(user_id=user_id, message=str("qwq"))
        logger.info(f"私信发送成功给用户 {user_id}")
    except Exception as e:
        logger.error(f"私信发送失败给用户 {user_id}: {e}")

    # 启动定时任务
    if 'baohuo_task' not in [job.id for job in scheduler.get_jobs()]:
        scheduler.add_job(baohuo, 'interval', minutes=30, id='baohuo_task')
        logger.info("定时任务已添加")
    else:
        logger.info("定时任务已存在")

# 定时任务函数
async def baohuo():
    global bot_1
    user_id = 1280993766
    try:
        await bot_1.send_private_msg(user_id=user_id, message="qwq")
        logger.info(f"定时任务：私信发送成功给用户 {user_id}")
    except Exception as e:
        logger.error(f"定时任务：私信发送失败给用户 {user_id}: {e}")

# 注册定时任务
@scheduler.scheduled_job('interval', minutes=30, id='baohuo_task')
async def schedule_baohuo():
    await baohuo()