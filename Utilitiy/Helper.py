import csv
import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def Read_Config():
    with open('config.json') as config_file:
        return json.load(config_file)


def Get_Driver(config):
    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')

    if config["browser"] == "chrome":
        return webdriver.Chrome(options=options)
    elif config["browser"] == "firefox":
        return webdriver.firefox(options=options)
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')


def AdjustValue(actualValue, adjustmentValue):
    return str(int(actualValue) + adjustmentValue)


def Write_Output(output, config):
    outputFile = open(config["outputFilePath"], 'w', newline='')

    with outputFile:
        headers = ['Form_Id', 'Test_Status', 'Expected_Output', 'Actual_Output']
        writer = csv.DictWriter(outputFile, fieldnames=headers)
        writer.writeheader()

        for result in output:
            writer.writerow({'Form_Id': result.formId, 'Test_Status': result.testStatus,
                             'Expected_Output': result.expectedOutput, 'Actual_Output': result.actualOutput})


def Sleep(second):
    time.sleep(float(second))


def MapI2DiseaseCodeByValue(value):
    if value.lower() == "not present":
        return "2"
    elif value.lower() == "primary diagnosis/diagnoses for current stay":
        return "3"
    elif value.lower() == "diagnosis present receiving active treatment":
        return "4"
    elif value.lower() == "diagnosis present monitored but no active treatment":
        return "5"
    else:
        return "1"


def MapI2CodingSystemIdByValue(value):
    if value.lower() == "icd-10":
        return "1"
    elif value.lower() == "icd-9":
        return "2"
