# Win11 Edit Menu Enabler and Default Program Setter

This program enables the **"Edit"** option in the right-click context menu for specific file extensions in Windows 11 and allows users to configure the default program for editing those files by modifying the Windows Registry.

## Overview

Windows 11 allows configuration of default applications for various file types. However, the **"Edit"** menu item is not available by default for some extensions in the context menu. This program addresses that limitation by:
1. Adding the **"Edit"** option for selected file extensions.
2. Setting a default application (e.g., Kate, Notepad, etc.) for editing those files.

These changes are achieved through registry modifications.

---

## Features
- **Enable "Edit" Context Menu**: Adds an **"Edit"** option to the right-click context menu for supported file extensions like `.bat`, `.txt`, `.log`, etc.
- **Set Default Edit Program**: Configures the default program to open selected file extensions for editing.
- **Registry Modifications**: Automatically creates and updates the necessary registry keys for context menu actions.
- **Cross-Version Support**: Fully compatible with Windows 11 and its latest updates.

---

## Usage
1. **Download the Program**: Visit the [Releases page](https://github.com/osmanonurkoc/edit_menu_configurator/releases) to download the latest version of the program.
2. **Prepare Required Files**: Download the `reg` folder from the repository's master branch and place it in the program's root directory.
3. **Run the Program**: Follow the instructions to enable the "Edit" menu and set the default editor for your chosen file extensions.

---

## How It Works
1. **Registry Modification**:  
   The program modifies the registry keys for specific file extensions to:
   - Add the **"Edit"** option in the context menu.
   - Specify the default program for editing.

2. **Supported File Extensions**:
   - `.bat`
   - `.txt`
   - `.log`
   - And more (configurable via the program).

---

## License
This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).  
You are free to use, modify, and distribute this program under the terms of the GPL.

### Disclaimer
This program modifies the Windows Registry, which can affect system behavior. Use it at your own risk. Always back up your registry before making changes.

---

## Contributions
Contributions are welcome! If you'd like to add support for more file extensions or improve functionality, feel free to fork the repository and submit a pull request.

---

## Download
Head to the [Releases page](https://github.com/osmanonurkoc/edit_menu_configurator/releases) to get the latest version of the program.

## Reddit verification 
u/kawai_pasha