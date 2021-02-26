class NEHCAlgorithmScore(object):
    def __init__(self, formId, NF_LOC_Adult_Value, LOC_Adult_Met_Reason, testStatus, expectedOutput1, actualOutput1, expectedOutput2, actualOutput2, rowNumber):
        self.formId = formId
        self.NF_LOC_Adult_Value = NF_LOC_Adult_Value
        self.LOC_Adult_Met_Reason = LOC_Adult_Met_Reason
        self.testStatus = "PASS" if testStatus else "FAIL"
        self.expectedOutput1 = expectedOutput1
        self.actualOutput1 = actualOutput1
        self.expectedOutput2 = expectedOutput2
        self.actualOutput2 = actualOutput2
        self.rowNumber = rowNumber



