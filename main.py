import sys
import logicmin
import itertools
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, \
    QTableWidget, QTableWidgetItem, QLineEdit, QTextEdit

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

        global inpSize, outpSize, inlabels, outlabels, pblties

        # Input and Output Text Boxes
        self.textboxin = QLineEdit(self)
        self.textboxin.setPlaceholderText("In")
        self.textboxin.move(410, 600)
        self.textboxin.resize(30, 30)

        self.textboxou = QLineEdit(self)
        self.textboxou.setPlaceholderText("Out")
        self.textboxou.move(442, 600)
        self.textboxou.resize(30, 30)

        # OK Button
        self.buttonSet = QPushButton('OK', self)
        self.buttonSet.move(410, 630)
        self.buttonSet.resize(60, 40)
        self.buttonSet.clicked.connect(self.on_click_set)
        self.show()

    def on_click_set(self):
        global inpSize, outpSize, inlabels, outlabels, pblties

        inpSize = int(self.textboxin.text())
        outpSize = int(self.textboxou.text())
        self.textboxou.hide()
        self.textboxin.hide()
        self.buttonSet.hide()

        inlabels = ["in" + str(i) for i in range(inpSize)]
        outlabels = ["out" + str(i) for i in range(outpSize)]
        horiz = inlabels + outlabels

        pblties = 2 ** inpSize

        # Data Table Setup
        self.datatable = QTableWidget(self)
        self.datatable.setColumnCount(inpSize + outpSize)
        self.datatable.setRowCount(pblties)
        self.datatable.setHorizontalHeaderLabels(horiz)
        self.datatable.resize(1250, 600)
        self.datatable.show()

        # Fill Table with Input Combinations
        lik = list(itertools.product([0, 1], repeat=inpSize))
        for i in range(pblties):
            for j in range(inpSize + outpSize):
                if j >= inpSize:
                    self.datatable.setItem(i, j, QTableWidgetItem('x'))
                else:
                    self.datatable.setItem(i, j, QTableWidgetItem(str(lik[i][j])))

        # Send Button
        buttonEnv = QPushButton('SEND', self)
        buttonEnv.setToolTip('Generate Boolean Function')
        buttonEnv.move(700, 650)
        buttonEnv.clicked.connect(self.on_click_send)
        buttonEnv.show()

        # Output Text Box
        self.textbox = QTextEdit(self)
        self.textbox.setText("")
        self.textbox.move(900, 630)
        self.textbox.resize(280, 40)
        self.textbox.show()

    def on_click_send(self):
        global inpSize, outpSize, inlabels, outlabels, pblties

        self.datatable.clearSelection()
        self.datatable.selectAll()

        strsin = ["" for _ in range(pblties)]
        strsout = ["" for _ in range(pblties)]

        for item in self.datatable.selectedItems():
            if item.column() >= inpSize:
                strsout[item.row()] += item.text()
            else:
                strsin[item.row()] += item.text()

        # Logic Minimization and Output
        t = logicmin.TT(inpSize, outpSize)
        for k in range(pblties):
            t.add(strsin[k], strsout[k])
        sols = t.solve()
        self.textbox.setText(sols.printN(xnames=inlabels, ynames=outlabels, info=False))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
