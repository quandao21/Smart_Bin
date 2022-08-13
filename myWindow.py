from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QChart, QChartView, QStackedBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from pyqtgraph import PlotWidget
import math


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("D:\PyQt\Smart_Bin_UI\Smart_Bin_ver1.ui", self)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        Type_1 = [12, 24, 32, 12, 42, 53, 34, 52, 63, 24, 43, 34]
        Type_2 = [22, 21, 22, 42, 22, 33, 54, 12, 53, 34, 23, 44]
        Type_3 = [32, 54, 12, 62, 22, 33, 44, 22, 43, 44, 23, 32]

        barSet_first_data_points = QBarSet('Type1')
        barSet_second_data_points = QBarSet('Type2')
        barSet_third_data_points = QBarSet('Type3')
        
        barSet_first_data_points.append(Type_1)
        barSet_second_data_points.append(Type_2)
        barSet_third_data_points.append(Type_3)

        self.series = QStackedBarSeries()
        self.series.append(barSet_first_data_points) 
        self.series.append(barSet_second_data_points)
        self.series.append(barSet_third_data_points)
        self.series.setLabelsVisible(True)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle('Monthly statistic')
        # self.chart.setAnimationOptions(QChart.SeriesA)

        month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        max_y_value = int(math.ceil(max(Type_1)/10)) + 20
        num = str([i for i in range(max_y_value)])
        self.axis_x = QBarCategoryAxis()
        self.axis_y = QBarCategoryAxis()
        self.axis_x.append(month)
        self.chart.setAxisX(self.axis_x)
        self.axis_y.append(num)
        self.chart.setAxisY(self.axis_y)

        self.chart_view = QChartView(self.chart)
        self.layout.addWidget(self.chart_view)



app = QApplication([])
window = UI()
window.show()
sys.exit(app.exec())