# Timetable_Helperrrrrrrr！

## Ⅰ项目介绍

### 本项目的开发目的在于适配**Timetable App**与**山东大学~~智慧~~教学服务平台**，由于App官方提供的导入课表功能在学校新的教务系统面前显得……难以形容，故开发这个项目用以便捷导入课程。

| 语言  | 引用库 | 用途说明 |
| :---: | :---: | :---: |
|Python | bs4(with lxml)<br>xlwt<br>re | HTML解析处理<br>xls解析处理<br>正则表达式 |

### **输入部分：**
由选课阶段**手动导出**的HTML文件（目前仅支持手动导出，自动登录导出是下一代更新内容），如图：

![教务系统](https://gitee.com/kevin_ud/timetable_helper/raw/master/picture/source1.jpg)
![教务系统](https://gitee.com/kevin_ud/timetable_helper/raw/master/picture/source2.jpg)

### **输出部分：**
参考```Timetable```开发者发布的[博文](https://www.jianshu.com/p/0c576ec144c5)，根据情况我选择了第一种模板来构建输出
![输出](https://upload-images.jianshu.io/upload_images/4679632-05afd34d030ef0b9.png)

## Ⅱ使用前须知
务必将安装引用库否则无法使用
```cmd
pip install beautifulsoup4 lxml xlwt
```

## Ⅲ使用效果

### 输出xls文件：
![xls](https://gitee.com/kevin_ud/timetable_helper/raw/master/picture/result.png)
### **教务系统课表查询**与**Timetable导入课程**效果对比
![EA_System](https://gitee.com/kevin_ud/timetable_helper/raw/master/picture/system.png)
![Timetable](https://gitee.com/kevin_ud/timetable_helper/raw/master/picture/timetable.jpg)