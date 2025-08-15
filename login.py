from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver path
chrome_path = r'C:\chromedriver-win64\chromedriver.exe'
service = Service(chrome_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    # Step 1: Open login page
    driver.get('https://presidencyuniversity.linways.com/ams/student/login')

    # Step 2: Login
    username = 'your roll-no'
    password = 'DD-MM-YYYY'

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    ).send_keys(username)

    driver.find_element(By.NAME, 'password').send_keys(password)

    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Sign in")]'))
    )
    sign_in_button.click()

    # Step 3: Wait for Attendance link and click it safely
    attendance_link = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'menu-group-anchor-STUDENT_SIDE_ATTENDANCE_MANAGEMENT'))
    )

    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", attendance_link)

    # Wait until clickable and click via JS to avoid interception
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'menu-group-anchor-STUDENT_SIDE_ATTENDANCE_MANAGEMENT'))
    )
    driver.execute_script("arguments[0].click();", attendance_link)

    # Step 4: Wait for Print button and click it
    print_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Print"]]'))
    )
    driver.execute_script("arguments[0].click();", print_button)

    print("✅ Attendance page opened and Print button clicked.")

    #Enter to quit the automation
    input("Press Enter to quit automation...")

finally:
    driver.quit()
