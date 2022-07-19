
class Find_solution():
    def __init__(self,lis_to_solve):
        self.list_ball_fs=[]
        self.lis_to_solve = lis_to_solve
        super(Find_solution, self).__init__()
        print("the original list is = ", self.lis_to_solve)
        self.likay = self.to_kayles(self.lis_to_solve)
        print("The Kayles list  =", self.likay)
        self.sol = self.nim(self.likay)
        print("sol =", self.sol)
        if self.sol == True:
            print("There is a winning list- You suppose to lose")
        else:
            self.find_sol(self.lis_to_solve)
    kayles= (0,	1,	2,	3,	1,	4,	3,	2,	1,	4,	2,	6, 4,	1,	2,	7,	1,	4,	3,	2,	1,	4,	6,	7,4, 1, 2, 8, 5, 4, 7, 2, 1, 8, 6, 7, 4, 1, 2, 3, 1, 4, 7, 2, 1, 8, 2, 7)
    nimber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(kayles)
    print(nimber)
    def nim(self,list):
        sxor = 0
        for i in range(len(list)):
            sxor = sxor ^ list[i]
    #    print("sxor = ", sxor)
        if sxor == 0:
            return True
        else:
            return False

    def calc_lists(self,lis):
        #  print(f"lis in calc = {lis}")
        # list_ball_fs = []
        self.list_ball_fs = []
        # Caculate list of balls=>list_ball and list of the number that point each ball=>list_of_i
        for i in range(len(lis)):
            #     print(f"len of lis in calc = {len(lis)}")
            if lis[i] == 0:
                self.list_ball_fs.append(0)
            else:  # item != 0
                for j in range(lis[i]):
                    self.list_ball_fs.append(1)
        print(f"list_balli in calc = {self.list_ball_fs}")
        return   self.list_ball_fs

    def to_kayles(self,orgList):
        self.likay = []
        for item in orgList:
            self.likay.append(self.kayles[item])
        return self.likay

    def find_sol(self, orglist):
        list_ball_org = []
        list_ball_new = []
#        print(f"len of kales = {len(kayles}")
        pointers_remove_buttons=[]
        pos_sol=False
        chknum  = max(orglist)
        for button in range(2): # button = 0 -> pick one button, else (1) -> pick 2 adjacent buttons
            if pos_sol == True: # That mean that there is a solution, so we finish to search
                break
            for number in range(len(orglist)):
                if pos_sol == True:  # That mean that there is a solution, so we finish to search
                    break
                chknum = orglist[number]
    #            print(f"chknum = {chknum}")
                for item in range(chknum-button):# check maxItem /maxItem-1 times for 1/2 buttons
                    slice1 = item
                    slice2 = chknum-item-button-1
                    pos = orglist.index(chknum)
                    listtst = orglist.copy()
                    if slice1 != 0:
                        listtst[pos]= slice1
                        listtst.insert(pos + 1, 0)
                        if button == 1 :
                            listtst.insert(pos + 1+button, 0)
                        if slice2 != 0:
                            listtst.insert(pos+2+button,slice2)
                        else:#slice2 = 0
                            pass
                    elif slice1 == 0:
                        if slice2 != 0:
                            listtst[pos] = slice1
                            if button == 1:
                                listtst.insert(pos + 1 + button, 0)
                            listtst.insert(pos + 1 + button, slice2)
                        else: #slice1 = 0 and slice2 = 0
                            listtst[pos] =0
                            if button == 1:
                                listtst.insert(pos,0)

      #              print("listtst5 = ", listtst)
                    liskal= self.to_kayles(listtst)
                    pos_sol = self.nim(liskal)
                    if pos_sol == True:
                        print(f"slice1 = {slice1}")
                        print(f"slice2 = {slice2}")
                        print(f"pos = {pos}")
                        print("From the original list take",button+1 , "button ", orglist)
                        print("Solution slice are : ",listtst)
                        print ("FOUND SOLUTION!!!!! GREAT")
                        list_ball_org = self.calc_lists(orglist)
                        print(f"orglist = {orglist}")
                        print(f"list_ball_org= {list_ball_org}")
                        print(f"listtst = {listtst}")
                        list_ball_new = self.calc_lists(listtst)
                        print(f"list_ball_new= {list_ball_new}")
                        for i in range(len(list_ball_org)):
                            if list_ball_org[i] != list_ball_new[i]:
                                pointers_remove_buttons.append(i)
                        for item in pointers_remove_buttons:
                            print(f"pointers_remove_buttons = {pointers_remove_buttons}")

                        return pointers_remove_buttons

        return [-1]


    def give_sol(self,listtst):
        return listtst

