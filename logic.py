from Agent import Agent
import world
import time
import sys 

agent = Agent()
    
def which_drection(start,end):
    if start[0]+1 == end[0]:
        return 'up'
    if start[0]-1 == end[0]:
        return 'down'
    if start[1]+1 == end[1]:
        return 'right'
    if start[1]-1 == end[1]:
        return 'left'

def delete_deplicate(ls):
    for i in range(len(ls)):
        if ls.count(ls[i]) != 1 :
            ls.remove(ls[i])
            delete_deplicate(ls)
            break    
    return ls

def find_wampus(agent,data):
    if agent.wampus_number == 1:
        visited = agent.visited
        answer = 'not_found_wampus'
        S_Num = 0
        S_Num += list(data.values()).count(['S'])
        S_Num += list(data.values()).count(['S','B'])
        ls = []
        ls2 = []
        if S_Num >= 2:
            if S_Num == 2:
                ls2.extend([eval(key)  for (key, value) in data.items() if value == ['S']])
                ls2.extend([eval(key)  for (key, value) in data.items() if value == ['S','B']])

            if S_Num > 2:
                ls.extend([key  for (key, value) in data.items() if value == ['S']])
                ls.extend([key  for (key, value) in data.items() if value == ['S','B']])
                for i in range(len(ls)):
                    for j in range(len(ls)):
                        if len(ls2) != 2:
                            if i>j:
                                if i==j:
                                    continue
                                else:
                                    if eval(ls[i])[0] == eval(ls[j])[0]:
                                        ls2.append(eval(ls[i]))
                                        ls2.append(eval(ls[j]))
                                        break
                                    elif eval(ls[i])[1] == eval(ls[j])[1]:
                                        ls2.append(eval(ls[i]))
                                        ls2.append(eval(ls[j]))
                                        break
            if ls2[0][0] == ls2[1][0]:
                answer = [ls2[0][0],(ls2[0][1]+ls2[1][1])/2]
            elif ls2[0][1] == ls2[1][1]:
                answer = [(ls2[0][0]+ls2[1][0])/2,ls2[0][1]]
            else:
                possible_answers = []
                possible_answers.append([ls2[0][0],ls2[1][1]])
                possible_answers.append([ls2[1][0],ls2[0][1]])
                answer = [x for x in possible_answers if x not in visited][0]
    else:
        visited = agent.visited
        answer = 'not_found_wampus'
        S_Num = 0
        S_Num += list(data.values()).count(['S'])
        S_Num += list(data.values()).count(['S','B'])
        a = []
        if S_Num > 2:
            a.extend([key  for (key, value) in data.items() if value == ['S']])
            a.extend([key  for (key, value) in data.items() if value == ['S','B']])

            for i in range(len(a)):
                for j in range(len(a)):
                    for k in range(len(a)):
                        if i == j or i == k or j == k:
                            continue
                        if k>j and j>i :
                            if eval(a[i])[0] == eval(a[j])[0]:
                                if abs(eval(a[i])[1] - eval(a[j])[1]) == 2:
                                    if eval(a[k])[0] == eval(a[i])[0]+1 or eval(a[k])[0] == eval(a[i])[0]-1:
                                        if eval(a[k])[1] == (eval(a[i])[1]+eval(a[j])[1])/2:
                                            answer = list((int(eval(a[i])[0]),int((eval(a[i])[1]+eval(a[j])[1])/2)))
                            elif eval(a[i])[0] == eval(a[k])[0]:
                                if abs(eval(a[i])[1] - eval(a[k])[1]) == 2:
                                    if eval(a[j])[0] == eval(a[i])[0]+1 or eval(a[j])[0] == eval(a[i])[0]-1:
                                        if eval(a[j])[1] == (eval(a[i])[1]+eval(a[k])[1])/2:
                                            answer = list((int(eval(a[i])[0]),int((eval(a[i])[1]+eval(a[k])[1])/2)))
                            elif eval(a[j])[0] == eval(a[k])[0]:
                                if abs(eval(a[j])[1] - eval(a[k])[1]) == 2:
                                    if eval(a[i])[0] == eval(a[j])[0]+1 or eval(a[i])[0] == eval(a[j])[0]-1:
                                        if eval(a[i])[1] == (eval(a[j])[1]+eval(a[k])[1])/2:
                                            answer = list((int(eval(a[j])[0]),int((eval(a[j])[1]+eval(a[k])[1])/2)))
                            elif eval(a[i])[1] == eval(a[j])[1]:
                                if abs(eval(a[i])[0] - eval(a[j])[0]) == 2:
                                    if eval(a[k])[1] == eval(a[i])[1]+1 or eval(a[k])[1] == eval(a[i])[1]-1:
                                        if eval(a[k])[0] == (eval(a[i])[0]+eval(a[j])[0])/2:
                                            answer = list((int((eval(a[i])[0]+eval(a[j])[0])/2),int(eval(a[i])[1])))
                            elif eval(a[i])[1] == eval(a[k])[1]:
                                if abs(eval(a[i])[0] - eval(a[k])[0]) == 2:
                                    if eval(a[j])[1] == eval(a[i])[1]+1 or eval(a[j])[1] == eval(a[i])[1]-1:
                                        if eval(a[j])[0] == (eval(a[i])[0]+eval(a[k])[0])/2:
                                            answer = list((int((eval(a[i])[0]+eval(a[k])[0])/2),int(eval(a[i])[1])))
                            elif eval(a[j])[1] == eval(a[k])[1]:
                                if abs(eval(a[j])[0] - eval(a[k])[0]) == 2:
                                    if eval(a[i])[1] == eval(a[k])[1]+1 or eval(a[i])[1] == eval(a[k])[1]-1:
                                        if eval(a[i])[0] == (eval(a[k])[0]+eval(a[j])[0])/2:
                                            answer = list((int((eval(a[k])[0]+eval(a[j])[0])/2),int(eval(a[k])[1])))
            if len(answer) == 0:
                answer = 'not_found_wampus'
            else:
                answer = answer

    return answer

def kill_wampus(agent , wampus_location , data):
    print('Killlling Wampus')
    answer = 'Not Killed !!!'
    wampus_direction = which_drection(agent.location,wampus_location)
    agent.shoot(wampus_direction)
    keys = []
    if agent.wampus_alive == False:
        keys.extend([eval(key)  for (key, value) in data.items() if value == ['S']])
        keys.extend([eval(key)  for (key, value) in data.items() if value == ['S','B']])
        for i in range (len(keys)):
            data[str(keys[i])].remove('S')
        answer = 'Wampus Killed !!!'
    return answer , data

def go_kill_wampus(agent, wampus_location , data):
    print('moving to Kill the Wampus')
    if agent.cell_data['S'] != 1:
        ls = []
        ls.extend([eval(key)  for (key, value) in data.items() if value == ['S']])
        ls.extend([eval(key)  for (key, value) in data.items() if value == ['S','B']])
        if len(ls) != 0:
            end = ls[0]
            route = agent.route_full[-1:agent.route_full.index(end)-1:-1]
            for i in range(len(route)-1):
                agent.move(which_drection(route[i],route[i+1]))

            if agent.cell_data['S'] == 1:
                answer , data = kill_wampus(agent, wampus_location , data)
    return answer , data

possible_wampus = []
possible_pit = []
data = {}
flag = 0
flag2 = 1
data[str(agent.location)] = []

agent.show()

def go_in(agent):
    global possible_wampus
    global possible_pit
    global data
    global flag
    global flag2
    print('moves =',agent.moves)
    if agent.moves >= 100:
        print('Nope')
        flag2 = 0
        sys.exit()
        
    time.sleep(0.5)

    for i in range (len(agent.available_moves)):
        print('--------------------------------------------------------')
        print('Location =',agent.location)
        if agent.found_gold == True:
            data[str(agent.location)] = ['G']
            
            if flag == 0:
                print('------ GOLD FOUND ------')
                print('way to gold = ',agent.route)
                print('way back to home = ',agent.route[::-1])
                flag += 1
            break

        if i != len(agent.available_moves)-1 :
            if agent.available_cells[i] in agent.visited:
                continue
        print(agent.available_moves[i])
        agent.move(agent.available_moves[i])

        if agent.ok == 1:
            if str(agent.location) not in list(data.keys()):
                data[str(agent.location)] = []
            agent.show()
            go_in(agent)

        if agent.ok == 0:

            if agent.cell_data['S'] == 1 and agent.cell_data['B'] == 1:
                if str(agent.location) not in list(data.keys()):
                    data[str(agent.location)] = ['S','B']

                possible_wampus.extend(agent.available_cells)
                possible_wampus = [x for x in possible_wampus if x not in agent.visited]
                possible_wampus = delete_deplicate(possible_wampus)
                possible_pit.extend(agent.available_cells)
                possible_pit = [x for x in possible_pit if x not in agent.visited]
                possible_pit = delete_deplicate(possible_pit)
                to_remove = []
                for k in range(len(possible_wampus)):
                    must_have_s = []
                    must_have_s.append([possible_wampus[k][0],possible_wampus[k][1]+1])
                    must_have_s.append([possible_wampus[k][0],possible_wampus[k][1]-1])
                    must_have_s.append([possible_wampus[k][0]+1,possible_wampus[k][1]])
                    must_have_s.append([possible_wampus[k][0]-1,possible_wampus[k][1]])

                    for j in range(len(must_have_s)):
                        if str(must_have_s[j]) in list(data.keys()):
                            if data[str(must_have_s[j])].count('S') < 1:
                                to_remove.append(possible_wampus[i])
                possible_wampus = [i for i in possible_wampus if i not in to_remove]
                agent.show()
                if len(possible_wampus) == 1:
                    answer , data = kill_wampus(agent , possible_wampus[0] , data)
                    print(answer)
                    agent.show()

                if agent.ok == 1:
                    go_in(agent)

                if find_wampus(agent,data) != 'not_found_wampus':
                    answer , data = kill_wampus(agent , find_wampus(agent , data) , data)
                    print(answer)

                if agent.wampus_alive == True:
                    back_direction = which_drection(agent.location,agent.route[-2])
                    print(back_direction)
                    agent.move(back_direction)
                    agent.show()

            elif agent.cell_data['S'] == 1:
                if str(agent.location) not in list(data.keys()):
                    data[str(agent.location)] = ['S']

                possible_wampus.extend(agent.available_cells)
                possible_wampus = [x for x in possible_wampus if x not in agent.visited]
                possible_wampus = delete_deplicate(possible_wampus)
                print('possible_wampus = ',possible_wampus)
                to_remove = []
                for k in range(len(possible_wampus)):
                    print(k)
                    print(possible_wampus[k])
                    must_have_s = []
                    must_have_s.append([possible_wampus[k][0],possible_wampus[k][1]+1])
                    must_have_s.append([possible_wampus[k][0],possible_wampus[k][1]-1])
                    must_have_s.append([possible_wampus[k][0]+1,possible_wampus[k][1]])
                    must_have_s.append([possible_wampus[k][0]-1,possible_wampus[k][1]])

                    for j in range(len(must_have_s)):
                        if str(must_have_s[j]) in list(data.keys()):
                            if data[str(must_have_s[j])].count('S') < 1:
                                to_remove.append(possible_wampus[i])
                possible_wampus = [i for i in possible_wampus if i not in to_remove]
                agent.show()
                if len(possible_wampus) == 1:
                    answer , data = kill_wampus(agent , possible_wampus[0] , data)
                    print(answer)
                    agent.show()

                if find_wampus(agent,data) != 'not_found_wampus':
                    answer , data = kill_wampus(agent , find_wampus(agent , data) , data)
                    print(answer)

                if agent.ok == 1:
                    go_in(agent)

                if agent.wampus_alive == True:
                    back_direction = which_drection(agent.location,agent.route[-2])
                    print(back_direction)
                    agent.move(back_direction)
                    agent.show()

            elif agent.cell_data['B'] == 1:
                if str(agent.location) not in list(data.keys()):
                    data[str(agent.location)] = ['B']

                possible_pit.extend(agent.available_cells)
                possible_pit = [x for x in possible_pit if x not in agent.visited]
                possible_pit = delete_deplicate(possible_pit)

                to_remove = []
                for k in range(len(possible_wampus)):
                    must_have_s = []
                    must_have_s.append([possible_wampus[k][0],possible_wampus[k][1]+1])
                    must_have_s.append([possible_wampus[k][0],possible_wampus[k][1]-1])
                    must_have_s.append([possible_wampus[k][0]+1,possible_wampus[k][1]])
                    must_have_s.append([possible_wampus[k][0]-1,possible_wampus[k][1]])

                    for j in range(len(must_have_s)):
                        if str(must_have_s[j]) in list(data.keys()):
                            if data[str(must_have_s[j])].count('S') < 1:
                                to_remove.append(possible_wampus[i])

                possible_wampus = [i for i in possible_wampus if i not in to_remove]

                agent.show()
                if len(possible_wampus) == 1:
                    answer , data = go_kill_wampus(agent , possible_wampus[0] , data)
                    print(answer)
                    agent.show()

                if agent.ok == 1:
                    go_in(agent)
                if agent.wampus_alive == True:
                    back_direction = which_drection(agent.location,agent.route[-2])
                    print(back_direction)
                    agent.move(back_direction)

        if flag == 1 or flag2 == 0:
            break
        print('wampus possible =',possible_wampus)
        print('pit possible =',possible_pit)
        print('Data =',data)
     
go_in(agent)