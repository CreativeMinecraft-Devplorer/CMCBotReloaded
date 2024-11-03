# 导入账户处理模块和必要的NoneBot模块
import CMCBot.LCAU as LCAU
from nonebot import on_command, require, on_message, on
from nonebot.rule import to_me, is_type
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment, GroupMessageEvent
from nonebot import logger
from nonebot.params import CommandArg, EventPlainText, EventMessage
import asyncio
import RandomPassword
from nonebot.exception import FinishedException
from CMCBot import AuthMeAccount
from CMCBot.crypt import md5_hash


# 初始化密码生成器
Rdp = RandomPassword.RandomPassword()

# 注册命令
AddAccount = on_command("注册", aliases={"注册","新建账户","reg","register","r"}, priority=5)

# 处理注册命令
@AddAccount.handle()
async def _(bot: Bot, message: GroupMessageEvent, args: Message = CommandArg()):
    """处理用户注册请求
    参数:
    - bot: Bot实例
    - message: GroupMessageEvent实例，包含消息事件信息
    - args: CommandArg，命令参数
    """
    args = args.extract_plain_text()
    UserId = message.user_id
    if not args:
        await AddAccount.finish("格式：/reg <MC游戏名字>")

    InputText = args
    try:
        FindQQ = AuthMeAccount.check_duplicate_account(tencent_qq=UserId)
        if FindQQ['isFind']:
            logger.info(f"用户{UserId}尝试注册已注册过的账户{InputText},阻断注册")
            await AddAccount.finish("您已经注册过了哦~")
        else:
            logger.info(f"用户{UserId}尝试注册新账户{InputText}，审核通过")
        pwd = Rdp.generate_random_password(length=8, 
                                       include_upper_case_alphabets=True, 
                                       include_lower_case_alphabets=True, 
                                       include_special_characters=False, 
                                       include_numbers=True)
        AuthMeAccount.add_authme_account(InputText, str(pwd), int(UserId))
        await bot.call_api("send_private_msg", user_id=UserId, message=f"您在CreativeMinecraft注册的账户如下：\nUserName: {InputText}\nPassword: {pwd}\n服务器信息：\n地址：minecraft.starryfun.icu\n端口：无[直接输入即可]\n版本：Java 1.12.2到1.21\n\n注意：\n 1.请妥善保管，不要丢失哦~\n 2.及时更改密码，避免被盗\n3.不要刷账户\n\n命令：\n1. /cp <原来的密码> <你要改的密码>: 更改密码\n2. /login {pwd}: 登录\n3. /totp: 绑定2FA")
        await AddAccount.finish(f"账户已发送到主人的账户下了呢~")
    except FinishedException:
        return 0
    except Exception as e:
        await AddAccount.finish(f"Err:{str(e)}")