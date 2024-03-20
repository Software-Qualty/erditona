import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert



class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tambahkan penundaan waktu sebelum menutup WebDriver
        time.sleep(5)

        # Menutup WebDriver
        self.driver.quit()

    def login(self, username, password):

        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")

        # Memasukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        time.sleep(2)

        # Klik tombol Login
        # button = self.driver.find_element(By.ID, "btnLogin")

        button = self.driver.find_element(By.ID, "button")
        button.click()

        time.sleep(2)

        # Tunggu maksimal 10 detik hingga alert muncul
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # Menangani alert dengan mengonfirmasi (klik OK)
        alert = self.driver.switch_to.alert
        alert.accept()
    
    def deleteSentimen(self):

       # Klik button pertama
        button = self.driver.find_element(By.XPATH, "//a[@href='sentimen.html']")
        button.click()

        time.sleep(1)

        # Klik kartu terlebih dahulu
        card = self.driver.find_element(By.XPATH, "//a[@href='./topik.html?id=65ad744aeb898618200db243']")
        card.click()

        time.sleep(2)

        # Cari tombol delete
        delete_button = self.driver.find_element(By.XPATH, "//button[@class='button is-danger']")
        delete_button.click()

        time.sleep(2)
        # Tanggapi alert konfirmasi
        alert = Alert(self.driver)
        alert.accept() 

        time.sleep(2)
        alert = Alert(self.driver)
        alert.accept() 

        time.sleep(2)


    def test_deleteSentimen(self):
        # Membuka halaman web
        # self.driver.get("http://127.0.0.1:5501/")
        self.driver.get("https://trensentimen.my.id/")

        time.sleep(2)

        self.login("erdito@gmail.com", "fghjkliow")

        time.sleep(2)

        self.deleteSentimen()


if __name__ == "__main__":
    unittest.main()