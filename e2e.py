from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
CHROME_DRIVER_PATH = "/home/shay79il/bin/chromedriver"


def test_scores_service(url):
    """
    Its purpose is to test our web service.
    It will
    - get the application URL as an input,
    - open a browser to that URL,
    - select the score element in our web page,
    - check that it is a number between 1 and 1000
    - return a boolean value if it’s true or not.
    """
    my_driver = webdriver.Chrome(ChromeDriverManager().install())
    # my_driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    my_driver.get(url)
    score = int(my_driver.find_element_by_xpath('//*[@id="score0"]').text)
    print(score)
    return 0 < score < 1000


def main():
    """
    Call our tests function.
    The main function will return -1 as an OS exit
    code if the tests failed and 0 if they passed.
    """
    url = "http://127.0.0.1:5001/score"
    if test_scores_service(url):
        print("exit(0)")
        return exit(0)
    else:
        print("exit(-1)")
        return exit(-1)


main()