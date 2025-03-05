# Google Form Auto-Submitter Documentation

## Overview
This Python script automates Google Form submissions using Selenium WebDriver. It fills out forms with random Marathi names and multiple-choice answers.

## Features
- Automated form submission
- Random name and answer selection
- Configurable submission count
- Logging and random delays

## Prerequisites
- Python 3.6+
- Google Chrome
- ChromeDriver (matching your Chrome version)

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install selenium faker
   ```

## Usage
1. Update `form_url` in `form_submitter.py` with your form URL.
2. Run the script:
   ```bash
   python form_submitter.py
   ```

## Customization
- **Names List**: Edit `marathi_names` in the script.
- **Submission Count**: Change in `multiple_submissions()`.
- **Delays**: Adjust `time.sleep()` values.

## Form Compatibility
Works with forms having text input and multiple-choice questions.

## Important Notes
- For educational use only.
- Ensure compliance with Google's terms.
- Runs in visible mode for debugging.

## Troubleshooting
- Ensure ChromeDriver is in PATH.
- Verify form URL and ChromeDriver version.

## Logging
Logs successful submissions and errors with timestamps.

