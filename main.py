import sys


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.addbutton.setStyleSheet("background-color: blue")
        self.ui.deletebutton.setStyleSheet("background-color: blue")
        self.ui.save.setStyleSheet("background-color: blue")
        self.ui.addbutton.clicked.connect(self.add)
        self.ui.deletebutton.clicked.connect(self.delete)
        self.ui.save.clicked.connect(self.save)

    def add(self):
        product = self.ui.product.text()
        count = self.ui.count.text()
        if len(product) > 50:
            QMessageBox.warning(self, "Error", "Product name is too long")
        elif product == "":
            QMessageBox.warning(self, "Error", "Product name is empty")
        elif int(count) == 0:
            QMessageBox.warning(self, "Error", "Count is empty")
        else:
            self.ui.listofproducts.addItem(product + " " + count)


    def delete(self):
        if self.ui.listofproducts.currentRow() == -1:
            QMessageBox.warning(self, "Error", "You must select an item to delete")
        else:
            self.ui.listofproducts.takeItem(self.ui.listofproducts.currentRow())
            QMessageBox.information(self, "Success", "Item deleted successfully")

    def save(self):
        f = open("products.txt", "w")
        for i in range(self.ui.listofproducts.count()):
            f.write(self.ui.listofproducts.item(i).text() + "\n")
        f.close()
        QMessageBox.information(self, "Success", "Items saved successfully")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())



