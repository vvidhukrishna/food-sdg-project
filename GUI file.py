import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class RecipeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window properties
        self.setWindowTitle("Recipe App")
        self.setGeometry(100, 100, 700, 600)
        self.setFixedSize(700, 600)
        self.setStyleSheet("background-color: #99e6ff;")

        # set font styles
        font = QFont("Playfair Display")
        font.setPointSize(18)
        font.setBold(True)

        # set font styles for buttons
        btn_font = QFont("Playfair Display")
        btn_font.setPointSize(16)
        btn_font.setBold(True)

        # create a frame for the user profile section
        self.profile_frame = QFrame(self)
        self.profile_frame.setGeometry(0, 0, 700, 150)
        self.profile_frame.setStyleSheet("background-color: #00ace6; border-radius: 10px; border: 1px solid blue;")
        self.profile_frame.setLineWidth(2)

        # create the user profile section labels
        self.profile_pic = QLabel(self.profile_frame)
        self.profile_pic.setPixmap(QPixmap("profile_pic.png").scaled(75, 75, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.profile_pic.setGeometry(25, 25, 75, 75)
        self.profile_pic.setStyleSheet("border-radius: 0px;")

        self.username_label = QLabel("Username", self.profile_frame)
        self.username_label.setGeometry(120, 35, 150, 60)
        self.username_label.setStyleSheet("font: bold 18pt 'PlayFair Display'; color: #0047b3;")

        self.reward = 0
        self.rewards_label = QLabel(f"Rewards: {self.reward}", self.profile_frame)
        self.rewards_label.setGeometry(500, 35, 180, 60)
        self.rewards_label.setStyleSheet("font: bold 18pt 'PlayFair Display'; color: #0047b3;")

        # set recipe fetch button
        self.fetch_btn = QPushButton("Fetch Recipe", self)
        self.fetch_btn.setGeometry(10, 160, 200, 50)
        self.fetch_btn.setFont(btn_font)
        self.fetch_btn.setStyleSheet("border: 2px solid green; background-color: #00cc88; color: #006652; border-radius: 25px;")

        # set ingredient list and add button
        self.ingredient_list = QListWidget(self)
        self.ingredient_list.setGeometry(320, 175, 350, 350)
        self.ingredient_list.setFont(font)

        self.add_btn = QPushButton("Add Ingredient", self)
        self.add_btn.setGeometry(400, 550, 200, 30)
        self.add_btn.setFont(btn_font)
        self.add_btn.setStyleSheet("border: 2px solid green; background-color: #00cc88; color: #006652; border-radius: 15px;")

        # connect signals and slots
        self.fetch_btn.clicked.connect(self.fetch_recipe)
        self.add_btn.clicked.connect(self.add_ingredient)

    def fetch_recipe(self):
        # TODO: add logic to fetch recipe based on ingredients

        # placeholder output
        recipe_list = ["Slow Cooker Apple Pork Tenderloin 673463", "Baked Cinnamon Apple Slices 633547",
                       "Traditional Apple Tart 663748", "Creamy Lime Pie Square Bites 715381",
                       "Napoleon - A Creamy Puff Pastry Cake 652952"]
        recipe_text = "\n".join(recipe_list)

        QMessageBox.information(self, "Recipe List", recipe_text)

    def add_ingredient(self):
        # TODO: add logic to add ingredient to the list
        item = QListWidgetItem("New Ingredient")
        self.ingredient_list.addItem(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RecipeApp()
    window.show()
    sys.exit(app.exec_())