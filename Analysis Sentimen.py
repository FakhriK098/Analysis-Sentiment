from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
import Connection, Preprocessing, TFIDF, Trainning, Testing

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabAll = QtWidgets.QTabWidget(self.centralwidget)
        self.tabAll.setGeometry(QtCore.QRect(0, 0, 1080, 720))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabAll.setFont(font)
        self.tabAll.setObjectName("tabAll")
        self.dataset = QtWidgets.QWidget()
        self.dataset.setObjectName("dataset")
        self.edFileLocation = QtWidgets.QLineEdit(self.dataset)
        self.edFileLocation.setGeometry(QtCore.QRect(140, 20, 196, 28))
        self.edFileLocation.setObjectName("edFileLocation")
        self.btnBrowse = QtWidgets.QPushButton(self.dataset)
        self.btnBrowse.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.btnBrowse.setObjectName("btnBrowse")
        self.tblDataset = QtWidgets.QTableWidget(self.dataset)
        self.tblDataset.setEnabled(True)
        self.tblDataset.setGeometry(QtCore.QRect(20, 70, 1030, 580))
        self.tblDataset.setMaximumSize(QtCore.QSize(1030, 580))
        self.tblDataset.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed | QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked)
        self.tblDataset.setObjectName("tblDataset")
        self.tblDataset.setColumnCount(3)
        self.tblDataset.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblDataset.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDataset.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDataset.setHorizontalHeaderItem(2, item)
        self.tabAll.addTab(self.dataset, "")
        self.dictionary = QtWidgets.QWidget()
        self.dictionary.setObjectName("dictionary")
        self.tabKamusAlay = QtWidgets.QTabWidget(self.dictionary)
        self.tabKamusAlay.setGeometry(QtCore.QRect(20, 20, 1031, 671))
        self.tabKamusAlay.setObjectName("tabKamusAlay")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tblStopword = QtWidgets.QTableWidget(self.tab)
        self.tblStopword.setGeometry(QtCore.QRect(20, 60, 980, 360))
        self.tblStopword.setMaximumSize(QtCore.QSize(980, 360))
        self.tblStopword.setObjectName("tblStopword")
        self.tblStopword.setColumnCount(1)
        self.tblStopword.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblStopword.setHorizontalHeaderItem(0, item)
        self.tabKamusAlay.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tblKamusAlay = QtWidgets.QTableWidget(self.tab_3)
        self.tblKamusAlay.setGeometry(QtCore.QRect(20, 60, 980, 360))
        self.tblKamusAlay.setMaximumSize(QtCore.QSize(980, 360))
        self.tblKamusAlay.setObjectName("tblKamusAlay")
        self.tblKamusAlay.setColumnCount(2)
        self.tblKamusAlay.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblKamusAlay.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblKamusAlay.setHorizontalHeaderItem(1, item)
        self.tabKamusAlay.addTab(self.tab_3, "")
        self.tabAll.addTab(self.dictionary, "")
        self.dataPreprocessing = QtWidgets.QWidget()
        self.dataPreprocessing.setObjectName("dataPreprocessing")
        self.tblPreprocessing = QtWidgets.QTableWidget(self.dataPreprocessing)
        self.tblPreprocessing.setGeometry(QtCore.QRect(20, 69, 1030, 581))
        self.tblPreprocessing.setMaximumSize(QtCore.QSize(1030, 630))
        self.tblPreprocessing.setObjectName("tblPreprocessing")
        self.tblPreprocessing.setColumnCount(3)
        self.tblPreprocessing.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblPreprocessing.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPreprocessing.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPreprocessing.setHorizontalHeaderItem(2, item)
        self.btnProcess = QtWidgets.QPushButton(self.dataPreprocessing)
        self.btnProcess.setGeometry(QtCore.QRect(20, 30, 93, 28))
        self.btnProcess.setObjectName("btnProcess")
        self.tabAll.addTab(self.dataPreprocessing, "")
        self.tfidf = QtWidgets.QWidget()
        self.tfidf.setObjectName("tfidf")
        self.tblTFIDF = QtWidgets.QTableWidget(self.tfidf)
        self.tblTFIDF.setGeometry(QtCore.QRect(20, 69, 1030, 581))
        self.tblTFIDF.setMaximumSize(QtCore.QSize(1030, 650))
        self.tblTFIDF.setObjectName("tblTFIDF")
        self.tblTFIDF.setColumnCount(6)
        self.tblTFIDF.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblTFIDF.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTFIDF.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTFIDF.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTFIDF.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTFIDF.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTFIDF.setHorizontalHeaderItem(5, item)
        self.btnProsesTf = QtWidgets.QPushButton(self.tfidf)
        self.btnProsesTf.setGeometry(QtCore.QRect(20, 30, 93, 28))
        self.btnProsesTf.setObjectName("btnProsesTf")
        self.tabAll.addTab(self.tfidf, "")
        self.klasifikasi = QtWidgets.QWidget()
        self.klasifikasi.setObjectName("klasifikasi")
        self.frame = QtWidgets.QFrame(self.klasifikasi)
        self.frame.setGeometry(QtCore.QRect(20, 20, 440, 290))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.edLambda = QtWidgets.QLineEdit(self.frame)
        self.edLambda.setGeometry(QtCore.QRect(220, 10, 201, 22))
        self.edLambda.setObjectName("edLambda")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 35, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.edLearningRate = QtWidgets.QLineEdit(self.frame)
        self.edLearningRate.setGeometry(QtCore.QRect(220, 40, 201, 22))
        self.edLearningRate.setObjectName("edLearningRate")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 65, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.edSlack = QtWidgets.QLineEdit(self.frame)
        self.edSlack.setGeometry(QtCore.QRect(220, 70, 201, 22))
        self.edSlack.setObjectName("edSlack")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 95, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.edIterasiMax = QtWidgets.QLineEdit(self.frame)
        self.edIterasiMax.setGeometry(QtCore.QRect(220, 100, 201, 22))
        self.edIterasiMax.setObjectName("edIterasiMax")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 125, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.edAlpha = QtWidgets.QLineEdit(self.frame)
        self.edAlpha.setGeometry(QtCore.QRect(220, 130, 201, 22))
        self.edAlpha.setObjectName("edAlpha")
        self.btnCalculate = QtWidgets.QPushButton(self.frame)
        self.btnCalculate.setGeometry(QtCore.QRect(10, 240, 93, 28))
        self.btnCalculate.setObjectName("btnCalculate")
        self.label_7 = QtWidgets.QLabel(self.klasifikasi)
        self.label_7.setGeometry(QtCore.QRect(20, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tblTrainning = QtWidgets.QTableWidget(self.klasifikasi)
        self.tblTrainning.setGeometry(QtCore.QRect(20, 370, 1030, 280))
        self.tblTrainning.setMaximumSize(QtCore.QSize(1030, 280))
        self.tblTrainning.setObjectName("tblTrainning")
        self.tblTrainning.setColumnCount(5)
        self.tblTrainning.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblTrainning.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTrainning.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTrainning.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTrainning.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblTrainning.setHorizontalHeaderItem(4, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.klasifikasi)
        self.tableWidget_2.setGeometry(QtCore.QRect(470, 20, 581, 291))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.tabAll.addTab(self.klasifikasi, "")
        self.testing = QtWidgets.QWidget()
        self.testing.setObjectName("testing")
        self.label_6 = QtWidgets.QLabel(self.testing)
        self.label_6.setGeometry(QtCore.QRect(260, 185, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.edKalimat = QtWidgets.QLineEdit(self.testing)
        self.edKalimat.setGeometry(QtCore.QRect(350, 180, 401, 31))
        self.edKalimat.setObjectName("edKalimat")
        self.edSentiment = QtWidgets.QLabel(self.testing)
        self.edSentiment.setGeometry(QtCore.QRect(240, 240, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edSentiment.setFont(font)
        self.edSentiment.setObjectName("edSentiment")
        self.lineEdit = QtWidgets.QLineEdit(self.testing)
        self.lineEdit.setGeometry(QtCore.QRect(350, 235, 401, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.testing)
        self.pushButton.setGeometry(QtCore.QRect(660, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.edSentiment_2 = QtWidgets.QLabel(self.testing)
        self.edSentiment_2.setGeometry(QtCore.QRect(190, 330, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.edSentiment_2.setFont(font)
        self.edSentiment_2.setObjectName("edSentiment_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.testing)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 330, 401, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabAll.addTab(self.testing, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabAll.setCurrentIndex(0)
        self.tabKamusAlay.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.btnBrowse.clicked.connect(self.showData)

        item = self.tblDataset.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User"))
        item = self.tblDataset.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tweet"))
        item = self.tblDataset.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sentiment"))
        self.tabAll.setTabText(self.tabAll.indexOf(self.dataset), _translate("MainWindow", "Dataset"))
        item = self.tblStopword.horizontalHeaderItem(0)

        self.showDictionary()
        item.setText(_translate("MainWindow", "Stopword"))
        self.tabKamusAlay.setTabText(self.tabKamusAlay.indexOf(self.tab), _translate("MainWindow", "Stopwords"))
        item = self.tblKamusAlay.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Kata Alay"))
        item = self.tblKamusAlay.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Kata Normal"))
        self.tabKamusAlay.setTabText(self.tabKamusAlay.indexOf(self.tab_3), _translate("MainWindow", "Kamus Alay"))
        self.tabAll.setTabText(self.tabAll.indexOf(self.dictionary), _translate("MainWindow", "Dictionary"))
        item = self.tblPreprocessing.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User"))
        item = self.tblPreprocessing.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tweet"))
        item = self.tblPreprocessing.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sentiment"))
        self.btnProcess.setText(_translate("MainWindow", "Process"))
        self.btnProcess.clicked.connect(self.preprocessing)

        self.tabAll.setTabText(self.tabAll.indexOf(self.dataPreprocessing),
                               _translate("MainWindow", "Data Preprocessing"))
        item = self.tblTFIDF.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User"))
        item = self.tblTFIDF.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tweet"))
        item = self.tblTFIDF.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sentiment"))
        item = self.tblTFIDF.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "TF Dict"))
        item = self.tblTFIDF.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TF-IDF"))
        item = self.tblTFIDF.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "TF-IDF Vector"))
        self.btnProsesTf.setText(_translate("MainWindow", "Process"))
        self.btnProsesTf.clicked.connect(self.termfrequency)

        self.tabAll.setTabText(self.tabAll.indexOf(self.tfidf), _translate("MainWindow", "TF-IDF"))
        self.label.setText(_translate("MainWindow", "Lambda"))
        self.label_2.setText(_translate("MainWindow", "Learning Rate"))
        self.label_3.setText(_translate("MainWindow", "Slack"))
        self.label_4.setText(_translate("MainWindow", "Jumlah Iterasi"))
        self.label_5.setText(_translate("MainWindow", "Alpha"))
        self.btnCalculate.setText(_translate("MainWindow", "Calculate"))
        self.btnCalculate.clicked.connect(self.klasifikasiSVM)

        self.showTrainning()
        self.label_7.setText(_translate("MainWindow", "Result"))
        item = self.tblTrainning.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User"))
        item = self.tblTrainning.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tweet"))
        item = self.tblTrainning.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Label (Manual)"))
        item = self.tblTrainning.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Label (System)"))
        item = self.tblTrainning.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Keterangan"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lambda"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Learning Rate"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Slack"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Alpha"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Akurasi"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Precision"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Recall"))
        self.tabAll.setTabText(self.tabAll.indexOf(self.klasifikasi), _translate("MainWindow", "Klasifikasi"))
        self.label_6.setText(_translate("MainWindow", "Kalimat"))
        self.edSentiment.setText(_translate("MainWindow", "Sentiment"))
        self.pushButton.setText(_translate("MainWindow", "Prediksi"))

        self.pushButton.clicked.connect(self.testingKalimat)
        self.edSentiment_2.setText(_translate("MainWindow", "System Result :"))
        self.tabAll.setTabText(self.tabAll.indexOf(self.testing), _translate("MainWindow", "Testing"))

    def showData(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        self.all_data = pd.read_csv(filename[0], sep=',', engine='python')

        self.edFileLocation.setText(filename[0])
        numRows = len(self.all_data.index)
        self.tblDataset.setColumnCount(len(self.all_data.columns))
        self.tblDataset.setRowCount(numRows)
        self.tblDataset.setHorizontalHeaderLabels(self.all_data.columns)
        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tblDataset.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.all_data.iat[i, j])))
        self.tblDataset.resizeColumnsToContents()

    def showDictionary(self):
        self.stopword = Connection.showStopword()

        numRowsS = len(self.stopword.index)
        self.tblStopword.setColumnCount(len(self.stopword.columns))
        self.tblStopword.setRowCount(numRowsS)
        self.tblStopword.setHorizontalHeaderLabels(self.stopword.columns)
        for i in range(numRowsS):
            for j in range(len(self.stopword.columns)):
                self.tblStopword.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.stopword.iat[i, j])))
        self.tblStopword.resizeColumnsToContents()

        self.kamusAlay = Connection.showKamusAlay()
        numRowsK = len(self.kamusAlay.index)
        self.tblKamusAlay.setColumnCount(len(self.kamusAlay.columns))
        self.tblKamusAlay.setRowCount(numRowsK)
        self.tblKamusAlay.setHorizontalHeaderLabels(self.kamusAlay.columns)
        for i in range(numRowsK):
            for j in range(len(self.kamusAlay.columns)):
                self.tblKamusAlay.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.kamusAlay.iat[i, j])))
        self.tblKamusAlay.resizeColumnsToContents()

    def preprocessing(self):

        self.all_data['Tweet'] = self.all_data['Tweet'].apply(Preprocessing.preprocessing)
        numRows = len(self.all_data.index)
        self.tblPreprocessing.setColumnCount(len(self.all_data.columns))
        self.tblPreprocessing.setRowCount(numRows)
        self.tblPreprocessing.setHorizontalHeaderLabels(self.all_data.columns)
        for i in range(numRows):
            for j in range(len(self.all_data.columns)):
                self.tblPreprocessing.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.all_data.iat[i, j])))
        self.tblPreprocessing.resizeColumnsToContents()

    def termfrequency(self):
        self.all_data_new = TFIDF.tfidf(self.all_data)
        self.all_data_new = self.all_data_new[['User', 'Tweet', 'Sentiment', 'TF-IDF-Vec']]
        numRow = len(self.all_data_new.index)
        self.tblTFIDF.setColumnCount(len(self.all_data_new.columns))
        self.tblTFIDF.setRowCount(numRow)
        self.tblTFIDF.setHorizontalHeaderLabels(self.all_data_new.columns)
        for i in range(numRow):
            for j in range(len(self.all_data_new.columns)):
                self.tblTFIDF.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.all_data_new.iat[i, j])))
        self.tblTFIDF.resizeColumnsToContents()
        self.data_latih = self.all_data_new.sample(frac=0.8)
        self.data_uji = self.all_data_new.loc[~self.all_data_new.index.isin(self.data_latih.index)]
        self.data_latih.reset_index(inplace=True, drop=True)
        self.data_uji.reset_index(inplace=True, drop=True)

    def showTrainning(self):
        self.hasil = Connection.showHasil()
        numRow = len(self.hasil.index)
        self.tableWidget_2.setColumnCount(len(self.hasil.columns))
        self.tableWidget_2.setRowCount(numRow)
        self.tableWidget_2.setHorizontalHeaderLabels(self.hasil.columns)
        for i in range(numRow):
            for j in range(len(self.hasil.columns)):
                self.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.hasil.iat[i, j])))
        self.tableWidget_2.resizeColumnsToContents()

    def klasifikasiSVM(self):
        self.lamda = float(self.edLambda.text())
        self.learningRate = float(self.edLearningRate.text())
        self.slack = float(self.edSlack.text())
        self.alpha = float(self.edAlpha.text())
        self.iterasi = int(self.edIterasiMax.text())
        self.final_data, self.akurasi, self.prec, self.recall, self.fix_data = Testing.trainning(self.data_latih, self.data_uji,
                                                                                                 self.alpha, self.lamda,
                                                                                                 self.learningRate, self.slack,
                                                                                                 self.iterasi)
        Connection.inputHasil(self.lamda, self.learningRate, self.slack, self.iterasi, self.alpha, self.akurasi, self.prec,
                              self.recall)

        self.final_data = self.final_data[['User', 'Tweet', 'Label', 'System Result']]
        numRow = len(self.final_data.index)
        self.tblTrainning.setColumnCount(len(self.final_data.columns))
        self.tblTrainning.setRowCount(numRow)
        self.tblTrainning.setHorizontalHeaderLabels(self.final_data.columns)
        for i in range(numRow):
            for j in range(len(self.final_data.columns)):
                self.tblTrainning.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.final_data.iat[i, j])))
        self.tblTrainning.resizeColumnsToContents()

        self.showTrainning()

    def testingKalimat(self):
        self.kalimat = self.edKalimat.text()
        self.Label = self.lineEdit.text()
        self.hasilPrediksi = Testing.testing(self.kalimat, self.Label)
        self.lineEdit_2.setText(self.hasilPrediksi)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
