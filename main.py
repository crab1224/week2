Llist = []

try:
    
    f = open('mission_computer_main.log', "r")
    rList = f.readlines()

    for i in rList[1:]:
        LI = i.strip().split(',')
        Llist.append(LI)

    print(Llist)

    Llist.sort(reverse=True)

    for k in Llist:
        print(k)    

    dic = {x[0]: {"event":x[1], "message":x[2]} for x in Llist}
    print(dic)

    f2 = open('mission_computer_main.json', "w")
    json_dump = '{\n'
    for key, value in dic.items():
        json_dump += '    "' + key + '": {\n'
        json_dump += '        "event": "' + value['event'] + '",\n'
        json_dump += '        "message": "' + value['message'] + '"\n'
        json_dump += '    },\n'

    json_dump = json_dump.strip(',\n') + '\n}'

    f2.write(json_dump)

    f.close()
    f2.close()

except Exception as e:
    print("예외처리")
except FileNotFoundError as e:
    print("파일을 찾을 수 없음 ")
except IOError as e: 
    print("입출력 오류 발생")