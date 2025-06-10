from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class TranslatePage:
    def __init__(self,driver):
        self.driver = driver
        self.pick_file_button = (By.CSS_SELECTOR,'[data-action="pickFile"]')
        self.upload_status_message = (By.CLASS_NAME,"dropMessage-text")
        self.error_message = (By.CLASS_NAME,"errorMessage-text")
        self.download_button =(By.CSS_SELECTOR,".button.button_view_primary.button_size_l")
        self.file_input = (By.CSS_SELECTOR,"input[type='file']")
        self.wait = WebDriverWait(driver,20)

    def choose_file(self,file_path):
        element = self.wait.until(EC.element_to_be_clickable(self.pick_file_button))
        element.click()
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dosya bulunamadı")
        self.wait.until(EC.presence_of_element_located(self.file_input)).send_keys(file_path)        

    def get_status_message(self):
        upload_message = self.wait_for_element_visible(self.upload_status_message).text
        return upload_message
        
    def get_error_message(self):
        error_message = self.wait_for_element_visible(self.error_message).text
        return error_message

    def wait_for_element_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def is_download_button_visible(self):
        return self.wait_for_element_visible(self.download_button).is_displayed()
    
    def download_file(self):
        self.wait_for_element_visible(self.download_button).click()

    def is_file_download(self,file_name):
        download_folder = os.path.join(os.path.expanduser("~"),"Downloads")
        file_path = os.path.join(download_folder,file_name)
        return os.path.exists(file_path)