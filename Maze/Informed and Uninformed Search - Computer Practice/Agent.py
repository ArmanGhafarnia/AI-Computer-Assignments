import colors
from queue import Queue


class Agent:
    def __init__(self, board):
        self.position = board.get_agent_pos()
        self.current_state = board.get_current_state()
        self.board = board

    def get_position(self):
        return self.position

    def set_position(self, position, board):
        self.position = position
        board.set_agent_pos(position)
        board.update_board(self.current_state)

    def percept(self, board):
        # perception :
        # sets the current state
        # Use get_current_state function to get the maze matrix. - make your state
        self.current_state = board.get_current_state()

        pass

    def move(self, direction, color):
        # make your next move based on your perception
        # check if the move destination is not blocked
        # if not blocked:
        # use red color to show visited tiles.
        # something like :
        # current_pos = self.get_position()
        x, y = direction[0], direction[1]
        self.board.colorize(x, y, color)

        # then move to destination - set new position
        # something like :
        # self.set_position(direction)
        pass

    def get_actions(self, cord, o_list, c_list, flag):
        actions = []
        x = cord[0]
        y = cord[1]
        o_list_temp = list()
        if flag:
            while (not o_list.empty()):
                o_list_temp.append(o_list.get())
        else:
            o_list_temp = o_list

        if x - 1 >= 0:
            if not self.current_state[x - 1][y].is_blocked():
                cord = (x - 1, y)
                if (cord not in o_list_temp):
                    if (cord not in c_list):
                        actions.append(cord)

        if y - 1 >= 0:
            if not self.current_state[x][y - 1].is_blocked():
                cord = (x, y - 1)
                if (cord not in o_list_temp):
                    if (cord not in c_list):
                        actions.append(cord)

        if x + 1 < 13:
            if not self.current_state[x + 1][y].is_blocked():
                cord = (x + 1, y)
                if (cord not in o_list_temp):
                    if (cord not in c_list):
                        actions.append(cord)

        if y + 1 < 13:
            if not self.current_state[x][y + 1].is_blocked():
                cord = (x,  y + 1)
                if (cord not in o_list_temp):
                    if (cord not in c_list):
                        actions.append(cord)
        # returns a list of valid actions

        if flag:
            for i in range(len(o_list_temp)):
                o_list.put(o_list_temp[i])

        return actions

    def bfs(self, environment):
        # now go on !
        self.percept(environment)
        o_list = Queue()
        c_list = list()
        agent_tile = self.position
        o_list.put(agent_tile)
        while (not o_list.empty()):
            tile = o_list.get()
            if self.current_state[tile[0]][tile[1]].isGoal:
                break
            self.move(tile, colors.red)
            c_list.append(tile)
            actions = self.get_actions(tile, o_list, c_list, True)
            for element in actions:
                o_list.put(element)
            for i in range(len(actions)):
                self.current_state[actions[i][0]][actions[i][1]].parent = tile

        itr = (12, 0)
        while self.current_state[itr[0]][itr[1]].parent != None:
            self.move(itr, colors.green)
            itr = self.current_state[itr[0]][itr[1]].parent
        self.move(itr, colors.green)
        # use green color and colorize method to show the path.
        pass

    def dfs(self, environment):
        self.percept(environment)
        o_list = list()
        c_list = list()
        agent_tile = self.position
        o_list.append(agent_tile)
        while (len(o_list) != 0):
            tile = o_list[len(o_list) - 1]
            if self.current_state[tile[0]][tile[1]].isGoal:
                break
            self.move(tile, colors.red)
            c_list.append(tile)
            o_list.pop()
            actions = self.get_actions(tile, o_list, c_list, False)
            o_list.extend(actions)
            for i in range(len(actions)):
                self.current_state[actions[i][0]][actions[i][1]].parent = tile

        itr = (12, 0)
        while self.current_state[itr[0]][itr[1]].parent != None:
            self.move(itr, colors.green)
            itr = self.current_state[itr[0]][itr[1]].parent
        self.move(itr, colors.green)

    def a_star(self, environment):
        self.percept(environment)
        o_list = list()
        c_list = list()
        agent_tile = self.position
        o_list.append(agent_tile)
        while (len(o_list) != 0):
            n = len(o_list)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if self.current_state[o_list[j][0]][o_list[j][1]].h > self.current_state[o_list[j + 1][0]][o_list[j + 1][1]].h:
                        o_list[j], o_list[j + 1] = o_list[j + 1], o_list[j]

            tile = o_list[0]
            if self.current_state[tile[0]][tile[1]].isGoal:
                break
            self.move(tile, colors.red)
            c_list.append(tile)
            o_list.remove(tile)
            actions = self.get_actions(tile, o_list, c_list, False)
            o_list.extend(actions)
            for i in range(len(actions)):
                self.current_state[actions[i][0]][actions[i][1]].parent = tile

        itr = (12, 0)
        while self.current_state[itr[0]][itr[1]].parent != None:
            self.move(itr, colors.green)
            itr = self.current_state[itr[0]][itr[1]].parent
        self.move(itr, colors.green)
