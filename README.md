# Python.org Test Automation Project

**This project is a test automation framework** for the [Python.org](https://www.python.org/) website, built with **Selenium WebDriver** and **pytest**. It automates core site functionality, including navigation, search, downloads, documentation, and events pages.

## Project Structure

project_root/<br>
├── pages/<br>
│ ├── base_page.py<br>
│ ├── home_page.py<br>
│ ├── documentation_page.py<br>
│ ├── python_docs_page.py<br>
│ ├── downloads_page.py<br>
│ └── events_page.py<br>
├── tests/<br>
│ ├── conftest.py<br>
│ ├── test_home_page.py<br>
│ ├── test_documentation.py<br>
│ ├── test_downloads.py<br>
│ └── test_events.py<br>
├── reports/<br>
├── pytest.ini<br>
├── requirements.txt<br>
└── README.md<br>


## Features

- **Page Object Model (POM)** for maintainable, reusable page interactions  
- Test cases for:  
  - **Home page:** search functionality, navigation menu visibility  
  - **Documentation page:** button visibility and redirection  
  - **Downloads page:** latest Python release visibility  
  - **Events page:** current events list  
- Configurable browser support (**Chrome** and **Firefox**) via `--browser` pytest option  
- Test categorization with **pytest markers** (`smoke`, `search`, `navigation`, `downloads`, `events`, `docs`)  
- HTML report generation with **pytest-html**  

## Notes

- This is a practice/portfolio project for learning test automation, some improvements may be possible.

## Skills Demonstrated

- Test Automation with Selenium WebDriver
- Test organization using pytest, fixtures, and markers
- Page Object Model (POM) pattern
- Writing maintainable and reusable test scripts
- Cross-browser testing basics
- HTML report generation

## 🚀 Getting Started

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run tests**

By default, all tests run in Chrome. To run them in Firefox:

```bash
pytest --browser firefox
```

Generate html report:

```bash
pytest --browser firefox --html=reports/report.html
```

Run a specific test with marker:

```bash
pytest -m smoke --browser firefox
```
