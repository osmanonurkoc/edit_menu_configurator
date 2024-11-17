import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, QWidget, QFileDialog, QMessageBox

class RegEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Edit Menu Configurator @osmanonurkoc")
        self.setGeometry(300, 200, 500, 200)

        # Main layout
        layout = QGridLayout()

        # Dropdown menu for .reg files
        layout.addWidget(QLabel("Select a file extension:"), 0, 0)
        self.reg_dropdown = QComboBox()
        layout.addWidget(self.reg_dropdown, 0, 1, 1, 2)
        self.populate_reg_files("./reg")

        # Program path selection
        layout.addWidget(QLabel("Program Path:"), 1, 0)
        self.program_path = QLineEdit()
        layout.addWidget(self.program_path, 1, 1)
        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.select_program)
        layout.addWidget(browse_btn, 1, 2)

        # Buttons for actions
        edit_btn = QPushButton("Edit and Register")
        edit_btn.clicked.connect(self.edit_and_register)
        layout.addWidget(edit_btn, 2, 1, 1, 2)

        # Set the main layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def populate_reg_files(self, folder):
        self.reg_dropdown.clear()
        if not os.path.exists(folder):
            QMessageBox.critical(self, "Error", f"The folder '{folder}' does not exist.")
            return

        reg_files = [f for f in os.listdir(folder) if f.endswith(".reg")]
        if reg_files:
            self.reg_dropdown.addItems([os.path.splitext(f)[0] for f in reg_files])
        else:
            QMessageBox.warning(self, "No Files", "No .reg files found in the './reg' folder.")

    def select_program(self):
        program, _ = QFileDialog.getOpenFileName(self, "Select Program Executable", "", "Executable Files (*.exe)")
        if program:
            self.program_path.setText(program)

    def edit_and_register(self):
        reg_file_name = self.reg_dropdown.currentText()
        if not reg_file_name:
            QMessageBox.warning(self, "Warning", "Please select a .reg file to edit.")
            return

        if not self.program_path.text():
            QMessageBox.warning(self, "Warning", "Please specify a program path.")
            return

        # Add the .reg extension back to the filename
        reg_file = os.path.join("./reg", reg_file_name + ".reg")
        program_path = self.program_path.text()

        # Replace single slashes (/) with double backslashes (\\) in the program path
        program_path = program_path.replace("/", "\\\\")  # Double backslashes for registry path

        # Add one backslash at the end of the path if not present
        if not program_path.endswith("\\"):
            program_path += "\\"

        # Read and modify the .reg file
        try:
            with open(reg_file, "r", encoding="utf-16le") as file:
                content = file.read()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to read the .reg file: {e}")
            return

        # Replace the placeholder in the reg file with the correctly formatted program path
        modified_content = content.replace("$PROGRAM", program_path)

        # Save the modified content back to a temporary file
        temp_file_path = os.path.join(os.getcwd(), "generated_temp.reg")
        with open(temp_file_path, "w", encoding="utf-16le") as temp:
            temp.write(modified_content)

        # Print out the path of the generated reg file for debugging
        print(f"Generated .reg file location: {temp_file_path}")

        # Register the .reg file
        try:
            subprocess.run(["reg", "import", temp_file_path], check=True)
            QMessageBox.information(self, "Success", f"The registry file has been imported successfully.")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Failed to import the registry file: {str(e)}")
        finally:
            os.remove(temp_file_path)  # Delete the temp file after use

if __name__ == "__main__":
    app = QApplication([])
    window = RegEditorApp()
    window.show()
    app.exec_()
