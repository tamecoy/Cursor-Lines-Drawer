# Cursor Lines Drawer

This Python script utilizes the `win32gui`, `win32api`, and `pynput` libraries to draw vertical and horizontal lines on the desktop screen when the mouse is clicked. The red lines are drawn at the cursor position.

## Prerequisites

- Python installed
- Required Python packages: `pynput`, `pywin32`

## Usage

1. Install the required packages:

    ```bash
    pip install pynput pywin32
    ```

2. Run the script:

    ```bash
    python cursor_lines_drawer.py
    ```

3. Click on the desktop to draw lines at the cursor position.

## Code Overview

- **`draw_cursor_lines(x, y)`**: Draws vertical and horizontal red lines at the cursor position on the desktop.

- **`erase_cursor_lines()`**: Erases the previously drawn lines on the desktop.

- **`on_click(x, y, button, pressed)`**: Event handler triggered on mouse click. Draws lines on click and erases them on release.

- **`if __name__ == "__main__":`**: Initiates the script and starts the mouse listener.

Feel free to modify the script according to your preferences or integrate it into other projects.

**Note:** This script uses the `win32gui` library, which is Windows-specific.
