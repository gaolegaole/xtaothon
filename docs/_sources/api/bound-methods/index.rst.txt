:github_url: https://github.com/Xtao-Labs/docs-all

绑定方法
=============

某些 Telethon 类型定义了所谓的绑定方法。绑定方法是指附加到该类实例的类的函数。

.. code-block:: python
    :emphasize-lines: 6

    from telethon.sync import TelegramClient, events

    app = Client("my_account", api_id, api_hash)

    async def handler(context):
        await context.reply('绑定方法。')

    app.add_event_handler(handler, events.NewMessage(**args))

    app.run_until_disconnected()

.. contents:: 目录
    :backlinks: none
    :local:

-----

.. currentmodule:: telethon.tl.types

消息
-------

.. hlist::
    :columns: 3

    - :meth:`~message.reply`
    - :meth:`~message.forward_to`
    - :meth:`~message.edit`
    - :meth:`~message.delete`
    - :meth:`~message.mark_read`
    - :meth:`~message.pin`
    - :meth:`~message.unpin`

.. toctree::
    :hidden:

    message.reply <message.reply>
    message.forward_to <message.forward_to>
    message.edit <message.edit>
    message.delete <message.delete>
    message.mark_read <message.mark_read>
    message.pin <message.pin>
    message.unpin <message.unpin>
