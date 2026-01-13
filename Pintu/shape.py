import copy
import itertools
import matplotlib.pyplot as plt
import numpy as np


# 每块拼图为一组[x,y]坐标，要求先按y排序，再按x排序后第一个坐标为[0,0]
# 避免重复，使用tuple加set去重

# 归一化处理，排序并使第一个为[0,0]
def format(shape):
    shape = list(shape)
    shape.sort(key=(lambda e:(e[1], e[0])))
    x0, y0 = shape[0]
    return tuple((x - x0, y - y0) for x, y in shape)

# 顺时针旋转90度
def xuanzhuan(shape):
    return tuple((y, -x) for x, y in shape)

# 水平翻转
def fanzhuan(shape):
    return tuple((-x, y) for x, y in shape)

# 得到所有等价形状
def getall(shape):
    r = set()
    shape = format(shape)
    r.add(shape)
    shape = xuanzhuan(shape)
    r.add(format(shape))
    shape = xuanzhuan(shape)
    r.add(format(shape))
    shape = xuanzhuan(shape)
    r.add(format(shape))
    shape = fanzhuan(shape)
    r.add(format(shape))
    shape = xuanzhuan(shape)
    r.add(format(shape))
    shape = xuanzhuan(shape)
    r.add(format(shape))
    shape = xuanzhuan(shape)
    r.add(format(shape))
    return list(r)

class Shape:
    def __init__(self, shape):
        self.all = getall(shape)

class PingTu:
    def __init__(self, pos):
        self.m = len(pos)
        self.n = 0
        for s, t in pos:
            self.n = max(self.n, t + 1)
        self.pos = [[" "]*self.n for _ in range(self.m)]
        self.posNum = 0
        self.shapes={}
        self.shapeNum = 0

        for i, (s, t) in enumerate(pos):
            self.posNum += t - s + 1
            for j in range(s, t + 1):
                self.pos[i][j] = None

    def addShape(self, name, shape):
        s = Shape(shape)
        self.shapes[name] = s
        self.shapeNum += len(s.all[0])

    def step(self, sx, sy, ns):
        if not ns:
            self.r += 1

            self.solutions.append(copy.deepcopy(self.pingtu))
            return



        self.i += 1
        # 找到第一个空位
        x0 = sx
        y0 = sy
        while 1:
            v = self.pingtu[x0][y0]
            if not v:
                break

            x0 += 1
            if x0 == self.m:
                y0 += 1
                x0 = 0

        for i, name in enumerate(ns):
            shape = self.shapes[name]
            for si, s in enumerate(shape.all):
                # 看是否能填入
                for x, y in s:
                    x += x0
                    y += y0
                    if x < 0 or x >= self.m:
                        break
                    if y < 0 or y >= self.n:
                        break

                    v = self.pingtu[x][y]
                    if not v:
                        self.pingtu[x][y] = name
                    else:
                        break
                else:
                    _ns = ns[:i] + ns[i + 1:]
                    self.step(x0, y0, _ns)

                # 恢复值
                for x, y in s:
                    x += x0
                    y += y0
                    if x < 0 or x >= self.m:
                        break
                    if y < 0 or y >= self.n:
                        break

                    if self.pingtu[x][y] == name:
                        self.pingtu[x][y] = None
                    else:
                        break

    def pingtu(self, pos=[]):
        if self.shapeNum + len(pos) != self.posNum:
            print("数量不对:", self.posNum, self.shapeNum, len(pos))
            return

        self.pingtu = copy.deepcopy(self.pos)
        for x, y in pos:
            self.pingtu[x][y] = " "

        self.r = 0
        self.i = 0
        self.solutions = []   # 新增：存所有解
        self.holes = pos   # 记录空格坐标 [(mx,my),(dx,dy)]




        ns = list(self.shapes)
        self.step(0, 0, ns)

        print("搜索次数:", self.i, "解的数量:", self.r)
        self.show_pages()     # 搜索结束后统一可视化

    def show(self, board, title=None):
        """
        board: self.pingtu
        """
        h = len(board)
        w = len(board[0])

        # 每种拼块一个编号
        names = sorted({c for row in board for c in row if c not in (None, " ")})
        name2id = {name: i + 1 for i, name in enumerate(names)}

        grid = np.full((h, w), np.nan)

        for i in range(h):
            for j in range(w):
                v = board[i][j]
                if v == " ":
                    grid[i, j] = -1   # 禁区
                elif v is None:
                    grid[i, j] = 0    # 空
                else:
                    grid[i, j] = name2id[v]

        plt.figure()
        cmap = plt.cm.tab20
        cmap.set_bad(color="white")   # NaN
        plt.imshow(grid, cmap=cmap, interpolation="nearest")
        plt.xticks([])
        plt.yticks([])
        if title:
            plt.title(title)
        plt.show()

    def show_pages(self):
        import matplotlib.pyplot as plt
        import numpy as np
        from matplotlib.widgets import Button

        if not self.solutions:
            print("没有解")
            return

        idx = 0
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)

        def draw(i):
            ax.clear()
            board = self.solutions[i]

            h = len(board)
            w = len(board[0])

            names = sorted({c for row in board for c in row if c not in (None, " ")})
            name2id = {name: k + 1 for k, name in enumerate(names)}

            grid = np.full((h, w), np.nan)
            for x in range(h):
                for y in range(w):
                    v = board[x][y]
                    if v == " ":
                        grid[x, y] = np.nan
                    elif v is None:
                        grid[x, y] = 0
                    else:
                        grid[x, y] = name2id[v]

            ax.imshow(grid, interpolation="nearest")
            ax.set_title(f"Solution {i+1} / {len(self.solutions)}")
            ax.set_xticks([])
            ax.set_yticks([])
            # ===== 在空格位置写 月 / 日 =====
            if hasattr(self, "holes") and hasattr(self, "labels"):
                for (x, y), text in zip(self.holes, self.labels):
                    ax.text(
                        y, x, str(text),
                        ha="center", va="center",
                        fontsize=16, fontweight="bold", color="black"
                    )
                    fig.canvas.draw_idle()

        draw(idx)

        axprev = plt.axes([0.25, 0.05, 0.15, 0.075])
        axnext = plt.axes([0.6, 0.05, 0.15, 0.075])

        bprev = Button(axprev, '← Prev')
        bnext = Button(axnext, 'Next →')

        def prev(event):
            nonlocal idx
            idx = (idx - 1) % len(self.solutions)
            draw(idx)

        def next(event):
            nonlocal idx
            idx = (idx + 1) % len(self.solutions)
            draw(idx)

        bprev.on_clicked(prev)
        bnext.on_clicked(next)

        plt.show()

        

        





