:github_url: https://github.com/Xtao-Labs/docs-all

欢迎来到 Xtaothon
===================

.. raw:: html

    <div align="center">
        <a href="/">
            <div><img src="_static/xtaothon.png" alt="Xtaothon Logo" width="420"></div>
        </a>
    </div>

    <p align="center">
        <b>Telegram MTProto API Framework for Python</b>

        <br>
        <a href="https://github.com/LonamiWebs/Telethon">
            Source Code
        </a>
        •
        <a href="https://github.com/LonamiWebs/Telethon/releases">
            Releases
        </a>
        •
        <a href="https://t.me/Telethon_CN_Chat">
            Community
        </a>
    </p>

.. code-block:: python

    from telethon.sync import TelegramClient, events

    with TelegramClient('name', api_id, api_hash) as client:
       client.send_message('me', 'Hello, myself!')
       print(client.download_profile_photo('me'))

       @client.on(events.NewMessage(pattern='(?i).*Hello'))
       async def handler(event):
          await event.reply('Hey!')

       client.run_until_disconnected()

Telegram 是一款十分受欢迎的简洁的即时通讯软件。**Telethon** 旨在使您能够轻松使用 `Python` 编写可以与 Telegram_ 进行交互的 Python 程序。

.. _Telegram: https://telegram.org

快速使用这篇文档
----------------------------------

内容总共被分成几大独立主题，这些主题可以从侧边栏或通过页面下方的 :guilabel:`下一项` 按钮来访问。
下方我们提供了几个常用的主题以供快速访问。

.. admonition :: 云服务器优惠
    :class: tip

    如果您需要服务器来托管您的程序我们推荐使用 **NSD Cloud**. 通过
    `链接 <https://nsdcloud.net/aff.php?aff=2>`_ 注册就可以帮助 Xtaothon 。

出发
^^^^^^^^^^^

.. hlist::
    :columns: 2

    - :doc:`快速开始 <intro/quickstart>`: 快速使用 Telethon 创建一个应用程序。
    - :doc:`调用方法 <start/invoking>`: 快速调用 Telethon 的内置方法来与 Telegram 交互。
    - :doc:`处理消息 <start/updates>`: 快速处理来自 Telegram 的新消息。

API
^^^^^^^^^^^^^

.. hlist::
    :columns: 2

    - :doc:`Telethon Client <api/client>`: Client 类的详细可配置参数。
    - :doc:`内置方法 <api/methods/index>`: 可用的高级方法列表。
    - :doc:`内置类型 <api/types/index>`: 可用的高级类型列表。
    - :doc:`绑定方法 <api/bound-methods/index>`: 方便的绑定方法列表。

更多
^^^^

.. hlist::
    :columns: 2

    - :doc:`Telethon FAQ <faq>`: Telethon 常见问题。
    - :doc:`常见短语 <glossary>`: 一些常见短语的释意。
    - :doc:`支持 Xtaothon <support>`: 支持 Xtaothon 的方式。

最后更新于 |today|

.. toctree::
    :hidden:
    :caption: 简介

    intro/quickstart
    intro/install

.. toctree::
    :hidden:
    :caption: 开始

    start/auth
    start/invoking
    start/updates

.. toctree::
    :hidden:
    :caption: API

    api/client
    api/methods/index
    api/types/index
    api/bound-methods/index
    api/handlers

.. toctree::
    :hidden:
    :caption: 主题指南

    topics/proxy
    topics/text-formatting

.. toctree::
    :hidden:
    :caption: 更多

    faq
    glossary
    support