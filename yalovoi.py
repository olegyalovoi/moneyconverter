Код з попереднього уроку:

dodatok.py

class ConverterLogic:
    def __init__(self):
        self.rates = {
            'USD' : 1.0,
            'UAH' : 42.0,
            'EUR' : 0.85,
            "BTC" : 0.0000097
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        return amount * self.rates[to_currency] / self.rates[from_currency]


main.py

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from dodatok import ConverterLogic

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.logic = ConverterLogic()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Converter")
        self.resize(300,200)

        currencies = ["USD", "UAH", "EUR", "BTC"]

        self.amount_label = QLabel("Sum:")
        self.amount_input = QLineEdit()

        self.from_currency_label = QLabel("3 waluty:")
        self.from_currency_combo = QComboBox()

        self.from_currency_combo.addItems(currencies)

        self.to_currency_label = QLabel("To waluty:")
        self.to_currency_combo = QComboBox()
        self.to_currency_combo.addItems(currencies)

        self.result_label = QLabel("Result:")
        self.result_display = QLabel("0.00")

        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_currency)

        layout = QBoxLayout()

        layout.addLayout(self.create_hbox_layout(self.amount_label, self.amount_input))
        layout.addLayout(self.create_hbox_layout(self.from_currency_label, self.from_currency_combo))
        layout.addLayout(self.create_hbox_layout(self.to_currency_label, self.to_currency_combo))
        layout.addLayout(self.create_hbox_layout(self.result_label, self.result_display))

        layout.addWidget(self.convert_button)
                         
        self.setLayout(layout)
        self.aplly_styles()
        self.show()
    
    def create_hbox_layout(self, label, widget):
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(widget)
        return hbox
    def convert_currency(self):
        try:
            amount = float(self.amount_input.text())
            from_currency = self.from_currency_combo.currentText()
            to_currency = self.to_currency_combo.currentText()

            converted_amount = self.logic.convert(amount, from_currency, to_currency)
            self.result_display.setText(f'{converted_anmount:.2f}')
        except ValueError:
            self.show_error_message('Invalid Input')
    
    def show_error_message(self, title, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog = setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.exec_()

    def apply_styles(self):
        self.setStyleSheet('''
            QLabel {
                font_size: 14px;
            }
            QLineEdit {
                font-size: 14px;
            }
            QComboBox {
                font-size: 14px;
            }
            QPushButton {
                font_size: 14px;
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                bakground-color: #45ab049
            }
           ''')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CurrencyConverter()
    sys.exit(app.exec_())