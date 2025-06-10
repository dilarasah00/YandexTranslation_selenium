from pages.document_translate_page import  TranslatePage
import pytest
import json
import os

def get_json_file(json_file):
    with open(json_file,encoding= "utf-8") as file:
        return json.load(file)
    
def prepare_page_and_file(driver,files_path):
        driver.get("https://translate.yandex.com/tr/doc")
        page = TranslatePage(driver)
        test_data_folder = os.path.join(os.getcwd(),"data","files")
        full_path = os.path.join(test_data_folder,files_path["file_name"])
        return page,full_path

class TestTranslationPage:

    @pytest.mark.parametrize("files_path", get_json_file("data/valid_file_path.json"))
    def test_valid_file(self,driver,files_path):
        page, full_path = prepare_page_and_file(driver,files_path)
        page.choose_file(full_path)
        assert page.is_download_button_visible(), "indirme butonu gözükmüyor"
        assert page.get_status_message() == files_path["status_message"] ,"mesaj alınmadı"
        page.download_file()

        assert page.is_file_download(files_path["file_name"]), "indirilenlerde dosya bulunamadı"

    @pytest.mark.parametrize("files_path", get_json_file("data/invalid_files_path.json"))
    def test_invalid_file(self,driver,files_path):
        page, full_path = prepare_page_and_file(driver, files_path)
        page.choose_file(full_path)
        assert page.get_error_message() == files_path["status_message"] , "hata mesajında bir sorun var."


