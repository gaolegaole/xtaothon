:github_url: https://github.com/Xtao-Labs/docs-all

快速开始
===========

通过下面的步骤您就可以创建一个 Telethon 应用程序了，快开始吧！

安装 Telethon
----------------------

1. 使用命令 ``pip3 install -U telethon`` 安装 Telethon 。

2. 打开网站 https://my.telegram.org/apps :doc:`申请属于您自己的 Telegram API key <../start/auth>` 。

3.  打开文本编辑器并粘贴以下内容：

    .. code-block:: python

        from telethon.sync import TelegramClient, events

        api_id = 12345
        api_hash = "0123456789abcdef0123456789abcdef"

        with TelegramClient('name', api_id, api_hash) as client:
            client.send_message('me', 'Hello, myself!')

4. 用您在第二步生成的值替换 *api_id* 和 *api_hash* 。

5. 报错文件名为 ``main.py`` 。

6. 使用命令 ``python3 main.py`` 开始运行。

7. 通过控制台提示进行账户授权。

8. 加入我们的 `交流社区`_.

享受 API
-------------

这只是运行 Telethon 的一个简单例子，在接下来的文档中，我们可以学习使用更加高级的方法。

想要继续学习吗？ 你可以点击 :doc:`调用方法 <../start/invoking>` 继续学习。

.. _交流社区: https://t.me/Telethon_CN_Chat