from enum import Enum
from typing import TypedDict

from pydantic import BaseModel


class HeroModel(BaseModel):
    id: str
    name: str
    avatar: str
    title: str
    cities: str
    class Config:
        schema_extra = {
            "example": {
                "id": "suyang@gkleifeng.com",
                "name": '苏阳',
                "city": "北京",
                "avatar": '/Users/mark/Projects/HandFuture/website/2.12 分享卡片设计文件夹(_F)/Links/苏阳_avatar.jpg',
                "title": '杰出的民族摇滚音乐家、当代艺术家',
                "desc": '他将“花儿”、“秦腔”等西北民间音乐及传统曲艺形式，与流行音乐进行嫁接、改良和解构，经由西方现代音乐的理论和手法，创造出一种全新的音乐语言。',
            }
        }
