:github_url: https://github.com/Xtao-Labs/docs-all

安装指南
=============

**Telethon** 所需要的 Python 的版本至少为 3.5 。我们推荐您使用最新的 Python 和 pip 版本。

- 从 https://www.python.org/downloads/ 中下载 **Python 3** (或者使用系统包管理器)。
- 从 https://pip.pypa.io/en/latest/installing/ 中安装 **pip** 。

.. important::

    Telethon 仅支持 **Python 3.5+** 。

.. contents:: 目录
    :backlinks: none
    :depth: 1
    :local:

-----

安装
----------------

-   将 Telethon 安装和升级到其最新稳定版本的最简单方法是使用 **pip**:

    .. code-block:: text

        $ python3 -m pip install --upgrade telethon

安装开发版本
-------------

如果您希望尝试新功能，则可以运行以下命令安装开发版本：

.. important::

    开发版本可能会发生错误，不建议用于生产环境。

.. code-block:: text

    $ python3 -m pip install --upgrade https://github.com/LonamiWebs/Telethon/archive/master.zip

验证安装
---------

要验证是否正确安装了 Telethon ，请运行以下命令：（如果没有错误显示即安装成功）

.. code-block:: text

    $ python3 -c "import telethon; print(telethon.__version__)"