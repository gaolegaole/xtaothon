:github_url: https://github.com/Xtao-Labs/docs-all

处理消息
================

手动调用 :doc:`API 方法 <invoking>` 非常方便，但是如何让程序在新消息到达时做出反应呢？
此页面将告诉您 Telethon 如何处理更新以及如何在 Telethon 中处理此类事件。让我们来看看它们是如何工作的。

.. contents:: 目录
    :backlinks: none
    :depth: 1
    :local:

-----

定义处理程序
----------------

首先您需要在 :doc:`Handlers <../api/handlers>` 中找到需要处理的事件的处理程序。

每个处理程序处理特定事件。支持同一事件注册多个回调函数。

注册处理程序
---------------------

使用 add_handler()
^^^^^^^^^^^^^^^^^^^

使用 :meth:`~pyrogram.client.add_handler` 方法注册新的处理程序：

.. code-block:: python

    from telethon.sync import TelegramClient, events

    app = Client("my_account", api_id, api_hash)

    async def handler(context):
        print(context.text)

    app.add_event_handler(handler, events.NewMessage(**args))

    app.run_until_disconnected()
