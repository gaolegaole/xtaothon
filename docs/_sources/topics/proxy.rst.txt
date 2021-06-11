:github_url: https://github.com/Xtao-Labs/docs-all

SOCKS5 Proxy
============

Telethon 支持带有或者不带有验证的代理。

.. contents:: 目录
    :backlinks: none
    :depth: 1
    :local:

-----

使用
-----

-  您可以使用 Client 类中的 *proxy* 参数来设置代理:

   .. code-block:: python

       from telethon.sync import TelegramClient
       import socks

       app = Client(
           session_name="example",
           proxy=(
               socks.SOCKS5,
               "socks.example.com",
               1080,
               username="<your_username>",
               password="<your_password>"
           )
       )

       app.start()

       ...

.. note:: 如果您的代理不需要授权，您可以将 ``username`` 和 ``password`` 的值留空或者直接在参数中删除这两项。