from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# 枚举左上右下以及四个定点
Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)


class FramelessWindow(QWidget):
    # 四周边距
    Margins = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._pressed = False
        self.Direction = None

        # 鼠标跟踪
        self.setMouseTracking(True)
        # 布局
        layout = QWidget(self)
        # 预留边界用于实现无边框窗口调整大小
        layout.setContentsMargins(
            self.Margins, self.Margins, self.Margins, self.Margins
        )

    def _resizeWidget(self, pos):
        """调整窗口大小"""
        if self.Direction is None:
            return
        m_pos = pos - self._m_pos
        x_pos, y_pos = m_pos.x(), m_pos.y()
        geometry = self.geometry()
        x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
        if self.Direction == LeftTop:  # 左上角
            if w - x_pos > self.minimumWidth():
                x += x_pos
                w -= x_pos
            if h - y_pos > self.minimumHeight():
                y += y_pos
                h -= y_pos
        elif self.Direction == RightBottom:  # 右下角
            if w + x_pos > self.minimumWidth():
                w += x_pos
                self._m_pos = pos
            if h + y_pos > self.minimumHeight():
                h += y_pos
                self._m_pos = pos
        elif self.Direction == RightTop:  # 右上角
            if h - y_pos > self.minimumHeight():
                y += y_pos
                h -= y_pos
            if w + x_pos > self.minimumWidth():
                w += x_pos
                self._m_pos.setX(pos.x())
        elif self.Direction == LeftBottom:  # 左下角
            if w - x_pos > self.minimumWidth():
                x += x_pos
                w -= x_pos
            if h + y_pos > self.minimumHeight():
                h += y_pos
                self._m_pos.setY(pos.y())
        elif self.Direction == Left:  # 左边
            if w - x_pos > self.minimumWidth():
                x += x_pos
                w -= x_pos
            else:
                return
        elif self.Direction == Right:  # 右边
            if w + x_pos > self.minimumWidth():
                w += x_pos
                self._m_pos = pos
            else:
                return
        elif self.Direction == Top:  # 上面
            if h - y_pos > self.minimumHeight():
                y += y_pos
                h -= y_pos
            else:
                return
        elif self.Direction == Bottom:  # 下面
            if h + y_pos > self.minimumHeight():
                h += y_pos
                self._m_pos = pos
            else:
                return
        self.setGeometry(x, y, w, h)
