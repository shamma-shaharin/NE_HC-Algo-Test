import urllib.parse as urlparse
from urllib.parse import parse_qs

from selenium.webdriver.support.ui import Select

from Model.NEHCAlgorithmScore import *
from Service.SectionSubmitService import *


def Login(driver, config):
    driver.get(config["baseUrl"] + config["loginAPI"])

    username = driver.find_element_by_id("loginName")
    username.clear()
    username.send_keys(config["userName"])

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(config["password"])

    providerCode = driver.find_element_by_name("providerCode")
    providerCode.clear()
    providerCode.send_keys(config["providerCode"])

    driver.find_element_by_name("submitButton").click()


def Create_Form(driver, config):
    driver.get(config["baseUrl"] + config["individualListAPI"])
    driver.get(config["baseUrl"] + config["createFormAPI"])

    # DropDown value select
    select = Select(driver.find_element_by_id('assessment.assessmentData.type'))
    select.select_by_value('NE_HC')

    select = Select(driver.find_element_by_id('assessment.assessmentData.assessmentVersion'))
    select.select_by_value('9.1.2')
    driver.find_element_by_name("_action_save").click()
    url = driver.current_url

    parsed = urlparse.urlparse(url)
    formId = parse_qs(parsed.query)['formId'][0]

    return formId


def Submit_Sections(driver, row):
    Submit_Section_A(driver, row)
    Submit_Section_B(driver, row)
    Submit_Section_C(driver, row)
    Submit_Section_D(driver, row)
    Submit_Section_E(driver, row)
    Submit_Section_F(driver, row)
    Submit_Section_G(driver, row)
    Submit_Section_H(driver, row)
    Submit_Section_I(driver, row)
    Submit_Section_J(driver, row)
    Submit_Section_K(driver, row)
    Submit_Section_L(driver, row)
    Submit_Section_M(driver, row)
    Submit_Section_N(driver, row)
    Submit_Section_O(driver, row)
    Submit_Section_P(driver, row)
    Submit_Section_Q(driver, row)
    Submit_Section_R(driver, row)
    Submit_Section_S(driver, row)
    # Submit_Section_T(driver, row)


def Submit_Form(driver, row, formId, output, rowNumber):
    driver.find_element_by_name("_action_update_show").click()
    driver.find_element_by_name("_action_submit").click()

    Get_Score_And_Determine_Output(driver, formId, output, row, rowNumber)

    driver.find_element_by_name("_action_confirm").click()


def Get_Score_And_Determine_Output(driver, formId, output, row, rowNumber):
    NF_LOC_Adult_Value = driver.find_elements_by_xpath(
        "//table[@class='table table-bordered table-striped ']/tbody/tr[1]/td[2]")[0].text
    NF_LOC_Adult_Value_Label = driver.find_elements_by_xpath(
        "//table[@class='table table-bordered table-striped ']/tbody/tr[1]/td[3]")[0].text

    LOC_Adult_Met_Reason_Value = driver.find_elements_by_xpath(
        "//table[@class='table table-bordered table-striped ']/tbody/tr[3]/td[2]")[0].text
    LOC_Adult_Met_Reason_Value_Label = driver.find_elements_by_xpath(
        "//table[@class='table table-bordered table-striped ']/tbody/tr[3]/td[3]")[0].text

    expectedOutput1 = row["Expected_Output_1"]
    expectedOutput2 = row["Expected_Output_2"]
    testStatus = expectedOutput1.strip().lower() == NF_LOC_Adult_Value.strip().lower() and expectedOutput2.strip().lower() == LOC_Adult_Met_Reason_Value.strip().lower()
    output.append(
        NEHCAlgorithmScore(formId, NF_LOC_Adult_Value, LOC_Adult_Met_Reason_Value, testStatus, expectedOutput1,
                           NF_LOC_Adult_Value, expectedOutput2,
                           LOC_Adult_Met_Reason_Value, rowNumber))
