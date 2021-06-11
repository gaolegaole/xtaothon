# noinspection PyUnresolvedReferences
class Client:
    """Telethon Client，与 Telegram 互动的主要手段。

    参数:
        session (``str``):
            如果给出了字符串（它可以是完整路径）则将会保存 ``.session`` 文件；如果没有，则不会保存会话，并且在程序结束后，您应该调用
            `client.log_out()` 。

            请注意，如果传递字符串，则文件将保存为当前工作目录下，并且您还可以传递绝对路径。

        api_id (``int`` | ``str``):
            从 https://my.telegram.org 获取到的 *api_id* 。

        api_hash (``str``, *optional*):
            从 https://my.telegram.org 获取到的 *api_hash* 。

        bot_token （``str``, *可选*):
            如果设置了 Bot token，则将直接使用 Bot 身份登录。

        app_version (``str``, *可选*):
            应用版本号，默认设置为 `telethon.version.__version__` 。

        device_model (``str``, *optional*):
            设备型号，默认设置为 `·`platform.uname().machine` 。

        system_version (``str``, *optional*):
            操作系统版本，默认设置为 `platform.uname().release` 。

        lang_code (``str``, *optional*):
            客户端上使用的 ISO 639-1 标准的语言代码。默认为 “en”。

        use_ipv6 (``bool``, *可选*):
            如果设置为 `True` ，则将使用 ipv6 连接 Telegram 服务器。默认关闭 (通过 IPv4).

        proxy (``tuple``, ``str``, ``dict``, *可选*):
            MTProxy: `('hostname', port, 'secret')` ；socks5: `(socks.SOCKS5, "socks.example.com", 1080)` 获取更多
            代理配置详情：https://github.com/Anorov/PySocks#usage-1

        timeout (``int``, ``float``, *可选*):
            设置链接超时所要等待的秒数。

        flood_sleep_threshold (``int``, ``float``, *可选*):
            设置当出现 `FloodWaitError` 时自动休眠应用程序的时间。
    """

    def start(self):
        """启动客户端（在必要时连接和登录）。

        此方法将使客户端连接到 Telegram 服务器，如果是一个新的客户端，会自动进行交互式的授权过程。

        返回:
            :obj:`~telethon.Client`: 启动的 client本身。

        Raises:
            ConnectionError: 如果您尝试启动已启动客户端。

        Example:
            .. code-block:: python
                :emphasize-lines: 4

                from telethon.sync import TelegramClient, events

                app = Client("my_account", api_id, api_hash)
                app.start()

                # Call API methods

                app.disconnect()

        """

    def disconnect(self):
        """断开客户端与 Telegram 服务器的连接。

        此方法将客户端与 Telegram 服务器断开连接，并停止底层任务。

        返回:
            :obj:`~telethon.Client`: 停止的 client本身。

        Raises:
            OSError: 如果您尝试停止已停止的客户端。

        Example:
            .. code-block:: python
                :emphasize-lines: 8

                from telethon.sync import TelegramClient, events

                app = Client("my_account", api_id, api_hash)
                app.start()

                # Call API methods

                app.disconnect()

        """

    # Message
    def send_message(self):
        """向指定的用户，群组或频道发送消息。

        默认文本解析模式与官方应用程序相同（Markdown）

        向 bot 发送 start 参数命令 (例如 ``?start=data``) 同样可行，请直接发送 ``/start data`` 。

        参数:
            entity (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                接收消息的对象

            message (``str`` | :obj:`~telethon.tl.types.message`):
                要发送的消息或消息对象。

                消息的最大长度为 ``35,000`` 字节或 ``4,096`` 个字符。较长的消息不会自动分割，如果要发送的文本长于最大长度，则应手动分割。

            reply_to (``int`` | :obj:`~telethon.tl.types.message`, *可选*):
                要回复的消息 id 或者消息对象。

            parse_mode (``str``, *可选*):
                文本格式解析器配置。值支持 `markdown` （`md`)， `html` （`htm`)， `None`。

            link_preview (``bool``, *可选*):
                配置是否展示消息预览，默认开启。

            buttons (``list``), *可选*):
                配置消息按钮，参见示例，仅支持 bot 登录时。

                限制：
                    最多可以有 ``100`` 个按钮（更多将被忽略）。
                    每行最多可以有 ``8`` 个按钮（更多将被忽略）。
                    按钮的最大回调数据为 ``64`` 字节。

            silent (``bool``, *可选*):
                配置是否静默消息，默认关闭。

            schedule (``float``, *可选*):
                配置是否定时消息，默认不配置。

        返回:
            :obj:`~telethon.tl.types.message`: 成功则将返回已发送的消息。

        Example:
            .. code-block:: python

                # 默认使用 Markdown 解析器解析文本。
                await client.send_message('me', 'Hello **world**!')

                # 更改客户端的默认解析器。
                client.parse_mode = 'html'

                await client.send_message('me', 'Some <b>bold</b> and <i>italic</i> text')
                await client.send_message('me', 'An <a href="https://example.com">URL</a>')
                await client.send_message('me', '<a href="tg://user?id=me">Mentions</a>')

                # 混合解析
                client.parse_mode = None

                # 手动配置单条消息的解析器为 Markdown 。
                await client.send_message('me', 'Hello, **world**!', parse_mode='md')

                # 手动配置单条消息的解析器为 Html 。
                await client.send_message('me', 'Hello, <i>world</i>!', parse_mode='html')

                # 如果使用 Bot 登录，则您可以使用按钮：
                from telethon import events, Button

                @client.on(events.CallbackQuery)
                async def callback(event):
                    await event.edit('感谢点击 {}!'.format(event.data))

                # 单个按钮
                await client.send_message(chat, '只是一个会回调 "clk1" 的按钮。',
                                          buttons=Button.inline('点我', b'clk1'))

                # 多个按钮
                await client.send_message(chat, '选一个吧！', buttons=[
                    [Button.inline('回调'), Button.inline('这是回调')],
                    [Button.url('访问网站', 'https://example.com')]
                ])

                # 消息需要回复
                await client.send_message(chat, '欢迎', buttons=[
                    Button.text('感谢!', resize=True, single_use=True),
                    Button.request_phone('发送电话号码'),
                    Button.request_location('发送位置')
                ])

                # 强制回复或清除按钮。
                await client.send_message(chat, '回复我', buttons=Button.force_reply())
                await client.send_message(chat, '清楚按钮', buttons=Button.clear())

                # 定时 5 分钟后发送消息
                from datetime import timedelta
                await client.send_message(chat, '你好，未来！', schedule=timedelta(minutes=5))
        """

    def edit_message(self):
        """编辑指定消息，更改其文本或媒体文件。

        参数:
            entity (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                接收消息的对象

            text (``str``, *可选*):
                要编辑的消息文本。

                消息的最大长度为 ``35,000`` 字节或 ``4,096`` 个字符。

            message (``int`` | ``str`` | :obj:`~telethon.tl.types.message`, *可选*):
                要编辑的消息 id 或者消息对象。

            parse_mode (``str``, *可选*):
                文本格式解析器配置。值支持 `markdown` （`md`)， `html` （`htm`)， `None`。

            link_preview (``bool``, *可选*):
                配置是否展示消息预览，默认开启。

            file (``str``, ``bytes``, *可选*):
                如果参数为 ``str`` ，则将再此路径下寻找文件（支持相对/绝对路径）。

                请注意：如果原消息为纯文本时，配置此项将会报错。

            buttons (``list``), *可选*):
                配置消息按钮，参见示例，仅支持 bot 登录时。

                限制：
                    最多可以有 ``100`` 个按钮（更多将被忽略）。
                    每行最多可以有 ``8`` 个按钮（更多将被忽略）。
                    按钮的最大回调数据为 ``64`` 字节。

            schedule (``float``, *可选*):
                配置是否定时消息，默认不配置。

        Raises:
            MessageAuthorRequiredError: 如果您不是消息的发送者。

            MessageNotModifiedError: 如果要编辑的消息和原消息一样。

            MessageIdInvalidError: 如果消息的 ID 无效（消息 ID 本身可能是正确的，但无法编辑此 ID 对应的消息。）

        Example:
            .. code-block:: python

                message = await client.send_message(chat, '你好')

                await client.edit_message(chat, message, '你好!')
                # 或者
                await client.edit_message(chat, message.id, '你好!!')
                # 或者
                await client.edit_message(message, '你好!!!')
        """

    def delete_messages(self):
        """删除指定消息。

        参数:
            entity (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                接收消息的对象

            message_ids  (``list`` | ``int`` | :obj:`~telethon.tl.types.message`, *可选*):
                要删除的消息 id 列表或者单个消息 id 或者消息对象。

        Example:
            .. code-block:: python

                await client.delete_messages(chat, messages)
        """

    def forward_messages(self):
        """转发指定消息。

        参数:
            entity (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                接收消息的对象

            message_ids (``list`` | ``int`` | :obj:`~telethon.tl.types.message`, *可选*):
                要删除的消息 id 列表或者单个消息 id 或者消息对象。

            from_peer (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                指定转发消息的来源。如果 message_ids 传递的参数是数字。

            silent (``bool``, *可选*):
                配置是否静默消息，默认关闭。

            schedule (``float``, *可选*):
                配置是否定时消息，默认不配置。

        返回:
            :obj:`~telethon.tl.types.message`: 成功则将返回已转发的消息。（如果转发的是一组消息，则返回列表）

            请注意：批量转发时，如果所有需要转发的消息都无效（即删除）则会抛出 ``MessageIdInvalidError`` 错误；
            如果只有一些消息无效，则只是返回的列表中没有这些消息。

        Raises:
            MessageIdInvalidError: 如果消息的 ID 无效

        Example:
            .. code-block:: python

                # 单条消息
                await client.forward_messages(chat, message)
                # 或者
                await client.forward_messages(chat, message_id, from_chat)
                # 或者
                await message.forward_to(chat)

                # 多条消息
                await client.forward_messages(chat, messages)

                # 作为一个副本发送（不带转发来源）
                await client.send_message(chat, message)
        """

    def iter_messages(self):
        """搜索指定对话中的消息。

        参数:
            entity (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                需要检索的对话的对象

            limit (``int`` | ``None``, *可选*):
                限制要检索的消息数。由于API的限制，检索超过 ``3000`` 条消息将需要超过半分钟。

                配置为 ``None`` ，并不会返回所有历史。

            offset_date (``float``, *可选*):
                将从此时间之前开始检索消息。

            offset_id (``int``, *可选*):
                将从此消息 id 之前开始检索消息。

            max_id (``int``, *可选*):
                配置要检索到的消息的最大 id 值。

            min_id (``int``, *可选*):
                配置要检索到的消息的最小 id 值。

            search (``str``, *可选*):
                配置检索的字符串。

            filter (``MessagesFilter``, *可选*):
                过滤消息类型。

            from_user (:obj:`~telethon.tl.types.user`, *可选*)
                指定消息发送者。

            reverse (``bool``, *可选*):
                如果设置为 ``True``，则消息将以相反的顺序返回。这意味着 ``offset_id`` 或者 ``offset_date`` 参数的含义是相反的。
                ``min_id`` 等同于 ``offset_id`` 。

            reply_to (``int``, *可选*):
                返回频道消息的所有评论消息。

                此功能只能用于链接了某个频道的*讨论组*。在其他对话中使用它将抛出 ``PeridInValiderror`` 错误。

                使用此参数时，``filter`` 和 ``search`` 参数无效，因为 Telegram 的 API 不支持搜索回复中的消息。

        Yields:

            消息对象 :obj:`~telethon.tl.types.message`

        Raises:

            PeridInValiderror: 此对话不是链接了频道的讨论组。

        Example:
            .. code-block:: python

                # 从最新消息开始检索
                async for message in client.iter_messages(chat):
                    print(message.id, message.text)

                # 从第一条消息开始检索
                async for message in client.iter_messages(chat, reverse=True):
                    print(message.id, message.text)

                # 只返回我发送的消息
                async for message in client.iter_messages(chat, from_user='me'):
                    print(message.text)

                # 通过 Telegram 服务器检索匹配的文本消息
                async for message in client.iter_messages(chat, search='hello'):
                    print(message.id)

                # 检索特定类型的消息（例如：图片）
                from telethon.tl.types import InputMessagesFilterPhotos
                async for message in client.iter_messages(chat, filter=InputMessagesFilterPhotos):
                    print(message.photo)

                # 检索指定频道消息的评论
                async for message in client.iter_messages(channel, reply_to=123):
                    print(message.chat.title, message.text)
        """

    def get_messages(self):
        """
        和 .. automethod:: telethon.Client.iter_messages() 一样，但是返回的是一个 ``List`` 。

        Example:
            .. code-block:: python

                # 获取对话所有照片数
                from telethon.tl.types import InputMessagesFilterPhotos
                photos = await client.get_messages(chat, None, filter=InputMessagesFilterPhotos)
                print(photos.total)

                # 通过消息 id 获取消息
                message_1337 = await client.get_messages(chat, ids=1337)
        """

    def pin_message(self):
        """置顶指定消息

        参数:
            entity (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                需要置顶的对话的对象。

            message (``int`` | ``None`` | :obj:`~telethon.tl.types.message`, *可选*):
                要置顶的消息 id 或者消息对象。如果值为 ``None``，则将取消置顶所有消息。

            notify (``bool``, *可选*):
                配置是否通知群成员。与官方应用程序不同，默认不通知所有成员。

        Example:
            .. code-block:: python

                # 置顶消息
                message = await client.send_message(chat, 'Pinotifying is fun!')
                await client.pin_message(chat, message, notify=True)
        """

    def unpin_message(self):
        """取消置顶指定消息

        参数:
            entity (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                需要取消置顶的对话的对象。

            message (``int`` | ``None`` | :obj:`~telethon.tl.types.message`, *可选*):
                要置顶的消息 id 或者消息对象。如果值为 ``None``，则将取消置顶所有消息。

        Example:
            .. code-block:: python

                # 取消置顶所有消息
                await client.unpin_message(chat)
        """

    def send_read_acknowledge(self):
        """将消息标记为已读，可选择是否清除提及提示。

        如果不提供消息和 ``max_id`` ，则将标记所有消息为已读。

        参数:
            entity (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                需要标记已读的对话的对象。

            message (``list`` | :obj:`~telethon.tl.types.message`, *可选*):
                标记此消息及其之前的所有消息为已读。

            max_id (``int``, *可选*):
                标记此消息 id 及其之前的所有消息为已读。

            clear_mentions (``bool``, *可选*):
                配置是否清除提及按钮。

        Example:
            .. code-block:: python

                # 使用消息对象
                await client.send_read_acknowledge(chat, message)
                # 或者使用消息 id
                await client.send_read_acknowledge(chat, message_id)
                # 或者已读所有消息
                await client.send_read_acknowledge(chat, messages)
        """

    # Upload
    def send_file(self):
        """向指定对话发送文件。

        .. note::

            安装 ``hachoir3`` 包（``hachoir`` 模块），它可以被用于获取音频和视频元信息。

            安装 ``pillow`` 包，它可以自动调整图片尺寸以支持 Telegram 上传，但是，如果使用 ``InputFile`` 发送图片，则无法完成。

        参数:
            entity (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                需要发送文件的对话的对象。

            file (``str`` | ``bytes`` | ``file`` | ``media``):
                支持路径、包含文件的 ``bytes``、网络链接、``file_id``、文件句柄（例如 ``message.media``）。

            caption (``str``, *可选*):
                配置媒体文件的说明文字。

            force_document (``bool``, *可选*):
                强制以文件方式发送图片等。

            reply_to (``int`` | :obj:`~telethon.tl.types.message`, *可选*):
                要回复的消息 id 或者消息对象。

            parse_mode (``str``, *可选*):
                文本格式解析器配置。值支持 `markdown` （`md`)， `html` （`htm`)， `None`。

            buttons (``list``), *可选*):
                配置消息按钮，参见示例，仅支持 bot 登录时。

                限制：
                    最多可以有 ``100`` 个按钮（更多将被忽略）。
                    每行最多可以有 ``8`` 个按钮（更多将被忽略）。
                    按钮的最大回调数据为 ``64`` 字节。

            silent (``bool``, *可选*):
                配置是否静默消息，默认关闭。

            schedule (``float``, *可选*):
                配置是否定时消息，默认不配置。

        返回:
            :obj:`~telethon.tl.types.message`: 如果成功则返回消息对象。

        Example:
            .. code-block:: python

                # 图片文件
                await client.send_file(chat, '/my/photos/me.jpg', caption="It's me!")
                # 或者
                await client.send_message(chat, "It's me!", file='/my/photos/me.jpg')

                # 语音文件
                await client.send_file(chat, '/my/songs/song.mp3', voice_note=True)
                await client.send_file(chat, '/my/videos/video.mp4', video_note=True)

                # 自定义缩略图
                await client.send_file(chat, '/my/documents/doc.txt', thumb='photo.jpg')

                # 文件
                await client.send_file(chat, '/my/photos/photo.png', force_document=True)

                # 图辑
                await client.send_file(chat, [
                    '/my/photos/holiday1.jpg',
                    '/my/photos/holiday2.jpg',
                    '/my/drawings/portrait.png'
                ])

                # 提示上传进度
                def callback(current, total):
                    print('Uploaded', current, 'out of', total,
                          'bytes: {:.2%}'.format(current / total))

                await client.send_file(chat, file, progress_callback=callback)

                # 骰子，包括飞镖和其他动态表情符号
                from telethon.tl import types
                await client.send_file(chat, types.InputMediaDice(''))
                await client.send_file(chat, types.InputMediaDice('🎯'))

                # 联系人
                await client.send_file(chat, types.InputMediaContact(
                    phone_number='+34 123 456 789',
                    first_name='Example',
                    last_name='',
                    vcard=''
                ))
        """

    # Download
    def download_media(self):
        """下载消息对象包含的媒体文件。

        .. note::

            如果下载太慢，则应考虑安装 ``cryptg`` （``pip3 install cryptg``）

        参数:
            entity (:obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`):
                需要发送文件的对话的对象。

            file (``str`` | ``file``):
                输出文件路径，目录或流等对象。如果该路径存在并且是文件，则将覆盖。

        返回:
            None: 如果消息中不存在媒体文件，如果为指定路径则将返回文件路径。

        Example:
            .. code-block:: python

                path = await client.download_media(message)
                await client.download_media(message, filename)
                # 或者
                path = await message.download_media()
                await message.download_media(filename)

                # 提示下载进度
                def callback(current, total):
                    print('Downloaded', current, 'out of', total,
                          'bytes: {:.2%}'.format(current / total))

                await client.download_media(message, progress_callback=callback)
        """

    # Users
    def get_me(self):
        """获取当前客户端所登录的用户信息。

        返回:
            :obj:`~telethon.tl.types.user`: 如果成功则返回用户对象。

        Example:
            .. code-block:: python

                me = await client.get_me()
        """

    def get_entity(self):
        """获取指定对话信息。

        .. note::

            使用此方法解析用户名不会自带缓存，对时间内您一般解析 ``50`` 个用户名就会收到请求过快错误。
            推荐优先使用 .. automethod:: telethon.Client.get_input_entity() 来请求缓存的用户名数据。

        参数:
            entity (``str`` | ``int``):
                需要获取的对话的对象。

        Raise:
            ValueError: 指定的对话不存在。

        Return:
            :obj:`~telethon.tl.types.user` | :obj:`~telethon.tl.types.chat` | :obj:`~telethon.tl.types.channel`: 如果请求成功。

        Example:
            .. code-block:: python

                from telethon import utils

                me = await client.get_entity('me')
                print(utils.get_display_name(me))

                chat = await client.get_input_entity('username')
                async for message in client.iter_messages(chat):
                    ...

                # 可以直接使用用户名
                async for message in client.iter_messages('username'):
                    ...

                # 请注意，您的联系人中必须拥有此电话号码才可以请求到数据。
                some_id = await client.get_peer_id('+34123456789')
        """

    def get_input_entity(self):
        """获取指定对话的对象。

        参数:
            entity (``str`` | ``int``):
                需要获取的对话的对象。

        Raise:
            ValueError: 指定的对话不存在。

        Example:
            .. code-block:: python

                user = await client.get_input_entity('username')
                chat = await client.get_input_entity(-123456789)
        """
