import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Leningen:
    # Go to Leningen from menu
    mnu_FinanInstrumenten_xpath = "//span[contains(text(),'Financiële instrumenten')]"
    mnuitem_Leningen_xpath = "//div[3]//li[3]//span[1]"
    # New button
    btn_Nieuws_xpath = "//button[@class='primary']//i[@class='fa fa-plus-circle']"
    # Choice een sort from lening
    drd_Sortleningen_xpath = "//div[@class='editor-container']//select[@class='select-control']"
    btn_OK_xpath = "//button[contains(text(),'OK')]"
    # Fulling creen
    drd_ChoiceSortLeningen_xpath = "//div[contains(@data-field,'LoanType')]/select"
    btn_Geneer_xpath = "//button[@class='id-textbox-button']"
    txt_Nomiale_Waader_Xpath = "//div[contains(@data-field,'Nominal')]/input"
    drd_Relaties_xpath = "//div[contains(@data-field,'FinancierID')]/div/span"
    # Search number from Realties
    txt_NumberRealtie_xpath = "//*[@class='filter-row']/td[contains(@style,'top: 27px;')]/div[contains(@data-code-id,'NumericTextBox')]/input"
    td_Frirst_Number_xpath = "//tr[@class='first']/td[1]"
    td_NoRelatieIn_xpath = "//*[@class='grid-message']/tr/td[contains(text(),'Er zijn geen resultaten gevonden.')]"
    txt_StartDatum_xpath="//*[@data-field='StartDate']/input"
    btn_Sluiten_xpath="//button[@class='ui-datepicker-close ui-state-default ui-priority-primary ui-corner-all']"
    txt_Looptijd_xpath="//*[@data-field='Term']/input"
    btn_Opslaan_xpath="//span[contains(text(),'Opslaan')]"
    lbl_AutoIngvul_xpath="//div[contains(@class,'-container c2')]/div[1]/div/div/child::ul"
    def __init__(self, driver):
        self.driver = driver

    # Go to Leningen from menu
    def clickMenuFinanInstrumenten(self):
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH,self.mnu_FinanInstrumenten_xpath))).click()

    def clickMenuitemLeningen(self):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.XPATH,self.mnuitem_Leningen_xpath))).click()

    # New button
    def clickNieuws(self):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.XPATH,self.btn_Nieuws_xpath))).click()
        #self.driver.find_element_by_xpath(self.btn_Nieuws_xpath).click()

    # Choice een sort from lening
    def clickItemDrop(self, leningsort):
        element = WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.XPATH,self.drd_Sortleningen_xpath)))
        drp_element = Select(element)
        index = 0
        if leningsort == "Leningen" or leningsort == "leningen":
            index = 0
        elif leningsort == "Belegging" or leningsort == "belegging":
            index = 1
        elif leningsort == "Callgeld" or leningsort == "callgeld":
            index = 2
        elif leningsort == "CashMoney" or leningsort == "cashMoney":
            index = 3
        elif leningsort == "Deposito" or leningsort == "Deposito":
            index = 4
        else:
            index = 0
        drp_element.select_by_index(index)

    def clickOk(self):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.XPATH,self.btn_OK_xpath))).click()

    # Fulling creen
    # Cai menu nay la dynamic phai xem lai Xpath
    def clickLeningItem(self, values):
        element = WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.XPATH,self.drd_ChoiceSortLeningen_xpath)))  # Xpath can xem lai
        drp = Select(element)
        index = 0
        if values == 'Belegging' or values == 'belegging':
            index = 1
        else:
            index = 0
        drp.select_by_index(index)

    def click_Geneer(self):
        self.driver.find_element_by_xpath(self.btn_Geneer_xpath).click()

    def set_NominaleWaarde(self, value):
        self.driver.find_element_by_xpath(self.txt_Nomiale_Waader_Xpath).send_keys(value)

    def click_RealtieExpand(self):
        self.driver.find_element_by_xpath(self.drd_Relaties_xpath).click()
        time.sleep(1)

    def set_RealatieNumber(self, value):
        element = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, self.txt_NumberRealtie_xpath)))
        element.send_keys(value)
        return value

    def get_1stCel(self):
        element = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, self.td_Frirst_Number_xpath)))
        cel1 = element.text
        return cel1

    def click_1stCel(self):
        element = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, self.td_Frirst_Number_xpath)))
        element.click()

    def get_NoRelatie(self):
        element = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, self.td_NoRelatieIn_xpath)))
        cel1 = element.text
        return cel1
    def setStartDate(self,value):
        self.driver.find_element_by_xpath(self.txt_StartDatum_xpath).send_keys(value)
    def clickSluiten(self):
        element=WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.XPATH,self.btn_Sluiten_xpath)))
        element.click()
    def set_Looptijd(self,value):
        self.driver.find_element_by_xpath(self.txt_Looptijd_xpath).send_keys(value)
    def click_Opslaan(self):
        self.driver.find_element_by_xpath(self.btn_Opslaan_xpath).click()
    def get_WarningAutoIngevuld(self):
        list=[]
        list=self.driver.find_elements_by_xpath(self.lbl_AutoIngvul_xpath)
        lang=len(list)
        text=list[0].text
        warning='Eén of meerdere waarden zijn automatisch ingevuld. Controleer a.u.b. deze waarden en indien deze waarden correct zijn klik nogmaals op opslaan.'
        if text==warning:
            return True
        else:
            return False
    def get_WarningDateForm(self):
        list = []
        list = self.driver.find_elements_by_xpath(self.lbl_AutoIngvul_xpath)
        lang = len(list)
        text = list[0].text
        warning = 'Één of meerdere velden hebben een ongeldige waarde.'
        if text == warning:
            return True
        else:
            return False



