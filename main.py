from time import clock

import Process
import Utils

############### start to set env ################
CNT = 2
# TARGET_FILE_PATH = "D:/000_WORK/KimNahye/20200304/Lib 10fg - 복사본.xlsx"
PREFIX_TARGET_ARR = [
    # "D:/000_WORK/KimNahye/20200304/Lib 10fg - 복사본 (2) - 복사본.xlsx"
    # "D:/000_WORK/KimNahye/20200304/Lib 10fg.xlsx"
    "D:/000_WORK/KimNahye/20200304/Genomic 10ng_다시.xlsx"
    , "INDEX"
    , "barcode"
    , "guide"
    , "EA"
    , "Library barcode"
    , "Library guide"
    , "barcode_ox"
    , "Guide_ox"
    , "guide_index"
    ]

# array for COMP_FILE_PATH, COL_NAMES of Guide.xlsx
PREFIX_COMP_ARR = [
    "D:/000_WORK/KimNahye/20200304/Guide.xlsx"
    , "INDEX"
    , "Guide (X19)"
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    , ""
    ]

# REULT_PATH = "D:/000_WORK/KimNahye/20200304/Lib 10fg_result_test"
# REULT_PATH = "D:/000_WORK/KimNahye/20200304/Lib 10fg_result_"
REULT_PATH = "D:/000_WORK/KimNahye/20200304/Genomic 10ng_다시_result_"
############### end setting env #################

def main():
    process1 = Process.Process(PREFIX_COMP_ARR)
    idx_guide_dict = process1.get_index_guide()
    process2 = Process.Process(PREFIX_TARGET_ARR)
    target_dict = process2.get_target_seq()
    # print(len(target_dict))
    # print(target_dict)
    result = process2.get_data(CNT,idx_guide_dict,target_dict)
    util = Utils.Util([REULT_PATH, result])
    util.make_excel()




start_time = clock()
print("start>>>>>>>>>>>>>>>>>>")
main()
print("::::::::::: %.2f seconds ::::::::::::::" % (clock() - start_time))