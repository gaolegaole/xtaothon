:github_url: https://github.com/Xtao-Labs/docs-all

客户端
========

您已进入API参考部分，您可以在其中找到有关 Telethon 的 API 的详细信息。

此页面是关于 Client 类的，它公开了一些高级方法，以便更加轻松访问 API 。

.. code-block:: python
    :emphasize-lines: 1-3

    from telethon.sync import TelegramClient, events

    app = Client("my_account", api_id, api_hash)

    async def handler(context):
        print(context.text)

    app.add_event_handler(handler, events.NewMessage(**args))

    app.run_until_disconnected()

-----

详细信息
-------------

.. autoclass:: telethon.Client()
