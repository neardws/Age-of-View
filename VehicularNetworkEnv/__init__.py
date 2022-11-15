# -*- coding: UTF-8 -*-
"""
@Project ：Age-of-View
@File    ：__init__.py.py
@Author  ：Neardws
@Date    ：6/22/21 4:12 下午 
"""
from gym.envs.registration import register

register(
    id='vehicular-networks-v0',
    entry_point='gym_foo.envs:VehicularNetworksEnv',
)

