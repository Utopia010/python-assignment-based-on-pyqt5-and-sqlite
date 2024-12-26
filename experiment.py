from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QLabel, QLineEdit, \
    QDialogButtonBox
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QRect, QPoint
from PyQt5.QtGui import QFont, QColor
import re
import sqlite3
import os


class Welcome(QWidget):
    def __init__(self, position: QRect = QRect(500, 500, 900, 600), parent: QWidget = None):
        super().__init__(parent)
        self.setGeometry(position)

        self.lable = QLabel("欢迎来到ATM模拟系统", self)
        self.font = QFont("Consolas")
        self.font.setPointSize(15)
        self.setFont(self.font)

        self.lable.setAlignment(Qt.AlignCenter)
        self.lable.setGeometry(QRect(0, 200, 900, 50))

        self.logButton = QPushButton("登录", self)
        self.logButton.setGeometry(200, 300, 200, 100)
        self.signButton = QPushButton("注册", self)
        self.signButton.setGeometry(500, 300, 200, 100)

    def connectLogButton(self, func):
        self.logButton.pressed.connect(func)

    def connectSignButton(self, func):
        self.signButton.pressed.connect(func)


class Log(QWidget):
    def __init__(self, position: QRect = QRect(500, 500, 900, 600), parent: QWidget = None):
        super().__init__(parent)
        self.setGeometry(position)
        self.font = QFont("Consolas")
        self.font.setPointSize(15)
        self.setFont(self.font)

        self.lableMain = QLabel("登录", self)
        self.lableMain.setGeometry(QRect(0, 100, 900, 50))
        self.lableMain.setAlignment(Qt.AlignCenter)
        self.font.setPointSize(20)
        self.lableMain.setFont(self.font)

        self.lableAccount = QLabel("输入账号", self)
        self.lableAccount.setGeometry(QRect(150, 200, 900, 50))
        self.lineEditAccount = QLineEdit(self)
        self.lineEditAccount.setGeometry(QRect(150, 250, 600, 50))

        self.lablePassWord = QLabel("输入密码", self)
        self.lablePassWord.setGeometry(QRect(150, 300, 900, 50))
        self.lineEditPassword = QLineEdit(self)
        self.lineEditPassword.setMaxLength(6)
        self.lineEditPassword.setGeometry(QRect(150, 350, 600, 50))
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.buttonIconPassword = QPushButton("+", self)
        self.buttonIconPassword.setGeometry(QRect(700, 350, 50, 50))

        self.enterButton = QPushButton("确认", self)
        self.enterButton.setGeometry(QRect(150, 450, 100, 50))
        self.signButton = QPushButton("注册", self)
        self.signButton.setGeometry(QRect(650, 450, 100, 50))

        self.buttonIconPassword.pressed.connect(self.swapIcon)
        self.enterButton.pressed.connect(self.checkAccoutPassword)
        self.signButton.pressed.connect(self.resetJumpSign)

    def resetJumpSign(self):
        self.isOKPassword = False
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.buttonIconPassword.setText('+')
        self.lineEditPassword.setText('')
        self.lineEditAccount.setText('')

        self.font.setPointSize(15)
        self.lableAccount.setFont(self.font)
        self.lableAccount.setStyleSheet(f'color: black;')
        self.lableAccount.setText("输入账号")
        self.lablePassWord.setFont((self.font))
        self.lablePassWord.setStyleSheet(f'color: black;')
        self.lablePassWord.setText("输入密码")

    def resetEnter(self):
        if self.isOKPassword:
            self.isOKPassword = False
            self.lineEditPassword.setEchoMode(QLineEdit.Password)
            self.buttonIconPassword.setText('+')
            self.lineEditPassword.setText('')
            self.lineEditAccount.setText('')

            self.font.setPointSize(15)
            self.lableAccount.setFont(self.font)
            self.lableAccount.setStyleSheet(f'color: black;')
            self.lableAccount.setText("输入账号")
            self.lablePassWord.setFont((self.font))
            self.lablePassWord.setStyleSheet(f'color: black;')
            self.lablePassWord.setText("输入密码")

    def connectEnterButton(self, func):
        self.enterButton.pressed.connect(func)

    def connectSignButton(self, func):
        self.signButton.pressed.connect(func)

    def swapIcon(self):
        if self.buttonIconPassword.text() == '+':
            self.buttonIconPassword.setText('-')
            self.lineEditPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.buttonIconPassword.setText('+')
            self.lineEditPassword.setEchoMode(QLineEdit.Password)

    def checkAccoutPassword(self):
        self.isOKPassword: bool = True
        self.font.setPointSize(15)
        self.lableAccount.setFont(self.font)
        self.lableAccount.setStyleSheet(f'color: black;')
        self.lableAccount.setText("输入账号")
        self.lablePassWord.setStyleSheet(f'color: black;')
        self.lablePassWord.setText("输入密码")

        if len(self.lineEditAccount.text()) == 0:
            self.lableAccount.setFont(self.font)
            self.lableAccount.setText("账号不能为空")
            self.lableAccount.setStyleSheet(f'color: red;')
            self.isOKPassword = False

        if bool(re.search('[^a-zA-Z0-9]', self.lineEditAccount.text())):
            self.lableAccount.setFont(self.font)
            self.lableAccount.setText("账户名只能由数字与字母构成")
            self.lableAccount.setStyleSheet(f'color: red;')
            self.isOKPassword = False

        if bool(re.search('[^a-zA-Z0-9]', self.lineEditPassword.text())):
            self.lablePassWord.setFont(self.font)
            self.lablePassWord.setText("密码只能由数字与字母构成")
            self.lablePassWord.setStyleSheet(f'color: red;')
            self.isOKPassword = False

        if len(self.lineEditPassword.text()) != 6:
            self.lablePassWord.setFont(self.font)
            self.lablePassWord.setText("密码需要六位")
            self.lablePassWord.setStyleSheet(f'color: red;')
            self.isOKPassword = False
        print(self.isOKPassword)


def getData(self):
    pass


class Sign(QWidget):
    def __init__(self, position: QRect = QRect(500, 500, 900, 600), parent: QWidget = None):
        super().__init__(parent)
        self.setGeometry(position)
        self.font = QFont("Consolas")
        self.font.setPointSize(15)
        self.setFont(self.font)

        self.isOKPassword: bool = False

        self.lableMain = QLabel("注册", self)
        self.lableMain.setGeometry(QRect(0, 100, 900, 50))
        self.lableMain.setAlignment(Qt.AlignCenter)
        self.font.setPointSize(20)
        self.lableMain.setFont(self.font)

        self.lableAccount = QLabel("输入账号", self)
        self.lableAccount.setGeometry(QRect(150, 150, 900, 50))
        self.lineEditAccount = QLineEdit(self)
        self.lineEditAccount.setGeometry(QRect(150, 200, 600, 50))

        self.lablePassWord = QLabel("输入密码", self)
        self.lablePassWord.setGeometry(QRect(150, 250, 900, 50))
        self.lineEditPassword = QLineEdit(self)
        self.lineEditPassword.setMaxLength(6)
        self.lineEditPassword.setGeometry(QRect(150, 300, 600, 50))
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.buttonIconPassword = QPushButton("+", self)
        self.buttonIconPassword.setGeometry(QRect(700, 300, 50, 50))

        self.lableEnsurePassWord = QLabel("确认密码", self)
        self.lableEnsurePassWord.setGeometry(QRect(150, 350, 900, 50))
        self.lineEditEnsurePassword = QLineEdit(self)
        self.lineEditEnsurePassword.setMaxLength(6)
        self.lineEditEnsurePassword.setGeometry(QRect(150, 400, 600, 50))
        self.lineEditEnsurePassword.setEchoMode(QLineEdit.Password)
        self.buttonIconEnsurePassword = QPushButton("+", self)
        self.buttonIconEnsurePassword.setGeometry(QRect(700, 400, 50, 50))

        self.enterButton = QPushButton("确认", self)
        self.enterButton.setGeometry(QRect(150, 500, 100, 50))
        self.logButton = QPushButton("登录", self)
        self.logButton.setGeometry(QRect(650, 500, 100, 50))

        self.buttonIconPassword.clicked.connect(self.swapIcon)
        self.buttonIconEnsurePassword.clicked.connect(self.swapIconEnsure)
        self.logButton.pressed.connect(self.resetLog)

    def resetEnter(self):
        if self.isOKPassword:
            self.isOKPassword = False
            self.lineEditPassword.setEchoMode(QLineEdit.Password)
            self.buttonIconPassword.setText('+')
            self.lineEditPassword.setText('')
            self.lineEditEnsurePassword.setEchoMode(QLineEdit.Password)
            self.buttonIconEnsurePassword.setText('+')
            self.lineEditEnsurePassword.setText('')
            self.lineEditAccount.setText('')

            self.font.setPointSize(15)
            self.lableAccount.setFont(self.font)
            self.lableAccount.setText("输入账号")
            self.lableAccount.setStyleSheet(f'color: black;')
            self.lableEnsurePassWord.setFont(self.font)
            self.lableEnsurePassWord.setText("确认密码")
            self.lableEnsurePassWord.setStyleSheet(f'color: black;')

    def resetLog(self):
        self.isOKPassword = False
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.buttonIconPassword.setText('+')
        self.lineEditPassword.setText('')
        self.lineEditEnsurePassword.setEchoMode(QLineEdit.Password)
        self.buttonIconEnsurePassword.setText('+')
        self.lineEditEnsurePassword.setText('')
        self.lineEditAccount.setText('')

        self.font.setPointSize(15)
        self.lableAccount.setFont(self.font)
        self.lableAccount.setText("输入账号")
        self.lableAccount.setStyleSheet(f'color: black;')
        self.lableEnsurePassWord.setFont(self.font)
        self.lableEnsurePassWord.setText("确认密码")
        self.lableEnsurePassWord.setStyleSheet(f'color: black;')

    def checkAccountPassword(self, data: list):
        self.isOKPassword = True
        self.font.setPointSize(15)
        self.lableAccount.setFont(self.font)
        self.lableAccount.setText("输入账号")
        self.lableAccount.setStyleSheet(f'color: black;')
        self.lableEnsurePassWord.setText("确认密码")
        self.lableEnsurePassWord.setStyleSheet(f'color: black;')

        if len(self.lineEditAccount.text()) == 0:
            self.lableAccount.setFont(self.font)
            self.lableAccount.setText("账号不能为空")
            self.lableAccount.setStyleSheet(f'color: red;')
            self.isOKPassword = False

        if bool(re.search('[^a-zA-Z0-9]', self.lineEditAccount.text())):
            self.lableAccount.setFont(self.font)
            self.lableAccount.setText("账户名只能由数字与字母构成")
            self.lableAccount.setStyleSheet(f'color: red;')
            self.isOKPassword = False

        if bool(re.search('[^a-zA-Z0-9]', self.lineEditPassword.text())):
            self.lableEnsurePassWord.setFont(self.font)
            self.lableEnsurePassWord.setText("密码只能由数字与字母构成")
            self.lableEnsurePassWord.setStyleSheet(f'color: red;')
            self.isOKPassword = False

        if len(self.lineEditPassword.text()) != 6:
            self.lableEnsurePassWord.setFont(self.font)
            self.lableEnsurePassWord.setText("密码需要六位")
            self.lableEnsurePassWord.setStyleSheet(f'color: red;')
            self.isOKPassword = False

        if self.lineEditPassword.text() != self.lineEditEnsurePassword.text():
            self.lableEnsurePassWord.setFont(self.font)
            self.lableEnsurePassWord.setText("前后密码不一样")
            self.lableEnsurePassWord.setStyleSheet(f'color: red;')
            self.isOKPassword = False

        for account in data:
            if account[1] == self.lineEditAccount.text():
                self.lableAccount.setFont(self.font)
                self.lableAccount.setText("账号已存在")
                self.lableAccount.setStyleSheet(f'color: red;')
                self.isOKPassword = False

    def connectEnterButton(self, func):
        self.enterButton.pressed.connect(func)

    def connectLogButton(self, func):
        self.logButton.pressed.connect(func)

    def swapIcon(self):
        if self.buttonIconPassword.text() == '+':
            self.buttonIconPassword.setText('-')
            self.lineEditPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.buttonIconPassword.setText('+')
            self.lineEditPassword.setEchoMode(QLineEdit.Password)

    def swapIconEnsure(self):
        if self.buttonIconEnsurePassword.text() == '+':
            self.buttonIconEnsurePassword.setText('-')
            self.lineEditEnsurePassword.setEchoMode(QLineEdit.Normal)
        else:
            self.buttonIconEnsurePassword.setText('+')
            self.lineEditEnsurePassword.setEchoMode(QLineEdit.Password)


def jumpInto(last: QWidget, next: QWidget, is_jump: bool = True):
    if is_jump:
        last.hide()
        next.show()


class Withdraw(QWidget):
    def __init__(self, position: QRect = QRect(500, 500, 900, 600), parent: QWidget = None):
        super().__init__(parent)
        self.setGeometry(position)
        self.font = QFont("Consolas")
        self.font.setPointSize(15)
        self.setFont(self.font)
        self.withdrawButton = list()
        self.currentMoneyIndex: int = -1

        self.titleWithdraw = QLabel("取款", self)
        self.font.setPointSize(20)
        self.titleWithdraw.setFont(self.font)
        self.titleWithdraw.setGeometry(QRect(0, 100, 900, 50))
        self.titleWithdraw.setAlignment(Qt.AlignCenter)
        self.withdrawButton.append(QPushButton("100", self))
        self.withdrawButton[0].setGeometry(QRect(50, 200, 200, 100))
        self.withdrawButton.append(QPushButton("200", self))
        self.withdrawButton[1].setGeometry(QRect(350, 200, 200, 100))
        self.withdrawButton.append(QPushButton("500", self))
        self.withdrawButton[2].setGeometry(QRect(650, 200, 200, 100))
        self.withdrawButton.append(QPushButton("1000", self))
        self.withdrawButton[3].setGeometry(QRect(50, 300, 200, 100))
        self.withdrawButton.append(QPushButton("2000", self))
        self.withdrawButton[4].setGeometry(QRect(350, 300, 200, 100))
        self.withdrawButton.append(QPushButton("5000", self))
        self.withdrawButton[5].setGeometry(QRect(650, 300, 200, 100))

        self.withdrawButton[0].pressed.connect(lambda: self.changeColor(0))
        self.withdrawButton[1].pressed.connect(lambda: self.changeColor(1))
        self.withdrawButton[2].pressed.connect(lambda: self.changeColor(2))
        self.withdrawButton[3].pressed.connect(lambda: self.changeColor(3))
        self.withdrawButton[4].pressed.connect(lambda: self.changeColor(4))
        self.withdrawButton[5].pressed.connect(lambda: self.changeColor(5))

        self.enterButton = QPushButton("确认", self)
        self.enterButton.setGeometry(QRect(150, 450, 200, 100))
        self.backButton = QPushButton("返回", self)
        self.backButton.setGeometry(QRect(550, 450, 200, 100))

        self.backButton.pressed.connect(self.resetBackButton)

    def reserEnterButton(self):
        self.font.setPointSize(15)
        self.titleWithdraw.setFont(self.font)
        self.titleWithdraw.setText("取款成功")
        self.titleWithdraw.setStyleSheet(f'color: black;')

        self.currentMoneyIndex = -1
        for i in range(0, 6):
            self.withdrawButton[i].setStyleSheet("background-color: white")
            self.withdrawButton[i].setFont(self.font)

    def resetBackButton(self):
        self.titleWithdraw.setText("取款")
        self.font.setPointSize(20)
        self.titleWithdraw.setFont(self.font)
        self.titleWithdraw.setStyleSheet(f"color: black")
        self.currentMoneyIndex = -1

        self.font.setPointSize(15)
        for i in range(0, 6):
            self.withdrawButton[i].setStyleSheet("background-color: white")
            self.withdrawButton[i].setFont(self.font)

    def changeColor(self, index: int):
        self.font.setPointSize(15)
        for i in range(0, 6):
            self.withdrawButton[i].setStyleSheet("background-color: white")
            self.withdrawButton[i].setFont(self.font)
        self.withdrawButton[index].setStyleSheet("background-color: yellow")
        self.currentMoneyIndex = index

    def connectMoneyButtons(self, func):
        for i in range(0, 5):
            self.withdrawButton[i].pressed.connect(func)

    def connectBackButton(self, func):
        self.backButton.pressed.connect(func)

    def connectEnterButton(self, func):
        self.enterButton.pressed.connect(func)


class Deposit(QWidget):
    def __init__(self, position: QRect = QRect(500, 500, 900, 600), parent: QWidget = None):
        super().__init__(parent)
        self.setGeometry(position)
        self.font = QFont("Consolas")
        self.font.setPointSize(15)
        self.setFont(self.font)

        self.titleDeposit = QLabel("存款", self)
        self.titleDeposit.setGeometry(QRect(0, 100, 900, 50))
        self.font.setPointSize(20)
        self.titleDeposit.setFont(self.font)
        self.font.setPointSize(15)
        self.titleDeposit.setAlignment(Qt.AlignCenter)

        self.lableDepositAmount = QLabel("输入存款金额", self)
        self.lableDepositAmount.setAlignment(Qt.AlignCenter)
        self.lableDepositAmount.setGeometry(QRect(150, 200, 600, 50))
        self.lineEditDeposit = QLineEdit(self)
        self.lineEditDeposit.setGeometry(QRect(150, 300, 600, 50))
        self.lineEditDeposit.setMaxLength(9)

        self.enterButton = QPushButton("确定", self)
        self.enterButton.setGeometry(QRect(150, 450, 200, 100))
        self.backButton = QPushButton("返回", self)
        self.backButton.setGeometry(QRect(650, 450, 200, 100))

        self.backButton.pressed.connect(self.resetBack)
        self.enterButton.pressed.connect(self.checkLineEdit)

        self.isOk: bool = False

    def resetBack(self):
        self.lineEditDeposit.setText('')
        self.lableDepositAmount.setFont(self.font)
        self.lableDepositAmount.setText("输入存款金额")
        self.lableDepositAmount.setStyleSheet("color: black")
        self.isOk = False

    def checkLineEdit(self):
        self.isOk = True
        self.lableDepositAmount.setText("输入存款金额")
        self.lableDepositAmount.setStyleSheet("color: black")
        self.lableDepositAmount.setFont(self.font)
        if bool(re.search("[^0123456789]", self.lineEditDeposit.text())):
            self.lableDepositAmount.setText("不要输入非数字")
            self.lableDepositAmount.setStyleSheet("color: red")
            self.lableDepositAmount.setFont(self.font)
            self.isOk = False
        if self.isOk:
            self.lableDepositAmount.setText("存款成功")
            self.lableDepositAmount.setStyleSheet("color: black")
            self.lableDepositAmount.setFont(self.font)

    def connectEnterButton(self, func):
        self.enterButton.pressed.connect(func)

    def connectBackButton(self, func):
        self.backButton.pressed.connect(func)


class MainContrl(QWidget):
    def __init__(self):
        super().__init__()
        self.m_filename: str = "example.db"
        if not os.path.exists(self.m_filename):
            self.m_connection = sqlite3.connect(self.m_filename)
            self.m_cursor = self.m_connection.cursor()
            self.create_table()
            self.m_columns = list[
                ('id', 'INTEGER', 0),
                ('account', 'TEXT', 0),
                ('password', 'TEXT', 0),
                ('saving', 'INTEGER', 0),
            ]
            self.data = list()


        self.m_connection = sqlite3.connect(self.m_filename)
        self.m_cursor = self.m_connection.cursor()
        self.m_columns = list()
        self.m_columnsData = self.get_table_info()
        self.m_cursor.execute(f"SELECT * FROM users")
        self.data: list = self.m_cursor.fetchall()
        self.lenData = len(self.data)
        if len(self.m_columnsData):
            for value in self.m_columnsData:
                self.m_columns.append(tuple([value[1], value[2], value[4]]))
            del self.m_columns[0]


        self.currentAccout = dict()
        self.newAccount = dict()
        self.toAccout = dict()
        self.changeMoney: int = 0
        self.isEnoughSaving: bool = False

    def reloadLib(self):
        self.m_cursor.execute(f"SELECT * FROM users")
        self.data: list = self.m_cursor.fetchall()

    def createNewAccount(self, account: str, password: str, saving, is_add: bool = True):
        if is_add:
            self.newAccount["account"] = account
            self.newAccount["password"] = password
            self.newAccount["saving"] = saving
        self.commitData()
        self.reloadLib()

    def updataCurrentAccount(self, account: str, password: str, saving, is_add: bool = True):
        if is_add:
            self.currentAccout["account"] = account
            self.currentAccout["password"] = password
            self.currentAccout["saving"] = saving

    def updateCurrentAccountDeposit(self, isOk: bool = True):
        if len(self.currentAccout) and self.changeMoney != 0 and isOk:
            self.currentAccout["saving"] = self.currentAccout["saving"] + self.changeMoney
            self.changeMoney = 0
        self.commitData()

    def updateTransferMoney(self, isOk: bool = True):
        if len(self.currentAccout) and len(self.toAccout) and self.changeMoney != 0 and isOk:
            self.currentAccout["saving"]=self.currentAccout["saving"]-self.changeMoney
            self.toAccout["saving"]= self.toAccout["saving"]+self.changeMoney
            self.commitData()


    def updateCurrentWithdrawMoney(self):
        if len(self.currentAccout) and self.changeMoney != 0 and self.isEnoughSaving:
            self.currentAccout["saving"] = self.currentAccout["saving"] - self.changeMoney
            self.changeMoney = 0
        self.commitData()

    def commitData(self):
        if len(self.currentAccout):
            for index, value in enumerate(self.data):
                if value[1] == self.currentAccout["account"]:
                    self.data[index] = tuple([index + 1, self.currentAccout["account"],
                                              self.currentAccout["password"], self.currentAccout["saving"]])
        if len(self.toAccout):
            for index, value in enumerate(self.data):
                if value[1] == self.toAccout["account"]:
                    self.data[index] = tuple([index + 1, self.toAccout["account"],
                                              self.toAccout["password"], self.toAccout["saving"]])
        for data in self.data:
            self.m_cursor.execute(f'''UPDATE users
                    SET saving = {data[3]}
                    WHERE  id ={data[0]}''')
        if len(self.newAccount):
            self.insert_data([(self.newAccount["account"], self.newAccount["password"], self.newAccount["saving"])])

        self.m_connection.commit()

    def setWithDrawChangeMoney(self, index: int = -1):
        match index:
            case 0:
                self.changeMoney = 100
            case 1:
                self.changeMoney = 200
            case 2:
                self.changeMoney = 500
            case 3:
                self.changeMoney = 1000
            case 4:
                self.changeMoney = 2000
            case 5:
                self.changeMoney = 5000

    def setDepositChangeMoney(self, deposit: Deposit):
        if deposit.isOk:
            self.changeMoney = int(deposit.lineEditDeposit.text())
            deposit.lineEditDeposit.setText('')

    def checkAccountPassword(self, account: str, password: str, log: Log):
        if not log.isOKPassword:
            return
        log.isOKPassword = False
        for data in self.data:
            if data[1] == account and data[2] == password:
                self.currentAccout["account"] = account
                self.currentAccout["password"] = password
                self.currentAccout["saving"] = data[3]
                print(self.currentAccout)
                log.isOKPassword = True
                break

        if not log.isOKPassword:
            log.lableAccount.setFont(log.font)
            log.lableAccount.setText("账号密码错误")
            log.lableAccount.setStyleSheet(f'color: red;')

    def checkAccout(self, account: str):
        for data in self.data:
            if data[1] == account:
                self.toAccout["account"] = data[1]
                self.toAccout["password"] = data[2]
                self.toAccout["saving"] = data[3]
                return

    def create_table(self, name_table: str = "users"):
        self.m_cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name_table} 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
            account TEXT,
            password TEXT,
            saving INTEGER )''')

    def append_cloumn(self, name_cloumn: str, type_cloumn: str, default_value: str = "NULL",
                      name_table: str = "users", ):
        self.m_columns.append(tuple([name_cloumn, type_cloumn, default_value]))
        self.m_cursor.execute(f'''ALTER TABLE {name_table} ADD COLUMN 
            {name_cloumn} {type_cloumn} DEFAULT {default_value}''')

    def insert_data(self, data: list, name_table: str = "users", ):
        names = ", ".join([element[0] for element in self.m_columns])
        placeholders = ", ".join(["?" for element in self.m_columns])
        for element in data:
            if not self.check_type(element): return
            self.m_cursor.execute(f"INSERT INTO {name_table} ({names}) VALUES ({placeholders})", element)

    def type_transform(self, type_str: str):
        match type_str:
            case "INTEGER":
                return type(1)
            case "TEXT":
                return type("")
            case "REAL":
                return type(1.0)
            case "NULL":
                return type(None)

    def check_type(self, data: tuple) -> bool:
        if len(data) != len(self.m_columns):
            print("Error: The number of data is not equal to the number of columns")
            return False
        else:
            list1 = [self.type_transform(element[1]) for element in self.m_columns]
            list2 = [type(element) for element in data]
            if list1 != list2:
                print("Error: The type of data is not equal to the type of columns")
                return False
            return True

    def get_all_data(self, name_table: str = "users"):
        self.m_cursor.execute(f"SELECT * FROM {name_table}")
        return self.m_cursor.fetchall()

    def get_data_cloumn(self, name_cloumn: str, name_table: str = "users"):
        self.m_cursor.execute(f"SELECT {name_cloumn} FROM {name_table}")
        return self.m_cursor.fetchall()

    def get_table_info(self, name_table: str = "users"):
        self.m_cursor.execute(f"PRAGMA table_info({name_table});")
        return self.m_cursor.fetchall()

    def checkSaving(self, withdraw: Withdraw):
        if withdraw.currentMoneyIndex == -1:
            withdraw.font.setPointSize(15)
            withdraw.titleWithdraw.setFont(withdraw.font)
            withdraw.titleWithdraw.setText("未选择取款数目")
            withdraw.titleWithdraw.setStyleSheet(f'color: red;')
            self.isEnoughSaving = False
            return
        self.setWithDrawChangeMoney(withdraw.currentMoneyIndex)
        if self.currentAccout["saving"] < self.changeMoney:
            withdraw.font.setPointSize(15)
            withdraw.titleWithdraw.setFont(withdraw.font)
            withdraw.titleWithdraw.setText("余额不足")
            withdraw.titleWithdraw.setStyleSheet(f'color: red;')
            self.changeMoney = 0
            self.isEnoughSaving = False
            return

        withdraw.reserEnterButton()

        self.isEnoughSaving = True

        self.updateCurrentWithdrawMoney()

    def clearAllData(self):
        self.currentAccout.clear()
        self.changeMoney = 0
        self.newAccount.clear()
        self.toAccout.clear()
        self.isEnoughSaving = False

    def __del__(self):
        self.commitData()
        self.m_cursor.close()
        self.m_connection.close()


class Operate(QWidget):
    def __init__(self, position: QRect = QRect(500, 500, 900, 600), parent: QWidget = None):
        super().__init__(parent)
        self.setGeometry(position)
        self.font = QFont("Consolas")
        self.font.setPointSize(15)
        self.setFont(self.font)

        self.buttonWithdraw = QPushButton("取钱", self)
        self.buttonWithdraw.setGeometry(QRect(50, 150, 200, 100))
        self.depositButton = QPushButton("存钱", self)
        self.depositButton.setGeometry(QRect(350, 150, 200, 100))
        self.transferButton = QPushButton("转账", self)
        self.transferButton.setGeometry(QRect(650, 150, 200, 100))
        self.savingButton = QPushButton("余额", self)
        self.savingButton.setGeometry(QRect(50, 350, 200, 100))
        self.exitButton = QPushButton("退出", self)
        self.exitButton.setGeometry(QRect(650, 350, 200, 100))

    def connectExitButton(self, func):
        self.exitButton.pressed.connect(func)

    def connectExitButton(self, func):
        self.exitButton.pressed.connect(func)

    def connectRestButton(self, func):
        self.savingButton.pressed.connect(func)

    def connectDeposit(self, func):
        self.depositButton.pressed.connect(func)

    def connectWithdraw(self, func):
        self.buttonWithdraw.pressed.connect(func)

    def connectTransfer(self, func):
        self.transferButton.pressed.connect(func)

    def connectExit(self, func):
        self.exitButton.pressed.connect(func)

    def resetAccountData(self, mainContrl: MainContrl):
        mainContrl.currentAccout.clear()
        mainContrl.toAccout.clear()
        mainContrl.changeMoney = 0


class Rest(QWidget):
    def __init__(self, position: QRect = QRect(500, 500, 900, 600), parent: QWidget = None):
        super().__init__(parent)
        self.setGeometry(position)
        self.font = QFont("Consolas")
        self.font.setPointSize(20)
        self.setFont(self.font)

        self.lableAccountInfor = QLabel(self)
        self.lableAccountInfor.setGeometry(QRect(0, 200, 900, 50))
        self.lableAccountInfor.setAlignment(Qt.AlignCenter)
        self.lableRestMoney = QLabel(self)
        self.lableRestMoney.setGeometry(QRect(0, 300, 900, 50))
        self.lableRestMoney.setAlignment(Qt.AlignCenter)

        self.backButton = QPushButton("返回", self)
        self.backButton.setGeometry(QRect(350, 450, 200, 100))

    def connectMain(self, main: MainContrl):
        self.lableAccountInfor.setText("账号：" + main.currentAccout["account"])
        self.lableRestMoney.setText("余额" + str(main.currentAccout["saving"]))

    def connectBackButton(self, func):
        self.backButton.pressed.connect(func)


class Transfer(QWidget):
    def __init__(self, position: QRect = QRect(500, 500, 900, 600), parent: QWidget = None):
        super().__init__(parent)
        self.setGeometry(position)
        self.font = QFont("Consolas")
        self.font.setPointSize(15)
        self.setFont(self.font)

        self.title = QLabel("转账", self)
        self.title.setGeometry(QRect(300, 100, 300, 50))
        self.title.setAlignment(Qt.AlignHCenter)
        self.font.setPointSize(20)
        self.title.setFont(self.font)
        self.font.setPointSize(15)

        self.lableAccount = QLabel("输入转账的账户", self)
        self.lableAccount.setGeometry(QRect(150, 200, 600, 50))
        self.lineEditAccount = QLineEdit(self)
        self.lineEditAccount.setGeometry(QRect(150, 250, 600, 50))

        self.lableMoney = QLabel("输入转账金额", self)
        self.lableMoney.setGeometry(QRect(150, 300, 600, 50))
        self.lineEditMoney = QLineEdit(self)
        self.lineEditMoney.setGeometry(QRect(150, 350, 600, 50))

        self.enterButton = QPushButton("确认", self)
        self.enterButton.setGeometry(QRect(150, 450, 200, 100))
        self.backButton = QPushButton("返回", self)
        self.backButton.setGeometry(QRect(650, 450, 200, 100))

        self.backButton.pressed.connect(self.resetBack)
        self.enterButton.pressed.connect(self.checkInput)

        self.isOk: bool = False

    def connectEnter(self, func):
        self.enterButton.pressed.connect(func)

    def connectBack(self, func):
        self.backButton.pressed.connect(func)

    def resetEnter(self):
        if self.isOk:
            self.isOk = False
            self.lableMoney.setFont(self.font)
            self.lableMoney.setStyleSheet("color: black")
            self.lableMoney.setText("输入转账金额")
            self.lableAccount.setFont(self.font)
            self.lableAccount.setStyleSheet("color: black")
            self.lableAccount.setText("输入转账的账户")
            self.lineEditMoney.clear()
            self.lineEditAccount.clear()

    def resetBack(self):
        self.isOk = False
        self.lableMoney.setFont(self.font)
        self.lableMoney.setStyleSheet("color: black")
        self.lableMoney.setText("输入转账金额")
        self.lableAccount.setFont(self.font)
        self.lableAccount.setStyleSheet("color: black")
        self.lableAccount.setText("输入转账的账户")
        self.lineEditMoney.clear()
        self.lineEditAccount.clear()

    def checkAccountMoney(self, main: MainContrl):
        if not self.isOk:
            return
        self.lableMoney.setStyleSheet("color: black")
        self.lableMoney.setText("输入转账金额")
        self.lableAccount.setStyleSheet("color: black")
        self.lableAccount.setText("输入转账的账户")
        main.toAccout.clear()
        for data in main.data:
            if data[1] == self.lineEditAccount.text() and data[1] != main.currentAccout["account"]:
                main.toAccout["account"] = data[1]
                main.toAccout["password"] = data[2]
                main.toAccout["saving"] = data[3]
        if len(main.toAccout) == 0:
            self.lableAccount.setText("没有此用户")
            self.lableAccount.setStyleSheet("color: red")
            self.isOk = False
            return
        if int(self.lineEditMoney.text()) > main.currentAccout["saving"]:
            self.lableMoney.setText("余额不足")
            self.lableMoney.setStyleSheet("color: red")
            self.isOk = False
            return
        self.isOk = True
        main.changeMoney=int(self.lineEditMoney.text())

    def checkInput(self):
        self.lableMoney.setFont(self.font)
        self.lableMoney.setStyleSheet("color: black")
        self.lableMoney.setText("输入转账金额")
        self.lableAccount.setFont(self.font)
        self.lableAccount.setStyleSheet("color: black")
        self.lableAccount.setText("输入转账的账户")
        self.isOk: bool = True
        if self.lineEditMoney.text() == '':
            self.lableMoney.setFont(self.font)
            self.lableMoney.setText("不能为空")
            self.lableMoney.setStyleSheet('color: red')
            self.isOk: bool = False
            return
        if self.lineEditAccount.text() == '':
            self.lableAccount.setFont(self.font)
            self.lableAccount.setText("不能为空")
            self.lableAccount.setStyleSheet('color: red')
            self.isOk: bool = False
            return

        if bool(re.search("[^a-zA-Z0-9]", self.lineEditAccount.text())):
            self.lableAccount.setFont(self.font)
            self.lableAccount.setText("账号不能有非数字与非字母符号")
            self.lableAccount.setStyleSheet('color: red')
            self.isOk: bool = False
            return
        if bool(re.search("[^0123456789]", self.lineEditMoney.text())):
            self.lableMoney.setFont(self.font)
            self.lableMoney.setText("不能输入非数字")
            self.lableMoney.setStyleSheet('color: red')
            self.isOk: bool = False
            return


def connectEnter(self, func):
    self.enterButton.pressed.connect(func)


def connectBack(self, func):
    self.backButton.pressed.connect(func)


if __name__ == "__main__":
    app = QApplication([])

    main = MainContrl()
    print(main.data)
    print(main.m_columns)

    welcome = Welcome()
    sign = Sign()
    log = Log()
    deposit = Deposit()  # 检查输入框内容，设置back按钮的重置操作
    welcome.connectSignButton(lambda: jumpInto(welcome, sign))
    welcome.connectLogButton(lambda: jumpInto(welcome, log))
    log.connectEnterButton(
        lambda: main.checkAccountPassword(log.lineEditAccount.text(), log.lineEditPassword.text(), log))
    sign.connectEnterButton(lambda: sign.checkAccountPassword(main.data))
    sign.connectEnterButton(lambda: main.createNewAccount(sign.lineEditAccount.text(),
                                                          sign.lineEditPassword.text(), 0, sign.isOKPassword))

    sign.connectEnterButton(lambda: jumpInto(sign, welcome, sign.isOKPassword))
    sign.connectEnterButton(sign.resetEnter)
    sign.connectEnterButton(main.clearAllData)

    log.connectSignButton(lambda: jumpInto(log, sign))
    sign.connectLogButton(lambda: jumpInto(sign, log))

    log.connectEnterButton(lambda: jumpInto(log, operate, log.isOKPassword))
    log.connectEnterButton(log.resetEnter)

    operate = Operate()
    operate.connectExit(main.clearAllData)
    operate.connectWithdraw(lambda: jumpInto(operate, withdraw))
    operate.connectDeposit(lambda: jumpInto(operate, deposit))

    deposit.connectBackButton(lambda: jumpInto(deposit, operate))  # 回到operate界面
    deposit.connectEnterButton(lambda: main.setDepositChangeMoney(deposit))  # 设置取款金额，清空输入框
    deposit.connectEnterButton(lambda: main.updateCurrentAccountDeposit(deposit.isOk))  # 更新账户存款，重置存款金额，提交数据

    withdraw = Withdraw()
    withdraw.connectBackButton(lambda: jumpInto(withdraw, operate))  # 返回操作界面
    withdraw.connectEnterButton(lambda: main.checkSaving(withdraw))

    rest = Rest()
    operate.connectRestButton(lambda: rest.connectMain(main))
    operate.connectRestButton(lambda: jumpInto(operate, rest))
    rest.connectBackButton(lambda: jumpInto(rest, operate))
    operate.connectExitButton(lambda: jumpInto(operate, welcome))
    operate.connectExitButton(main.clearAllData)
    welcome.show()
    operate.connectTransfer(lambda: jumpInto(operate, transfer))
    transfer = Transfer()
    transfer.connectEnter(lambda: transfer.checkAccountMoney(main))
    transfer.connectEnter(lambda: main.updateTransferMoney(transfer.isOk))

    transfer.connectEnter(lambda: jumpInto(transfer, operate, transfer.isOk))
    transfer.connectEnter(transfer.resetEnter)
    transfer.connectBack(lambda: jumpInto(transfer, operate))

    app.exec_()
