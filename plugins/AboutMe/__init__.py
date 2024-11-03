# 导入账户处理模块和必要的NoneBot模块
import CMCBot.LCAU as LCAU
from nonebot import on_command, logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
import json

About = on_command("关于", aliases={"关于", "about"}, priority=5)

@About.handle()
async def _(bot: Bot, event: GroupMessageEvent) -> None:
    AboutText = []
    try:
        with open("about.json", mode="r", encoding="UTF-8") as Aboutf:
            AboutText1 = json.load(Aboutf)
            AboutText.append(f"+==={AboutText1['BotName']}======+\n")
            AboutText.append(f"版本：{AboutText1['version']}\n")
            AboutText.append(f"介绍：{AboutText1['description']}\n")
            AboutText.append(f"作者：{AboutText1['author']}\n")
            AboutText.append(f"+======功能=========+\n")
            for item in AboutText1.get("function", []):
                AboutText.append(f"{item}\n")
            AboutText.append(f"+======命令=========+\n")
            for item in AboutText1.get("command", []):
                AboutText.append(f"{item}\n")
            AboutText.append(f"+===================+\n")
            logger.info("AboutText: " + ''.join(AboutText))
    except FileNotFoundError:
        logger.error("about.json not found")
        AboutText = ["文件不存在，请联系管理员。"]
    except Exception as e:
        logger.error(f"出现错误: {e}")
        AboutText = ["出现错误，请联系管理员。"]

    await About.finish(''.join(AboutText))
