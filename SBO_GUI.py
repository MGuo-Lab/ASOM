# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SBO.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QStackedWidget, QTextEdit, QWidget)

class Ui_SBO(object):
    def setupUi(self, SBO):
        if not SBO.objectName():
            SBO.setObjectName(u"SBO")
        SBO.resize(1027, 672)
        self.lable_Data_Upload = QLabel(SBO)
        self.lable_Data_Upload.setObjectName(u"lable_Data_Upload")
        self.lable_Data_Upload.setGeometry(QRect(110, 20, 81, 16))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setBold(True)
        self.lable_Data_Upload.setFont(font)
        self.lable_Data_Upload.setTextFormat(Qt.TextFormat.AutoText)
        self.pushButton_Input_Data = QPushButton(SBO)
        self.pushButton_Input_Data.setObjectName(u"pushButton_Input_Data")
        self.pushButton_Input_Data.setGeometry(QRect(20, 60, 101, 24))
        self.pushButton_Output_Data = QPushButton(SBO)
        self.pushButton_Output_Data.setObjectName(u"pushButton_Output_Data")
        self.pushButton_Output_Data.setGeometry(QRect(20, 180, 101, 24))
        self.lable_Application = QLabel(SBO)
        self.lable_Application.setObjectName(u"lable_Application")
        self.lable_Application.setGeometry(QRect(420, 20, 101, 16))
        font1 = QFont()
        font1.setBold(True)
        self.lable_Application.setFont(font1)
        self.comboBox_Model = QComboBox(SBO)
        self.comboBox_Model.addItem("")
        self.comboBox_Model.addItem("")
        self.comboBox_Model.addItem("")
        self.comboBox_Model.addItem("")
        self.comboBox_Model.addItem("")
        self.comboBox_Model.setObjectName(u"comboBox_Model")
        self.comboBox_Model.setGeometry(QRect(370, 70, 205, 21))
        self.comboBox_Model.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.pushButton_Fit = QPushButton(SBO)
        self.pushButton_Fit.setObjectName(u"pushButton_Fit")
        self.pushButton_Fit.setGeometry(QRect(410, 530, 121, 24))
        self.label_Input_Pre = QLabel(SBO)
        self.label_Input_Pre.setObjectName(u"label_Input_Pre")
        self.label_Input_Pre.setGeometry(QRect(750, 20, 121, 16))
        self.label_Input_Pre.setFont(font1)
        self.textEdit_Input_Predict = QTextEdit(SBO)
        self.textEdit_Input_Predict.setObjectName(u"textEdit_Input_Predict")
        self.textEdit_Input_Predict.setGeometry(QRect(700, 50, 241, 71))
        self.pushButton_Predict = QPushButton(SBO)
        self.pushButton_Predict.setObjectName(u"pushButton_Predict")
        self.pushButton_Predict.setGeometry(QRect(770, 140, 101, 24))
        self.groupBox_Optimise = QGroupBox(SBO)
        self.groupBox_Optimise.setObjectName(u"groupBox_Optimise")
        self.groupBox_Optimise.setGeometry(QRect(670, 240, 291, 361))
        self.groupBox_Optimise.setFont(font1)
        self.groupBox_Optimise.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_Optimise_Method = QComboBox(self.groupBox_Optimise)
        self.comboBox_Optimise_Method.addItem("")
        self.comboBox_Optimise_Method.addItem("")
        self.comboBox_Optimise_Method.setObjectName(u"comboBox_Optimise_Method")
        self.comboBox_Optimise_Method.setGeometry(QRect(140, 40, 129, 21))
        font2 = QFont()
        font2.setBold(False)
        self.comboBox_Optimise_Method.setFont(font2)
        self.comboBox_Optimise_Method.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.label_Optimize_Method = QLabel(self.groupBox_Optimise)
        self.label_Optimize_Method.setObjectName(u"label_Optimize_Method")
        self.label_Optimize_Method.setGeometry(QRect(40, 40, 71, 16))
        self.label_Optimize_Method.setFont(font2)
        self.pushButton_Optimise = QPushButton(self.groupBox_Optimise)
        self.pushButton_Optimise.setObjectName(u"pushButton_Optimise")
        self.pushButton_Optimise.setGeometry(QRect(100, 300, 75, 24))
        self.pushButton_Optimise.setFont(font2)
        self.stackedWidget_Optimisation = QStackedWidget(self.groupBox_Optimise)
        self.stackedWidget_Optimisation.setObjectName(u"stackedWidget_Optimisation")
        self.stackedWidget_Optimisation.setGeometry(QRect(10, 80, 271, 181))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.groupBox_Genetic_Params = QGroupBox(self.page)
        self.groupBox_Genetic_Params.setObjectName(u"groupBox_Genetic_Params")
        self.groupBox_Genetic_Params.setGeometry(QRect(10, 10, 251, 161))
        self.groupBox_Genetic_Params.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Num_Individuals = QLabel(self.groupBox_Genetic_Params)
        self.label_Num_Individuals.setObjectName(u"label_Num_Individuals")
        self.label_Num_Individuals.setGeometry(QRect(60, 30, 131, 16))
        self.label_Num_Individuals.setFont(font2)
        self.lineEdit_Num_Individuals = QLineEdit(self.groupBox_Genetic_Params)
        self.lineEdit_Num_Individuals.setObjectName(u"lineEdit_Num_Individuals")
        self.lineEdit_Num_Individuals.setGeometry(QRect(20, 50, 211, 20))
        self.label_Num_Generations = QLabel(self.groupBox_Genetic_Params)
        self.label_Num_Generations.setObjectName(u"label_Num_Generations")
        self.label_Num_Generations.setGeometry(QRect(60, 100, 141, 16))
        self.label_Num_Generations.setFont(font2)
        self.lineEdit_Num_Generations = QLineEdit(self.groupBox_Genetic_Params)
        self.lineEdit_Num_Generations.setObjectName(u"lineEdit_Num_Generations")
        self.lineEdit_Num_Generations.setGeometry(QRect(20, 120, 211, 20))
        self.stackedWidget_Optimisation.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.groupBox_Solvers = QGroupBox(self.page_2)
        self.groupBox_Solvers.setObjectName(u"groupBox_Solvers")
        self.groupBox_Solvers.setGeometry(QRect(10, 40, 241, 101))
        self.groupBox_Solvers.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_Solvers = QComboBox(self.groupBox_Solvers)
        self.comboBox_Solvers.addItem("")
        self.comboBox_Solvers.addItem("")
        self.comboBox_Solvers.addItem("")
        self.comboBox_Solvers.addItem("")
        self.comboBox_Solvers.setObjectName(u"comboBox_Solvers")
        self.comboBox_Solvers.setGeometry(QRect(40, 40, 161, 22))
        self.comboBox_Solvers.setFont(font2)
        self.stackedWidget_Optimisation.addWidget(self.page_2)
        self.pushButton_Performance = QPushButton(SBO)
        self.pushButton_Performance.setObjectName(u"pushButton_Performance")
        self.pushButton_Performance.setGeometry(QRect(410, 590, 121, 24))
        self.textEdit_Input_Data = QTextEdit(SBO)
        self.textEdit_Input_Data.setObjectName(u"textEdit_Input_Data")
        self.textEdit_Input_Data.setGeometry(QRect(140, 60, 141, 31))
        self.textEdit_Output_Data = QTextEdit(SBO)
        self.textEdit_Output_Data.setObjectName(u"textEdit_Output_Data")
        self.textEdit_Output_Data.setGeometry(QRect(140, 180, 141, 31))
        self.pushButto_Process = QPushButton(SBO)
        self.pushButto_Process.setObjectName(u"pushButto_Process")
        self.pushButto_Process.setGeometry(QRect(20, 270, 101, 24))
        self.textEdit_Process = QTextEdit(SBO)
        self.textEdit_Process.setObjectName(u"textEdit_Process")
        self.textEdit_Process.setGeometry(QRect(140, 270, 141, 31))
        self.textEdit_Results = QTextEdit(SBO)
        self.textEdit_Results.setObjectName(u"textEdit_Results")
        self.textEdit_Results.setGeometry(QRect(10, 390, 261, 251))
        self.label_Results = QLabel(SBO)
        self.label_Results.setObjectName(u"label_Results")
        self.label_Results.setGeometry(QRect(100, 370, 71, 20))
        self.label_Results.setFont(font1)
        self.label_Results.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_Space = QPushButton(SBO)
        self.pushButton_Space.setObjectName(u"pushButton_Space")
        self.pushButton_Space.setGeometry(QRect(20, 120, 101, 24))
        self.textEdit_Space = QTextEdit(SBO)
        self.textEdit_Space.setObjectName(u"textEdit_Space")
        self.textEdit_Space.setGeometry(QRect(140, 120, 141, 31))
        self.radioButton_Process = QRadioButton(SBO)
        self.radioButton_Process.setObjectName(u"radioButton_Process")
        self.radioButton_Process.setGeometry(QRect(60, 230, 151, 20))
        self.radioButton_Process.setFont(font1)
        self.pushButton_Scale = QPushButton(SBO)
        self.pushButton_Scale.setObjectName(u"pushButton_Scale")
        self.pushButton_Scale.setGeometry(QRect(100, 320, 75, 24))
        self.stackedWidget_Model = QStackedWidget(SBO)
        self.stackedWidget_Model.setObjectName(u"stackedWidget_Model")
        self.stackedWidget_Model.setGeometry(QRect(350, 100, 231, 421))
        self.stackedWidget_Model.setFrameShape(QFrame.Shape.NoFrame)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.groupBox_Kernel = QGroupBox(self.page_3)
        self.groupBox_Kernel.setObjectName(u"groupBox_Kernel")
        self.groupBox_Kernel.setGeometry(QRect(20, 0, 201, 81))
        self.groupBox_Kernel.setFont(font1)
        self.groupBox_Kernel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_Kernel = QComboBox(self.groupBox_Kernel)
        self.comboBox_Kernel.addItem("")
        self.comboBox_Kernel.addItem("")
        self.comboBox_Kernel.addItem("")
        self.comboBox_Kernel.addItem("")
        self.comboBox_Kernel.addItem("")
        self.comboBox_Kernel.addItem("")
        self.comboBox_Kernel.addItem("")
        self.comboBox_Kernel.addItem("")
        self.comboBox_Kernel.setObjectName(u"comboBox_Kernel")
        self.comboBox_Kernel.setGeometry(QRect(10, 30, 161, 21))
        self.comboBox_Kernel.setFont(font2)
        self.comboBox_Kernel.setMaxVisibleItems(5)
        self.comboBox_Kernel.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.stackedWidget_Model.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.groupBox_Activation = QGroupBox(self.page_4)
        self.groupBox_Activation.setObjectName(u"groupBox_Activation")
        self.groupBox_Activation.setGeometry(QRect(20, 0, 201, 80))
        self.groupBox_Activation.setFont(font1)
        self.groupBox_Activation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_Activation = QComboBox(self.groupBox_Activation)
        self.comboBox_Activation.addItem("")
        self.comboBox_Activation.addItem("")
        self.comboBox_Activation.addItem("")
        self.comboBox_Activation.addItem("")
        self.comboBox_Activation.addItem("")
        self.comboBox_Activation.addItem("")
        self.comboBox_Activation.addItem("")
        self.comboBox_Activation.setObjectName(u"comboBox_Activation")
        self.comboBox_Activation.setGeometry(QRect(10, 30, 161, 21))
        self.comboBox_Activation.setFont(font2)
        self.comboBox_Activation.setMaxVisibleItems(5)
        self.comboBox_Activation.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.groupBox_NN_Param = QGroupBox(self.page_4)
        self.groupBox_NN_Param.setObjectName(u"groupBox_NN_Param")
        self.groupBox_NN_Param.setGeometry(QRect(20, 90, 201, 291))
        self.groupBox_NN_Param.setFont(font1)
        self.groupBox_NN_Param.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Batch_Size = QLabel(self.groupBox_NN_Param)
        self.label_Batch_Size.setObjectName(u"label_Batch_Size")
        self.label_Batch_Size.setGeometry(QRect(10, 90, 61, 16))
        self.label_Batch_Size.setFont(font2)
        self.lineEdit_Batch_Size = QLineEdit(self.groupBox_NN_Param)
        self.lineEdit_Batch_Size.setObjectName(u"lineEdit_Batch_Size")
        self.lineEdit_Batch_Size.setGeometry(QRect(80, 90, 113, 20))
        self.label_Epochs = QLabel(self.groupBox_NN_Param)
        self.label_Epochs.setObjectName(u"label_Epochs")
        self.label_Epochs.setGeometry(QRect(10, 140, 54, 16))
        self.label_Epochs.setFont(font2)
        self.lineEdit_Epochs = QLineEdit(self.groupBox_NN_Param)
        self.lineEdit_Epochs.setObjectName(u"lineEdit_Epochs")
        self.lineEdit_Epochs.setGeometry(QRect(80, 140, 113, 20))
        self.label_Learn_Rate = QLabel(self.groupBox_NN_Param)
        self.label_Learn_Rate.setObjectName(u"label_Learn_Rate")
        self.label_Learn_Rate.setGeometry(QRect(10, 190, 54, 16))
        self.label_Learn_Rate.setFont(font2)
        self.lineEdit_Learning_Rate = QLineEdit(self.groupBox_NN_Param)
        self.lineEdit_Learning_Rate.setObjectName(u"lineEdit_Learning_Rate")
        self.lineEdit_Learning_Rate.setGeometry(QRect(80, 190, 113, 20))
        self.label_Weight_Decay = QLabel(self.groupBox_NN_Param)
        self.label_Weight_Decay.setObjectName(u"label_Weight_Decay")
        self.label_Weight_Decay.setGeometry(QRect(10, 240, 54, 16))
        self.label_Weight_Decay.setFont(font2)
        self.lineEdit_Weight_Decay = QLineEdit(self.groupBox_NN_Param)
        self.lineEdit_Weight_Decay.setObjectName(u"lineEdit_Weight_Decay")
        self.lineEdit_Weight_Decay.setGeometry(QRect(80, 240, 113, 20))
        self.label_Nodes = QLabel(self.groupBox_NN_Param)
        self.label_Nodes.setObjectName(u"label_Nodes")
        self.label_Nodes.setGeometry(QRect(10, 40, 51, 16))
        self.label_Nodes.setFont(font2)
        self.lineEdit_Nodes = QLineEdit(self.groupBox_NN_Param)
        self.lineEdit_Nodes.setObjectName(u"lineEdit_Nodes")
        self.lineEdit_Nodes.setGeometry(QRect(80, 40, 113, 20))
        self.label_each_layer = QLabel(self.groupBox_NN_Param)
        self.label_each_layer.setObjectName(u"label_each_layer")
        self.label_each_layer.setGeometry(QRect(10, 60, 71, 16))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(False)
        self.label_each_layer.setFont(font3)
        self.stackedWidget_Model.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.groupBox_HB_Gaussion = QGroupBox(self.page_5)
        self.groupBox_HB_Gaussion.setObjectName(u"groupBox_HB_Gaussion")
        self.groupBox_HB_Gaussion.setGeometry(QRect(20, 0, 201, 81))
        self.groupBox_HB_Gaussion.setFont(font1)
        self.groupBox_HB_Gaussion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_HB_Gaukernel = QComboBox(self.groupBox_HB_Gaussion)
        self.comboBox_HB_Gaukernel.addItem("")
        self.comboBox_HB_Gaukernel.addItem("")
        self.comboBox_HB_Gaukernel.addItem("")
        self.comboBox_HB_Gaukernel.addItem("")
        self.comboBox_HB_Gaukernel.addItem("")
        self.comboBox_HB_Gaukernel.addItem("")
        self.comboBox_HB_Gaukernel.addItem("")
        self.comboBox_HB_Gaukernel.addItem("")
        self.comboBox_HB_Gaukernel.setObjectName(u"comboBox_HB_Gaukernel")
        self.comboBox_HB_Gaukernel.setGeometry(QRect(10, 30, 161, 21))
        self.comboBox_HB_Gaukernel.setFont(font2)
        self.comboBox_HB_Gaukernel.setMaxVisibleItems(5)
        self.comboBox_HB_Gaukernel.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.groupBox_HB_NN = QGroupBox(self.page_5)
        self.groupBox_HB_NN.setObjectName(u"groupBox_HB_NN")
        self.groupBox_HB_NN.setGeometry(QRect(20, 90, 201, 301))
        self.groupBox_HB_NN.setFont(font1)
        self.groupBox_HB_NN.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_HB_NNbatchSize = QLabel(self.groupBox_HB_NN)
        self.label_HB_NNbatchSize.setObjectName(u"label_HB_NNbatchSize")
        self.label_HB_NNbatchSize.setGeometry(QRect(10, 130, 61, 16))
        self.label_HB_NNbatchSize.setFont(font2)
        self.lineEdit_HB_NNbatchSize = QLineEdit(self.groupBox_HB_NN)
        self.lineEdit_HB_NNbatchSize.setObjectName(u"lineEdit_HB_NNbatchSize")
        self.lineEdit_HB_NNbatchSize.setGeometry(QRect(80, 130, 113, 20))
        self.label_HB_NNepochs = QLabel(self.groupBox_HB_NN)
        self.label_HB_NNepochs.setObjectName(u"label_HB_NNepochs")
        self.label_HB_NNepochs.setGeometry(QRect(10, 180, 54, 16))
        self.label_HB_NNepochs.setFont(font2)
        self.lineEdit_HB_NNepochs = QLineEdit(self.groupBox_HB_NN)
        self.lineEdit_HB_NNepochs.setObjectName(u"lineEdit_HB_NNepochs")
        self.lineEdit_HB_NNepochs.setGeometry(QRect(80, 180, 113, 20))
        self.label_HB_NNlearnrate = QLabel(self.groupBox_HB_NN)
        self.label_HB_NNlearnrate.setObjectName(u"label_HB_NNlearnrate")
        self.label_HB_NNlearnrate.setGeometry(QRect(10, 220, 54, 16))
        self.label_HB_NNlearnrate.setFont(font2)
        self.lineEdit_HB_NNlearnrate = QLineEdit(self.groupBox_HB_NN)
        self.lineEdit_HB_NNlearnrate.setObjectName(u"lineEdit_HB_NNlearnrate")
        self.lineEdit_HB_NNlearnrate.setGeometry(QRect(80, 220, 113, 20))
        self.label_HB_NNweightdecay = QLabel(self.groupBox_HB_NN)
        self.label_HB_NNweightdecay.setObjectName(u"label_HB_NNweightdecay")
        self.label_HB_NNweightdecay.setGeometry(QRect(10, 260, 54, 16))
        self.label_HB_NNweightdecay.setFont(font2)
        self.lineEdit_HB_NNweightdecay = QLineEdit(self.groupBox_HB_NN)
        self.lineEdit_HB_NNweightdecay.setObjectName(u"lineEdit_HB_NNweightdecay")
        self.lineEdit_HB_NNweightdecay.setGeometry(QRect(80, 260, 113, 20))
        self.label_HB_NNnodes = QLabel(self.groupBox_HB_NN)
        self.label_HB_NNnodes.setObjectName(u"label_HB_NNnodes")
        self.label_HB_NNnodes.setGeometry(QRect(10, 80, 51, 16))
        self.label_HB_NNnodes.setFont(font2)
        self.lineEdit_HB_NNnodes = QLineEdit(self.groupBox_HB_NN)
        self.lineEdit_HB_NNnodes.setObjectName(u"lineEdit_HB_NNnodes")
        self.lineEdit_HB_NNnodes.setGeometry(QRect(80, 80, 113, 20))
        self.label_each_layer_2 = QLabel(self.groupBox_HB_NN)
        self.label_each_layer_2.setObjectName(u"label_each_layer_2")
        self.label_each_layer_2.setGeometry(QRect(10, 100, 71, 16))
        self.label_each_layer_2.setFont(font3)
        self.label_HB_NNactivate = QLabel(self.groupBox_HB_NN)
        self.label_HB_NNactivate.setObjectName(u"label_HB_NNactivate")
        self.label_HB_NNactivate.setGeometry(QRect(10, 40, 61, 16))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        self.label_HB_NNactivate.setFont(font4)
        self.comboBox_HB_NNactivate = QComboBox(self.groupBox_HB_NN)
        self.comboBox_HB_NNactivate.addItem("")
        self.comboBox_HB_NNactivate.addItem("")
        self.comboBox_HB_NNactivate.addItem("")
        self.comboBox_HB_NNactivate.addItem("")
        self.comboBox_HB_NNactivate.addItem("")
        self.comboBox_HB_NNactivate.addItem("")
        self.comboBox_HB_NNactivate.addItem("")
        self.comboBox_HB_NNactivate.setObjectName(u"comboBox_HB_NNactivate")
        self.comboBox_HB_NNactivate.setGeometry(QRect(80, 40, 111, 21))
        self.comboBox_HB_NNactivate.setFont(font2)
        self.comboBox_HB_NNactivate.setMaxVisibleItems(5)
        self.comboBox_HB_NNactivate.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.stackedWidget_Model.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget_Model.addWidget(self.page_6)

        self.retranslateUi(SBO)

        self.pushButto_Process.hide()
        self.textEdit_Process.hide()
        self.radioButton_Process.toggled.connect(self.on_Process_changed)
        self.comboBox_Model.currentIndexChanged.connect(self.on_Model_changed)
        self.comboBox_Optimise_Method.currentIndexChanged.connect(self.on_Optimise_Method_changed)

        self.stackedWidget_Optimisation.setCurrentIndex(0)
        self.stackedWidget_Model.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SBO)
    # setupUi

    def retranslateUi(self, SBO):
        SBO.setWindowTitle(QCoreApplication.translate("SBO", u"ASOM", None))
        self.lable_Data_Upload.setText(QCoreApplication.translate("SBO", u"Data Upload", None))
        self.pushButton_Input_Data.setText(QCoreApplication.translate("SBO", u"Input", None))
        self.pushButton_Output_Data.setText(QCoreApplication.translate("SBO", u"Output", None))
        self.lable_Application.setText(QCoreApplication.translate("SBO", u"Model Selection", None))
        self.comboBox_Model.setItemText(0, QCoreApplication.translate("SBO", u"Gaussian Process(Regression)", None))
        self.comboBox_Model.setItemText(1, QCoreApplication.translate("SBO", u"Gaussian Process(Classification)", None))
        self.comboBox_Model.setItemText(2, QCoreApplication.translate("SBO", u"Neural Network(Regression)", None))
        self.comboBox_Model.setItemText(3, QCoreApplication.translate("SBO", u"Neural Network(Classification)", None))
        self.comboBox_Model.setItemText(4, QCoreApplication.translate("SBO", u"Hybrid(Regression)", None))

        self.pushButton_Fit.setText(QCoreApplication.translate("SBO", u"Fit", None))
        self.label_Input_Pre.setText(QCoreApplication.translate("SBO", u"Input For Prediction", None))
        self.pushButton_Predict.setText(QCoreApplication.translate("SBO", u"Predict", None))
        self.groupBox_Optimise.setTitle(QCoreApplication.translate("SBO", u"Optimisation", None))
        self.comboBox_Optimise_Method.setItemText(0, QCoreApplication.translate("SBO", u"Genetic Algorithm", None))
        self.comboBox_Optimise_Method.setItemText(1, QCoreApplication.translate("SBO", u"Surrogate Model", None))

        self.label_Optimize_Method.setText(QCoreApplication.translate("SBO", u"Method", None))
        self.pushButton_Optimise.setText(QCoreApplication.translate("SBO", u"Optimise", None))
        self.groupBox_Genetic_Params.setTitle(QCoreApplication.translate("SBO", u"Genetic Parameters", None))
        self.label_Num_Individuals.setText(QCoreApplication.translate("SBO", u"Number of Individuals", None))
        self.label_Num_Generations.setText(QCoreApplication.translate("SBO", u"Number of Generations", None))
        self.groupBox_Solvers.setTitle(QCoreApplication.translate("SBO", u"Solvers", None))
        self.comboBox_Solvers.setItemText(0, QCoreApplication.translate("SBO", u"BARON", None))
        self.comboBox_Solvers.setItemText(1, QCoreApplication.translate("SBO", u"ipopt", None))
        self.comboBox_Solvers.setItemText(2, QCoreApplication.translate("SBO", u"bonmin", None))
        self.comboBox_Solvers.setItemText(3, QCoreApplication.translate("SBO", u"Couenne", None))

        self.pushButton_Performance.setText(QCoreApplication.translate("SBO", u"Performance", None))
        self.pushButto_Process.setText(QCoreApplication.translate("SBO", u"Process", None))
        self.label_Results.setText(QCoreApplication.translate("SBO", u"Results", None))
        self.pushButton_Space.setText(QCoreApplication.translate("SBO", u"Spcae", None))
        self.radioButton_Process.setText(QCoreApplication.translate("SBO", u"Process Covergence", None))
        self.pushButton_Scale.setText(QCoreApplication.translate("SBO", u"Confirm", None))
        self.groupBox_Kernel.setTitle(QCoreApplication.translate("SBO", u"Kernel Function", None))
        self.comboBox_Kernel.setItemText(0, QCoreApplication.translate("SBO", u"rbf", None))
        self.comboBox_Kernel.setItemText(1, QCoreApplication.translate("SBO", u"linear", None))
        self.comboBox_Kernel.setItemText(2, QCoreApplication.translate("SBO", u"polynomial", None))
        self.comboBox_Kernel.setItemText(3, QCoreApplication.translate("SBO", u"RationalQuadratic", None))
        self.comboBox_Kernel.setItemText(4, QCoreApplication.translate("SBO", u"ExpSineSquared", None))
        self.comboBox_Kernel.setItemText(5, QCoreApplication.translate("SBO", u"Matern", None))
        self.comboBox_Kernel.setItemText(6, QCoreApplication.translate("SBO", u"Sum_RBF", None))
        self.comboBox_Kernel.setItemText(7, QCoreApplication.translate("SBO", u"Sum_RQ", None))

        self.groupBox_Activation.setTitle(QCoreApplication.translate("SBO", u"Activation Function", None))
        self.comboBox_Activation.setItemText(0, QCoreApplication.translate("SBO", u"tanh", None))
        self.comboBox_Activation.setItemText(1, QCoreApplication.translate("SBO", u"sigmoid", None))
        self.comboBox_Activation.setItemText(2, QCoreApplication.translate("SBO", u"softplus", None))
        self.comboBox_Activation.setItemText(3, QCoreApplication.translate("SBO", u"relu", None))
        self.comboBox_Activation.setItemText(4, QCoreApplication.translate("SBO", u"linear", None))
        self.comboBox_Activation.setItemText(5, QCoreApplication.translate("SBO", u"hardsigmoid", None))
        self.comboBox_Activation.setItemText(6, QCoreApplication.translate("SBO", u"leaky relu", None))

        self.groupBox_NN_Param.setTitle(QCoreApplication.translate("SBO", u"Parameters", None))
        self.label_Batch_Size.setText(QCoreApplication.translate("SBO", u"Batch Size", None))
        self.label_Epochs.setText(QCoreApplication.translate("SBO", u"Epochs", None))
        self.label_Learn_Rate.setText(QCoreApplication.translate("SBO", u"L-Rate", None))
        self.label_Weight_Decay.setText(QCoreApplication.translate("SBO", u"Decay", None))
        self.label_Nodes.setText(QCoreApplication.translate("SBO", u"Nodes", None))
        self.label_each_layer.setText(QCoreApplication.translate("SBO", u"(each Layer)", None))
        self.groupBox_HB_Gaussion.setTitle(QCoreApplication.translate("SBO", u"Gaussion Kernel", None))
        self.comboBox_HB_Gaukernel.setItemText(0, QCoreApplication.translate("SBO", u"rbf", None))
        self.comboBox_HB_Gaukernel.setItemText(1, QCoreApplication.translate("SBO", u"linear", None))
        self.comboBox_HB_Gaukernel.setItemText(2, QCoreApplication.translate("SBO", u"polynomial", None))
        self.comboBox_HB_Gaukernel.setItemText(3, QCoreApplication.translate("SBO", u"RationalQuadratic", None))
        self.comboBox_HB_Gaukernel.setItemText(4, QCoreApplication.translate("SBO", u"ExpSineSquared", None))
        self.comboBox_HB_Gaukernel.setItemText(5, QCoreApplication.translate("SBO", u"Matern", None))
        self.comboBox_HB_Gaukernel.setItemText(6, QCoreApplication.translate("SBO", u"Sum_RBF", None))
        self.comboBox_HB_Gaukernel.setItemText(7, QCoreApplication.translate("SBO", u"Sum_RQ", None))

        self.groupBox_HB_NN.setTitle(QCoreApplication.translate("SBO", u"NN Part", None))
        self.label_HB_NNbatchSize.setText(QCoreApplication.translate("SBO", u"Batch Size", None))
        self.label_HB_NNepochs.setText(QCoreApplication.translate("SBO", u"Epochs", None))
        self.label_HB_NNlearnrate.setText(QCoreApplication.translate("SBO", u"L-Rate", None))
        self.label_HB_NNweightdecay.setText(QCoreApplication.translate("SBO", u"Decay", None))
        self.label_HB_NNnodes.setText(QCoreApplication.translate("SBO", u"Nodes", None))
        self.label_each_layer_2.setText(QCoreApplication.translate("SBO", u"(each Layer)", None))
        self.label_HB_NNactivate.setText(QCoreApplication.translate("SBO", u"Activation", None))
        self.comboBox_HB_NNactivate.setItemText(0, QCoreApplication.translate("SBO", u"tanh", None))
        self.comboBox_HB_NNactivate.setItemText(1, QCoreApplication.translate("SBO", u"sigmoid", None))
        self.comboBox_HB_NNactivate.setItemText(2, QCoreApplication.translate("SBO", u"softplus", None))
        self.comboBox_HB_NNactivate.setItemText(3, QCoreApplication.translate("SBO", u"relu", None))
        self.comboBox_HB_NNactivate.setItemText(4, QCoreApplication.translate("SBO", u"linear", None))
        self.comboBox_HB_NNactivate.setItemText(5, QCoreApplication.translate("SBO", u"hardsigmoid", None))
        self.comboBox_HB_NNactivate.setItemText(6, QCoreApplication.translate("SBO", u"leaky relu", None))

    # retranslateUi
    def on_Model_changed(self):
        if self.comboBox_Model.currentIndex() == 0:
            self.stackedWidget_Model.setCurrentIndex(0)
        elif self.comboBox_Model.currentIndex() in (2, 3):
            self.stackedWidget_Model.setCurrentIndex(1)
        elif self.comboBox_Model.currentIndex() == 4:
            self.stackedWidget_Model.setCurrentIndex(2)
        else:
            self.stackedWidget_Model.setCurrentIndex(3)

    def on_Optimise_Method_changed(self):
        if self.comboBox_Optimise_Method.currentIndex() == 0:
            self.stackedWidget_Optimisation.setCurrentIndex(0)
        else:
            self.stackedWidget_Optimisation.setCurrentIndex(1)

    def on_Process_changed(self):
        if self.radioButton_Process.isChecked():
            self.pushButto_Process.show()
            self.textEdit_Process.show()
        else:
            self.pushButto_Process.hide()
            self.textEdit_Process.hide()
