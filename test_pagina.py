from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_pagina_hola_mundo():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000")  # Asume que la página se sirve localmente en el puerto 8000
    assert "Hola Mundo" in driver.page_source
    driver.quit()
