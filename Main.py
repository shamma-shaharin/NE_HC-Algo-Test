import unittest
from Service.NEHCAssessmentFormService import *
from Service.SectionSubmitService import *


class Test(unittest.TestCase):
    def test_submit_ne_hc_assessment_form(self):
        config = Read_Config()
        driver = Get_Driver(config)

        Login(driver, config)

        output = []

        with open(config["inputFilePath"]) as inputFile:
            inputRows = csv.DictReader(inputFile)

            for row in inputRows:
                formId = Create_Form(driver, config)
                Submit_Sections(driver, row)
                Submit_Form(driver, row, formId, output)

            Write_Output(output, config)


if __name__ == "__main__":
    unittest.main()
