:github_url: https://github.com/Xtao-Labs/docs-all

可用方法
=================

此页面是关于 Telethon 方法的。这里列出的所有方法都绑定到 :class:`~telethon.Client` 类。

.. code-block:: python
    :emphasize-lines: 4

    from telethon.sync import TelegramClient, events

    with TelegramClient('name', api_id, api_hash) as client:
       client.send_message('me', 'Hello, myself!')

.. contents:: 目录
    :backlinks: none
    :local:

-----

.. currentmodule:: telethon.Client

基础
---------

.. autosummary::
    :nosignatures:

    start <start>
    disconnect <disconnect>

.. toctree::
    :hidden:

    start <start>
    disconnect <disconnect>


消息
---------

.. autosummary::
    :nosignatures:

    send_message <send_message>
    edit_message <edit_message>
    delete_messages <delete_messages>
    forward_messages <forward_messages>
    iter_messages <iter_messages>
    get_messages <get_messages>
    pin_message <pin_message>
    unpin_message <unpin_message>
    send_read_acknowledge <send_read_acknowledge>

.. toctree::
    :hidden:

    send_message <send_message>
    edit_message <edit_message>
    delete_messages <delete_messages>
    forward_messages <forward_messages>
    iter_messages <iter_messages>
    get_messages <get_messages>
    pin_message <pin_message>
    unpin_message <unpin_message>
    send_read_acknowledge <send_read_acknowledge>

上传
---------

.. autosummary::
    :nosignatures:

    send_file <send_file>

.. toctree::
    :hidden:

    send_file <send_file>

下载
---------

.. autosummary::
    :nosignatures:

    download_media <download_media>

.. toctree::
    :hidden:

    download_media <download_media>

用户
---------

.. autosummary::
    :nosignatures:

    get_me <get_me>
    get_entity <get_entity>
    get_input_entity <get_input_entity>

.. toctree::
    :hidden:

    get_me <get_me>
    get_entity <get_entity>
    get_input_entity <get_input_entity>
