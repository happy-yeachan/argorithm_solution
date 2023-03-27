# def solution(info, query):
#     answer = []    
#     for i in query:
#         tmp = i.replace("and ", "")
#         tmp = tmp.split()
#         count = 0  
#         for j in info:
#             tmp2 = j.split()
#             flag = True
#             if int(tmp2[4]) < int(tmp[4]):
#                 flag = False
#             else:           
#                 for idx in range(4):
#                     if tmp[idx] == "-":
#                         continue
#                     else:
#                         if tmp[idx] != tmp2[idx]:
#                             flag = False
#                             break
#             if flag:
#                 count += 1            
#         answer.append(count)
#     return answer








print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))