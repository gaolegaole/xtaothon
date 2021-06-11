:github_url: https://github.com/Xtao-Labs/docs-all

消息更新处理器
===============

Handlers 用于告诉 Telethon 处理哪种类型的消息更新。

.. code-block:: python
    :emphasize-lines: 8, 10

    from telethon.sync import TelegramClient, events

    app = Client("my_account", api_id, api_hash)

    async def handler(context):
        print(context.text)

    app.add_event_handler(handler, events.NewMessage(**args))

    app.run_until_disconnected()

.. contents:: 目录
    :backlinks: none
    :depth: 1
    :local:

-----

.. currentmodule:: telethon.events

索引
-----

.. hlist::
    :columns: 3

    - :class:`NewMessage`

-----

详细信息
----------

.. Handlers
.. autoclass:: NewMessage()
