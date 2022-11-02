from random import random
import world

class Agent:

    def __init__(self):
        self.alive = True
        self.world = world.makeworld()
        self.location = [0,0]
        self.moves = 0
        self.direction = 'up'
        self.ok = 1
        self.bullet = 1
        self.visited = [[0,0]]
        self.route_full = [[0,0]]
        self.route = [[0,0]]
        self.available_moves = []
        self.available_cells = []
        self.found_gold = False
        self.wampus_alive = True
        self.cell_data = self.world[self.location[0]][self.location[1]]
        self.find_available_moves()
        self.find_available_cells()
        self.wampus_number = 0
        self.how_many_wampus()
        
    def find_available_moves(self):
        self.available_moves = []
        if self.location[0] < len(self.world)-1:
            self.available_moves.append('up')
        if self.location[0] > 0:
            self.available_moves.append('down')
        if self.location[1] < len(self.world)-1:
            self.available_moves.append('right')
        if self.location[1] > 0:
            self.available_moves.append('left')

        if len(self.route) >= 2:
            back_direction = self.which_drection(self.route[-1],self.route[-2])
            if self.available_moves.count(back_direction) == 1:
                self.available_moves.append(back_direction)
                self.available_moves.remove(back_direction)

    def how_many_wampus(self):
        wampus_number = 0
        for i in range(len(self.world)):
            for j in range(len(self.world)):
                if self.world[i][j]['S'] == 1 :
                    wampus_number += 1
        self.wampus_number = wampus_number

    def which_drection(self,start,end):
        if start[0]+1 == end[0]:
            return 'up'
        if start[0]-1 == end[0]:
            return 'down'
        if start[1]+1 == end[1]:
            return 'right'
        if start[1]-1 == end[1]:
            return 'left'

    def find_available_cells(self):
        self.available_cells = []
        self.find_available_moves()
        for i in range (len(self.available_moves)):
            if self.available_moves[i] == 'up' :
                # print(list((self.location[0]+1,self.location[1])))
                self.available_cells.append(list((self.location[0]+1,self.location[1])))
            elif self.available_moves[i] == 'down' :
                self.available_cells.append(list((self.location[0]-1,self.location[1])))
            elif self.available_moves[i] == 'right' :
                self.available_cells.append(list((self.location[0],self.location[1]+1)))
            elif self.available_moves[i] == 'left' :
                self.available_cells.append(list((self.location[0],self.location[1]-1)))


    def die(self):
        if self.world[self.location[0]][self.location[1]]['W'] == 1:
            self.world[self.location[0]][self.location[1]]['A'] = 0
            self.alive = False
        if self.world[self.location[0]][self.location[1]]['P'] == 1:
            self.world[self.location[0]][self.location[1]]['A'] = 0
            self.alive = False
        
        self.cell_data = self.world[self.location[0]][self.location[1]]

    def is_ok(self):
        if self.cell_data['B'] != 1 and self.cell_data['S'] != 1:
            self.ok = 1
        else:
            self.ok = 0

    def shoot(self,direction):
        
        if self.bullet == 1:
            if self.direction != direction:
                self.direction = direction
                self.moves += 1

            self.moves += 1
            self.bullet = 0
            if direction == 'up':
                for i in range (len(self.world) - self.location[0]):
                    if self.world[self.location[0]+i][self.location[1]]['W'] == 1 :
                        self.wampus_alive = False
                        self.world[self.location[0]+i][self.location[1]]['W'] = 0
                        for k in range(len(self.world)):
                            for l in range(len(self.world)):
                                self.world[k][l]['S'] = 0
            if direction == 'down':
                for i in range (self.location[0]):
                    if self.world[self.location[0]-i][self.location[1]]['W'] == 1 :
                        self.wampus_alive = False
                        self.world[self.location[0]-i][self.location[1]]['W'] = 0
                        for k in range(len(self.world)):
                            for l in range(len(self.world)):
                                self.world[k][l]['S'] = 0
            if direction == 'right':
                for i in range (len(self.world) - self.location[1]):
                    if self.world[self.location[0]][self.location[1]+i]['W'] == 1 :
                        self.wampus_alive = False
                        self.world[self.location[0]][self.location[1]+i]['W'] = 0
                        for k in range(len(self.world)):
                            for l in range(len(self.world)):
                                self.world[k][l]['S'] = 0
            if direction == 'left':
                for i in range (self.location[1]):
                    if self.world[self.location[0]][self.location[1]-i]['W'] == 1 :
                        self.wampus_alive = False
                        self.world[self.location[0]][self.location[1]-i]['W'] = 0
                        for k in range(len(self.world)):
                            for l in range(len(self.world)):
                                self.world[k][l]['S'] = 0
        self.is_ok()
                    

    def grab(self):
        if self.world[self.location[0]][self.location[1]]['G'] == 1:
            self.moves += 1
            self.world[self.location[0]][self.location[1]]['G'] = 0
            self.found_gold = True

        self.cell_data = self.world[self.location[0]][self.location[1]]

    def move(self,direction):
        self.moves += 1
        self.direction = direction

        self.world[self.location[0]][self.location[1]]['A'] = 0

        if self.direction == 'up' :
            self.location = [self.location[0]+1,self.location[1]]
            self.world[self.location[0]][self.location[1]]['A'] = 1
        elif self.direction == 'down' :
            self.location = [self.location[0]-1,self.location[1]]
            self.world[self.location[0]][self.location[1]]['A'] = 1
        elif self.direction == 'right' :
            self.location = [self.location[0],self.location[1]+1]
            self.world[self.location[0]][self.location[1]]['A'] = 1
        elif self.direction == 'left' :
            self.location = [self.location[0],self.location[1]-1]
            self.world[self.location[0]][self.location[1]]['A'] = 1

        if self.location not in self.visited:
            self.visited.append(self.location)

        if self.route.count(self.location) != 0:
            self.route = self.route[:self.route.index(self.location)+1]
        else:
            self.route.append(self.location)

        self.route_full.append(self.location)

        self.die()
        self.grab()
        self.is_ok()
        self.find_available_cells()
        self.find_available_moves()
        self.cell_data = self.world[self.location[0]][self.location[1]]

    def show(self):
        for i in range(len(self.world)):
            for j in range(len(self.world)):
                print(str(i)+'-'+str(j)+' ',self.world[i][j])
        print('------------------------------------')


#     def start(self):
#         print('route ',self.route)
#         print('cr ',self.location)
#         # print(self.beauty)
#         # print('av ',self.available_cells)
#         self.move('right')
#         print('route ',self.route)
#         print('cr ',self.location)
#         # print(self.beauty)
#         # print('av ',self.available_cells)
#         self.move('right')
#         print('route ',self.route)
#         print('cr ',self.location)
#         # print(self.beauty)
#         # print('av ',self.available_cells)
#         self.move('left')
#         print('route ',self.route)
#         print('cr ',self.location)
#         # print(self.beauty)
#         # print('av ',self.available_cells)
#         self.move('left')
#         print('route ',self.route)
#         print('cr ',self.location)
#         # print(self.route)
#         # self.move('up')
#         # print(self.available_cells)
#         # print(self.route)
#         # while(self.moves < 5):
#         #     self.die()
#         #     self.grab()
#         #     self.find_available_moves()
#         #     self.move(self.available_moves[round(random()*(len(self.available_moves)-1))])
#         #     if self.is_ok() == 1:
#         #         continue
#             # if self.is_ok() != 1 :
#             #     sef.route


#     #    for i in range(3):
#     #         self.find_available_moves()
#     #         self.move(self.available_moves[round(random()*(len(self.available_moves)-1))])
#     #         self.show() 
#         # self.show()
#         # self.move('right')
#         # self.show()
#         # self.shoot('up')
#         # self.show()
#         # self.move('up')
#         # self.show()
#         # self.move('up')
#         # self.show()
#         # self.grab()
#         # self.show()
        

        
# # agent = Agent()
# # agent.start()


