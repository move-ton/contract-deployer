# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledQVMEfD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from tonclient.client import TonClient,DEVNET_BASE_URL
import os
from tonclient.types import Abi, KeyPair, DeploySet, CallSet, Signer, \
    MessageSource, StateInitSource
import base64
from tonclient.net import TonQLQuery

client = TonClient(network={'server_address': DEVNET_BASE_URL}, abi={'message_expiration_timeout': 30000})

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1384, 1133)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.openfile = QToolButton(self.centralwidget)
        self.openfile.setObjectName(u"toolButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openfile.sizePolicy().hasHeightForWidth())
        self.openfile.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.openfile)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.address = QLabel(self.centralwidget)
        self.address.setObjectName(u"address")

        self.horizontalLayout_3.addWidget(self.address)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.public_key = QLabel(self.centralwidget)
        self.public_key.setObjectName(u"public_key")

        self.horizontalLayout_4.addWidget(self.public_key)

        self.generateNewKeyFile = QPushButton(self.centralwidget)
        self.generateNewKeyFile.setObjectName(u"generateNewKeyFile")

        self.horizontalLayout_4.addWidget(self.generateNewKeyFile)

        self.openKeyFile = QPushButton(self.centralwidget)
        self.openKeyFile.setObjectName(u"openKeyFile")

        self.horizontalLayout_4.addWidget(self.openKeyFile)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mainnetButton = QCheckBox(self.centralwidget)
        self.mainnetButton.setObjectName(u"mainnetButton")

        self.horizontalLayout_2.addWidget(self.mainnetButton)

        self.gettesttokenButton = QPushButton(self.centralwidget)
        self.gettesttokenButton.setObjectName(u"gettesttokenButton")

        self.horizontalLayout_2.addWidget(self.gettesttokenButton)

        self.deploy = QPushButton(self.centralwidget)
        self.deploy.setObjectName(u"deploy")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.deploy.sizePolicy().hasHeightForWidth())
        self.deploy.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.deploy)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_7.addWidget(self.checkBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_7.addWidget(self.pushButton_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainnetButton.clicked[bool].connect(self.gettesttokenButton.setDisabled)


        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openfile.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Save file", None))
        self.address.setText(QCoreApplication.translate("MainWindow", u"Address of contract", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"compile", None))
        self.mainnetButton.setText(QCoreApplication.translate("MainWindow", u"mainnet", None))
        self.gettesttokenButton.setText(QCoreApplication.translate("MainWindow", u"get test token", None))
        self.deploy.setText(QCoreApplication.translate("MainWindow", u"deploy", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"functionName", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"attribute", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"attribute", None))
        self.generateNewKeyFile.setText(QCoreApplication.translate("MainWindow",u'Generate New Key File'))
        self.openKeyFile.setText(QCoreApplication.translate("MainWindow", u'Open Key File'))
        self.public_key.setText(QCoreApplication.translate("MainWindow", u'public_key:'))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

class TonWrapper(object):

    def __init__(self,network={'server_address': DEVNET_BASE_URL},samples_dir='abi'):
        self.BASE_DIR = os.path.dirname(__file__)
        self.SAMPLES_DIR = os.path.join(self.BASE_DIR, 'abi')
        self.async_core_client = TonClient(network={'server_address': DEVNET_BASE_URL})

    def get_testnet_grams(self,address: str):
        giver_abi = Abi.from_json_path(
            path=os.path.join(self.SAMPLES_DIR, 'Giver.abi.json'))
        call_set = CallSet(
            function_name='grant',
            inputs={'addr': address})
        self.async_core_client.processing.process_message(
            abi=giver_abi, signer=Signer(), address='0:653b9a6452c7a982c6dc92b2da9eba832ade1c467699ebb3b43dca6d77b780dd',
            call_set=call_set, send_events=False)

    def get_address(self,signer,abi,tvc,constructor_header={},workchaind_id=0):
        deploy_set = DeploySet(tvc=tvc)
        call_set = CallSet(
            function_name='constructor',
            header=constructor_header)
        message_source = MessageSource.from_encoding_params(
            abi=abi, signer=signer, deploy_set=deploy_set,
            call_set=call_set)
        state_init_source = StateInitSource.from_message(
            message=message_source)
        encoded = self.async_core_client.abi.encode_account(
            state_init=state_init_source)
        return f'{workchaind_id}:' + encoded['id']

    @staticmethod
    def open_tvc(path):
        with open(path, 'rb') as fp:
            return base64.b64encode(fp.read()).decode()


    def generate_sign_keys(self):
        return self.async_core_client.crypto.generate_random_sign_keys()

    def deploy_contract(self,abi,tvc,signer,constructor_header={}):
        deploy_set = DeploySet(tvc=tvc)
        call_set = CallSet(
            function_name='constructor', inputs=constructor_header)
        deploy_message = self.async_core_client.abi.encode_message(
            abi=abi, signer=signer, deploy_set=deploy_set, call_set=call_set)
        return deploy_message

    def deploy_wallet(self,signer):
        return self.deploy_contract(abi=Abi.from_json_path(
            path=os.path.join(self.SAMPLES_DIR, 'wallet.abi.json')),tvc=self.open_tvc('abi/wallet.tvc'),signer=signer)

    def send_grams(self,address: str,value:int,signer, bounce: bool,workchaind_id):
        wallet_abi = Abi.from_json_path(
            path=os.path.join(self.SAMPLES_DIR, 'wallet.abi.json'))
        call_set = CallSet(
            function_name='sendTransaction',
            inputs={'dest': address, 'value': value, 'bounce': bounce})

        message_source = MessageSource.from_encoding_params(
            abi=wallet_abi, signer=signer, address=self.get_address(signer,wallet_abi,self.open_tvc('abi/wallet.tvc'),workchaind_id=workchaind_id),
            call_set=call_set)
        self.async_core_client.processing.process_message(
            message=message_source, send_events=False)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        QMainWindow.__init__(self)

        # Initialize UI
        self.ui = self.setupUi(self)
        print("AAA")
        self.openfile.clicked.connect(self.open_file)
        self.wrapper = TonWrapper()
        self.toolButton.clicked.connect(self.save_file)
        self.generateNewKeyFile.clicked.connect(self.generate_key)
        self.openKeyFile.clicked.connect(self.open_key)
        self.pushButton.clicked.connect(self.compile_contract)
        self.gettesttokenButton.clicked.connect(self.get_testnet_token)

    def tr(self, text):
        return QObject.tr(self, text)

    def compile_contract(self):
        if not ".tmp_contract_deployer" in os.listdir():
            os.mkdir(".tmp_contract_deployer")
        f = open(f'.tmp_contract_deployer/.contract.sol','w')
        f.write(self.plainTextEdit.toPlainText())
        f.close()

        home_dir = os.system("solc .tmp_contract_deployer/.contract.sol")
        os.system("tvm_linker compile .contract.code --abi-json .contract.abi.json --lib stdlib_sol.tvm -o .contract.tvc")
        with open(".contract.abi.json","r") as f:
            abi = f.read()
        addr = self.wrapper.get_address(Signer(self.main_key),Abi.from_json_path(
            path='.contract.abi.json'),self.wrapper.open_tvc(".contract.tvc"))
        self.address.setText(QCoreApplication.translate("MainWindow", f"Address of contract: {addr}", None))
        self.addr = addr
        query = TonQLQuery(collection='accounts')
        query = query.set_filter(id__eq=addr)
        query = query.set_result('balance')
        result = client.net.query_collection(query)
        print(result)
        if len(result) == 0:
            balance = 0
        else:
            balance = round(int(result[0]['balance'],16) / 10 ** 9,3)
        print(result)
        self.label_2.setText(QCoreApplication.translate("MainWindow", f"Balance: {balance} 💎", None))
    def get_testnet_token(self):
        self.wrapper.get_testnet_grams(self.addr)
        query = TonQLQuery(collection='accounts')
        query = query.set_filter(id__eq=self.addr)
        query = query.set_result('balance')
        result = client.net.query_collection(query)

        if len(result) == 0:
            balance = 0
        else:
            balance = round(int(result[0]) / 10 ** 9, 3)
        print(result)
        self.label_2.setText(QCoreApplication.translate("MainWindow", f"Balance: {balance} 💎", None))
    def open_key(self):
        path_to_file, _ = QFileDialog.getOpenFileName(self, self.tr("Load keys"), self.tr("~/Desktop/"),
                                                      self.tr("Keys (*.keys.json)"))
        key = KeyPair.load(path_to_file,True)
        self.main_key = key
        self.public_key.setText(QCoreApplication.translate("MainWindow", u'public_key: ' + key.public))

    def generate_key(self):
        key = client.crypto.generate_random_sign_keys()
        path_to_file, _ = QFileDialog.getSaveFileName(self, self.tr("Save keys"), self.tr("~/Desktop/"),
                                                      self.tr("Keys (*.keys.json)"))
        key.dump(path=path_to_file,as_binary=True)
        self.main_key = key
        self.public_key.setText(QCoreApplication.translate("MainWindow", u'public_key: ' + key.public))
    def open_file(self):
        print("AAA")
        path_to_file, _ = QFileDialog.getOpenFileName(self, self.tr("Load Contract"), self.tr("~/Desktop/"),
                                                      self.tr("Contracts (*.sol)"))
        f = open(path_to_file,"r")
        self.plainTextEdit.setPlainText(open(path_to_file,"r").read())
        f.close()
    def save_file(self):
        print("AAA")
        path_to_file, _ = QFileDialog.getSaveFileName(self, self.tr("Save Contract"), self.tr("~/Desktop/"),
                                                      self.tr("Contract (*.sol)"))
        f = open(path_to_file,"w")
        f.write(self.plainTextEdit.toPlainText())
        f.close()

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())