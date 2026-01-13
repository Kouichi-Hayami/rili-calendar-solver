import shape

rilie_w = shape.PingTu([[0,5],[0,5],[0,6],[0,6],[0,6],[0,6],[0,6],[4,6]])
rilie_w.addShape("T", [[0,0],[1,0],[2,0],[1,1],[1,2]])
rilie_w.addShape("L", [[0,0],[1,0],[2,0],[0,1],[0,2]])
rilie_w.addShape("l", [[0,0],[1,0],[0,1],[0,2],[0,3]])
rilie_w.addShape("b", [[0,0],[1,0],[0,1],[1,1],[0,2]])
rilie_w.addShape("|", [[0,0],[0,1],[0,2],[0,3]])
rilie_w.addShape("7", [[0,0],[0,1],[0,2],[1,0]])
rilie_w.addShape("n", [[0,0],[1,0],[1,1],[1,2],[0,2]])
rilie_w.addShape("Z", [[0,0],[1,0],[1,-1],[1,-2],[2,-2]])
rilie_w.addShape("z", [[0,0],[1,0],[1,-1],[2,-1]])
rilie_w.addShape("2", [[0,0],[1,0],[1,-1],[2,-1],[3,-1]])

rilie = shape.PingTu([[0,5],[0,5],[0,6],[0,6],[0,6],[0,6],[0,2]])
rilie.addShape("L", [[0,0],[1,0],[2,0],[0,1],[0,2]])
rilie.addShape("l", [[0,0],[1,0],[0,1],[0,2],[0,3]])
rilie.addShape("b", [[0,0],[1,0],[0,1],[1,1],[0,2]])
rilie.addShape("B", [[0,0],[1,0],[0,1],[1,1],[0,2],[1,2]])
rilie.addShape("n", [[0,0],[0,1],[1,1],[2,1],[2,0]])
rilie.addShape("t", [[0,0],[1,0],[2,0],[3,0],[2,1]])
rilie.addShape("Z", [[0,0],[1,0],[1,-1],[1,-2],[2,-2]])
rilie.addShape("2", [[0,0],[1,0],[1,-1],[2,-1],[3,-1]])

MONTH_POS = {
    1:(0,0), 2:(0,1), 3:(0,2), 4:(0,3), 5:(0,4), 6:(0,5),
    7:(1,0), 8:(1,1), 9:(1,2),10:(1,3),11:(1,4),12:(1,5),
}

DAY_POS = {
     1:(2,0),  2:(2,1),  3:(2,2),  4:(2,3),  5:(2,4),  6:(2,5),  7:(2,6),
     8:(3,0),  9:(3,1), 10:(3,2), 11:(3,3), 12:(3,4), 13:(3,5), 14:(3,6),
    15:(4,0), 16:(4,1), 17:(4,2), 18:(4,3), 19:(4,4), 20:(4,5), 21:(4,6),
    22:(5,0), 23:(5,1), 24:(5,2), 25:(5,3), 26:(5,4), 27:(5,5), 28:(5,6),
    29:(6,0), 30:(6,1), 31:(6,2),
}

MONTH_NUM_TO_NAME = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}

WEEK_POS = {
    1: (6, 3),  # Mon
    2: (6, 4),  # Tue
    3: (6, 5),  # Wed
    4: (6, 6),  # Thu
    5: (7, 4),  # Fri
    6: (7, 5),  # Sat
    7: (7, 6),  # Sun
}

WEEK_NUM_TO_NAME = {
    1: "Mon",
    2: "Tue",
    3: "Wed",
    4: "Thu",
    5: "Fri",
    6: "Sat",
    7: "Sun",
}


def main():
    m = int(input("请输入月份 (1-12): "))
    d = int(input("请输入日期 (1-31): "))

    if m not in MONTH_POS or d not in DAY_POS:
        print("非法日期")
        return

    w = input("请输入星期 (1=Mon ... 7=Sun，可留空): ").strip()

    # ========= 不输入星期 → 用 rilie =========
    if w == "":
        holes = [MONTH_POS[m], DAY_POS[d]]
        month_name = MONTH_NUM_TO_NAME[m]
        rilie.labels = [month_name, str(d)]
        rilie.pingtu([MONTH_POS[m], DAY_POS[d]])

        return

    # ========= 输入星期 → 用 rilie_w =========
    if not w.isdigit():
        print("星期请输入 1-7，或直接回车跳过")
        return

    w_num = int(w)
    if w_num not in WEEK_NUM_TO_NAME:
        print("星期请输入 1-7")
        return

    week_name = WEEK_NUM_TO_NAME[w_num]

    if w_num not in WEEK_POS:
        print("没有该星期的坐标，请检查 WEEK_POS")
        return

    holes = [
        MONTH_POS[m],
        DAY_POS[d],
        WEEK_POS[w_num]   # ✅ 这里一定是 (x, y)
    ]

    month_name = MONTH_NUM_TO_NAME[m]
    rilie_w.labels = [month_name, str(d), week_name]
    rilie_w.pingtu([MONTH_POS[m], DAY_POS[d], WEEK_POS[w_num]])




if __name__ == "__main__":
    main()

