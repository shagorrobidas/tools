# Shotter - A Collection of Web Tools

Shotter is a web application built with Django that provides a dashboard of useful, everyday tools. This project aims to be a simple, self-hosted suite of utilities.

![Dashboard Screenshot](https://via.placeholder.com/700x350.png?text=App+Screenshot+Here)

## ✨ Features

Currently, the following tools are available:

*   **🔗 URL Shortener:** Convert long, cumbersome URLs into short, easy-to-share links.
*   **🖼️ Images to PDF:** Upload multiple images and combine them into a single, downloadable PDF file.
*   **... and more to come!**

## 🛠️ Technology Stack

*   **Backend:** Python, Django
*   **Frontend:** HTML, Bootstrap 5
*   **Database:** SQLite (for development)

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.8+
*   pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/shotter.git
    cd shotter
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    *(Note: Make sure you have a `requirements.txt` file)*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.
