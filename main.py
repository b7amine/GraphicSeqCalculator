import sys
import logicmin
import itertools
from PyQt5.QtWidgets import QApplication,  QPushButton, QDialog,  \
    QTableWidget ,QTableWidgetItem ,QLineEdit,QTextEdit



class App(QDialog):




    def __init__(self):
        super().__init__()


        self.title = 'SEQUENTIAL'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 320
        self.initUI()


    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, 1500, 1500)
        global inpSize # cardinal variables d'entrées dans notre cas rf0 rf1  pr1 pr2 pr3
        global outpSize # cardinal variables de sorties pr1 pr2 pr3
        global inlabels # labels des variables
        global outlabels #
        global pblties # 2^(inpsize)

        self.textboxou = QLineEdit(self)
        self.textboxou.setPlaceholderText("Out")

        self.textboxou.move(442, 600)
        self.textboxou.resize(30, 30)


        self.textboxin = QLineEdit(self)
        self.textboxin.setText("")
        self.textboxin.setPlaceholderText("In")
        self.textboxin.move(410, 600)
        self.textboxin.resize(30, 30)


        inlabels = []
        outlabels = []
        global horiz




        self.buttonSet = QPushButton('OK', self)
        self.buttonSet.move(410, 630)
        self.buttonSet.resize(60,40)
        self.buttonSet.clicked.connect(self.on_lickvarou)

        self.show()




    def on_lickvarou(self):


        global inpSize
        global outpSize
        global inlabels
        global outlabels
        global pblties

        inlabels = []
        outlabels = []
        outpSize = int(self.textboxou.text())

        inpSize = int(self.textboxin.text())
        self.textboxou.hide()
        self.textboxin.hide()
        self.buttonSet.hide()
        horiz=[]
        pblties = 2 ** inpSize
        ii = 0
        while (ii < inpSize):
            inlabels.append("in" + str(ii))
            horiz.append("in" + str(ii))
            ii = ii + 1
        ii = 0
        while (ii < outpSize):
            outlabels.append("out" + str(ii))
            horiz.append("out" + str(ii))
            ii = ii + 1

        self.datatable = QTableWidget(parent=self)
        self.datatable.setColumnCount(inpSize + outpSize)
        self.datatable.setRowCount(pblties)
        self.datatable.setHorizontalHeaderLabels(horiz)
        self.datatable.show()
        QTableWidget.resize(self.datatable, 1250, 600)


        self.textbox = QTextEdit(self)
        self.textbox.setText("")
        self.textbox.move(900, 630)
        self.textbox.resize(280, 40)
        self.textbox.show()

        lik = list(itertools.product([0, 1],
                                     repeat=inpSize))
        i = 0
        while (i < pblties):
            j = 0
            while (j < (inpSize + outpSize)):
                if (j > inpSize - 1):

                    self.datatable.setItem(i, j, QTableWidgetItem('x'))
                else:
                    self.datatable.setItem(i, j, QTableWidgetItem(str(lik.__getitem__(i).__getitem__(j))))
                j = j + 1
            i = i + 1


        buttonEnv = QPushButton('ENVOYER', self)
        buttonEnv.setToolTip('This is an example button')
        buttonEnv.move(700, 650)
        buttonEnv.clicked.connect(self.on_lick)
        buttonEnv.show()




    def on_lick(self):
        global inpSize
        global outpSize
        global inlabels
        global outlabels
        global pblties
        print("hala")
        self.datatable.clearSelection()
        self.datatable.selectAll()
        strsin = ["" for x in range(pblties)]
        strsout = ["" for x in range(pblties)]

        z=0
        for currentQTableWidgetItem in self.datatable.selectedItems():
            if (currentQTableWidgetItem.column() > inpSize-1):
                strsout[currentQTableWidgetItem.row()]=strsout[currentQTableWidgetItem.row()]+currentQTableWidgetItem.text()
            else:
                strsin[currentQTableWidgetItem.row()]=strsin[currentQTableWidgetItem.row()]+currentQTableWidgetItem.text()






        k=0
        t = logicmin.TT(inpSize, outpSize)
        while(k<pblties):
            t.add(strsin[k],strsout[k])
            k=k+1
        sols = t.solve()
        self.textbox.setText(sols.printN(xnames=inlabels, ynames=outlabels, info=False))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
