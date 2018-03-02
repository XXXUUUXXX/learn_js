JavaScript是一种运行在浏览器中的解释型的编程语言，主要解决前端和用户交互的问题，包括使用交互和数据交互。

web中只有JavaScript能跨平台，跨浏览器驱动网页，与用户交互

ECMAScript是一种语言标准，而JavaScript是网景公司对ECMAScript标准的一种实现


JavaScript代码可以直接嵌在网页的任何地方，不过通常我们都把JavaScript代码放到<head>中：
由<script>...</script>包含的代码就是JavaScript代码，它将直接被浏览器执行
<html>
<head>
  <script>
    alert('Hello, world');
  </script>
</head>
<body>
  ...
</body>
</html>

第二种方法是把JavaScript代码放到一个单独的.js文件，然后在HTML中通过<script src="..."></script>引入这个文件，/static/js/abc.js就会被浏览器执行
<html>
<head>
  <script src="/static/js/abc.js"></script>
</head>
<body>
  ...
</body>
</html>

把JavaScript代码放入一个单独的.js文件中更利于维护代码，并且多个页面可以各自引用同一份.js文件
可以在同一个页面中引入多个.js文件，还可以在页面中多次编写<script> js代码... </script>，浏览器按照顺序依次执行

有时候<script>标签还设置了一个type属性：
<script type="text/javascript">
  ...
</script>
但这是没有必要的，因为默认的type就是JavaScript，所以不必显式地把type指定为JavaScript。

运行JavaScript：
    要让浏览器运行JavaScript，必须先有一个HTML页面，在HTML页面中引入JavaScript，然后，让浏览器加载该HTML页面，就可以执行JavaScript代码。
    由于浏览器的安全限制，以file://开头的地址无法执行如联网等JavaScript代码，需要以http://开头的地址来正常执行所有JavaScript代码

注释：
    // 单行注释
    /* 多行注释 */

语法：
    和java语言类似，每个语句以分号;结束，语句块用{...}，但JavaScript不强制要求每个语句的结尾加分号;
浏览器中负责执行JavaScript代码的引擎会自动在每个语句的结尾补上分号;，
让JavaScript引擎自动加分号在某些情况下会改变程序的语义，导致运行结果与期望不一致。

赋值语句：
    var x = 1;
    var x = 1; var y = 2; // 不建议一行写多个语句!
语句块是一组语句的集合，例如下面的代码先做了一个判断，如果判断成立，将执行{...}中的所有语句：
if (2 > 1) {    //花括号{...}内的语句具有缩进，通常是4个空格
    x = 1;
    y = 2;
    z = 3;
}
{...}还可以嵌套，形成层级结构：
if (2 > 1) {
    x = 1;
    y = 2;
    z = 3;
    if (x < y) {
        z = 4;
    }
    if (x > y) {
        z = 5;
    }
}

注意，JavaScript严格区分大小写，如果弄错了大小写，程序将报错或者运行不正常