from Utilitiy.Helper import *


def Submit_Section_A(driver, row):
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_B(driver, row):
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_C(driver, row):
    C1_Cog_Skills = driver.find_element_by_xpath(
        "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["C1_Cog_Skills"], 1) + "']")
    C1_Cog_Skills.click()

    C2a_Short_term = driver.find_element_by_xpath(
        "//input[@name='answers[1].refData' and @value='" + AdjustValue(row["C2a_Short_term"], 1) + "']")
    C2a_Short_term.click()

    C2b_Procedural = driver.find_element_by_xpath(
        "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["C2b_Procedural"], 1) + "']")
    C2b_Procedural.click()

    C2c_Situational = driver.find_element_by_xpath(
        "//input[@name='answers[3].refData' and @value='" + AdjustValue(row["C2c_Situational"], 1) + "']")
    C2c_Situational.click()

    C3a_Easily_dist = driver.find_element_by_xpath(
        "//input[@name='answers[4].refData' and @value='" + AdjustValue(row["C3a_Easily_dist"], 1) + "']")
    C3a_Easily_dist.click()

    C3b_Epis_disorg_speech = driver.find_element_by_xpath(
        "//input[@name='answers[5].refData' and @value='" + AdjustValue(row["C3b_Epis_disorg_speech"], 1) + "']")
    C3b_Epis_disorg_speech.click()

    C3c_Ment_func_varies = driver.find_element_by_xpath(
        "//input[@name='answers[6].refData' and @value='" + AdjustValue(row["C3c_Ment_func_varies"], 1) + "']")
    C3c_Ment_func_varies.click()

    C4_Acute_change_mental = driver.find_element_by_xpath(
        "//input[@name='answers[7].refData' and @value='" + AdjustValue(row["C4_Acute_change_mental"], 1) + "']")
    C4_Acute_change_mental.click()

    if row["C5_Change_dec_making"] == '8':
        C5_Change_dec_making = driver.find_element_by_xpath(
            "//input[@name='answers[8].refData' and @value='" + AdjustValue(row["C5_Change_dec_making"], -4) + "']")
    else:
        C5_Change_dec_making = driver.find_element_by_xpath(
            "//input[@name='answers[8].refData' and @value='" + AdjustValue(row["C5_Change_dec_making"], 1) + "']")
    C5_Change_dec_making.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_D(driver, row):
    D1_Makes_Self_Understood = driver.find_element_by_xpath(
        "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["D1_Makes_Self_Understood"], 0) + "']")
    D1_Makes_Self_Understood.click()

    D2_Understand_others = driver.find_element_by_xpath(
        "//input[@name='answers[1].refData' and @value='" + AdjustValue(row["D2_Understand_others"], 0) + "']")
    D2_Understand_others.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_E(driver, row):
    E3a = driver.find_element_by_xpath(
        "//input[@name='answers[14].refData' and @value='" + AdjustValue(row["E3a"], 0) + "']")
    E3a.click()

    E3b = driver.find_element_by_xpath(
        "//input[@name='answers[15].refData' and @value='" + AdjustValue(row["E3b"], 0) + "']")
    E3b.click()

    E3c = driver.find_element_by_xpath(
        "//input[@name='answers[16].refData' and @value='" + AdjustValue(row["E3c"], 0) + "']")
    E3c.click()

    E3d = driver.find_element_by_xpath(
        "//input[@name='answers[17].refData' and @value='" + AdjustValue(row["E3d"], 0) + "']")
    E3d.click()

    E3e = driver.find_element_by_xpath(
        "//input[@name='answers[18].refData' and @value='" + AdjustValue(row["E3e"], 0) + "']")
    E3e.click()

    E3f = driver.find_element_by_xpath(
        "//input[@name='answers[19].refData' and @value='" + AdjustValue(row["E3f"], 0) + "']")
    E3f.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_F(driver, row):
    F3 = driver.find_element_by_xpath(
        "//input[@name='answers[7].refData' and @value='" + AdjustValue(row["F3"], 0) + "']")
    F3.click()
    F4 = driver.find_element_by_xpath(
        "//input[@name='answers[8].refData' and @value='" + AdjustValue(row["F4"], 0) + "']")
    F4.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_G(driver, row):
    G1c_Manage_fin_Capacity = driver.find_element_by_xpath(
        "//input[@name='answers[5].refData' and @value='" + AdjustValue(row["G1c_Manage_fin_Capacity"], 1) + "']")
    G1c_Manage_fin_Capacity.click()

    G1d_Capacity = driver.find_element_by_xpath(
        "//input[@name='answers[7].refData' and @value='" + AdjustValue(row["G1d_Capacity"], 1) + "']")
    G1d_Capacity.click()

    G1e_Phone_use_Capacity = driver.find_element_by_xpath(
        "//input[@name='answers[9].refData' and @value='" + AdjustValue(row["G1e_Phone_use_Capacity"], 1) + "']")
    G1e_Phone_use_Capacity.click()

    G1g_Shopping_Capacity = driver.find_element_by_xpath(
        "//input[@name='answers[13].refData' and @value='" + AdjustValue(row["G1g_Shopping_Capacity"], 1) + "']")
    G1g_Shopping_Capacity.click()

    G1h_Transport_Capacity = driver.find_element_by_xpath(
        "//input[@name='answers[15].refData' and @value='" + AdjustValue(row["G1h_Transport_Capacity"], 1) + "']")
    G1h_Transport_Capacity.click()

    G2a_bathing = driver.find_element_by_xpath(
        "//input[@name='answers[16].refData' and @value='" + AdjustValue(row["G2a_bathing"], 0) + "']")
    G2a_bathing.click()  # Values UI & Backend - 0,1,2,3,4,5,6,8

    G2b_pers_hygiene = driver.find_element_by_xpath(
        "//input[@name='answers[17].refData' and @value='" + AdjustValue(row["G2b_pers_hygiene"], 0) + "']")
    G2b_pers_hygiene.click()

    G2c_dressing_upper = driver.find_element_by_xpath(
        "//input[@name='answers[18].refData' and @value='" + AdjustValue(row["G2c_dressing_upper"], 0) + "']")
    G2c_dressing_upper.click()

    G2d_dressing_lower = driver.find_element_by_xpath(
        "//input[@name='answers[19].refData' and @value='" + AdjustValue(row["G2d_dressing_lower"], 0) + "']")
    G2d_dressing_lower.click()

    G2e_walking = driver.find_element_by_xpath(
        "//input[@name='answers[20].refData' and @value='" + AdjustValue(row["G2e_walking"], 0) + "']")
    G2e_walking.click()

    G2f_locomotion = driver.find_element_by_xpath(
        "//input[@name='answers[21].refData' and @value='" + AdjustValue(row["G2f_locomotion"], 0) + "']")
    G2f_locomotion.click()

    G2g_transfer_toilet = driver.find_element_by_xpath(
        "//input[@name='answers[22].refData' and @value='" + AdjustValue(row["G2g_transfer_toilet"], 0) + "']")
    G2g_transfer_toilet.click()

    G2h_toilet_use = driver.find_element_by_xpath(
        "//input[@name='answers[23].refData' and @value='" + AdjustValue(row["G2h_toilet_use"], 0) + "']")
    G2h_toilet_use.click()

    G2j_eating = driver.find_element_by_xpath(
        "//input[@name='answers[25].refData' and @value='" + AdjustValue(row["G2j_eating"], 0) + "']")
    G2j_eating.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_H(driver, row):
    if row["H1_bladder_cont"] == '8':
        H1_bladder_cont = driver.find_element_by_xpath(
            "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["H1_bladder_cont"], -1) + "']")
    else:
        H1_bladder_cont = driver.find_element_by_xpath(
            "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["H1_bladder_cont"], 1) + "']")
    H1_bladder_cont.click()

    if row["H3_bowel_cont"] == '8':
        H3_bowel_cont = driver.find_element_by_xpath(
            "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["H3_bowel_cont"], -1) + "']")
    else:
        H3_bowel_cont = driver.find_element_by_xpath(
            "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["H3_bowel_cont"], 1) + "']")
    H3_bowel_cont.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_I(driver, row):
    I1a_Hip_Fracture = driver.find_element_by_xpath(
        "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["I1a_Hip_Fracture"], 0) + "']")
    I1a_Hip_Fracture.click()

    I1b_Other_Fracture = driver.find_element_by_xpath(
        "//input[@name='answers[1].refData' and @value='" + AdjustValue(row["I1b_Other_Fracture"], 0) + "']")
    I1b_Other_Fracture.click()

    I1c_Alzheimers = driver.find_element_by_xpath(
        "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["I1c_Alzheimers"], 0) + "']")
    I1c_Alzheimers.click()

    I1d_Dementia = driver.find_element_by_xpath(
        "//input[@name='answers[3].refData' and @value='" + AdjustValue(row["I1d_Dementia"], 0) + "']")
    I1d_Dementia.click()

    I1l_COPD = driver.find_element_by_xpath(
        "//input[@name='answers[11].refData' and @value='" + AdjustValue(row["I1l_COPD"], 0) + "']")
    I1l_COPD.click()

    I1m_CHF = driver.find_element_by_xpath(
        "//input[@name='answers[12].refData' and @value='" + AdjustValue(row["I1m_CHF"], 0) + "']")
    I1m_CHF.click()

    I1t_Cancer = driver.find_element_by_xpath(
        "//input[@name='answers[19].refData' and @value='" + AdjustValue(row["I1t_Cancer"], 0) + "']")
    I1t_Cancer.click()

    Other_Disease_Modal = driver.find_element_by_xpath("//input[@class='btn btn-default'][2]")
    Other_Disease_Modal.click()
    Sleep(0.5)

    I2_Diagnosis = driver.find_element_by_id("diagnosisModal_iI2Diagnosis")
    I2_Diagnosis.clear()
    I2_Diagnosis.send_keys(row["I2_Diagnosis"])

    I2_Disease_Code_Dropdown_btn = driver.find_element_by_xpath("//button[@data-id='diagnosisModal_iI2DiseaseCode']")
    I2_Disease_Code_Dropdown_btn.click()
    I2_Disease_Code_Option = driver.find_element_by_xpath(
        "//ul[@class='dropdown-menu inner']/li["
        + MapI2DiseaseCodeByValue(row["I2_Disease_Code"])
        + "]/a/span[@class='text']")
    I2_Disease_Code_Option.click()

    I2_Coding_System = driver.find_element_by_id(MapI2CodingSystemIdByValue(row["I2_Coding_System"]))
    I2_Coding_System.click()

    I2_ICD_Code = driver.find_element_by_id("diagnosisModal_iI2IcdCode")
    I2_ICD_Code.clear()
    I2_ICD_Code.send_keys(row["I2_ICD_Code"])

    Other_Disease_Modal_Continue_Btn = driver.find_element_by_xpath(
        "//div[@class='form-group col-sm-12']/button[@class='btn btn-default']")
    Other_Disease_Modal_Continue_Btn.click()
    Sleep(0.5)

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_J(driver, row):
    J3a_balance = driver.find_element_by_xpath(
        "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["J3a_balance"], 1) + "']")
    J3a_balance.click()

    J3b_balance = driver.find_element_by_xpath(
        "//input[@name='answers[3].refData' and @value='" + AdjustValue(row["J3b_balance"], 1) + "']")
    J3b_balance.click()

    J2_Recent_falls = driver.find_element_by_xpath(
        "//input[@name='answers[1].refData' and @value='" + AdjustValue(row["J2_Recent_falls"], 1) + "']")
    J2_Recent_falls.click()

    J3j_Aphasia = driver.find_element_by_xpath(
        "//input[@name='answers[11].refData' and @value='" + AdjustValue(row["J3j_Aphasia"], 1) + "']")
    J3j_Aphasia.click()

    J7a_Instability_of_cond = driver.find_element_by_xpath(
        "//input[@name='answers[30].refData' and @value='" + AdjustValue(row["J7a_Instability_of_cond"], 1) + "']")
    J7a_Instability_of_cond.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_K(driver, row):
    K2a_Nutritional_issues = driver.find_element_by_xpath(
        "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["K2a_Nutritional_issues"], 1) + "']")
    K2a_Nutritional_issues.click()

    K3_Nutritional_Intake = driver.find_element_by_xpath(
        "//input[@name='answers[6].refData' and @value='" + AdjustValue(row["K3_Nutritional_Intake"], 0) + "']")
    K3_Nutritional_Intake.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_L(driver, row):
    L1_Most_severe_pressure_ulcer = driver.find_element_by_xpath(
        "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["L1_Most_severe_pressure_ulcer"],
                                                                        0) + "']")
    L1_Most_severe_pressure_ulcer.click()

    L4_Major_Skin_Problems = driver.find_element_by_xpath(
        "//input[@name='answers[3].refData' and @value='" + AdjustValue(row["L4_Major_Skin_Problems"], 1) + "']")
    L4_Major_Skin_Problems.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_M(driver, row):
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_N(driver, row):
    N2a_Chemo = driver.find_element_by_xpath(
        "//input[@name='answers[8].refData' and @value='" + AdjustValue(row["N2a_Chemo"], 0) + "']")
    N2a_Chemo.click()

    N2b_Dialysis = driver.find_element_by_xpath(
        "//input[@name='answers[9].refData' and @value='" + AdjustValue(row["N2b_Dialysis"], 0) + "']")
    N2b_Dialysis.click()

    N2d_IV_medication = driver.find_element_by_xpath(
        "//input[@name='answers[11].refData' and @value='" + AdjustValue(row["N2d_IV_medication"], 0) + "']")
    N2d_IV_medication.click()

    N2f_radiation = driver.find_element_by_xpath(
        "//input[@name='answers[13].refData' and @value='" + AdjustValue(row["N2f_radiation"], 0) + "']")
    N2f_radiation.click()

    N2g_suctioning = driver.find_element_by_xpath(
        "//input[@name='answers[14].refData' and @value='" + AdjustValue(row["N2g_suctioning"], 0) + "']")
    N2g_suctioning.click()

    N2h_tracheostomy_care = driver.find_element_by_xpath(
        "//input[@name='answers[15].refData' and @value='" + AdjustValue(row["N2h_tracheostomy_care"], 0) + "']")
    N2h_tracheostomy_care.click()

    N2i_Transfusion = driver.find_element_by_xpath(
        "//input[@name='answers[16].refData' and @value='" + AdjustValue(row["N2i_Transfusion"], 0) + "']")
    N2i_Transfusion.click()

    N2j_Vent_resp = driver.find_element_by_xpath(
        "//input[@name='answers[17].refData' and @value='" + AdjustValue(row["N2j_Vent_resp"], 0) + "']")
    N2j_Vent_resp.click()

    N2k_Wound_care = driver.find_element_by_xpath(
        "//input[@name='answers[18].refData' and @value='" + AdjustValue(row["N2k_Wound_care"], 0) + "']")
    N2k_Wound_care.click()

    N2n_Turning_repos = driver.find_element_by_xpath(
        "//input[@name='answers[21].refData' and @value='" + AdjustValue(row["N2n_Turning_repos"], 0) + "']")
    N2n_Turning_repos.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_O(driver, row):
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_P(driver, row):
    P1_Areas_Inf_Help_d1 = driver.find_element_by_xpath(
        "//input[@name='answers[6].refData' and @value='" + AdjustValue(row["P1_Areas_Inf_Help_d1"], 0) + "']")
    P1_Areas_Inf_Help_d1.click()

    P1_Areas_Inf_Help_d2 = driver.find_element_by_xpath(
        "//input[@name='answers[7].refData' and @value='" + AdjustValue(row["P1_Areas_Inf_Help_d2"], 0) + "']")
    P1_Areas_Inf_Help_d2.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_Q(driver, row):
    Q1a_Home_Disrepair = driver.find_element_by_xpath(
        "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["Q1a_Home_Disrepair"], 1) + "']")
    Q1a_Home_Disrepair.click()

    Q1b_Home_Squalid = driver.find_element_by_xpath(
        "//input[@name='answers[1].refData' and @value='" + AdjustValue(row["Q1b_Home_Squalid"], 1) + "']")
    Q1b_Home_Squalid.click()

    Q1c_Home_Inad_heat_cool = driver.find_element_by_xpath(
        "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["Q1c_Home_Inad_heat_cool"], 1) + "']")
    Q1c_Home_Inad_heat_cool.click()

    Q1d_Home_Lack_pers_safe = driver.find_element_by_xpath(
        "//input[@name='answers[3].refData' and @value='" + AdjustValue(row["Q1d_Home_Lack_pers_safe"], 1) + "']")
    Q1d_Home_Lack_pers_safe.click()

    Q1e_Home_Lim_access = driver.find_element_by_xpath(
        "//input[@name='answers[4].refData' and @value='" + AdjustValue(row["Q1e_Home_Lim_access"], 1) + "']")
    Q1e_Home_Lim_access.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_R(driver, row):
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_S(driver, row):
    driver.find_element_by_name("_action_update_next").click()


# def Submit_Section_T(driver, row):
#     driver.find_element_by_name("_action_update_next").click()
