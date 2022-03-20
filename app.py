import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QHBoxLayout, QComboBox, QApplication, QMainWindow, QLabel, QLineEdit, QPushButton


class MainWindow(QMainWindow):

    def __init__(self, prod_df):
        super().__init__()
        self.prod_df = prod_df
        self.total_kcal = 0
        self.setGeometry(200, 200, 500, 500)


        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()


    def UiComponents(self):

        self.total_kcal_label = QLabel(self)
        self.total_kcal_label.setText("Podaj łączną ilośc kcal na posiłek:")
        self.total_kcal_label.move(10, 2)

        self.total_kcal_btn = QPushButton('Zapisz', self)
        self.total_kcal_btn.move(250, 2)

        # When the 'clicked' signal of the button is emitted, call some function (which acts as a slot):
        #self.total_kcal_btn.clicked.connect(self.get_total_kcal)

        self.total_kcal_btn.clicked.connect(self.get_total_kcal)

        print(self.total_kcal)








    # Function to pass the entered string along to the function from another file





        self.total_kcal_input = QLineEdit(self)
        self.total_kcal_input.move(200, 2)



        self.test_label = QLabel(self)
        self.test_label.move(100,100)
        self.test_label.setText(self.total_kcal_input.text())

        self.prod_combobox = QComboBox(self)

        # Adding elements to combobox
        for prod in self.prod_df["Product_name"]:
            self.prod_combobox.addItem(prod)

        # Adjust size to the max element len
        self.prod_combobox.adjustSize()
        self.prod_combobox.move(10, 40)
        self.prod_combobox.currentTextChanged.connect(self.combo_selected)

        # Label on combobox
        self.combo_label = QLabel(self)
        self.combo_label.setText("Wybierz produkt")
        self.combo_label.move(10, 14)


        # Label for selected product
        self.sel_combo_label = QLabel(self)
        self.sel_combo_label.move(180, 35)

        # combo_label.setText(self.combobox1.activated[str].connect(self.combo_text))
        # combobox1.adjustSize()

    def get_total_kcal(self):
        self.total_kcal = self.total_kcal_input.text()


    def combo_selected(self):
        item = self.prod_combobox.currentText()
        self.sel_combo_label.setText("Wybrałeś : " + item)






prod_df = pd.read_csv('produkty.csv')
app = QApplication(sys.argv)
w = MainWindow(prod_df)
w.show()
app.exec_()


exit()

        # self.setGeometry(200, 200, 500, 500)
        # combobox1 = QComboBox(self)
        #
        # for product in prod_df["Product_name"]:
        #     combobox1.addItem(product)
        #
        #     # zabrac to z konstruktora
        #
        #
        #
        #
        # combobox1.activated[str].connect(combo_text)
        # label = QLabel(self)
        # label.move(50, 30)
        # label.setText(self.combobox1.activated[str].connect(self.combo_text))
        # combobox1.adjustSize()
        #
        # def combo_text(self, text):
        #     self.text = self.combobox1.currentText()
















# class combodemo(QMainWindow):
#     def __init__(self, parent=None):
#         super(combodemo, self).__init__(parent)
#
#         # layout = QHBoxLayout()
#         self.cb = QComboBox()
#         self.cb.addItem("C")
#         self.cb.addItem("C++")
#         self.cb.addItems(["Java", "C#", "Python"])



    #     self.cb.currentIndexChanged(self.selectionchange())
    #
    #     layout.addWidget(self.cb)
    #     self.setLayout(layout)
    #     self.setWindowTitle("combo box demo")
    #
    # def selectionchange(self, i):
    #     print(
    #     "Items in the list are :")
    #
    #     for count in range(self.cb.count()):
    #         print(
    #         self.cb.itemText(count))
    #     print(
    #     "Current index", i, "selection changed ", self.cb.currentText())

#
# def main():
#     app = QApplication(sys.argv)
#     ex = combodemo()
#     ex.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()


# import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QHeaderView
#
# def window():
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     win.setGeometry(500, 200, 800, 600)
#     win.setWindowTitle("najs")
#
#
#
#     product_table = QTableWidget(win)
#
#     product_table.setMinimumWidth(450)
#     product_table.setMinimumHeight(100)
#     product_table.setRowCount(4)
#
#     # Column count
#     product_table.setColumnCount(2)
#
#     product_table.setItem(0, 0, QTableWidgetItem("Name"))
#
#
#     product_table.horizontalHeader().setStretchLastSection(True)
#     product_table.horizontalHeader().setSectionResizeMode(
#         QHeaderView.Stretch)
#
#
#
#     product_table.move(20, 20)
#     product_table.show()
#
#
#     win.show()
#     sys.exit(app.exec_())
#
#
#
# window()