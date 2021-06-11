:github_url: https://github.com/Xtao-Labs/docs-all

授权
=============

本节教程将会教会您如何使用 Telethon 登录 Bot 或者 User 。

.. contents:: 目录
    :backlinks: none
    :depth: 1
    :local:

-----

API key
------------------

在 :doc:`快速开始 <../intro/quickstart>` 中需要您申请属于您自己的 Telegram API key 。

#. 访问 https://my.telegram.org/apps 并且使用您的 Telegram 账户登录。
#. 填写表格以注册新的 Telegram 应用程序。
#. 完成! API key 由这两个值组成： **api_id** 和 **api_hash**.


.. note::

    API key 对每个用户是唯一的，并且仅一个值就可以授权多个 User （和 bot） 通过 MTProto API 访问 Telegram 数据库。

登录
------------------

为了使用这个 API, Telegram 要求用户通过电话号码授权。
Telethon 将会自动处理此过程，您需要做的只是创建一个实例 :class:`~telethon.Client` 类并且定义一个 ``session_name``  (e.g.: "my_account")
并且调用 :meth:`~telethon.Client.start` 方法:

.. code-block:: python

    from telethon import TelegramClient

    client = TelegramClient('my_account', api_id, api_hash)

    # 使用 Bot token 登录
    await client.start(bot_token='bot_token')

    # 使用 User 账户登录
    await client.start()
    # Enter phone number: +86**********
    # Please enter the code you received: 12345
    # Please enter your password: *******
    # (You are now logged in)

    # 使用一个 context manager 来登录 (这相当于直接调用 start()):
    with client:
        pass

这会创建一个交互 Shell 要求您输入 **电话号码** (包括您的 `国家代码`_) 和 **验证码**:

成功登录后，将创建一个名为 ``my_account.session`` 的新文件，允许 Telethon 使用您的登录的账户信息执行 API。
重新启动应用程序时，将自动加载此文件，只要您的账户登录文件还是可用的，Telethon 将不会要求您重新登录。

.. important::

    您的 ``*.session`` 文件是私密的并且必须保证安全。

.. _国家代码: https://en.wikipedia.org/wiki/List_of_country_calling_codes