import unittest

from Model.ErrorResponse import *
from Service.NEHCAssessmentFormService import *
from Service.SectionSubmitService import *


class Test(unittest.TestCase):
    def test_submit_ne_hc_assessment_form(self):
        config = Read_Config()
        driver = Get_Driver(config)

        Login(driver, config)

        output = []
        errorOutput = []

        with open(config["inputFilePath"]) as inputFile:
            inputRows = csv.DictReader(inputFile)
            rowNumber = 2

            for row in inputRows:
                try:
                    row = RemoveWhitespaces(row)
                    formId = Create_Form(driver, config)
                    Submit_Sections(driver, row)
                    Submit_Form(driver, row, formId, output, rowNumber)
                except Exception as ex:
                    errorOutput.append(ErrorResponse(formId, str(rowNumber), repr(ex)))
                finally:
                    rowNumber += 1

            if output.__len__() != 0:
                Write_Output(output, config)

            if errorOutput.__len__() != 0:
                Write_Error_Output(errorOutput, config)


if __name__ == "__main__":
    unittest.main()
