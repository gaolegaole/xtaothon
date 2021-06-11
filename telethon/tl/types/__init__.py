# noinspection PyUnresolvedReferences
class message:
    """一条消息。

    参数:
        id (``int``):
            对话中消息的唯一消息标识符。

        from_id (``PeerUser`` | ``PeerChat`` | ``PeerChannel``, *可选*):
            发送人。

        peer_id (``PeerUser`` | ``PeerChat`` | ``PeerChannel``, *可选*):
            对话信息。

        text (``str``)
            文本

        raw_text (``str``)
            纯文本

        is_reply (``bool``)
            如果此消息是回复消息则值为 ``True``

        date (``int``)
            消息发送时间
    """

    def reply(self):
        """快速回复消息。

        参见方法 :meth:`~telethon.Client.send_message`

        参数 ``entity`` 和 ``reply_to`` 已经自动配置。"""

    def forward_to(self):
        """快速转发消息。

        参见方法 :meth:`~telethon.Client.forward_messages`

        参数 ``messages`` 和 ``from_peer`` 已经自动配置。"""

    def edit(self):
        """快速编辑消息。

        参见方法 :meth:`~telethon.Client.edit_message`

        参数 ``entity`` 和 ``message`` 已经自动配置。"""

    def delete(self):
        """快速删除消息。

        参见方法 :meth:`~telethon.Client.delete_messages`

        参数 ``entity`` 和 ``message_ids`` 已经自动配置。"""

    def mark_read(self):
        """快速已读消息。

        参见方法 :meth:`~telethon.Client.send_read_acknowledge`

        参数 ``entity`` 和 ``message`` 已经自动配置。"""

    def pin(self):
        """快速置顶消息。

        参见方法 :meth:`~telethon.Client.pin_message`

        参数 ``entity`` 和 ``message`` 已经自动配置。"""

    def unpin(self):
        """快速取消置顶消息。

        参见方法 :meth:`~telethon.Client.unpin_message`

        参数 ``entity`` 和 ``message`` 已经自动配置。"""


class user:
    """A Telegram user or bot.

    参数:
        id (``int``):
            唯一标识符。
        is_self (``bool``):
            如果是当前客户端登录用户，则返回 ``True`` 。
        bot (``bool``):
            如果是机器人，则返回 ``True`` 。
        verified (``bool``):
            如果是官方认证，则返回 ``True`` 。
        restricted (``bool``):
            如果是收到限制，则返回 ``True`` 。
        fake (``bool``):
            如果是被标记为冒充，则返回 ``True`` 。
        first_name (``str``):
            first name
        last_name (``str``, *可选*):
            如果未配置，则返回 ``None`` 。
        username (``str``, *可选*):
            如果未配置，则返回 ``None`` 。
        phone (``str``, *可选*):
            如果无法读取，则返回 ``None`` 。
        lang_code (``str``, *可选*):
            如果无法读取，则返回 ``None`` 。
    """


class chat:
    """A chat.

    参数:
        id (``int``):
            唯一标识符。
        title (``str``):
            标题
        username (``str``, *可选*):
            如果未配置，则返回 ``None`` 。
        participants_count (``int``):
            群成员数
        date (``int``):
            可能是创建日期？
        slowmode_enabled (``bool``):
            是否开启慢速模式，如果无法获取则返回 ``None`` 。
        creator (``bool``):
            如果当前客户端登录用户是创建者，则返回 ``True`` 。
        kicked (``bool``):
            如果当前客户端登录用户被踢出，则返回 ``True`` 。
        left (``bool``):
            如果当前客户端登录用户已退出，则返回 ``True`` 。
        call_active (``bool``):
            如果群语音已激活，则返回 ``True`` 。
        call_not_empty (``bool``):
            如果群语音有成员，则返回 ``True`` 。
    """


class channel:
    """A channel.

    参数:
        id (``int``):
            唯一标识符。
        title (``str``):
            标题
        username (``str``, *可选*):
            如果未配置，则返回 ``None`` 。
        participants_count (``int``):
            成员数，如果无法获取则返回 ``None`` 。
        date (``int``):
            可能是创建日期？
        creator (``bool``):
            如果当前客户端登录用户是创建者，则返回 ``True`` 。
        left (``bool``):
            如果当前客户端登录用户已退出，则返回 ``True`` 。
        verified (``bool``):
            如果是官方认证，则返回 ``True`` 。
        restricted (``bool``):
            如果是收到限制，则返回 ``True`` 。
        fake (``bool``):
            如果是被标记为冒充，则返回 ``True`` 。
        has_link (``bool``):
            如果链接到了一个讨论群，则返回 ``True``。
        has_geo （``bool``):
            如果拥有地理位置信息，则返回 ``True`` 。
        call_active (``bool``):
            如果语音已激活，则返回 ``True`` 。
        call_not_empty (``bool``):
            如果语音有成员，则返回 ``True`` 。
    """