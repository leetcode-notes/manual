# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import os, glob, sys
import numpy as np
from keras.preprocessing import image
import time
import glob

MAKE_IMAGES = 10 # 何倍に水増しするかの設定（倍率）
INTERVAL = 0.1 # 画像生成処理のインターバル

def augmentImage(x):
  # 画像の水増しに使うフィルターを定義
  datagenX = image.ImageDataGenerator(
    # -20度～20度の範囲でランダムに回転を行う
    rotation_range = 20,
    # 上下平行移動
    height_shift_range = 0.3,
    # 左右平行移動
    width_shift_range = 0.3,
    # -10度～10度の範囲でランダムにせん断
    shear_range = 10,
    # [0.5, 1.2]の範囲でランダムに拡大縮小する
    zoom_range = [0.5, 1.2],
    # [-25.0, 25.0]の範囲でランダムに画素値に値を足す
    channel_shift_range = 25.,
    # 水平方向へのランダムの反転
    horizontal_flip = False,
    # 垂直方向へのランダムの反転
    vertical_flip = False
  )

  # 画像の水増しを行うジェネレータを準備
  genX = datagenX.flow(x, batch_size=1, save_to_dir=loadAndSavePath,
             save_prefix='aData', save_format='jpg')

  return genX


