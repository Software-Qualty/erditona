import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SystemTest(unittest.TestCase):
    def setUp(self):
        # Inisialisasi WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Tunggu sebelum menutup WebDriver
        self.driver.quit()

    def login(self, username, password):
        # Temukan input email dan password
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")

        # Masukkan nama pengguna dan kata sandi
        email_input.send_keys(username)
        password_input.send_keys(password)

        # Klik tombol login
        button = self.driver.find_element(By.ID, "button")
        button.click()

        # Tunggu alert muncul
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            # Tangani alert dengan menerima (klik OK)
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            # Jika alert tidak muncul dalam 10 detik, tangani sesuai kebutuhan
            pass

        print("Login berhasil")

    def deleteSentimen(self):
        # Klik tombol pertama
        button = self.driver.find_element(By.XPATH, "//a[@href='sentimen.html']")
        button.click()

        # Tunggu halaman dimuat
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='./topik.html?id=65fa7e3e7f64cff07549e983']")))

        # Klik kartu
        card = self.driver.find_element(By.XPATH, "//a[@href='./topik.html?id=65fa7e3e7f64cff07549e983']")
        card.click()

        # Tunggu tombol hapus dapat diklik
        delete_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button is-danger']")))
        delete_button.click()

        # Tunggu konfirmasi alert
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            # Tangani alert konfirmasi dengan menerima (klik OK)
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            # Jika alert tidak muncul dalam 10 detik, tangani sesuai kebutuhan
            pass

        # Tunggu alert kedua
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            # Tangani alert kedua dengan menerima (klik OK)
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            # Jika alert tidak muncul dalam 10 detik, tangani sesuai kebutuhan
            pass

        print("Sentimen berhasil dihapus")

    def test_deleteSentimen(self):
        # Buka halaman web
        self.driver.get("https://trensentimen.my.id/")

        # Login
        self.login("erdito@gmail.com", "fghjkliow")

        # Lakukan penghapusan sentimen
        self.deleteSentimen()

        print("Test berhasil")


if __name__ == "__main__":
    unittest.main()
