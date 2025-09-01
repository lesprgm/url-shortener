# URL Shortener

A simple URL shortener web application built with Python and Flask.

## Features

- Shorten long URLs to a unique 8-character ID.
- Redirects shortened URLs to their original destination.
- Stores shortened URLs in a JSON file.
- Simple, clean user interface.
- URL validation to ensure proper formatting.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install Flask
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

   The application will be running at `http://127.0.0.1:5000`.

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Enter a long URL in the input field and click "Shorten".
3. The shortened URL will be displayed.
4. You can use the shortened URL to redirect to the original URL.

## File Structure

```
/
├── app.py           
├── storage.json     
├── static/
│   └── style.css    
└── templates/
    └── index.html   
```

# Created by Leslie Osei-Anane and Godfred Tekpor

