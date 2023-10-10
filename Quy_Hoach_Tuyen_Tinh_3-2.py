import numpy as np
from scipy.optimize import linprog
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class TableView(QtWidgets.QTableWidget):
    def __init__(self, num_rows, num_columns, title, *args):
        super().__init__(*args)
        self.setRowCount(num_rows)
        self.setColumnCount(num_columns)
        self.setHorizontalHeaderLabels([f'Column {i + 1}' for i in range(num_columns)])
        self.setVerticalHeaderLabels([f'Constraint {i + 1}' for i in range(num_rows)])
        self.setData()
        self.setWindowTitle(title)  # Đặt tiêu đề cho TableView

    def setData(self):
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                # item.setTextAlignment(QtCore.Qt.AlignCenter)
                # item.setText(f'Item {i + 1}-{j + 1}')
                # self.setItem(i, j, item)

    def get_data(self):
        num_rows = self.rowCount()
        num_columns = self.columnCount()
        data = np.zeros((num_rows, num_columns))
        for row in range(num_rows):
            for col in range(num_columns):
                item = self.item(row, col)
                if item is not None:
                    data[row, col] = float(item.text())
        return data

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 564)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 331, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 85, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.so_bien = QtWidgets.QSpinBox(parent=self.groupBox)
        self.so_bien.setGeometry(QtCore.QRect(270, 50, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.so_bien.setFont(font)
        self.so_bien.setRange(2, 10)
        self.so_bien.setObjectName("so_bien")
        self.so_rang_buoc = QtWidgets.QSpinBox(parent=self.groupBox)
        self.so_rang_buoc.setGeometry(QtCore.QRect(270, 90, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.so_rang_buoc.setFont(font)
        self.so_rang_buoc.setRange(2, 10)
        self.so_rang_buoc.setObjectName("so_rang_buoc")
        self.datlai = QtWidgets.QPushButton(parent=self.groupBox,clicked=lambda: self.Dat_Lai())
        self.datlai.setGeometry(QtCore.QRect(10, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.datlai.setFont(font)
        self.datlai.setObjectName("datlai")
        self.chon = QtWidgets.QPushButton(parent=self.groupBox,clicked=lambda: self.createTableViews())
        self.chon.setGeometry(QtCore.QRect(230, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.chon.setFont(font)
        self.chon.setObjectName("chon")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 10, 321, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.thoat = QtWidgets.QPushButton(parent=self.groupBox_2,clicked=lambda: self.Thoat())
        self.thoat.setGeometry(QtCore.QRect(10, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.thoat.setFont(font)
        self.thoat.setObjectName("thoat")
        self.giai = QtWidgets.QPushButton(parent=self.groupBox_2,clicked=lambda: self.giai_bai_toan())
        self.giai.setGeometry(QtCore.QRect(180, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.giai.setFont(font)
        self.giai.setObjectName("giai")
        self.bien_toi_uu_x = QtWidgets.QTableView(parent=self.groupBox_2)
        self.bien_toi_uu_x.setGeometry(QtCore.QRect(0, 30, 300, 100))
        self.bien_toi_uu_x.setObjectName("bien_toi_uu_x")
        self.gia_tri_toi_uu_z = QtWidgets.QLabel(parent=self.groupBox_2)
        self.gia_tri_toi_uu_z.setGeometry(QtCore.QRect(70, 146, 121, 31))
        # self.gia_tri_toi_uu_z.setClearButtonEnabled(False)
        self.gia_tri_toi_uu_z.setObjectName("gia_tri_toi_uu_z")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Tạo QVBoxLayout cho TabWidget
        self.tab_layout = QtWidgets.QVBoxLayout(MainWindow)
        self.tab_layout.setGeometry(QtCore.QRect(10, 10, 200, 1200))

        self.tab_widget = QtWidgets.QTabWidget(MainWindow)
        self.tab_widget.setGeometry(QtCore.QRect(10, 280, 600, 220))
        self.tab_widget.setObjectName("tab_widget")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.table_views = []

        self.comboBoxOptimization = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxOptimization.setGeometry(QtCore.QRect(220, 135, 111, 31))
        self.comboBoxOptimization.setObjectName("comboBoxOptimization")
        self.comboBoxOptimization.addItem("max")
        self.comboBoxOptimization.addItem("min")


    def Dat_Lai(self):
        for table_view in self.table_views:
            index = self.tab_widget.indexOf(table_view)
            if index >= 0:
                self.tab_widget.removeTab(index)  # Loại bỏ TableView khỏi TabWidget
            table_view.deleteLater()  # Xóa TableView
        self.table_views = []

    def Thoat(self):
        sys.exit()

    def giai_bai_toan(self):
        # Lấy dữ liệu từ các QTableView
        A = self.table_views[1].get_data()  # Ví dụ: Lấy dữ liệu từ Table A
        c = self.table_views[0].get_data()  # Ví dụ: Lấy dữ liệu từ Table C
        b = self.table_views[2].get_data()  # Ví dụ: Lấy dữ liệu từ Table B

        optimization_type = self.comboBoxOptimization.currentText()
        if optimization_type == "max":
            c *= -1

        # Thực hiện giải bài toán tối ưu
        try:
            result = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None)] * len(c), method='highs')
        except:
            print("hàm vô nghiệm")
        self.update_table_and_edit(result.x, result.fun)

        # In kết quả
        # print("Biến tối ưu x:", result.x)
        # print("Giá trị tối ưu z:", result.fun)

    def update_table_and_edit(self, x, z):
        # Cập nhật dữ liệu vào QTableView
        model = QtGui.QStandardItemModel()
        for i, value in enumerate(x):
            item = QtGui.QStandardItem(str(value))
            model.setItem(0, i, item)
        self.bien_toi_uu_x.setModel(model)

        # Cập nhật giá trị tối ưu vào QLineEdit
        self.gia_tri_toi_uu_z.setText(str(z))

    def createTableViews(self):
        num_rows_a = self.so_rang_buoc.value()
        num_columns_a = self.so_bien.value()
        num_columns_c = self.so_bien.value()
        num_rows_b = self.so_rang_buoc.value()

        self.Dat_Lai()

        table_c = TableView(1, num_columns_c, "Chỉ số hàm mục tiêu c", self.tab_widget)
        self.tab_widget.addTab(table_c, "Chỉ số hàm mục tiêu c")
        self.table_views.append(table_c)

        # Tạo và thêm TableView A vào TabWidget
        table_a = TableView(num_rows_a, num_columns_a, "Ma Trận A", self.tab_widget)
        self.tab_widget.addTab(table_a, "Ma Trận A")
        self.table_views.append(table_a)

        # Tạo và thêm TableView C vào TabWidget

        # Tạo và thêm TableView B vào TabWidget
        table_b = TableView(num_rows_b, 1, "Vecto b", self.tab_widget)
        self.tab_widget.addTab(table_b, "Vecto b")
        self.table_views.append(table_b)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Giải bài toán quy hoạch tuyến tính"
                                                           " bằng phương pháp đơn hình"))
        self.groupBox.setTitle(_translate("MainWindow", "NHẬP DỮ LIỆU BÀI TOÁN"))
        self.label.setText(_translate("MainWindow", "NHẬP SỐ BIẾN:"))
        self.label_2.setText(_translate("MainWindow", "NHẬP SỐ RÀNG BUỘC:"))
        self.label_4.setText(_translate("MainWindow", "KẾT QUẢ:"))
        self.datlai.setText(_translate("MainWindow", "ĐẶT LẠI"))
        self.chon.setText(_translate("MainWindow", "CHỌN"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GIẢI BÀI TOÁN"))
        self.thoat.setText(_translate("MainWindow", "THOÁT"))
        self.giai.setText(_translate("MainWindow", "GIẢI"))
        self.label_3.setText(_translate("MainWindow", "NHẬP ĐÍCH:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        sys.exit(app.exec())
    except:
        print("exceping")