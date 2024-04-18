from selenium import webdriver

# WebDriver'ı başlat
driver = webdriver.Chrome()

# Web sayfasını aç
driver.get("https://www.example.com")

# JavaScript fonksiyonunu tanımla
js_script = """
function findElementLocator() {
    // Öğeyi bul
    var element = document.querySelector("#myElementID"); // Örneğin ID kullanarak
    // Öğenin locator'ünü döndür
    return element.outerHTML; // Örnek olarak HTML kodunu döndür
}

// JavaScript fonksiyonunu çağır ve sonucu döndür
return findElementLocator();
"""

# execute_script yöntemini kullanarak JavaScript fonksiyonunu çalıştır ve sonucu al
element_locator = driver.execute_script(js_script)

# Elde edilen locator'ü yazdır
print("Element Locator:", element_locator)

# WebDriver'ı kapat
driver.quit()
