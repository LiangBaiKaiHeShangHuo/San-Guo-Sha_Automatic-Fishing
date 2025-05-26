# 三国杀自动钓鱼脚本,仅供学习python使用
# 基于MuMu模拟器12,分辨率为手机版900X1600(DPI 320)
import win32gui as getwin
import pyautogui as autogui
import _thread as th
from time import sleep

ckech_img_isTrue = False

# 预加载
GoFishingOnceMore = './GoFishingOnceMore.png'
def Matching_Pixels_Eve(type):
    if type == "提竿":
        autogui.click(sgs["right"] - 250, sgs["bottom"] - 250)

def Matching_Pixels(x, y, color,callback,type):
    while True:
        if autogui.pixelMatchesColor(x, y, color, tolerance=30):
            callback(type)
            break
def check_img(url,region):
    global ckech_img_isTrue
    while True:
        try:
            imgs = autogui.locateOnScreen(url, region=region, confidence=0.7, grayscale=True)
            if imgs:
                ckech_img_isTrue = True
                sleep(1)
                autogui.click(autogui.center(imgs))
                break
        except:
            sleep(0.5)
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

xun = 5
currentXun = 0
while xun>0:
    currentXun += 1
    # 点击开始游戏
    sleep(1)
    print(f"开始钓鱼(第{currentXun}轮)")
    autogui.click(sgs["right"]-250,sgs["bottom"]-250)
    # 抛竿
    sleep(2)
    print(f"抛竿(第{currentXun}轮)")
    autogui.moveTo(sgs["right"]-250,sgs["bottom"]-150)
    autogui.dragTo(sgs["right"]-250,sgs["bottom"]-350,duration=0.5,button="left")
    # 提竿
    print(f"提竿(第{currentXun}轮)")
    Matching_Pixels(
        sgs["left"] + 525,
        sgs["top"] + 435,
        (247, 203, 107),
        Matching_Pixels_Eve,
        "提竿"
    )
    # 收线
    sleep(1)
    print(f"收线(第{currentXun}轮)")
    th.start_new_thread(
        check_img,
        (GoFishingOnceMore,MuMu["location"])
    )
    while True:
        if ckech_img_isTrue:
            break
        if autogui.pixelMatchesColor(sgs["right"]-550, sgs["top"]+75,(99, 77, 66), tolerance=30):
            autogui.click(sgs["right"] - 250, sgs["bottom"] - 250, clicks=5, interval=0.1, button="left")
        else:
            sleep(1)
    ckech_img_isTrue = False
    xun-=1