:github_url: https://github.com/Xtao-Labs/docs-all

常见短语
=================

此页面包含常见短语列表。

.. contents:: 目录
    :backlinks: none
    :depth: 1
    :local:

-----

列表
-----

.. glossary::
    :sorted:

    API
        应用程序编程接口：一组方法、协议和工具，通过为开发人员提供实用的组件，使程序开发变得更容易。

    API key
        用于向 Telegram ``验证`` 和/或 ``授权`` 特定应用程序的密码，以便其控制 API 的使用方式，例如，防止滥用 API。
        :doc:`API keys <intro/quickstart>`。

    DC
        也称为 *数据中心* ，是一个放置大量计算机系统并一起使用以实现服务的高质量和可用性的地方。

    RPC
        远程过程调用的首字母缩写词，即在某个远程位置（即 Telegram 服务器）而不是在您的本地机器上执行的函数。

    RPCError
        由 RPC 引起的错误，必须返回以代替成功的结果，以便让调用者知道出现问题。

    Bot API
        Telegram Bot API 只能使用 HTTP 作为应用层协议将普通机器人连接到 Telegram，并允许执行 Telegram API 。

    Userbot
        也称为 *user bot* 或简称 *ubot*，是通过第三方 Telegram 库登录的用户 --- 例如
        Telethon --- 自动执行某些行为，例如发送消息或对文本命令作出反应或任何其他事件。不要与 *bot* 混淆，即由
        `@BotFather <https://t.me/botfather>`_ 创建的普通 Telegram bot 。

    Session
        也称为 *登录会话* ，是由双方（客户端和服务器）创建和持有的严格个人数据，用于向单个帐户授予权限，而无需从头开始新的授权过程。

    Callback
        也称为 *回调函数* ，是一个用户定义的通用函数， *可以* 注册到框架，然后在发生特定事件时由框架回调。

    Handler
        一个环绕回调函数的对象，该函数 *实际上意味着* 要注册到框架中，然后将能够处理特定类型的事件，例如新传入的消息。
        :doc:`消息更新处理器 <start/updates>`.
