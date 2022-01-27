from bs4 import BeautifulSoup
import xlwt as xl
import re,os

path = os.getcwd()
soup = BeautifulSoup(open(path + '\\source.html','r',encoding='utf-8'), features="lxml")
text = soup.get_text().split('\n')[35:]
lenth = len(text)
courses = []

#提取课程文本信息
i = 0
while lenth >=19:
    courses.append(text[i:i+19])
    lenth -= 19
    i += 19
print("共有 " + str(len(courses)) + " 门课程")
#print(courses)

#提取课程详细信息：课程名、教师、时间、教室
name = []
teacher = []
time = []
room = []
for i in courses:
    name.append(i[1]+i[2] if i[1]+i[2] != '\xa0' else '')# = 1+2
    teacher.append(i[6] if i[6] != '\xa0' else '')# = 6
    time.append(i[7] if i[7] != '\xa0' else '')# = 7
    room.append(i[8] if i[8] != '\xa0' else '')# = courses[:][8]
    print(i[1]+i[2],i[6],i[7],i[8])

#print(len(time))

time_fixed = []
room_fixed = []

for i in range(len(time)):
    temp = [j for j in time[i].split(" ") if j != '']
    r_temp = [j for j in room[i].split("d") if j != '']
    #print(len(temp))
    #print(r_temp)
    tem = []
    r_tem = []
    for sg in range(len(temp)//3):
        tem.append(temp[sg*3:3+sg*3])
        r_tem.append(r_temp[sg] if r_temp != [] else '')
    time_fixed.append(tem)
    room_fixed.append(r_tem)
#print(len(time_fixed))

file = xl.Workbook("UTF-8")
sheet = file.add_sheet("sheet1")

y = 0
for i in range(len(time_fixed)):
    #print(0)
    for j in range(len(time_fixed[i])):
        t = time_fixed[i][j]
        r = room_fixed[i][j]
        #print(t)
        #print(r)
        #t = [week,day,time]
        #print(j)
        sheet.write(y,0,name[i])#name
        sheet.write(y,1,teacher[i].replace(',',' '))#teacher
        sheet.write(y,2,t[1].replace('星期',''))#day-星期
        sheet.write(y,3,t[2])#time
        sheet.write(y,4,re.sub("[兴隆山群楼校区南座]|[A-Z]",'',r))#room-兴隆山
        sheet.write(y,5,re.sub("[周]",'',t[0]).replace(',',' ').replace("单",' 单').replace("双",' 双'))#week-周,
        y += 1

file.save(path + '\\aim.xls')