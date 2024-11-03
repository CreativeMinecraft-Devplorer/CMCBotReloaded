import nonebot
from nonebot import on_notice, logger, on_request, on_metaevent, on_message
from nonebot.adapters.onebot.v11 import Bot, Event
from datetime import datetime

# 事件处理插件
notice_event = on_notice()
request_event = on_request()
meta_event = on_metaevent()
message_event = on_message()

def write_log(event_name: str, event_data: str):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] [{event_name}] - {event_data}\n")

# 事件名称与对应日志信息的映射
event_log_mapping = {
    "meta_event.lifecycle": "生命周期",
    "meta_event.lifecycle.enable": "生命周期 - OneBot 启用",
    "meta_event.lifecycle.disable": "生命周期 - OneBot 停用",
    "meta_event.lifecycle.connect": "生命周期 - WebSocket 连接成功",
    "meta_event.heartbeat": "心跳",
    "message.private": "私聊消息",
    "message.private.friend": "私聊消息 - 好友",
    "message.private.group": "私聊消息 - 群临时",
    "message.private.group_self": "私聊消息 - 群中自身发送",
    "message.private.other": "私聊消息 - 其他",
    "message.group": "群聊消息",
    "message.group.normal": "群聊消息 - 普通",
    "message.group.anonymous": "群聊消息 - 匿名消息",
    "message.group.notice": "群聊消息 - 系统提示",
    "message_sent.private": "私聊消息",
    "message_sent.private.friend": "私聊消息 - 好友",
    "message_sent.private.group": "私聊消息 - 群临时",
    "message_sent.private.group_self": "私聊消息 - 群中自身发送",
    "message_sent.private.other": "私聊消息 - 其他",
    "message_sent.group": "群聊消息",
    "message_sent.group.normal": "群聊消息 - 普通",
    "message_sent.group.anonymous": "群聊消息 - 匿名消息",
    "message_sent.group.notice": "群聊消息 - 系统提示",
    "request.friend": "加好友请求",
    "request.group.add": "加群请求 - 需要管理员权限",
    "request.group.invite": "邀请登录号入群",
    "notice.friend_add": "好友添加",
    "notice.friend_recall": "私聊消息撤回",
    "notice.offline_file": "接收到离线文件",
    "notice.client_status": "其他客户端在线状态变更",
    "notice.group_admin": "群聊管理员变动",
    "notice.group_admin.set": "群聊管理员变动 - 增加",
    "notice.group_admin.unset": "群聊管理员变动 - 减少",
    "notice.group_ban": "群聊禁言",
    "notice.group_ban.ban": "群聊禁言 - 禁言",
    "notice.group_ban.lift_ban": "群聊禁言 - 取消禁言",
    "notice.group_card": "群成员名片更新",
    "notice.group_decrease": "群聊成员减少",
    "notice.group_decrease.leave": "群聊成员减少 - 主动退群",
    "notice.group_decrease.kick": "群聊成员减少 - 成员被踢",
    "notice.group_decrease.kick_me": "群聊成员减少 - 登录号被踢",
    "notice.group_increase": "群聊成员增加",
    "notice.group_increase.approve": "群聊成员增加 - 管理员已同意入群",
    "notice.group_increase.invite": "群聊成员增加 - 管理员邀请入群",
    "notice.group_recall": "群聊消息撤回",
    "notice.group_upload": "群聊文件上传",
    "notice.group_msg_emoji_like": "群聊表情回应 - 仅收自己的，其他扩展接口拉取",
    "notice.essence": "群聊设精",
    "notice.essence.add": "群聊设精 - 增加",
    "notice.essence.delete": "群聊设精 - 取消",
    "notice.notify.poke": "戳一戳",
    "notice.notify.lucky_king": "群红包运气王",
    "notice.notify.honor": "群成员荣誉变更",
    "notice.notify.honor.talkative": "群成员荣誉变更 - 龙王",
    "notice.notify.honor.performer": "群成员荣誉变更 - 群聊之火",
    "notice.notify.honor.emotion": "群成员荣誉变更 - 快乐源泉",
    "notice.notify.input_status": "输入状态更新",
    "notice.notify.title": "群成员头衔变更",
    "notice.notify.profile_like": "点赞"
}


@notice_event.handle()
async def handle_notice_event(data: Event, bot: Bot):
    notice_event_name = data.get_event_name()
    log_message = event_log_mapping.get(notice_event_name, f"{notice_event_name}")
    write_log(log_message, data.get_event_description())


@request_event.handle()
async def handle_notice_event(data: Event, bot: Bot):
    request_event_name = data.get_event_name()
    log_message = event_log_mapping.get(request_event_name, f"{request_event_name}")
    write_log(log_message, data.get_event_description())

@meta_event.handle()
async def handle_meta_event(data: Event, bot: Bot):
    meta_event_name = data.get_event_name()
    log_message = event_log_mapping.get(meta_event_name, f"{meta_event_name}")
    write_log(log_message, data.get_event_description())

@message_event.handle()
async def handle_meta_event(data: Event, bot: Bot):
    msg_event_name = data.get_event_name()
    log_message = event_log_mapping.get(msg_event_name, f"{msg_event_name}")
    write_log(log_message, data.get_event_description())
