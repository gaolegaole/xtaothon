:github_url: https://github.com/Xtao-Labs/docs-all

FAQ
============

.. role:: strike
    :class: strike

此常见问题解答页面提供了有关 Telethon 的常见问题的答案。

.. contents:: 目录
    :backlinks: none
    :depth: 1
    :local:

-----

为什么什么都不提示？
----------------------------

那么它可能有错误，但你还没有启用日志记录。 要启用日志记录，请在主文件顶部添加以下代码：

.. code-block:: python

    import logging
    logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                        level=logging.WARNING)

您可以将日志记录级别更改为不同的内容，从较少信息到更多信息：

.. code-block:: python

    level=logging.CRITICAL  # 不会显示错误（与禁用相同）
    level=logging.ERROR     # 只会显示你没有处理的错误
    level=logging.WARNING   # 还将显示中等严重性的消息，例如内部 Telegram 问题
    level=logging.INFO      # 还将显示信息性消息，例如连接或断开连接
    level=logging.DEBUG     # 将显示大量输出以帮助调试库中的问题

我怎样才能过滤 FloodWaitError ？
-----------------------------------------

您可以通过导入 API 中的自定义错误来过滤：

.. code-block:: python

    from telethon import errors
    try:
        await client.send_message(chat, 'Hi')
    except errors.FloodWaitError as e:
        # e.seconds 是您被限制了多少秒才能重新调用此 API 。
        print('Flood for', e.seconds)

使用 Telethon 时我的帐户被删除/限制
------------------------------------------

如果您出于恶意使用 Telethon ，Telegram 可能会禁止您。

但是，您也可能是某个限制国家/地区的一部分，例如伊朗或俄罗斯。在这种情况下，我们有一个坏消息要告诉你。
Telegram 更有可能禁止这些号码，因为它们经常被用来向其他帐户发送垃圾消息，并且可能是通过使用这样的库。
我们可以给您的最佳建议是不要滥用 API，例如非常快速地调用许多请求，并且建议您通过官方应用程序注册账户。

我们也收到了来自哈萨克斯坦和中国的报告，在那里会无法连接 Telegram 服务器。要解决这些连接问题，您应该:doc:`使用代理 <topics/proxy>`。

Telegram 还可能禁止虚拟 (VoIP) 电话号码，因为它们很可能被用于发送垃圾消息。

如果您想检查您的帐户是否受到限制，只需向 Telegram 官方 Bot ``@SpamBot`` 发送消息即可。
您应该通过收到 ``PeerFloodError`` 之类的错误来注意到这一点，这意味着您受到限制。

sqlite3.OperationalError: database is locked
---------------------------------------------------------

较旧的进程仍在运行并使用相同的 “session” 文件。

当两个或多个客户端使用同一个会话时，会出现此错误：

您有一个使用相同会话文件的旧进程。
您有两个不同的脚本正在运行（交互式会话也算在内）。
您在同一脚本中有两个客户端同时运行。

解决方案是，如果您需要两个客户端，请使用两个会话。如果问题仍然存在并且您使用的是 Linux，则可以使用 ``fuser my.session`` 找出锁定文件的进程。
作为最后的手段，您可以重新启动系统。

event.chat or event.sender is None
-----------------------------------------

Telegram 为节省带宽并不总是发送此信息。如果您需要这些信息，您应该自己获取，因为除非您需要，否则库不会做不必要的工作：

.. code-block:: python

    async def handler(event):
        chat = await event.get_chat()
        sender = await event.get_sender()


我想将我的帐户从 DCX 迁移到 DCY 。
---------------------------------------------

首次注册帐户时，由 Telegram 根据电话号码来源决定将在哪个 DC 中创建新用户。

尽管 `Telegram 文档 <https://core.telegram.org/api/datacenter#user-migration>`_ 说明：服务器可能会自动迁移用户，
尽管 Telegram 本身也 `确认 <https://twitter.com/telegram/status/427131446655197184>`_ 存在此机制，但目前无法在任何情况下手动迁移您的帐户。
仅仅是因为该功能曾经计划但尚未实施。

感谢 `@gabriel <https://t.me/AnotherGroup/217699>`_ 确认该功能尚未实现。

为什么我的客户端在超级群组中反应缓慢？
---------------------------------------

此问题仅影响某些超级群组或超级群组中的某些成员。

由于 Telegram 内部的工作方式，您从其他成员接收和发送给其他成员的每条消息都必须通过群组创建者的 DC，在最坏的情况下，你、创建者和其他成员属于三个不同的
DC，其他成员的消息必须从他的 DC 传递到创建者的 DC，最后到达您的 DC。这个过程将不可避免地需要时间。

另一个导致响应缓慢的原因是消息是 **按优先级调度** 的。 根据成员身份，一些用户比其他用户更快地接收消息，对于大而繁忙的超级群组，延迟可能会变得
令人注意，特别是如果您属于优先级列表的低端：

1. 创建者。
2. 管理员。
3. Bots。
4. 提及到的用户。
5. 近期在线用户。
6. 其他成员。

感谢 `@Manuel15 <https://t.me/PyrogramChat/76990>`_ 提供优先级列表
