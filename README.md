# Threat Tracker

Threat Tracker is a simple Flask-based web application that allows users to upload server log files, parses critical information like IP addresses, timestamps, and status codes, and displays the parsed logs for easy analysis.

## Features

- Upload and parse server log files (e.g., Apache logs)  
- Extract IP addresses, timestamps, and HTTP status codes  
- Store parsed logs in a SQLite database  
- View parsed logs in a clean, tabular web interface  
- Built with Python, Flask, and SQLAlchemy  

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/tacotony45/threat-tracker.git
   cd threat-tracker
