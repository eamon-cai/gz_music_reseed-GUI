#! /usr/bin/python
# -*- coding: UTF-8 -*-
import ui
import os
import sys
import qss
import json
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from resize import FramelessWindow

file_info = {}


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def read_config():
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    return data


def write_config(json_dict):
    with open("config.json", "w+", encoding="utf-8") as f:
        f.write(json.dumps(json_dict))


def rewrite(info_dict):
    write_config(info_dict)
    with open("sample.py", "r", encoding="utf-8") as f1, open("config.py", "w+", encoding="utf-8") as f2:
        for line in f1.readlines():
            for k, v in info_dict.items():
                if k in line:
                    line = line.replace(k, v)
            f2.write(line)


class UiMainWindow(QMainWindow, ui.Ui_MainWindow, FramelessWindow):
    def __init__(self):
        # 继承父类init方法
        super().__init__()
        self.setupUi(self)
        self.init()  # 初始化
        self.connect()  # 连接控件
        self.show()

    # 初始化
    def init(self):
        self.setStyleSheet(qss.get(0))  # 样式
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 无边框
        self.setWindowIcon(QIcon("icon.ico"))  # 任务栏图标
        self.logo.setPixmap(QtGui.QPixmap("icon.ico").scaled(32, 32))  # 设置按钮图标
        self.setWindowOpacity(0.96)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.resize(1024, 768)  # 尺寸
        try:
            self.tab1_init()
            self.tab2_init()
            self.tab3_init()
        except Exception as e:
            print(e)

    # 连接控件
    def connect(self):
        self.minimum.clicked.connect(self.showMinimized)
        self.maxmum.clicked.connect(self.slot_max_or_recv)
        self.quit.clicked.connect(QCoreApplication.instance().quit)

    # 第一页初始化
    def tab1_init(self):
        # 第一页
        self.text_res.setReadOnly(True)  # 文本框只读
        self.btn_file.clicked.connect(self.set_file_path)
        self.btn_res.clicked.connect(self.set_res_path)

        self.btn_dic.clicked.connect(self.dic)

        config = read_config()
        self.file_dir.setText(config["file_path"])
        self.res_dir.setText(config["res_path"])
        self.dic_php.setText(config["dic_PHPSESSID"])
        self.dic_session.setText(config["dic_session"])
        self.dic_key.setText(config["dic_key"])
        self.dic_pass.setText(config["dic_pass"])

    # 第一页初始化
    def tab2_init(self):
        self.btn_red.clicked.connect(self.red)
        config = read_config()
        self.red_api.setText(config["red_api"])
        self.red_key.setText(config["red_key"])
        self.red_pass.setText(config["red_pass"])

    # 第一页初始化
    def tab3_init(self):
        self.btn_ops.clicked.connect(self.ops)
        config = read_config()
        self.ops_api.setText(config["ops_api"])
        self.ops_key.setText(config["ops_key"])
        self.ops_pass.setText(config["ops_pass"])

    # 重写窗口大小改变事件
    def slot_max_or_recv(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    # 重写鼠标事件
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写鼠标移动事件
        self._end_pos = e.pos() - self._startPos
        self.move(self.pos() + self._end_pos)

    def mousePressEvent(self, e: QMouseEvent):  # 重写鼠标按压事件
        if e.button() == Qt.LeftButton or e.button() == Qt.MiddleButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())
        else:
            self.rightMenuShow()

    def mouseReleaseEvent(self, e: QMouseEvent):  # 重写鼠标释放事件
        if e.button() == Qt.LeftButton or e.button() == Qt.MiddleButton:
            self._isTracking = False
            self._startPos = None
            self._end_pos = None
        else:
            pass

    def rightMenuShow(self):
        try:
            self.contextMenu = QMenu()
            self.contextMenu.popup(QCursor.pos())  # 菜单显示的位置
            self.actionA = self.contextMenu.addAction(u"空")
            self.actionA.triggered.connect(self.actionHandler)
            self.contextMenu.show()
        except Exception as e:
            self.printf(e)

    @staticmethod
    def actionHandler():
        print("action")

    # 文件浏览
    def set_file_path(self):
        config = read_config()
        file_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "浏览", config["file_path"]
        )
        self.file_dir.setText(file_path)

    # 文件浏览
    def set_res_path(self):
        config = read_config()
        res_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "浏览", config["res_path"]
        )
        self.res_dir.setText(res_path)

    def info_dic(self):
        key_dic = {
            "dic_PHPSESSID": self.dic_php.text(),
            "dic_session": self.dic_session.text(),
            "dic_key": self.dic_key.text(),
            "dic_pass": self.dic_pass.text(),
            "red_api": self.red_api.text(),
            "red_key": self.red_key.text(),
            "red_pass": self.red_pass.text(),
            "ops_api": self.ops_api.text(),
            "ops_key": self.ops_key.text(),
            "ops_pass": self.ops_pass.text(),
            "file_path": self.file_dir.text(),
            "res_path": self.res_dir.text()
        }
        return key_dic

    # 海豚
    def dic(self):
        rewrite(self.info_dic())
        self.bat("dic")

    # red
    def red(self):
        rewrite(self.info_dic())
        self.bat("red")

    # red
    def ops(self):
        rewrite(self.info_dic())
        self.bat("ops")

    def bat(self, site):
        reply = QMessageBox.question(
            self, "消息", "使用本软件，默认同意声明", QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:  # 确认删除
            path = os.getcwd()
            make_dir(path + "/cache/" + site)
            file_dir = self.file_dir.text()
            res_dir = self.res_dir.text()

            with open("./%s.bat" % site, "w", encoding="utf-8") as f:
                line = "python reseed.py --site %s --dir " % site + file_dir + " --result-dir " + res_dir + "\npause"
                f.write(line)
            self.printf("配置文件生成完毕,请双击bat文件运行")

    # 输出日志
    def printf(self, text):
        print(str(text))
        self.text_res.append(str(text))


app = QApplication(sys.argv)
win = UiMainWindow()
sys.exit(app.exec_())
