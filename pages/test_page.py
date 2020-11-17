from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestPage:

    # Form 1
    TEST_BTN = (By.CSS_SELECTOR, 'button:nth-of-type(1)  .label')
    N_INPUT = (By.CSS_SELECTOR, '#data-case-1-name')
    I_INPUT = (By.ID, 'data-case-1-id')
    Y_INPUT = (By.ID, 'data-case-1-id')
    L_INPUT = (By.ID,  'data-case-1-id')

    # foprm 2
    L_NAME_INPUT = (By.ID, 'data--name')
    E_INPUT = (By.ID,  'data--1--rle')
    X_INPUT = (By.ID,  'data--1-sx')
    D_CHECKBOX = (By.ID, 'data--1--did')
    I_CHECKBOX = (By.ID, 'data--1-oici')



    #form 3
    SINPUT = (By.ID,  'data-t-1-name')

    #form 4
    WBINPUT = (By.ID,  'qa-daname1"')
    EXINPUT = (By.ID,  'qa-daid1"')
    COPE = (By.ID, 'qa-data=ype1"')
    IKBOX = (By.ID,  'qa-data=ation1"')
    CBOX = (By.ID,  'qa-data="ced1"')
    DAED = (By.ID, 'qa-data="datetlected1"')
    DATONED = (By.ID,  'qa-datasioned1"')

    #form 5
    EXPUT = (By.ID,  'qa-data=naname1"')
    COE = (By.ID,  'qa-data="cype1"')
    EXNPUT = (By.ID,  'qa-dataid1"')
    EXN_DATE = (By.ID,  'qa-dattdate1"')
    IS_BOX = (By.ID,  'qa-data="dation1"')
    CONCKBOX = (By.ID,  'qa-damed1"')

    #form 6
    RECPUT = (By.ID,  'qa-data="enaname1"')
    EXTUT = (By.ID,  'qa-data="exd1"')
    COPE =(By.ID,  'qa-data="cpe1"')
    DACTED = (By.ID,  'qa-data="mecollected1"')
    DASIONED = (By.ID,  'qa-data="datetccessioned1"')
    IS_VAECKBOX = (By.ID,  'qa-data="iidation1"')
    CONKBOX = (By.ID,  'qa-data="comed1"')


    #form 7
    TEPUT = (By.ID,  'qa-data="teame1"')
    TEPE = (By.ID,  'qa-data="pe1"')
    TEE = (By.ID, 'qa-data="tede1"')
    TTUS = (By.ID,  'qa-data="teatus1"')
    TEDATE = (By.ID,  'qa-data="uedate1"')

    #Buttons
    AOD_BTN = (By.ID,  'qa-data="add"')
    ADTN = (By.ID,  'qa-data="add"')
    ADA_BTN = (By.ID,  'qa-data="addr"')
    ADORDER_BTN = (By.ID,  'qa-data="addr"')
    ADAL_BTN = (By.ID,  'qa-data="adal"')

    SUBMIT_BTN = (By.ID,  'qa-data="submit"')


    def __init__(self, browser):
        self.browser = browser

    def frame_switch_css(self, css_selector):
        self.browser.switch_to.frame(self.browser.find_element_by_css_selector(css_selector))

    def frame_switch_name(self, name):
        self.browser.switch_to.frame(self.browser.find_element_by_name(name))

    def case_form(self, name, sid, stid, faid):
        name_input = self.browser.find_element(*self.N_INPUT)
        sid_input = self.browser.find_element(*self.I_INPUT)
        stid_input = self.browser.find_element(*self.E_INPUT)
        faid_input = self.browser.find_element(*self.L_INPUT)

        name_input.send_keys(name)
        sid_input.send_keys(sid)
        stid_input.send_keys(stid)
        faid_input.send_keys(faid)

