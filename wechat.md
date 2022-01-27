# Timetable_Helperrrrrrrr！

## Ⅰ项目介绍

### 本项目的开发目的在于适配**Timetable App**与**山东大学~~智慧~~教学服务平台**（不得不说换的新系统与智慧毫不相关），由于App官方提供的导入课表功能在学校新的教务系统面前显得……<u>难以形容</u>，故开发这个项目用以便捷导入课程。

| 语言  | 引用库 | 用途说明 |
| :---: | :---: | :---: |
|Python | bs4(with lxml)<br>xlwt<br>re | HTML解析处理<br>xls解析处理<br>正则表达式 |

### **输入部分：**
由选课阶段**手动导出**的HTML文件（目前仅支持手动导出，自动登录导出是下一代更新内容），如图：

![教务系统](https://gitee.com/kevin_ud/timetable_helper/raw/master/picture/source1.jpg)
![教务系统](https://gitee.com/kevin_ud/timetable_helper/raw/master/picture/source2.jpg)

### **输出部分：**
参考```Timetable```开发者发布的[博文](https://www.jianshu.com/p/0c576ec144c5)，根据情况我选择了第一种模板来构建输出
![输出](https://gitee.com/kevin_ud/timetable_helper/raw/master/picture/example.png)

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

## Ⅳ主要代码思路
### **流程图如下**
![流程图](https://gitee.com/kevin_ud/timetable_helper/raw/master/picture/flow.drawio.png)

## Ⅴ关键步骤代码解析
### 1) 解析HTML
在这里我们使用的是```Beautifulsoup```去解析HTML，同时注意标注出使用```lxml```解析库
一个使用案例：
```Python
from bs4 import BeautifulSoup
#尤其要注意大小写不然报错
soup = BeautifulSoup("用户自定义",feature = "lxml")
#注意指出使用lxml解析库
print(soup)
```
输出
```python
<html><body><p>用户自定义</p></body></html>
```
这里的代码就是新建了一个html对象，内容就是上面所展示的，这里```“用户自定义”```的内容决定了```soup```中的内容是什么.

也可以用本地HTML文件建立对象，如：
```python
from bs4 import BeautifulSoup
path = /test.html
soup = BeautifulSoup(open(path),feature = "lxml")
print(soup)
```
这样就将已有的本地HTML文件解析出来了.

光解析出来没有用，我们还要找到我们想要的数据，这里```BeautifulSoup```为我们贴心的预设好了诸多方法，如：
首先我们新建一个文件```test.html```，内容有
```html
<html><head><title>Welcome to ZnYC</title></head>

<body>

<p class="title" name="ZnYC"><b>Welcome to ZnYC</b></p>

<p class="story">这里是ZnYC！非常感谢看到这里，我们会不定期更新一些奇奇怪怪的东西，欢迎关注！<br>您的赞赏是我们前进的最大动力！！<br>

<a href="https://gitee.com/kevin_ud" class="sister" id="link1">Kevin's Homepage</a>

</p>

<p class="story">Edited by Kevin</p>
```

用浏览器打开可以得到：
![HTML测试]()

然后用```Python-BeautifulSoup```测试以下输出
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('test.html',encoding = "utf-8"),features = "lxml")

print(soup.head)
print(soup.title)
print(soup.p)
print(soup.a)
```
得到以下结果：
```html
<head><title>Welcome to ZnYC</title></head>
<title>Welcome to ZnYC</title>
<p class="title" name="ZnYC"><b>Welcome to ZnYC</b></p>
<a class="sister" href="https://gitee.com/kevin_ud" id="link1">Kevin's Homepage</a>
```
我们看到每一次输出对应标签的内容都会被我们得到，那……所有的文字内容（显示在浏览器里的文字）是否可以被我们捕获呢？

```python
print(soup.text)
```
输出：（行号(1>、2>等)是笔者手动加入的）
```
1>Welcome to ZnYC
2>
3>Welcome to ZnYC
4>这里是ZnYC！非常感谢看到这里，我们会不定期更新一些奇奇怪怪的东西，欢迎关注！您的赞赏是我们前进的最大动力！！
5>Kevin's Homepage
6>
7>Edited by Kevin
```
我们看到网页标题、和所有网页内容都被我们得到了，而且非常有规律，那我们就可以进行下一步……数据处理！