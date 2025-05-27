import win32gui as getwin
import pyautogui as autogui
import _thread
import time

# 预加载
GoFishingOnceMore = './GoFishingOnceMore.png'

# 捕获MuMu模拟器12窗口
MuMu = {
    "location":getwin.GetWindowRect(getwin.FindWindow(None,"MuMu模拟器12")),
}
if not MuMu:
    print("请打开 MuMu模拟器12 后重试")

# 游戏窗口范围
sgs = {
    "left":MuMu["location"][0],
    "top":MuMu["location"][1] + 77,
    "right":MuMu["location"][2] - MuMu["location"][0],
    "bottom":MuMu["location"][3]
}

# print("开始钓鱼")
# autogui.click(sgs["right"]-250,sgs["bottom"]-250)
# # 抛竿
# time.sleep(2)
# print("抛竿")
# autogui.moveTo(sgs["right"]-250,sgs["bottom"]-150)
# autogui.dragTo(sgs["right"]-250,sgs["bottom"]-350,duration=0.5,button="left")
# 提竿


# autogui.moveTo(sgs["left"]+525,sgs["top"]+450)
autogui.moveTo(sgs["right"]-550,sgs["top"]+75)

# pyautogui.pixelMatchesColor(x, y, target_color)
# def Matching_Pixels(x,y,color):
#     print("kaishi")
#     while True:
#         if autogui.pixelMatchesColor(x, y, color,tolerance=30):
#             print("yy")
#             # _thread.exit()
#
# _thread.start_new_thread(Matching_Pixels,(sgs["left"]+525,sgs["top"]+435,(247, 203, 107)))
#
# time.sleep(10)

# 99, 77, 66