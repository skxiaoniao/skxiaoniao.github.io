# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time

import pyautogui
import cv2
import pydirectinput
import numpy as np
import os


def replay(locate_path, match_image):
    game_picture = cv2.imread(match_image)
    game_picture_gray = cv2.cvtColor(game_picture, cv2.COLOR_BGR2GRAY)
    height, width, channel = game_picture.shape

    pyautogui.screenshot().save(locate_path)
    picture = cv2.imread(locate_path)
    picture_gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(picture_gray, game_picture_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # position = list(zip(*result[::-1]))
    # print(min_val)
    # print(max_val)
    # print(min_loc)
    # print(max_loc)
    threshold = 0.75
    loc = np.where(result >= threshold)
    # conformance = max_val


    print('----------------开始查找-------------')
    print(min_val)
    print(max_val)
    if max_val > threshold:
        print('找到图像' + str(match_image) + '-------------')

        startX, startY = max_loc
        endX = startX + width
        endY = startY + height
        top_left = (startX, startY)
        bottom_right = (startX + width, startY + height)
        # cv2.rectangle(picture_gray, top_left, bottom_right, (0, 0, 255), 5)
        # cv2.imshow("img_rgb", picture_gray)
        # cv2.waitKey()
        avg = (int((startX + endX) / 2),
               int((startY + endY) / 2))
        duration_time = random.randrange(0, 2)
        pyautogui.moveTo(avg, duration=duration_time)
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        sleep_time = random.randrange(1, 2)
        time.sleep(sleep_time)


def attack(locate_path, match_image):

    game_picture = cv2.imread(match_image)
    game_picture_gray = cv2.cvtColor(game_picture, cv2.COLOR_BGR2GRAY)
    height, width, channel = game_picture.shape

    pyautogui.screenshot().save(locate_path)
    picture = cv2.imread(locate_path)
    picture_gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(picture_gray, game_picture_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # position = list(zip(*result[::-1]))
    # print(min_val)
    # print(max_val)
    # print(min_loc)
    # print(max_loc)
    threshold = 0.75
    loc = np.where(result >= threshold)
    # conformance = max_val


    print('----------------开始查找-------------')
    print(min_val)
    print(max_val)
    if max_val > threshold:
        print('找到图像' + str(match_image) + '-------------')

        startX, startY = max_loc
        endX = startX + width
        endY = startY + height
        top_left = (startX, startY)
        bottom_right = (startX + width, startY + height)
        # cv2.rectangle(picture_gray, top_left, bottom_right, (0, 0, 255), 5)
        # cv2.imshow("img_rgb", picture_gray)
        # cv2.waitKey()
        avg = (int((startX + endX) / 2),
               int((startY + endY) / 2))
        duration_time = random.randrange(0, 2)
        pyautogui.moveTo(avg, duration=duration_time)
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        pyautogui.doubleClick()
        sleep_time = random.randrange(1, 2)
        time.sleep(sleep_time)

def image_position(locate_path, match_image, filename):
    # pyautogui.screenshot().save(locate_path)
    # picture = cv2.imread(locate_path)
    # adventure_picture = cv2.imread(match_image)
    # height, width, channel = adventure_picture.shape
    #
    # result = cv2.matchTemplate(picture, adventure_picture, cv2.TM_SQDIFF_NORMED)
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #
    # threshold = 0.98
    # loc = np.where(result >= threshold)
    # print(len(loc))
    # print(max_val)
    # conformance = max_val
    # while conformance < 0.98:
    #     print("match_image1:" + match_image)
    #     result = cv2.matchTemplate(picture, adventure_picture, cv2.TM_CCOEFF_NORMED)
    #     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #     conformance = max_val
    #     # adventure_upper_left = cv2.minMaxLoc(result)[2]
    #     # adventure_lower_right = (adventure_upper_left[0] + width, adventure_upper_left[1] + height)
    #     # avg = (int((adventure_upper_left[0] + adventure_lower_right[0]) / 2),
    #     #        int((adventure_upper_left[1] + adventure_lower_right[1]) / 2))
    #     # pyautogui.click(avg)
    #     sleep_time = random.randrange(2, 3)
    #     time.sleep(sleep_time)
    #
    # print("match_image2:" + match_image)
    # adventure_upper_left = cv2.minMaxLoc(result)[2]
    # adventure_lower_right = (adventure_upper_left[0] + width, adventure_upper_left[1] + height)
    # avg = (int((adventure_upper_left[0] + adventure_lower_right[0]) / 2),
    #        int((adventure_upper_left[1] + adventure_lower_right[1]) / 2))
    # duration_time = random.randrange(0, 2)
    # pyautogui.moveTo(avg, duration=duration_time)
    # pyautogui.click()
    # sleep_time = random.randrange(1, 2)
    # time.sleep(sleep_time)

    game_picture = cv2.imread(match_image)
    game_picture_gray = cv2.cvtColor(game_picture, cv2.COLOR_BGR2GRAY)
    height, width, channel = game_picture.shape
    print('=============================')
    print('开始查找图像' + str(match_image))
    print('=============================')
    # cv2.imshow('Game Screenshot with Template', adventure_picture)
    # cv2.waitKey(0)

    while True:
        # 截取游戏窗口的屏幕截图
        pyautogui.screenshot().save(locate_path)
        picture = cv2.imread(locate_path)
        picture_gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)

        # cv2.imshow('Game Screenshot with Template', picture_gray)
        # cv2.waitKey(0)娃娃

        # 在游戏窗口截图中搜索模板图像
        result = cv2.matchTemplate(picture_gray, game_picture_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # position = list(zip(*result[::-1]))
        # print(min_val)
        # print(max_val)
        # print(min_loc)
        # print(max_loc)
        threshold = 0.75
        loc = np.where(result >= threshold)
        # conformance = max_val

        result_locate_image = './result/match_' + filename + '_1.png'
        result_match_image = './result/match_' + filename + '_2.png'

        cv2.imwrite(result_locate_image, picture_gray)
        cv2.imwrite(result_match_image, game_picture_gray)

        print('----------------开始查找-------------')
        print(min_val)
        print(max_val)
        if max_val > threshold:
            print('找到图像' + str(match_image) + '-------------')

            startX, startY = max_loc
            endX = startX + width
            endY = startY + height
            top_left = (startX, startY)
            bottom_right = (startX + width, startY + height)
            # cv2.rectangle(picture_gray, top_left, bottom_right, (0, 0, 255), 5)
            # cv2.imshow("img_rgb", picture_gray)
            # cv2.waitKey()
            avg = (int((startX + endX) / 2),
                   int((startY + endY) / 2))
            # duration_time = random.randrange(0, 0)
            pyautogui.moveTo(avg)
            pyautogui.click()
            sleep_time = random.randrange(1, 2)
            time.sleep(sleep_time)

            # 显示标记后的游戏窗口截图
            # cv2.imshow('Game Screenshot with Template', game_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            break
        else:
            print('未找到查找图像' + str(match_image) + '继续查找中' + '-------------')
            time.sleep(1)
            if filename == '8':
                attack('picture/attack.png', 'battle/attack.png')
                pydirectinput.keyDown('w')
                pydirectinput.press(['space'], presses=5, interval=0, logScreenshot=None, _pause=True)
                pydirectinput.press(['shift'], presses=5, interval=0, logScreenshot=None, _pause=True)
                pydirectinput.keyUp('w')
                pydirectinput.press(['1'], presses=2, interval=0, logScreenshot=None, _pause=True)
                pydirectinput.keyDown('w')
                pydirectinput.press(['2'], presses=2, interval=0, logScreenshot=None, _pause=True)
                pydirectinput.keyUp('w')
                pydirectinput.press(['3'], presses=2, interval=0, logScreenshot=None, _pause=True)
                pydirectinput.press(['4'], presses=2, interval=0, logScreenshot=None, _pause=True)
                pydirectinput.keyDown('w')
                pydirectinput.press(['e'], presses=2, interval=0, logScreenshot=None, _pause=True)
                pydirectinput.keyUp('w')
                pydirectinput.keyDown('w')

            if filename == '9':
                replay('picture/11.png', 'image/11.png')
            # pyautogui.doubleClick(clicks=2, interval=1, button='left')
            # 截取游戏窗口的屏幕截图
            # pyautogui.screenshot().save(locate_path)
            # picture = cv2.imread(locate_path)
            #
            # result = cv2.matchTemplate(picture, game_picture, cv2.TM_SQDIFF_NORMED)
            # position = list(zip(*result[::-1]))
            # print(len(position))
            # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            #
            # loc = np.where(result >= threshold)
            #
            # if len(loc) > 0:
            #     startX, startY = min_loc
            #     endX = startX + width
            #     endY = startY + height
            #     top_left = (startX, startY)
            #     bottom_right = (startX + width, startY + height)
            #     avg = (int((startX + endX) / 2),
            #            int((startY + endY) / 2))
            #     pyautogui.click(avg)
            #     sleep_time = random.randrange(2, 3)
            #     time.sleep(sleep_time)


def play():
    # pyautogui.press(['w'], presses=5, interval=1, logScreenshot=None, _pause=True)
    # pydirectinput.click()
    # pydirectinput.press('w')
    # pydirectinput.press('w')
    # pydirectinput.press('w')
    # pydirectinput.press('w')

    pydirectinput.press('tab')

    # pydirectinput.keyDown('w')
    # pydirectinput.press(['w'], presses=5, interval=0, logScreenshot=None, _pause=True)
    # size_x, size_y = pyautogui.size()
    # pyautogui.click(size_x / 2 - 100, size_y / 2, duration=0.5)

    # 冒险位置查找
    image_position('picture/1.png', 'image/1.png', '1')
    # 克罗姆军工厂
    image_position('picture/2.png', 'image/2.png', '2')
    # 进图
    image_position('picture/3.png', 'image/3.png', '3')
    # 组队挑战
    image_position('picture/4.png', 'image/4.png', '4')
    # 快读匹配
    image_position('picture/5.png', 'image/5.png', '5')
    # 战斗准备ds
    image_position('picture/6.png', 'image/6.png', '6')
    # 准备
    image_position('picture/7.png', 'image/7.png', '7')

    # sleep_time = random.randrange(50, 100)
    # time.sleep(sleep_time)

    # 战斗结束查找
    image_position('picture/8.png', 'image/8.png', '8')

    sleep_time = random.randrange(2, 3)
    time.sleep(sleep_time)
    # 退出
    image_position('picture/9.png', 'image/9.png', '9')

    # 确认
    image_position('picture/10.png', 'image/10.png', '10')
    sleep_time = random.randrange(5, 6)
    time.sleep(sleep_time)
    #
    # while 1 == 1 and count != 300:
    #     choice = random.choice('wad123455e')
    #     sleep_time = random.randrange(1, 2)
    #     time.sleep(sleep_time)
    #     pydirectinput.keyDown(choice)
    #     count = count + 1
    #     print(count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    time.sleep(3)
    window = pyautogui.getActiveWindow()
    # print(window)
    while 1 == 1:
        play()
    # play()

    # pyautog4ui.click()
    # print(pyautogui.size())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
