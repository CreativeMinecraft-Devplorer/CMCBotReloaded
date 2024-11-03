import nonebot
from nonebot import on_notice, logger, on_request
from nonebot.adapters.onebot.v11 import Bot, Event

# 事件处理插件
notice_event = on_notice()
request_event = on_request()


# 事件名称与对应日志信息的映射
event_log_mapping = {
    "notice.friend_add": "好友添加通知",
    "notice.friend_recall": "私聊消息撤回通知",
    "notice.group_admin.set": "群聊管理员变动 - 增加",
    "notice.group_admin.unset": "群聊管理员变动 - 减少",
    "notice.group_ban.ban": "群聊禁言 - 禁言",
    "notice.group_ban.lift_ban": "群聊禁言 - 取消禁言",
    "notice.group_card": "群成员名片更新",
    "notice.group_decrease.leave": "群聊成员减少 - 主动退群",
    "notice.group_decrease.kick": "群聊成员减少 - 成员被踢",
    "notice.group_increase.approve": "群聊成员增加 - 管理员已同意入群",
    "notice.group_increase.invite": "群聊成员增加 - 管理员邀请入群",
    "notice.group_recall": "群聊消息撤回通知",
    "notice.group_upload": "群聊文件上传通知",
    "notice.notify.input_status": "输入状态更新通知",
    "notice.profile_like": "点赞通知",
    "notice.notify.title": "群成员头衔变更通知",
    "notice.notify.honor": "群成员荣誉变更通知",
    "request.group.add": "加群请求通知",

}

@notice_event.handle()
async def handle_notice_event(data: Event, bot: Bot):
    notice_event_name = data.get_event_name()
    logger.info(f"收到新的通知：{notice_event_name}")
    logger.info(f"事件数据：{data.get_event_description()}")
    logger.info("判断事件...CheckEvent...")

    # 使用映射字典记录日志
    log_message = event_log_mapping.get(notice_event_name, f"未处理的事件类型：{notice_event_name}")
    logger.info(log_message)


@request_event.handle()
async def handle_notice_event(data: Event, bot: Bot):
    notice_event_name = data.get_event_name()
    logger.info(f"收到新的通知：{notice_event_name}")
    logger.info(f"事件数据：{data.get_event_description()}")
    logger.info("判断事件...CheckEvent...")

    # 使用映射字典记录日志
    log_message = event_log_mapping.get(notice_event_name, f"未处理的事件类型：{notice_event_name}")
    logger.info(log_message)