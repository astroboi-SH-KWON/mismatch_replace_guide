import Utils

class Process:

    def __init__(self,prefix):
        self.path = prefix[0]
        # column
        self.col01 = prefix[1]
        self.col02 = prefix[2]
        self.col03 = prefix[3]
        self.col04 = prefix[4]
        self.col05 = prefix[5]
        self.col06 = prefix[6]
        self.col07 = prefix[7]
        self.col08 = prefix[8]
        self.col09 = prefix[9]

    """
    get_index_guide : get temp_dict by key(column00)
    :param
        prefix = [
            excel file path
            , column01
            , column02 
        ]
    :return
        dict object { guide : INDEX }
    """
    def get_index_guide(self):
        prefix = [
            self.path
            , ""
        ]
        utils = Utils.Util(prefix)
        excel_dict = utils.get_excel_to_dict()
        read_index = excel_dict[self.col01]
        read_quide = excel_dict[self.col02]

        idx = 0
        temp_dict = {}
        for guide in read_quide.values():
            temp_dict[guide] = read_index[idx]
            # print(guide +" ::: " +read_index[idx])
            idx = idx + 1
        return temp_dict

    """
    get_index_guide1 : get temp_dict by key(column00) 
    :param
        prefix = [
            excel file path
            , column01
            , column02 
        ]
    :return
        dict object { guide : INDEX }
    """
    def get_index_guide1(self):
        prefix = [
            self.path
            ,""
        ]
        read_excel = Utils.Util(prefix)
        read_index_guide = read_excel.get_excel()
        # read_index = read_index_guide['INDEX']
        # read_quide = read_index_guide['Guide (X19)']
        read_index = read_index_guide[self.col01]
        read_quide = read_index_guide[self.col02]
        idx = 0
        temp_dict = {}
        for guide in read_quide:
            temp_dict[guide] = read_index[idx]
            # print(guide +" ::: " +read_index[idx])
            idx = idx + 1
        return temp_dict

    """
    get_target_seq : 
    :param
        prefix = [
            excel file path
            , column01
            , column02 ...
        ]
    :return
        dict object { 
            key : ['index', 'barcode', guide , ea, 'lib_barcode', 'lib_quide', 'O', 'X', ([],num)]
            , 0 : ['A_GAAGTA_PAM_7', 'ATGTCATACATACTC', 'TGAGTGGGCTTAGGAGGGG' , 1, 'ATGTCATACATACTC', 'GGAGGGAGCTGGGTTTTAG', 'O', 'X', (['',''],3)]
         }
    """
    def get_target_seq(self):
        prefix = [
            self.path
            , ""
        ]
        utils = Utils.Util(prefix)
        excel_dict = utils.get_excel_to_dict()
        read_index  = excel_dict[self.col01]
        read_barcode  = excel_dict[self.col02]
        read_guide = excel_dict[self.col03]
        read_ea = excel_dict[self.col04]
        read_lib_barcode = excel_dict[self.col05]
        read_lib_quide = excel_dict[self.col06]
        read_barcode_ox = excel_dict[self.col07]
        read_guide_ox = excel_dict[self.col08]
        read_quide_index = excel_dict[self.col09]

        # idx = 0
        temp_dict = {}
        for i in range(len(read_index)):
            temp_dict[i] = [
                read_index[i]
                , read_barcode[i]
                , read_guide[i]
                , read_ea[i]
                , read_lib_barcode[i]
                , read_lib_quide[i]
                , read_barcode_ox[i]
                , read_guide_ox[i]
                , read_quide_index[i]
            ]
            # idx = idx + 1
        return temp_dict

    """
    mismatch : count mismatching number from main_str to str_list
    :param
        main_str : a string to match 
        str_list : string from list to match
        mismatch_cnt : standard of mismatching number
    :return
        count : the result of mismatch counting
    """
    def mismatch(self, main_str, str_list, mismatch_cnt):
        count = 0
        for i in range(0, len(main_str)):
            if main_str[i] != str_list[i]:
                count += 1
            # exit the loop if count is highert than mismatch_cnt
            if count > mismatch_cnt: break
        return count

    """
    get_data : 
    :param
        mismatch_cnt : standard of mismatching number
        list_dict
        target_dict
    :return
        dict object { 
            key : ['index', 'barcode', guide , ea, 'lib_barcode', 'lib_quide', 'O', 'X', ([],num)]
            , 0 : ['A_GAAGTA_PAM_7', 'ATGTCATACATACTC', 'TGAGTGGGCTTAGGAGGGG' , 1, 'ATGTCATACATACTC', 'GGAGGGAGCTGGGTTTTAG', 'O', 'X', (['',''],3)]
         }
    """
    def get_data(self, mismatch_cnt, list_dict, target_dict):
        for key in target_dict.keys():
            guide = target_dict[key][2]
            lib_guide = target_dict[key][5]
            mis_tmp = self.mismatch(guide, lib_guide, mismatch_cnt)
            if mis_tmp > mismatch_cnt:
                # print(guide + " >>> " + lib_guide)
                tmp_dict = {}
                for x19_guide in list_dict.keys():
                    tmp = self.mismatch(guide, x19_guide, len(guide))
                    if tmp in tmp_dict:
                        tmp_dict[tmp].append(list_dict[x19_guide])
                    else:
                        tmp_dict[tmp] = [list_dict[x19_guide]]
                # print("sorted(tmp_dict.items())")
                # print(sorted(tmp_dict.items()))
                target_dict[key][8] = reversed(sorted(tmp_dict.items())[0])
            else:
                target_dict[key][7] = "O"
                target_dict[key][8] = (["PCR ERROR"] , mis_tmp)
        return target_dict
