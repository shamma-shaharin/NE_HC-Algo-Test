class NEHCAlgorithmScore(object):
    def __init__(self, formId, NF_LOC_Adult_Value, LOC_Adult_Met_Reason, testStatus, expectedOutput, actualOutput):
        self.formId = formId
        self.NF_LOC_Adult_Value = NF_LOC_Adult_Value
        self.LOC_Adult_Met_Reason = LOC_Adult_Met_Reason
        self.testStatus = "PASS" if testStatus else "FAIL"
        self.expectedOutput = expectedOutput
        self.actualOutput = actualOutput
