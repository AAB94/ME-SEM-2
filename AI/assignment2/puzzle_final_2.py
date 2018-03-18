'''
@Authors

Avinesh Benjamin (2017H1030080H)
Saradhi Krishna (2017H1030081H)
Dr Anmol Dhiman (2017H1030087H)

'''

'''
In variables src,dest or west,east
index 0 always represents Cannibal
index 1 always represents Missionary
'''
'''
Used to eliminated repetition eg
   E(1,3)     W(3,0)    E(2,3) 
        /          /         /
       /          /         /
    W(3,0)    E(2,3)    W(3,0)
    
In the above example W(3,0) state has already been visited from East 
doing again will result in loop so they are removed     
'''

east_vis = {}
west_vis = {}
soln = ""
CAN = 0  # Cannibales
MIS = 0  # Missionary
goal = False

def dfs(src, dest, turn):
    global east_vis
    global west_vis
    global CAN
    global MIS
    global soln
    if src[0] + src[1] == CAN + MIS and turn == 'e':
        #soln = print_move(dest,src,"e",[0,0]) + soln
        global goal
        goal = True
    elif turn == 'w':
        neigh = moves(src, dest, turn)

        for n in neigh:
            if not goal:
                wx,wy,ex,ey = n[0],n[1],n[2],n[3]
                if not east_vis[ex][ey]:
                    east_vis[ex][ey] = True
                    dfs([ex, ey], [wx, wy], 'e')
                    if goal:
                        boat = n[4]
                        soln = print_move([wx, wy],dest,"  ---->  ",boat) + print_move([wx, wy],[ex, ey],"e",[0,0]) + soln

    elif turn == 'e':
        neigh = moves(src, dest, turn)
        for n in neigh:
            if not goal:
                wx,wy,ex,ey = n[0],n[1],n[2],n[3]
                if not west_vis[ex][ey]:
                    west_vis[ex][ey] = True
                    dfs([wx, wy], [ex, ey], 'w')
                    if goal:
                        boat = n[4]
                        soln = print_move(dest,[ex, ey],"  <----  ",boat) + print_move([wx, wy],[ex, ey],"w",[0,0]) + soln

def moves(src, dest, turn):
    m = [(1,1),(1,0),(0,1),(2,0),(0,2)]
    arr = []
    if turn == 'w':
        for i in m:
            wx = src[0] - i[0]
            wy = src[1] - i[1]
            ex = dest[0] + i[0]
            ey = dest[1] + i[1]
            if wx >= 0 and wy >= 0 and legal(wx,wy):
                if legal(ex,ey):
                    arr.append((wx,wy,ex,ey,(i[0],i[1])))

    elif turn == 'e':
         for i in m:
            wx = dest[0] + i[0]
            wy = dest[1] + i[1]
            ex = src[0] - i[0]
            ey = src[1] - i[1]
            if legal(wx,wy):
                if ex >= 0 and ey >= 0 and legal(ex,ey):
                    arr.append((wx,wy,ex,ey,(i[0],i[1])))
    return arr


def legal(c, m):
    if c == 0 and m == 0:
        return True
    elif m == 0:
        return True
    elif m != 0 and c <= m:
        return True
    elif c == 0:
        return True
    return False


def print_move(west, east, boat_dir, boat):
    soln = " West Bank "
    if west[0] == 0:
        soln = soln + "__"
    else:
        temp = ""
        for i in range(west[0]):
            temp = temp + "C"
        soln = soln + temp

    if west[1] == 0:
        soln = soln + "__"
    else:
        temp = ""
        for i in range(west[1]):
            temp = temp + "M"
        soln = soln + temp

    if boat[0] == 2:
        soln = soln + "\t\t" + "\_C_C_/  " + boat_dir +"\t\t"

    elif boat[1] == 2:
        soln = soln + "\t\t" + "\_M_M_/  " + boat_dir +"\t\t"

    elif boat[0] == 1 and boat[1] == 0:
        soln = soln + "\t\t" + "\_C___/  " + boat_dir +"\t\t"

    elif boat[0] == 0 and boat[1] == 1:
        soln = soln + "\t" + "\___M_/" + boat_dir +"\t\t"

    elif boat[0] == 1 and boat[1] == 1:
        soln = soln + "\t\t" + "\_C_M_/" + boat_dir +"\t\t"

    elif boat[0] == 0 and boat[1] == 0 and boat_dir == "w":
        soln = soln +" \\____/\t\t\t"

    elif boat[0] == 0 and boat[1] == 0 and boat_dir == "e":
        soln = soln +"\t\t\t \\____/ "

    if east[0] == 0:
        soln = soln + "__"
    else:
        temp = ""
        for i in range(east[0]):
            temp = temp + "C"
        soln = soln + temp

    if east[1] == 0:
        soln = soln + "__"
    else:
        temp = ""
        for i in range(east[1]):
            temp = temp + "M"
        soln = soln + temp
    soln = soln + " East Bank\n\n"
    return soln


def setVis():
    global CAN
    global MIS
    for i in range(CAN + 1):
        east_vis[i] = {}
        west_vis[i] = {}
        for j in range(MIS + 1):
            east_vis[i][j] = False
            west_vis[i][j] = False


def main():
    global MIS
    global CAN
    global soln
    #MIS,CAN = 5,3
    
    print("Enter Number of Missionaries and Cannibals as M C")
    MIS,CAN = input().split(" ")
    MIS,CAN = int(MIS),int(CAN)
    
    if MIS < CAN:
        print("Invalid Input")
    else:
        #
        setVis()
        #print start state
        print("\n",print_move([CAN, MIS],[0,0],"w",[0,0]),end="")
        #
        dfs([CAN, MIS], [0,0],'w')
        if goal:
            print(soln)
        else:
            print(" No Solution Possible :( ")


if __name__ == "__main__":
    main()
