from nonebot import on_command, CommandSession
from hashlib import md5

from AnimeTrainer.configs import *
from AnimeTrainer.utils.cq_utils import *
from AnimeTrainer.utils.cq_parser import *

import numpy as np
import matplotlib.pyplot as plt
import datetime
import base64
import io


@on_command('image',
            aliases=('涩图', '色图', 'SetU'),
            only_to_me=False,
            shell_like=True)
async def image(session: CommandSession):
    args = session.current_arg_text.strip().split()
    if len(args) == 0:
        # noinspection PyBroadException
        try:
            for temp_group in GROUPS:
                if session.event.group_id == temp_group['group']:
                    response = f'{cq_image_parser()}你没有今日CP，快和{temp_group["nickname"]}贴贴去吧！'
                    break
            else:
                response = '本群没有开启涩图功能，请联系管理员开启'

            await send_message_async(session, response)

        except Exception:
            exception_handler("获取群成员列表失败", logging.WARNING, False,
                              session.event.group_id)
