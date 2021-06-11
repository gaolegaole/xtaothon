:github_url: https://github.com/Xtao-Labs/docs-all

文本格式
===============

.. role:: strike
    :class: strike

.. role:: underline
    :class: underline

.. role:: bold-underline
    :class: bold-underline

.. role:: strike-italic
    :class: strike-italic

Telethon 支持格式化消息为 Markdown 或者 HTML 。

.. contents:: 目录
    :backlinks: none
    :depth: 1
    :local:

-----

基本样式
------------

您可以在 Markdown 样式，HTML 样式之间进行选择。以下是 Telethon 目前支持的基本样式列表。

- **bold**
- *italic*
- :strike:`strike`
- :underline:`underline`
- `text URL <https://docs.xtaolabs.com>`_
- `user text mention <https://t.me/mrwangzhe>`_
- `inline fixed-width code`

.. note::

    提及用户功能仅适用于您在对话中见过此用户。

Markdown 样式
--------------

:meth:`~telethon.client.send_message` 在消息中使用以下语法：

.. code-block:: text

    **bold**

    __italic__

    --underline--

    ~~strike~~

    [text URL](https://docs.xtaolabs.com/)

    [text user mention](tg://user?id=347437156)

    `inline fixed-width code`

**Example**:

.. code-block:: python

    app.send_message(
        "me",
        (
            "**bold**, "
            "__italic__, "
            "--underline--, "
            "~~strike~~, "
            "[mention](tg://user?id=347437156), "
            "[URL](https://docs.xtaolabs.com), "
            "`code`"
        )
    )

HTML 样式
----------

:meth:`~telethon.client.send_message` 在消息中使用以下语法：

.. code-block:: text

    <b>bold</b>, <strong>bold</strong>

    <i>italic</i>, <em>italic</em>

    <u>underline</u>

    <s>strike</s>, <del>strike</del>, <strike>strike</strike>

    <a href="http://docs.xtaolabs.com/">text URL</a>

    <a href="tg://user?id=347437156">inline mention</a>

    <code>inline fixed-width code</code>

**Example**:

.. code-block:: python

    app.send_message(
        "haskell",
        (
            "<b>bold</b>, "
            "<i>italic</i>, "
            "<u>underline</u>, "
            "<s>strike</s>, "
            "<a href=\"tg://user?id=347437156\">mention</a>, "
            "<a href=\"https://docs.xtaolabs.com/\">URL</a>, "
            "<code>code</code>"
        ),
        parse_mode="html"
    )

.. note::

    所有不属于标签或 HTML 实体的 ``<``, ``>`` 和 ``&`` 符号必须替换为相应的 HTML 实体（
    ``<`` 替换为 ``&lt;``, ``>`` 替换为 ``&gt;`` 和 ``&`` 替换为 ``&amp;``)。您可以使用此代码段快速转义这些字符：

    .. code-block:: python

        import html

        text = "<my text>"
        text = html.escape(text)

        print(text)

    .. code-block:: text

        &lt;my text&gt;
