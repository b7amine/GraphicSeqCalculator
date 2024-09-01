class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'SEQUENTIAL'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1500, 1500)
        
        self.inpSize = None
        self.outpSize = None
        self.inlabels = []
        self.outlabels = []
        
        self.create_widgets()
        self.show()

    def create_widgets(self):
        # Create and position widgets using layout managers
        self.textboxin = QLineEdit(self)
        self.textboxin.setPlaceholderText("In")
        self.textboxin.resize(30, 30)

        self.textboxou = QLineEdit(self)
        self.textboxou.setPlaceholderText("Out")
        self.textboxou.resize(30, 30)

        self.buttonSet = QPushButton('OK', self)
        self.buttonSet.clicked.connect(self.on_click_set)
        
        # Layout management
        layout = QVBoxLayout()
        layout.addWidget(self.textboxin)
        layout.addWidget(self.textboxou)
        layout.addWidget(self.buttonSet)
        
        self.setLayout(layout)
        
    def on_click_set(self):
        try:
            self.inpSize = int(self.textboxin.text())
            self.outpSize = int(self.textboxou.text())
        except ValueError:
            print("Please enter valid integers for input and output sizes.")
            return
        
        self.setup_table()

    def setup_table(self):
        self.inlabels = [f"in{i}" for i in range(self.inpSize)]
        self.outlabels = [f"out{i}" for i in range(self.outpSize)]
        horiz = self​⬤
