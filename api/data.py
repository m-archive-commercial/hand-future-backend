import json
import shutil

from fastapi import APIRouter, Body

from path import GRAPH_DATA_PATH, GRAPH_DATA_BAK_PATH

data_router = APIRouter(prefix='/data', tags=['data'])


@data_router.get('/')
def get_data():
    with open(GRAPH_DATA_PATH, 'r') as f:
        return json.loads(f.read())


@data_router.put('/')
def set_data(data: dict = Body()):
    with open(GRAPH_DATA_PATH, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return True


@data_router.put('/reset')
def reset_data():
    shutil.copy2(GRAPH_DATA_BAK_PATH, GRAPH_DATA_PATH)
