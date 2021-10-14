qss = """
蓝色
/*#COLOR#;MAIN_COLOR=#00bcd4;BTN_HOVER_COLOR=#24d4e0;BTN_PRESSED_COLOR=#0296ad;ITEM_HOVER_COLOR=#cafcf9;ITEM_SELECTED_COLOR=#a2fcf9*/
/**********窗口样式*************/
QWidget#QSkinDemoClass,
QWidget#QSkinEditDialog,
QWidget#QMyMessageBox,
QWidget#QAboutDialog,
QWidget#formLayout
{
    border:1px solid #00bcd4;
    border-radius:5px;
    background: #FFFFFF;
}

/***********主窗口*************/
QWidget#centralwidget{
    background-color:#eef0f6;
    border-left:0.5px solid lightgray;
    border-right:0.5px solid lightgray;
    border-top:0.5px solid lightgray;
    border-bottom:0.5px solid #e5e5e5;
    border-radius:7px;
}

.QFrame{
    border:1px solid #00bcd4;
    border-radius:5px;
}

/***************标题栏*****************/
QWidget#widget_title{
    background: #00bcd4;
}

QWidget#widget_title2{
    background: #00bcd4;
}


/**********菜单栏窗口样式*************/
QWidget#widget_menu{
    /*background: #cafcf9;*/
   /* border: 1px solid #00bcd4;*/
    /*border-left: none;*/
    /*border-right: none;*/
}

/**********状态栏窗口样式*************/
QWidget#widget_status{
        background: #00bcd4;
        border: 1px solid #00bcd4;
        border-left: none;
        border-right: none;
        border-bottom: none;
}

QLabel#logo{
    image: url(:icon.ico);
}


QLabel#label_MessageType[MessageType="information"] {
        qproperty-pixmap: url(:/Skin/img/information);
}

QLabel#label_MessageType[MessageType="error"] {
        qproperty-pixmap: url(:/Skin/img/error);
}

QLabel#label_MessageType[MessageType="success"] {
        qproperty-pixmap: url(:/Skin/img/success);
}

QLabel#label_MessageType[MessageType="question"] {
        qproperty-pixmap: url(:/Skin/img/question);
}

QLabel#label_MessageType[MessageType="warning"] {
        qproperty-pixmap: url(:/Skin/img/warning);
}

/**********文本编辑框**********/
QTextEdit,QLineEdit {
    border: 1px solid #00bcd4;
    border-radius: 5px;
    padding: 2px;
    background: none;
    selection-background-color: #00bcd4;
}

QLineEdit[echoMode="2"] {
    lineedit-password-character: 9679;
}

.QGroupBox{
     border: 1px solid #00bcd4;
     border-radius: 5px;
     margin-top: 3ex;/* leave space at the top for the title */
}
.QGroupBox::title {
      subcontrol-origin: margin;
     position: relative;
     left: 10px;
 }
 

.QPushButton{
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 5px;
    border-radius:5px;
    background: #00bcd4;
}



.QPushButton[focusPolicy="0"] {
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 0px;
    border-radius:3px;
    background: #00bcd4;
}

.QPushButton:hover{
    background: #24d4e0
}

.QPushButton:pressed{
    background: #0296ad;
}


.QToolButton{
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 4px;
    border-radius:5px;
    background: #00bcd4;
}

.QToolButton[focusPolicy="0"] {
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 0px;
    border-radius:3px;
    background: #00bcd4;
}

.QToolButton:hover{
    background: #24d4e0
}

.QToolButton:pressed{
    background: #0296ad;
}

.QToolButton[pageTab="true"] {
    border: none;
    padding-top:5px;
    background: none;
    color: #000000;
    border-radius:0px;
}

.QToolButton[pageTab="true"]:hover {
    background-color:#EEEEEE;
    border: none;
}

.QToolButton[pageTab="true"]:pressed {
    border: 4px solid #00bcd4;
    border-top: none;
    border-right: none;
    border-bottom: none;
    background-color:#EEEEEE;
}
.QToolButton[pageTab="true"]:checked {
    border: 4px solid #00bcd4;
    border-top: none;
    border-right: none;
    border-bottom: none;
    background-color:#EEEEEE;
}

.QToolButton[TopPageTab="true"] {
    border: none;
    padding-top:10px;
    color: #FFFFFF;
    background: none;
    border-radius:0px;
}

.QToolButton[TopPageTab="true"]:hover {
    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0%), stop:1 rgba(4, 20, 7, 10%));
    border: none;
    color: #FFFFFF;
}

.QToolButton[TopPageTab="true"]:pressed {
    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0%), stop:1 rgba(4, 20, 7, 10%));
    border: none;
    color: #FFFFFF;
}
.QToolButton[TopPageTab="true"]:checked {
    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0%), stop:1 rgba(4, 20, 7, 10%));
    border: none;
    color: #FFFFFF;
}

QPushButton#menuButton_Min,QPushButton#menuButton_Max,QPushButton#menuButton_Close{
    border-radius:0px;
    color: #FFFFFF;
    background-color:rgba(0,0,0,0);
    border-style:none;
}

QPushButton#menuButton_Min:hover,QPushButton#menuButton_Max:hover{
    background-color: #24d4e0;
}
QPushButton#menuButton_Min:pressed,QPushButton#menuButton_Max:pressed{
    background-color: #0296ad;
}
QPushButton#menuButton_Close:hover{
    background-color: #FF5439;
}
QPushButton#menuButton_Close:pressed{
    background-color: #E04A32;
}

QCheckBox {
    spacing: 2px;
}

QCheckBox::indicator, QTableView::indicator, QListView::indicator, QTreeView::indicator, QGroupBox::indicator {
    width: 15px;
    height: 15px;
}

QCheckBox::indicator:unchecked, QTableView::indicator:unchecked, QListView::indicator:unchecked, QTreeView::indicator:unchecked, QGroupBox::indicator:unchecked {

}

QCheckBox::indicator:checked, QTableView::indicator:checked, QListView::indicator:checked, QTreeView::indicator:checked, QGroupBox::indicator:checked {

}

QRadioButton {
    spacing: 2px;
}

QRadioButton::indicator {
    width: 15px;
    height: 15px;
}

QRadioButton::indicator::unchecked {
    image: url(:/Skin/img/radio_normal.png);
}

QRadioButton::indicator::checked {
    image: url(:/Skin/img/radio_selected.png);
}

QComboBox,QDateEdit,QDateTimeEdit,QTimeEdit,QDoubleSpinBox,QSpinBox{
    border-radius: 3px;
    padding: 1px 5px 1px 5px;
    border: 1px solid #00bcd4;
    selection-background-color: #00bcd4;
}

QComboBox::drop-down,QDateEdit::drop-down,QDateTimeEdit::drop-down,QTimeEdit::drop-down,QDoubleSpinBox::drop-down,QSpinBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 1px;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    border-left-color: #00bcd4;
}

QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow {
    image: url(:/Skin/img/array_down.png);
    width:10px;
    height:9px;
}

QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
    image: url(:/Skin/img/array_up.png);
    width:10px;
    height:10px;
    padding:0px 3px 0px 0px;
}

QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
    image: url(:/Skin/img/array_down.png);
    width:10px;
    height:10px;
    padding:0px 3px 0px 0px;
}

/**********菜单栏**********/
QMenuBar {
        background: #cafcf9;
        border: 1px solid #00bcd4;
        border-left: none;
        border-right: none;
        border-top: none;
}
QMenuBar::item {
        border: 1px solid transparent;
        padding: 5px 10px 5px 10px;
        background: transparent;
}
QMenuBar::item:enabled {
        color: #000000;
}
QMenuBar::item:!enabled {
        color: rgb(155, 155, 155);
}
QMenuBar::item:enabled:selected {
        background: #a2fcf9;
}

QMenu {
    background-color:#FFFFFF;
    /*margin: 2px;*/
    border: 1px solid #00bcd4;
}

QMenu::item {
    padding: 2px 20px 2px 20px;
}

QMenu::indicator {
    width: 13px;
    height: 13px;
}

QMenu::item:selected {
    color: #FFFFFF;
    background: #00bcd4;
}

QMenu::separator {
    height: 1px;
    background: #00bcd4;
}

QProgressBar {
    border-radius: 5px;
    text-align: center;
    border: 1px solid #00bcd4;
}

QProgressBar::chunk {
    width: 5px;
    margin: 0.5px;
    background-color: #00bcd4;
}

QSlider::groove:horizontal,QSlider::add-page:horizontal {
    background: #D9D9D9;
    height: 8px;
    border-radius: 3px;
}

QSlider::sub-page:horizontal {
    height: 8px;
    border-radius: 3px;
    background: #00bcd4;
}

QSlider::handle:horizontal {
    width: 13px;
    margin-top: -3px;
    margin-bottom: -3px;
    border-radius: 6px;
    background: #00bcd4;
}

QSlider::handle:horizontal:hover {
    background: #0296ad;
}

QSlider::groove:vertical,QSlider::sub-page:vertical {
    background:#D9D9D9;
    width: 8px;
    border-radius: 3px;
}

QSlider::add-page:vertical {
    width: 8px;
    border-radius: 3px;
    background: #00bcd4;
}

QSlider::handle:vertical {
    height: 14px;
    margin-left: -3px;
    margin-right: -3px;
    border-radius: 6px;
    background: #00bcd4;
}

QSlider::handle:vertical:hover {
    background: #0296ad;
}

QScrollBar:vertical {
    width:10px;
    background-color:rgba(0,0,0,0);
    padding-top:10px;
    padding-bottom:10px;
}

QScrollBar:horizontal {
    height:10px;
    background-color:rgba(0,0,0,0);
    padding-left:10px;
    padding-right:10px;
}

QScrollBar::handle:vertical {
    width:10px;
    background: #00bcd4;
    border-radius:4px;
    min-height:50px;
}

QScrollBar::handle:horizontal {
    height:10px;
    background: #00bcd4;
    min-width:50px;
    border-radius:4px;
}

QScrollBar::handle:vertical:hover {
    width:10px;
    background: #0296ad;
}

QScrollBar::handle:horizontal:hover {
    height:10px;
    background: #0296ad;
}

QScrollBar::add-line:vertical {
    height:10px;
    width:10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/add-line_vertical.png);
}

QScrollBar::add-line:horizontal {
    height:10px;
    width:10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/add-line_horizontal.png);
}

QScrollBar::sub-line:vertical {
    height:10px;
    width:10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/sub-line_vertical.png);
}

QScrollBar::sub-line:horizontal {
    height:10px;
    width:10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/sub-line_horizontal.png);
}

QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {
    width:10px;
    background: #D9D9D9;
}

QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {
    height:10px;
    background: #D9D9D9;
}

QScrollArea {
    border: 0px ;
}

QTreeView,QListView,QTableView{
    border: 1px solid #00bcd4;
    selection-background-color: #00bcd4;
    outline:0px;
}

QTableView::item:selected, QListView::item:selected, QTreeView::item:selected {
    color: #000000;
    background: #a2fcf9;
}

QTableView::item:hover, QListView::item:hover, QTreeView::item:hover {
    color: #000000;
    background: #cafcf9;
}

QTableView::item, QListView::item, QTreeView::item {
    padding: 5px;
    margin: 0px;
}

QHeaderView::section {
    padding:3px;
    margin:0px;
    color:#FFFFFF;
    border: 1px solid #F0F0F0;
    background: #00bcd4;
}

QTabBar::tab{
    min-width: 80px;
    min-height: 25px;

    color:#000000;
    margin-right:1px;
    border: 1px solid #D9D9D9;
    border-left: none;
    border-right: none;
    border-top: none;
    background:#FFFFFF;
}

QTabBar::tab:selected,QTabBar::tab:hover{
    border-style:solid;
    border-color:#00bcd4;
}

QTabBar::tab:top,QTabBar::tab:bottom{
    padding:3px 8px 3px 8px;
}

QTabBar::tab:left,QTabBar::tab:right{
    padding:8px 3px 8px 3px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover{
    border-width:2px 0px 0px 0px;
}

QTabBar::tab:right:selected,QTabBar::tab:right:hover{
    border-width:0px 0px 0px 2px;
}

QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
    border-width:0px 0px 2px 0px;
}

QTabBar::tab:left:selected,QTabBar::tab:left:hover{
    border-width:0px 2px 0px 0px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover,QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
    border-left-width:1px;
    border-left-color:#D9D9D9;
    border-right-width:1px;
    border-right-color:#D9D9D9;
}

QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
    border-left-width:1px;
    border-left-color:#D9D9D9;
    border-right-width:1px;
    border-right-color:#D9D9D9;
}

QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
    border-top-width:1px;
    border-top-color:#D9D9D9;
    border-bottom-width:1px;
    border-bottom-color:#D9D9D9;
}

QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
    border-left-width:1px;
    border-left-color:#D9D9D9;
    border-right-width:1px;
    border-right-color:#D9D9D9;
}

QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
    border-top-width:1px;
    border-top-color:#D9D9D9;
    border-bottom-width:1px;
    border-bottom-color:#D9D9D9;
}

QStatusBar::item {
     border: 1px solid #00bcd4;
     border-radius: 3px;
}


#COLOR#;MAIN_COLOR=#22cb64;BTN_HOVER_COLOR=#47d679;BTN_PRESSED_COLOR=#13a34f;ITEM_HOVER_COLOR=#f1fcf3;ITEM_SELECTED_COLOR=#cdfcd9
/**********窗口样式*************/
QWidget#QSkinDemoClass,
QWidget#QSkinEditDialog,
QWidget#QMyMessageBox,
QWidget#QAboutDialog
{
    border:1px solid #22cb64;
    border-radius:0px;
    background: #FFFFFF;
}


.QFrame{
    border:1px solid #22cb64;
    border-radius:5px;
}

/***************标题栏*****************/
QWidget#widget_title{
    background: #22cb64;
}

QWidget#widget_title2{
    background: #22cb64;
}


/**********菜单栏窗口样式*************/
QWidget#widget_menu{
    /*background: #f1fcf3;*/
   /* border: 1px solid #22cb64;*/
    /*border-left: none;*/
    /*border-right: none;*/
}

/**********状态栏窗口样式*************/
QWidget#widget_status{
        background: #22cb64;
        border: 1px solid #22cb64;
        border-left: none;
        border-right: none;
        border-bottom: none;
}

QLabel#label_logo{
    image: url(:/Resources/logo.png);
}

QLabel#label_title{
    border-radius:0px;
    color: #FFFFFF;
    background-color:rgba(0,0,0,0);
    border-style:none;
}

QLabel#label_MessageType[MessageType="information"] {
        qproperty-pixmap: url(:/Skin/img/information);
}

QLabel#label_MessageType[MessageType="error"] {
        qproperty-pixmap: url(:/Skin/img/error);
}

QLabel#label_MessageType[MessageType="success"] {
        qproperty-pixmap: url(:/Skin/img/success);
}

QLabel#label_MessageType[MessageType="question"] {
        qproperty-pixmap: url(:/Skin/img/question);
}

QLabel#label_MessageType[MessageType="warning"] {
        qproperty-pixmap: url(:/Skin/img/warning);
}

/**********文本编辑框**********/
QTextEdit,QLineEdit {
    border: 1px solid #22cb64;
    border-radius: 5px;
    padding: 2px;
    background: none;
    selection-background-color: #22cb64;
}

QLineEdit[echoMode="2"] {
    lineedit-password-character: 9679;
}

.QGroupBox{
     border: 1px solid #22cb64;
     border-radius: 5px;
     margin-top: 3ex;/* leave space at the top for the title */
}
.QGroupBox::title {
      subcontrol-origin: margin;
     position: relative;
     left: 10px;
 }
 
 
.QPushButton{
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 5px;
    border-radius:5px;
    background: #22cb64;
}

.QPushButton[focusPolicy="0"] {
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 0px;
    border-radius:3px;
    background: #22cb64;
}

.QPushButton:hover{
    background: #47d679
}

.QPushButton:pressed{
    background: #13a34f;
}


.QToolButton{
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 4px;
    border-radius:5px;
    background: #22cb64;
}

.QToolButton[focusPolicy="0"] {
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 0px;
    border-radius:3px;
    background: #22cb64;
}

.QToolButton:hover{
    background: #47d679
}

.QToolButton:pressed{
    background: #13a34f;
}

.QToolButton[pageTab="true"] {
    border: none;
    padding-top:5px;
    background: none;
    color: #000000;
    border-radius:0px;
}

.QToolButton[pageTab="true"]:hover {
    background-color:#EEEEEE;
    border: none;
}

.QToolButton[pageTab="true"]:pressed {
    border: 4px solid #22cb64;
    border-top: none;
    border-right: none;
    border-bottom: none;
    background-color:#EEEEEE;
}
.QToolButton[pageTab="true"]:checked {
    border: 4px solid #22cb64;
    border-top: none;
    border-right: none;
    border-bottom: none;
    background-color:#EEEEEE;
}

.QToolButton[TopPageTab="true"] {
    border: none;
    padding-top:10px;
    color: #FFFFFF;
    background: none;
    border-radius:0px;
}

.QToolButton[TopPageTab="true"]:hover {
    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0%), stop:1 rgba(4, 20, 7, 10%));
    border: none;
    color: #FFFFFF;
}

.QToolButton[TopPageTab="true"]:pressed {
    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0%), stop:1 rgba(4, 20, 7, 10%));
    border: none;
    color: #FFFFFF;
}
.QToolButton[TopPageTab="true"]:checked {
    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0%), stop:1 rgba(4, 20, 7, 10%));
    border: none;
    color: #FFFFFF;
}

QPushButton#menuButton_Min,QPushButton#menuButton_Max,QPushButton#menuButton_Close{
    border-radius:0px;
    color: #FFFFFF;
    background-color:rgba(0,0,0,0);
    border-style:none;
}

QPushButton#menuButton_Min:hover,QPushButton#menuButton_Max:hover{
    background-color: #47d679;
}
QPushButton#menuButton_Min:pressed,QPushButton#menuButton_Max:pressed{
    background-color: #13a34f;
}
QPushButton#menuButton_Close:hover{
    background-color: #FF5439;
}
QPushButton#menuButton_Close:pressed{
    background-color: #E04A32;
}

QCheckBox {
    spacing: 2px;
}

QCheckBox::indicator, QTableView::indicator, QListView::indicator, QTreeView::indicator, QGroupBox::indicator {
    width: 20px;
    height: 20px;
}

QCheckBox::indicator:unchecked, QTableView::indicator:unchecked, QListView::indicator:unchecked, QTreeView::indicator:unchecked, QGroupBox::indicator:unchecked {

}

QCheckBox::indicator:checked, QTableView::indicator:checked, QListView::indicator:checked, QTreeView::indicator:checked, QGroupBox::indicator:checked {

}

QRadioButton {
    spacing: 2px;
}

QRadioButton::indicator {
    width: 15px;
    height: 15px;
}

QRadioButton::indicator::unchecked {
    image: url(:/Skin/img/radio_normal.png);
}

QRadioButton::indicator::checked {
    image: url(:/Skin/img/radio_selected.png);
}

QComboBox,QDateEdit,QDateTimeEdit,QTimeEdit,QDoubleSpinBox,QSpinBox{
    border-radius: 3px;
    padding: 1px 5px 1px 5px;
    border: 1px solid #22cb64;
    selection-background-color: #22cb64;
}

QComboBox::drop-down,QDateEdit::drop-down,QDateTimeEdit::drop-down,QTimeEdit::drop-down,QDoubleSpinBox::drop-down,QSpinBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 1px;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    border-left-color: #22cb64;
}

QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow {
    image: url(:/Skin/img/array_down.png);
    width:10px;
    height:9px;
}

QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
    image: url(:/Skin/img/array_up.png);
    width:10px;
    height:10px;
    padding:0px 3px 0px 0px;
}

QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
    image: url(:/Skin/img/array_down.png);
    width:10px;
    height:10px;
    padding:0px 3px 0px 0px;
}

/**********菜单栏**********/
QMenuBar {
        background: #f1fcf3;
        border: 1px solid #22cb64;
        border-left: none;
        border-right: none;
        border-top: none;
}
QMenuBar::item {
        border: 1px solid transparent;
        padding: 5px 10px 5px 10px;
        background: transparent;
}
QMenuBar::item:enabled {
        color: #000000;
}
QMenuBar::item:!enabled {
        color: rgb(155, 155, 155);
}
QMenuBar::item:enabled:selected {
        background: #cdfcd9;
}

QMenu {
    background-color:#FFFFFF;
    /*margin: 2px;*/
    border: 1px solid #22cb64;
}

QMenu::item {
    padding: 2px 20px 2px 20px;
}

QMenu::indicator {
    width: 13px;
    height: 13px;
}

QMenu::item:selected {
    color: #FFFFFF;
    background: #22cb64;
}

QMenu::separator {
    height: 1px;
    background: #22cb64;
}

QProgressBar {
    border-radius: 5px;
    text-align: center;
    border: 1px solid #22cb64;
}

QProgressBar::chunk {
    width: 5px;
    margin: 0.5px;
    background-color: #22cb64;
}

QSlider::groove:horizontal,QSlider::add-page:horizontal {
    background: #D9D9D9;
    height: 8px;
    border-radius: 3px;
}

QSlider::sub-page:horizontal {
    height: 8px;
    border-radius: 3px;
    background: #22cb64;
}

QSlider::handle:horizontal {
    width: 13px;
    margin-top: -3px;
    margin-bottom: -3px;
    border-radius: 6px;
    background: #22cb64;
}

QSlider::handle:horizontal:hover {
    background: #13a34f;
}

QSlider::groove:vertical,QSlider::sub-page:vertical {
    background:#D9D9D9;
    width: 8px;
    border-radius: 3px;
}

QSlider::add-page:vertical {
    width: 8px;
    border-radius: 3px;
    background: #22cb64;
}

QSlider::handle:vertical {
    height: 14px;
    margin-left: -3px;
    margin-right: -3px;
    border-radius: 6px;
    background: #22cb64;
}

QSlider::handle:vertical:hover {
    background: #13a34f;
}

QScrollBar:vertical {
    width:10px;
    background-color:rgba(0,0,0,0);
    padding-top:10px;
    padding-bottom:10px;
}

QScrollBar:horizontal {
    height:10px;
    background-color:rgba(0,0,0,0);
    padding-left:10px;
    padding-right:10px;
}

QScrollBar::handle:vertical {
    width:10px;
    background: #22cb64;
    border-radius:4px;
    min-height:50px;
}

QScrollBar::handle:horizontal {
    height:10px;
    background: #22cb64;
    min-width:50px;
    border-radius:4px;
}

QScrollBar::handle:vertical:hover {
    width:10px;
    background: #13a34f;
}

QScrollBar::handle:horizontal:hover {
    height:10px;
    background: #13a34f;
}

QScrollBar::add-line:vertical {
    height:10px;
    width:10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/add-line_vertical.png);
}

QScrollBar::add-line:horizontal {
    height:10px;
    width:10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/add-line_horizontal.png);
}

QScrollBar::sub-line:vertical {
    height:10px;
    width:10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/sub-line_vertical.png);
}

QScrollBar::sub-line:horizontal {
    height:10px;
    width:10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/sub-line_horizontal.png);
}

QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {
    width:10px;
    background: #D9D9D9;
}

QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {
    height:10px;
    background: #D9D9D9;
}

QScrollArea {
    border: 0px ;
}

QTreeView,QListView,QTableView{
    border: 1px solid #22cb64;
    selection-background-color: #22cb64;
    outline:0px;
}

QTableView::item:selected, QListView::item:selected, QTreeView::item:selected {
    color: #000000;
    background: #cdfcd9;
}

QTableView::item:hover, QListView::item:hover, QTreeView::item:hover {
    color: #000000;
    background: #f1fcf3;
}

QTableView::item, QListView::item, QTreeView::item {
    padding: 5px;
    margin: 0px;
}

QHeaderView::section {
    padding:3px;
    margin:0px;
    color:#FFFFFF;
    border: 1px solid #F0F0F0;
    background: #22cb64;
}

QTabBar::tab{
    min-width: 80px;
    min-height: 25px;

    color:#000000;
    margin-right:1px;
    border: 1px solid #D9D9D9;
    border-left: none;
    border-right: none;
    border-top: none;
    background:#FFFFFF;
}

QTabBar::tab:selected,QTabBar::tab:hover{
    border-style:solid;
    border-color:#22cb64;
}

QTabBar::tab:top,QTabBar::tab:bottom{
    padding:3px 8px 3px 8px;
}

QTabBar::tab:left,QTabBar::tab:right{
    padding:8px 3px 8px 3px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover{
    border-width:2px 0px 0px 0px;
}

QTabBar::tab:right:selected,QTabBar::tab:right:hover{
    border-width:0px 0px 0px 2px;
}

QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
    border-width:0px 0px 2px 0px;
}

QTabBar::tab:left:selected,QTabBar::tab:left:hover{
    border-width:0px 2px 0px 0px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover,QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
    border-left-width:1px;
    border-left-color:#D9D9D9;
    border-right-width:1px;
    border-right-color:#D9D9D9;
}

QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
    border-left-width:1px;
    border-left-color:#D9D9D9;
    border-right-width:1px;
    border-right-color:#D9D9D9;
}

QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
    border-top-width:1px;
    border-top-color:#D9D9D9;
    border-bottom-width:1px;
    border-bottom-color:#D9D9D9;
}

QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
    border-left-width:1px;
    border-left-color:#D9D9D9;
    border-right-width:1px;
    border-right-color:#D9D9D9;
}

QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
    border-top-width:1px;
    border-top-color:#D9D9D9;
    border-bottom-width:1px;
    border-bottom-color:#D9D9D9;
}

QStatusBar::item {
     border: 1px solid #22cb64;
     border-radius: 3px;
}

/*#COLOR#;MAIN_COLOR=#45b0c4;BTN_HOVER_COLOR=#6bc3ce;BTN_PRESSED_COLOR=#30889b;ITEM_HOVER_COLOR=#f1fcfc;ITEM_SELECTED_COLOR=#e9f4f4*/
/**********窗口样式*************/
QWidget#QSkinDemoClass,
QWidget#QSkinEditDialog,
QWidget#QMyMessageBox,
QWidget#QAboutDialog
{
    border:1px solid #45b0c4;
    border-radius:0px;
    background: #FFFFFF;
}


.QFrame{
    border:1px solid #45b0c4;
    border-radius:5px;
}

/***************标题栏*****************/
QWidget#widget_title{
    background: #45b0c4;
}

QWidget#widget_title2{
    background: #45b0c4;
}


/**********菜单栏窗口样式*************/
QWidget#widget_menu{
    /*background: #f1fcfc;*/
   /* border: 1px solid #45b0c4;*/
    /*border-left: none;*/
    /*border-right: none;*/
}

/**********状态栏窗口样式*************/
QWidget#widget_status{
        background: #45b0c4;
        border: 1px solid #45b0c4;
        border-left: none;
        border-right: none;
        border-bottom: none;
}

QLabel#label_logo{
    image: url(:/Resources/logo.png);
}

QLabel#label_title{
    border-radius:0px;
    color: #FFFFFF;
    background-color:rgba(0,0,0,0);
    border-style:none;
}

QLabel#label_MessageType[MessageType="information"] {
        qproperty-pixmap: url(:/Skin/img/information);
}

QLabel#label_MessageType[MessageType="error"] {
        qproperty-pixmap: url(:/Skin/img/error);
}

QLabel#label_MessageType[MessageType="success"] {
        qproperty-pixmap: url(:/Skin/img/success);
}

QLabel#label_MessageType[MessageType="question"] {
        qproperty-pixmap: url(:/Skin/img/question);
}

QLabel#label_MessageType[MessageType="warning"] {
        qproperty-pixmap: url(:/Skin/img/warning);
}

/**********文本编辑框**********/
QTextEdit,QLineEdit {
    border: 1px solid #45b0c4;
    border-radius: 5px;
    padding: 2px;
    background: none;
    selection-background-color: #45b0c4;
}

QLineEdit[echoMode="2"] {
    lineedit-password-character: 9679;
}

.QGroupBox{
     border: 1px solid #45b0c4;
     border-radius: 5px;
     margin-top: 3ex;/* leave space at the top for the title */
}
.QGroupBox::title {
      subcontrol-origin: margin;
     position: relative;
     left: 10px;
 }
 
.QPushButton{
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 5px;
    border-radius:5px;
    background: #45b0c4;
}

.QPushButton[focusPolicy="0"] {
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 0px;
    border-radius:3px;
    background: #45b0c4;
}

.QPushButton:hover{
    background: #6bc3ce
}

.QPushButton:pressed{
    background: #30889b;
}


.QToolButton{
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 4px;
    border-radius:5px;
    background: #45b0c4;
}

.QToolButton[focusPolicy="0"] {
    border-style: none;
    border: 0px;
    color: #FFFFFF;
    padding: 0px;
    border-radius:3px;
    background: #45b0c4;
}

.QToolButton:hover{
    background: #6bc3ce
}

.QToolButton:pressed{
    background: #30889b;
}

.QToolButton[pageTab="true"] {
    border: none;
    padding-top:5px;
    background: none;
    color: #000000;
    border-radius:0px;
}

.QToolButton[pageTab="true"]:hover {
    background-color:#EEEEEE;
    border: none;
}

.QToolButton[pageTab="true"]:pressed {
    border: 4px solid #45b0c4;
    border-top: none;
    border-right: none;
    border-bottom: none;
    background-color:#EEEEEE;
}
.QToolButton[pageTab="true"]:checked {
    border: 4px solid #45b0c4;
    border-top: none;
    border-right: none;
    border-bottom: none;
    background-color:#EEEEEE;
}

.QToolButton[TopPageTab="true"] {
    border: none;
    padding-top:10px;
    color: #FFFFFF;
    background: none;
    border-radius:0px;
}

.QToolButton[TopPageTab="true"]:hover {
    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0%), stop:1 rgba(4, 20, 7, 10%));
    border: none;
    color: #FFFFFF;
}

.QToolButton[TopPageTab="true"]:pressed {
    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0%), stop:1 rgba(4, 20, 7, 10%));
    border: none;
    color: #FFFFFF;
}
.QToolButton[TopPageTab="true"]:checked {
    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0%), stop:1 rgba(4, 20, 7, 10%));
    border: none;
    color: #FFFFFF;
}

QPushButton#menuButton_Min,QPushButton#menuButton_Max,QPushButton#menuButton_Close{
    border-radius:0px;
    color: #FFFFFF;
    background-color:rgba(0,0,0,0);
    border-style:none;
}

QPushButton#menuButton_Min:hover,QPushButton#menuButton_Max:hover{
    background-color: #6bc3ce;
}
QPushButton#menuButton_Min:pressed,QPushButton#menuButton_Max:pressed{
    background-color: #30889b;
}
QPushButton#menuButton_Close:hover{
    background-color: #FF5439;
}
QPushButton#menuButton_Close:pressed{
    background-color: #E04A32;
}

QCheckBox {
    spacing: 2px;
}

QCheckBox::indicator, QTableView::indicator, QListView::indicator, QTreeView::indicator, QGroupBox::indicator {
    width: 20px;
    height: 20px;
}

QCheckBox::indicator:unchecked, QTableView::indicator:unchecked, QListView::indicator:unchecked, QTreeView::indicator:unchecked, QGroupBox::indicator:unchecked {
    image: url(:/Skin/img/checkbox_unchecked.png);
}

QCheckBox::indicator:checked, QTableView::indicator:checked, QListView::indicator:checked, QTreeView::indicator:checked, QGroupBox::indicator:checked {
    image: url(:/Skin/img/checkbox_checked.png);
}

QRadioButton {
    spacing: 2px;
}

QRadioButton::indicator {
    width: 15px;
    height: 15px;
}

QRadioButton::indicator::unchecked {
    image: url(:/Skin/img/radio_normal.png);
}

QRadioButton::indicator::checked {
    image: url(:/Skin/img/radio_selected.png);
}

QComboBox,QDateEdit,QDateTimeEdit,QTimeEdit,QDoubleSpinBox,QSpinBox{
    border-radius: 3px;
    padding: 1px 5px 1px 5px;
    border: 1px solid #45b0c4;
    selection-background-color: #45b0c4;
}

QComboBox::drop-down,QDateEdit::drop-down,QDateTimeEdit::drop-down,QTimeEdit::drop-down,QDoubleSpinBox::drop-down,QSpinBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 1px;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    border-left-color: #45b0c4;
}

QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow {
    image: url(:/Skin/img/array_down.png);
    width:10px;
    height:9px;
}

QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
    image: url(:/Skin/img/array_up.png);
    width:10px;
    height:10px;
    padding:0px 3px 0px 0px;
}

QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
    image: url(:/Skin/img/array_down.png);
    width:10px;
    height:10px;
    padding:0px 3px 0px 0px;
}

/**********菜单栏**********/
QMenuBar {
        background: #f1fcfc;
        border: 1px solid #45b0c4;
        border-left: none;
        border-right: none;
        border-top: none;
}
QMenuBar::item {
        border: 1px solid transparent;
        padding: 5px 10px 5px 10px;
        background: transparent;
}
QMenuBar::item:enabled {
        color: #000000;
}
QMenuBar::item:!enabled {
        color: rgb(155, 155, 155);
}
QMenuBar::item:enabled:selected {
        background: #e9f4f4;
}

QMenu {
    background-color:#FFFFFF;
    /*margin: 2px;*/
    border: 1px solid #45b0c4;
}

QMenu::item {
    padding: 2px 20px 2px 20px;
}

QMenu::indicator {
    width: 13px;
    height: 13px;
}

QMenu::item:selected {
    color: #FFFFFF;
    background: #45b0c4;
}

QMenu::separator {
    height: 1px;
    background: #45b0c4;
}

QProgressBar {
    border-radius: 5px;
    text-align: center;
    border: 1px solid #45b0c4;
}

QProgressBar::chunk {
    width: 5px;
    margin: 0.5px;
    background-color: #45b0c4;
}

QSlider::groove:horizontal,QSlider::add-page:horizontal {
    background: #D9D9D9;
    height: 8px;
    border-radius: 3px;
}

QSlider::sub-page:horizontal {
    height: 8px;
    border-radius: 3px;
    background: #45b0c4;
}

QSlider::handle:horizontal {
    width: 13px;
    margin-top: -3px;
    margin-bottom: -3px;
    border-radius: 6px;
    background: #45b0c4;
}

QSlider::handle:horizontal:hover {
    background: #30889b;
}

QSlider::groove:vertical,QSlider::sub-page:vertical {
    background:#D9D9D9;
    width: 8px;
    border-radius: 3px;
}

QSlider::add-page:vertical {
    width: 8px;
    border-radius: 3px;
    background: #45b0c4;
}

QSlider::handle:vertical {
    height: 14px;
    margin-left: -3px;
    margin-right: -3px;
    border-radius: 6px;
    background: #45b0c4;
}

QSlider::handle:vertical:hover {
    background: #30889b;
}

QScrollBar:vertical {
    width:10px;
    background-color:rgba(0,0,0,0);
    padding-top:10px;
    padding-bottom:10px;
}

QScrollBar:horizontal {
    height:10px;
    background-color:rgba(0,0,0,0);
    padding-left:10px;
    padding-right:10px;
}

QScrollBar::handle:vertical {
    width:10px;
    background: #45b0c4;
    border-radius:4px;
    min-height:50px;
}

QScrollBar::handle:horizontal {
    height:10px;
    background: #45b0c4;
    min-width:50px;
    border-radius:4px;
}

QScrollBar::handle:vertical:hover {
    width:10px;
    background: #30889b;
}

QScrollBar::handle:horizontal:hover {
    height:10px;
    background: #30889b;
}

QScrollBar::add-line:vertical {
    height:10px;
    width:10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/add-line_vertical.png);
}

QScrollBar::add-line:horizontal {
    height:10px;
    width:10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/add-line_horizontal.png);
}

QScrollBar::sub-line:vertical {
    height:10px;
    width:10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/sub-line_vertical.png);
}

QScrollBar::sub-line:horizontal {
    height:10px;
    width:10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
    border-image:url(:/Skin/img/sub-line_horizontal.png);
}

QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {
    width:10px;
    background: #D9D9D9;
}

QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {
    height:10px;
    background: #D9D9D9;
}

QScrollArea {
    border: 0px ;
}

QTreeView,QListView,QTableView{
    border: 1px solid #45b0c4;
    selection-background-color: #45b0c4;
    outline:0px;
}

QTableView::item:selected, QListView::item:selected, QTreeView::item:selected {
    color: #000000;
    background: #e9f4f4;
}

QTableView::item:hover, QListView::item:hover, QTreeView::item:hover {
    color: #000000;
    background: #f1fcfc;
}

QTableView::item, QListView::item, QTreeView::item {
    padding: 5px;
    margin: 0px;
}

QHeaderView::section {
    padding:3px;
    margin:0px;
    color:#FFFFFF;
    border: 1px solid #F0F0F0;
    background: #45b0c4;
}

QTabBar::tab{
    min-width: 80px;
    min-height: 25px;

    color:#000000;
    margin-right:1px;
    border: 1px solid #D9D9D9;
    border-left: none;
    border-right: none;
    border-top: none;
    background:#FFFFFF;
}

QTabBar::tab:selected,QTabBar::tab:hover{
    border-style:solid;
    border-color:#45b0c4;
}

QTabBar::tab:top,QTabBar::tab:bottom{
    padding:3px 8px 3px 8px;
}

QTabBar::tab:left,QTabBar::tab:right{
    padding:8px 3px 8px 3px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover{
    border-width:2px 0px 0px 0px;
}

QTabBar::tab:right:selected,QTabBar::tab:right:hover{
    border-width:0px 0px 0px 2px;
}

QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
    border-width:0px 0px 2px 0px;
}

QTabBar::tab:left:selected,QTabBar::tab:left:hover{
    border-width:0px 2px 0px 0px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover,QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
    border-left-width:1px;
    border-left-color:#D9D9D9;
    border-right-width:1px;
    border-right-color:#D9D9D9;
}

QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
    border-left-width:1px;
    border-left-color:#D9D9D9;
    border-right-width:1px;
    border-right-color:#D9D9D9;
}

QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
    border-top-width:1px;
    border-top-color:#D9D9D9;
    border-bottom-width:1px;
    border-bottom-color:#D9D9D9;
}

QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
    border-left-width:1px;
    border-left-color:#D9D9D9;
    border-right-width:1px;
    border-right-color:#D9D9D9;
}

QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
    border-top-width:1px;
    border-top-color:#D9D9D9;
    border-bottom-width:1px;
    border-bottom-color:#D9D9D9;
}

QStatusBar::item {
     border: 1px solid #45b0c4;
     border-radius: 3px;
}



黑色
QPalette{background:#CFDDEE;}*{outline:0px;color:#324C6C;}

QWidget[form="true"],QLabel[frameShape="1"]{
border:1px solid #7F9AB8;
border-radius:0px;
}

QWidget[form="bottom"]{
background:#C0D3EB;
}

QWidget[form="bottom"] .QFrame{
border:1px solid #324C6C;
}

QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
border-radius:0px;
color:#324C6C;
background:none;
border-style:none;
}

QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
border-style:none;
border-radius:0px;
padding:5px;
color:#324C6C;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
}

QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
border-style:solid;
border-width:0px 0px 2px 0px;
padding:4px 4px 2px 4px;
border-color:#00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
}

QWidget[nav="left"] QAbstractButton{
border-radius:0px;
color:#324C6C;
background:none;
border-style:none;
}

QWidget[nav="left"] QAbstractButton:hover{
color:#FFFFFF;
background-color:#00BB9E;
}

QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
color:#324C6C;
border-style:solid;
border-width:0px 0px 0px 2px;
padding:4px 4px 4px 2px;
border-color:#00BB9E;
background-color:#CFDDEE;
}

QWidget[video="true"] QLabel{
color:#324C6C;
border:1px solid #7F9AB8;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
}

QWidget[video="true"] QLabel:focus{
border:1px solid #00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
border:1px solid #7F9AB8;
border-radius:3px;
padding:2px;
background:none;
selection-background-color:#C0D3EB;
selection-color:#324C6C;
}

QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
border:1px solid #7F9AB8;
}

QLineEdit[echoMode="2"]{
lineedit-password-character:9679;
}

.QFrame{
border:1px solid #7F9AB8;
border-radius:3px;
}

.QGroupBox{
border:1px solid #7F9AB8;
border-radius:5px;
margin-top:3ex;
}

.QGroupBox::title{
subcontrol-origin:margin;
position:relative;
left:10px;
}

.QPushButton,.QToolButton{
border-style:none;
border:1px solid #7F9AB8;
color:#324C6C;
padding:5px;
min-height:15px;
border-radius:5px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
}

.QPushButton:hover,.QToolButton:hover{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
}

.QPushButton:pressed,.QToolButton:pressed{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
}

.QToolButton::menu-indicator{
image:None;
}

QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
border-radius:3px;
color:#324C6C;
padding:3px;
margin:0px;
background:none;
border-style:none;
}

QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
color:#FFFFFF;
margin:1px 1px 2px 1px;
background-color:rgba(51,127,209,230);
}

QPushButton#btnMenu_Close:hover{
color:#FFFFFF;
margin:1px 1px 2px 1px;
background-color:rgba(238,0,0,128);
}

QRadioButton::indicator{
width:15px;
height:15px;
}

QRadioButton::indicator::unchecked{
image:url(:/qss/blue/radiobutton_unchecked.png);
}

QRadioButton::indicator::unchecked:disabled{
image:url(:/qss/blue/radiobutton_unchecked_disable.png);
}

QRadioButton::indicator::checked{
image:url(:/qss/blue/radiobutton_checked.png);
}

QRadioButton::indicator::checked:disabled{
image:url(:/qss/blue/radiobutton_checked_disable.png);
}

QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
padding:0px -3px 0px 3px;
}

QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
width:13px;
height:13px;
}

QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
image:url(:/qss/blue/checkbox_unchecked.png);
}

QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
image:url(:/qss/blue/checkbox_unchecked_disable.png);
}

QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
image:url(:/qss/blue/checkbox_checked.png);
}

QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
image:url(:/qss/blue/checkbox_checked_disable.png);
}

QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
image:url(:/qss/blue/checkbox_parcial.png);
}

QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
image:url(:/qss/blue/checkbox_parcial_disable.png);
}

QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
image:url(:/qss/blue/add_top.png);
width:10px;
height:10px;
padding:2px 5px 0px 0px;
}

QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
image:url(:/qss/blue/add_bottom.png);
width:10px;
height:10px;
padding:0px 5px 2px 0px;
}

QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
top:-2px;
}
  
QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
bottom:-2px;
}

QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
image:url(:/qss/blue/add_bottom.png);
width:10px;
height:10px;
right:2px;
}

QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
subcontrol-origin:padding;
subcontrol-position:top right;
width:15px;
border-left-width:0px;
border-left-style:solid;
border-top-right-radius:3px;
border-bottom-right-radius:3px;
border-left-color:#7F9AB8;
}

QComboBox::drop-down:on{
top:1px;
}

QMenuBar::item{
color:#324C6C;
background-color:#C0D3EB;
margin:0px;
padding:3px 10px;
}

QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
color:#324C6C;
background-color:#C0D3EB;
border:1px solid #7F9AB8;
margin:0px;
}

QMenu::item{
padding:3px 20px;
}

QMenu::indicator{
width:13px;
height:13px;
}

QMenu::item:selected,QMenuBar::item:selected{
color:#324C6C;
border:0px solid #7F9AB8;
background:#D2E3F5;
}

QMenu::separator{
height:1px;
background:#7F9AB8;
}

QProgressBar{
min-height:10px;
background:#C0D3EB;
border-radius:5px;
text-align:center;
border:1px solid #C0D3EB;
}

QProgressBar:chunk{
border-radius:5px;
background-color:#7F9AB8;
}

QSlider::groove:horizontal{
background:#C0D3EB;
height:8px;
border-radius:4px;
}

QSlider::add-page:horizontal{
background:#C0D3EB;
height:8px;
border-radius:4px;
}

QSlider::sub-page:horizontal{
background:#7F9AB8;
height:8px;
border-radius:4px;
}

QSlider::handle:horizontal{
width:13px;
margin-top:-3px;
margin-bottom:-3px;
border-radius:6px;
background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #CFDDEE,stop:0.8 #7F9AB8);
}

QSlider::groove:vertical{
width:8px;
border-radius:4px;
background:#C0D3EB;
}

QSlider::add-page:vertical{
width:8px;
border-radius:4px;
background:#C0D3EB;
}

QSlider::sub-page:vertical{
width:8px;
border-radius:4px;
background:#7F9AB8;
}

QSlider::handle:vertical{
height:14px;
margin-left:-3px;
margin-right:-3px;
border-radius:6px;
background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #CFDDEE,stop:0.8 #7F9AB8);
}

QScrollBar:horizontal{
background:#C0D3EB;
padding:0px;
border-radius:6px;
max-height:12px;
}

QScrollBar::handle:horizontal{
background:#CADDF3;
min-width:50px;
border-radius:6px;
}

QScrollBar::handle:horizontal:hover{
background:#7F9AB8;
}

QScrollBar::handle:horizontal:pressed{
background:#7F9AB8;
}

QScrollBar::add-page:horizontal{
background:none;
}

QScrollBar::sub-page:horizontal{
background:none;
}

QScrollBar::add-line:horizontal{
background:none;
}

QScrollBar::sub-line:horizontal{
background:none;
}

QScrollBar:vertical{
background:#C0D3EB;
padding:0px;
border-radius:6px;
max-width:12px;
}

QScrollBar::handle:vertical{
background:#CADDF3;
min-height:50px;
border-radius:6px;
}

QScrollBar::handle:vertical:hover{
background:#7F9AB8;
}

QScrollBar::handle:vertical:pressed{
background:#7F9AB8;
}

QScrollBar::add-page:vertical{
background:none;
}

QScrollBar::sub-page:vertical{
background:none;
}

QScrollBar::add-line:vertical{
background:none;
}

QScrollBar::sub-line:vertical{
background:none;
}

QScrollArea{
border:0px;
}

QTreeView,QListView,QTableView::pane{
border:1px solid #7F9AB8;
selection-background-color:#D2E3F5;
selection-color:#324C6C;
alternate-background-color:#CADDF3;
gridline-color:#7F9AB8;
}

QTabWidget{
border-width: 0px;
border-color:white;
border-style:outset;
border-radius: 3px;
background-color: rgb(132, 171, 208);
background: transparent;
}

QTreeView::branch:closed:has-children{
margin:4px;
border-image:url(:/qss/blue/branch_open.png);
}

QTreeView::branch:open:has-children{
margin:4px;
border-image:url(:/qss/blue/branch_close.png);
}

QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{
background:#CFDDEE;
}

QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{
color:#324C6C;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
}

QTableView::item:hover,QListView::item:hover,QTreeView::item:hover{
color:#324C6C;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
}

QTableView::item,QListView::item,QTreeView::item{
padding:1px;
margin:0px;
}

QHeaderView::section,QTableCornerButton:section{
padding:3px;
margin:0px;
color:#324C6C;
border:1px solid #7F9AB8;
border-left-width:0px;
border-right-width:1px;
border-top-width:0px;
border-bottom-width:1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
}

QTabBar::tab{
border:1px solid #7F9AB8;
color:#324C6C;
margin:0px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
}

QTabBar::tab:selected,QTabBar::tab:hover{
border-style:solid;
border-color:#00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
}

QTabBar::tab:top,QTabBar::tab:bottom{
padding:3px 8px 3px 8px;
}

QTabBar::tab:left,QTabBar::tab:right{
padding:8px 3px 8px 3px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover{
border-width:2px 0px 0px 0px;
}

QTabBar::tab:right:selected,QTabBar::tab:right:hover{
border-width:0px 0px 0px 2px;
}

QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
border-width:0px 0px 2px 0px;
}

QTabBar::tab:left:selected,QTabBar::tab:left:hover{
border-width:0px 2px 0px 0px;
}

QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
border-left-width:1px;
border-left-color:#7F9AB8;
}

QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
border-top-width:1px;
border-top-color:#7F9AB8;
}

QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
border-right-width:1px;
border-right-color:#7F9AB8;
}

QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
border-bottom-width:1px;
border-bottom-color:#7F9AB8;
}

QStatusBar::item{
border:0px solid #C0D3EB;
border-radius:3px;
}

QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
padding:3px;
border-radius:5px;
color:#324C6C;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
}

QToolTip{
border:0px solid #324C6C;
padding:1px;
color:#324C6C;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
}

QToolBox::tab:selected{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #D2E3F5,stop:1 #CADDF3);
}

QPrintPreviewDialog QToolButton{
border:0px solid #324C6C;
border-radius:0px;
margin:0px;
padding:3px;
background:none;
}

QColorDialog QPushButton,QFileDialog QPushButton{
min-width:80px;
}

QToolButton#qt_calendar_prevmonth{
icon-size:0px;
min-width:20px;
image:url(:/qss/blue/calendar_prevmonth.png);
}

QToolButton#qt_calendar_nextmonth{
icon-size:0px;
min-width:20px;
image:url(:/qss/blue/calendar_nextmonth.png);
}

QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
border:0px solid #324C6C;
border-radius:3px;
margin:3px 3px 3px 3px;
padding:3px;
background:none;
}

QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
border:1px solid #7F9AB8;
}

QCalendarWidget QSpinBox#qt_calendar_yearedit{
margin:2px;
}

QCalendarWidget QToolButton::menu-indicator{
image:None;
}

QCalendarWidget QTableView{
border-width:0px;
}

QCalendarWidget QWidget#qt_calendar_navigationbar{
border:1px solid #7F9AB8;
border-width:1px 1px 0px 1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #C0D3EB,stop:1 #BCCFE7);
}

QComboBox QAbstractItemView::item{
min-height:20px;
min-width:10px;
}

QTableView[model="true"]::item{
padding:0px;
margin:0px;
}

QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{
border-width:0px;
border-radius:0px;
}

QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{
border-width:0px;
border-radius:0px;
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
background:#CFDDEE;
}

*:disabled{
background:#CFDDEE;
border-color:#C0D3EB;
}

/*TextColor:#324C6C*/
/*PanelColor:#CFDDEE*/
/*BorderColor:#7F9AB8*/
/*NormalColorStart:#C0D3EB*/
/*NormalColorEnd:#BCCFE7*/
/*DarkColorStart:#D2E3F5*/
/*DarkColorEnd:#CADDF3*/
/*HighColor:#00BB9E*/
"""


def get(num):
    if num == 0:
        return qss
