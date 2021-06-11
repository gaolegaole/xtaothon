:github_url: https://github.com/Xtao-Labs/docs-all

调用方法
===============

此时，我们已成功 :doc:`安装 Telethon <../intro/install>` 并且 :doc:`授权 <auth>` 了我们的帐户。
是时候开始调用 API 与 Telegram 交互了！

.. contents:: 目录
    :backlinks: none
    :depth: 1
    :local:

-----

基础用法
-----------

使用 Telegram 进行 API 方法调用非常简单。下面是我们将逐步讲解的基本示例代码：

.. code-block:: python

    from telethon.sync import TelegramClient, events

    app = TelegramClient("my_account", api_id, api_hash)

    async def main():
        await client.send_message('me', 'Hello, myself!')

    with app:
        app.loop.run_until_complete(main())

逐步讲解
^^^^^^^^^^^^^^^^^^

#.  导入 Client 类：

    .. code-block:: python

        from telethon.sync import TelegramClient, events

#.  现在实例化一个新的 Client 对象：

    .. code-block:: python

        app = TelegramClient("my_account", api_id, api_hash)

#.  定义客户端要执行的 main 函数：

    .. code-block:: python

        async def main():
            # 给自己发送 “Hello, myself!”
            await client.send_message('me', 'Hello, myself!')

#.  ``with`` context manager 是启动，执行和停止客户端的快捷方式：

    .. code-block:: python

        with app:

#.  现在你可以调用 main 函数：

    .. code-block:: python

        app.loop.run_until_complete(main())

Context Manager
---------------

``with`` 语句启动一个 context manager ，用作自动调用 :meth:`~telethon.Client.start`
和 :meth:`~telethon.Client.disconnect`，这是 Telethon 正常工作所需的方法。context manager 也会优雅地停止客户端，
即使您的代码中出现了未处理的异常时也是如此。

异步调用
------------------

.. important::

    请注意，Telethon 是一个异步库，因此，您应该习惯它并学习一些基本的 asyncio 。这将对您编写应用程序有很大的帮助。

.. code-block:: python

    from telethon.sync import TelegramClient, events

    app = TelegramClient("my_account", api_id, api_hash)

    async def main():
        await client.send_message('me', 'Hello, myself!')

    with app:
        app.loop.run_until_complete(main())

