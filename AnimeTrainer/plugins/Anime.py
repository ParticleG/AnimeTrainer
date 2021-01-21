from nonebot import on_command, CommandSession
from hashlib import md5

from AnimeTrainer.configs import *
from AnimeTrainer.utils.cq_utils import *
from AnimeTrainer.utils.cq_parser import *

import numpy as np
import matplotlib.pyplot as plt
import datetime
import random
import os


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
                    file_names = []
                    for parent_dir, sub_dirs, filenames in os.walk(PATHS['IMAGE_PATH']):
                        file_names += filenames

                    index = random.randint(0, len(file_names) - 1)
                    print(os.path.join(PATHS["IMAGE_PATH"], file_names[index]))
                    response = f'{cq_image_parser(os.path.join(PATHS["IMAGE_PATH"], file_names[index]))}'
                    break
            else:
                response = '本群没有开启涩图功能，请联系管理员开启'

            await send_message_async(session, response)

        except Exception:
            exception_handler("获取群成员列表失败", logging.WARNING, False,
                              session.event.group_id)
