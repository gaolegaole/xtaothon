class NewMessage:
    """``chats=None, incoming=None, outgoing=None, from_users=None, forwards=None, pattern=None``

    消息处理程序类。用于处理来自任何对话（私聊、群组、频道）的文本，媒体消息。
    它需要与 :meth:`~telethon.Client.add_handler` 一起使用。

    参数：
        incoming (``bool``，``可选``):
            如果设置为 ``True`` ，则只能处理接收到的消息。与 ``outgoing`` 相互排斥（只能设置一个 ``False``）。
        outgoing (``bool``，``可选``):
            如果设置为 ``True`` ，则只能处理此账户通过其他客户端发出的消息。与 ``incoming`` 相互排斥（只能设置一个 ``False``）。
        from_users (:obj:`User`，``可选``):
            不像 ``chats`` 参数，此项会筛选出来自此/这些用户的所有消息。如果您只想筛选出来自此/这些用户的私聊对话，请使用 ``chats`` 参数。
        forwards (``bool``，``可选``):
            是否处理转发消息。默认情况下，将处理转发和普通消息。如果设置为 ``True``，则只处理转发消息；如果设置为 ``False``，则只处理普通消息。
        pattern (``str``,``callable``,``Pattern``，``可选``):
            如果设置，只有匹配此模式的消息将被处理。您可以指定 Regex 字符串或者编译的正则表达式模式，如果与消息匹配则将被处理；
            如果是可调函数，返回值为 ``True`` 时消息将被处理。

    Example
        .. code-block:: python

            import asyncio
            from telethon import events
            @client.on(events.NewMessage(pattern='(?i)hello.+'))
            async def handler(event):
                # Respond whenever someone says "Hello" and something else
                await event.reply('Hey!')
            @client.on(events.NewMessage(outgoing=True, pattern='!ping'))
            async def handler(event):
                # Say "!pong" whenever you send "!ping", then delete both messages
                m = await event.respond('!pong')
                await asyncio.sleep(5)
                await client.delete_messages(event.chat_id, [event.id, m.id])
    """
