from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from faker import Faker
import random
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GoogleFormSubmitter:
    def __init__(self, form_url):
        self.form_url = form_url
        # List of Marathi names in English
        self.marathi_names = [
            "Aarav Patil", "Sai Deshmukh", "Arjun Kulkarni", "Vedant Joshi", 
            "Soham Pawar", "Advait Deshpande", "Atharva More", "Pranav Bhosale",
            "Omkar Shinde", "Tanmay Wagh", "Swara Kadam", "Ananya Gokhale", 
            "Saanvi Jadhav", "Isha Kale", "Prisha Mane", "Vihaan Gaikwad",
            "Aditya Phadke", "Ishaan Mohite", "Kabir Sawant", "Reyansh Thakur",
            "Avani Patel", "Riya Shirke", "Aarohi Chavan", "Anvi Marathe",
            "Anika Dixit", "Myra Iyer", "Kiara Parikh", "Zara Nadkarni",
            "Aadya Kelkar", "Mishka Bhatt", "Vivaan Apte", "Shaurya Naik",
            "Dhruv Mhatre", "Arnav Sane", "Yash Gavande", "Rudra Bhide",
            "Sahil Karve", "Krish Ogale", "Dev Panse", "Rohan Sathe",
            "Kavya Deokar", "Diya Barve", "Aditi Godse", "Siya Khare",
            "Pari Dange", "Aashi Lele", "Navya Ranade", "Tara Nene",
            "Kyra Chitale", "Mira Bedekar"
        ]
        self.setup_driver()

    def setup_driver(self):
        """Configure Chrome with necessary options"""
        options = webdriver.ChromeOptions()
        # Comment out or remove the headless mode
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def generate_random_name(self):
        """Generate a random Marathi name"""
        return random.choice(self.marathi_names)

    def find_and_fill_name_field(self):
        """Find and fill the name input field"""
        try:
            # Look for text input field
            name_field = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
            )
            name_field.send_keys(self.generate_random_name())
        except TimeoutException:
            logging.error("Could not find name input field")
            raise

    def find_and_fill_multiple_choice(self):
        """Find and select random answers for all multiple choice questions"""
        try:
            # Find all multiple choice containers
            question_containers = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[role="radiogroup"]'))
            )

            for container in question_containers:
                # Find all radio buttons within this question
                options = container.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
                if options:
                    # Select a random option
                    random_option = random.choice(options)
                    self.driver.execute_script("arguments[0].scrollIntoView();", random_option)
                    random_option.click()
                    time.sleep(0.5)  # Small delay between selections

        except TimeoutException:
            logging.error("Could not find multiple choice questions")
            raise

    def submit_form(self):
        """Click the submit button"""
        try:
            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[role="button"]'))
            )
            submit_button.click()
            time.sleep(2)  # Wait for submission to complete
        except TimeoutException:
            logging.error("Could not find submit button")
            raise

    def single_submission(self):
        """Perform a single form submission"""
        try:
            self.driver.get(self.form_url)
            self.find_and_fill_name_field()
            self.find_and_fill_multiple_choice()
            self.submit_form()
            return True
        except Exception as e:
            logging.error(f"Error during submission: {str(e)}")
            return False

    def multiple_submissions(self, count=50):
        """Perform multiple form submissions"""
        successful = 0
        for i in range(count):
            try:
                if self.single_submission():
                    successful += 1
                    logging.info(f"Successfully completed submission {successful}/{count}")
                    # Random delay between submissions (2-5 seconds)
                    time.sleep(random.uniform(2, 5))
            except Exception as e:
                logging.error(f"Failed submission {i+1}: {str(e)}")

        logging.info(f"Completed {successful} successful submissions out of {count}")
        self.driver.quit()

def main():
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSddmVz6XdhuIN7H5e0HM9FwTvqqpCGmXoHYfk0lPOTgi3Kmvg/viewform"
    
    try:
        submitter = GoogleFormSubmitter(form_url)
        submitter.multiple_submissions(50)
    except Exception as e:
        logging.error(f"Fatal error: {str(e)}")

if __name__ == "__main__":
    main() 