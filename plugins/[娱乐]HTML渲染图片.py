import imgkit
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot import on_command, require, on_message, on
from nonebot.rule import to_me, is_type
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment, GroupMessageEvent
from nonebot import logger
from nonebot.params import CommandArg, EventPlainText, EventMessage
import asyncio
import CMCBot.LCAU as LCAU
import CMCBot.WebView as WebView
from CMCBot.quote import Quote
import time
import re
import requests
from nonebot.exception import FinishedException

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 定义临时目录路径
TEMP_DIR = "plugins\\temp\\"

def sanitize_url(url):
    replacements = {
        'http': 'URL',
        '/': '_',
        ':': '_',
        '?': '_',
        '&': '_',
        '=': '_',
        '.': '_'
    }
    # 使用正则表达式替换所有字符
    pattern = '|'.join(re.escape(key) for key in replacements.keys())
    sanitized_url = re.sub(pattern, lambda m: replacements[m.group()], url)
    return sanitized_url


XRS = on_command("text", aliases={"text"}, priority=5)
@XRS.handle()
async def _(bot: Bot, message: GroupMessageEvent, event: GroupMessageEvent, args: Message = CommandArg()):
    args = args.extract_plain_text()
    UserID = message.user_id
    UserInfo = await bot.get_stranger_info(user_id=UserID)
    UserName = UserInfo["nickname"]
    try:
        path = await WebView.html2img(Quote(UserID, str(args), UserName=UserName), f"plugins/temp/html2img_output.png")
        # await asyncio.sleep(1)
        await XRS.finish(Message(MessageSegment.image(f"C:\\Users\\liu_q\\Documents\\Project\\CMCBot\\plugins\\temp\\html2img_output.png")))
    except FinishedException:
        logger.info("完成会话！")
    except Exception as e:
        logger.error(f"处理URL时出现错误：{e}")
        await XRS.finish(f"处理URL时出现错误：{e}")


URL = on_command("url", aliases={"url"}, priority=5)
@URL.handle()
async def _(bot: Bot, message: GroupMessageEvent, event: GroupMessageEvent, args: Message = CommandArg()):
    args = args.extract_plain_text()
    groupID = message.group_id
    try:
        path = await WebView.url2img(str(args), f"{TEMP_DIR}{sanitize_url(str(args))}.png")
        # await asyncio.sleep(1)
        await bot.call_api("send_group_msg", group_id=groupID, message="Puppeteer指导：Harcic#8042\n提示：请勿访问隐私页面，每次的渲染请求都会有缓存！有可能会在异常情况下发送出您的图片！")
        await URL.finish(Message(MessageSegment.image(f"C:\\Users\\liu_q\\Documents\\Project\\CMCBot\\{TEMP_DIR}{sanitize_url(str(args))}.png")))
    except FinishedException:
        logger.info("完成会话！")
    except Exception as e:
        logger.error(f"处理URL时出现错误：{e}")
        await URL.finish(f"处理URL时出现错误：{e}")