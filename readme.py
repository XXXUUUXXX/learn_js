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

数据类型：
    Number：
        JavaScript不区分整数和浮点数，统一用Number表示
            123; // 整数123
            0.456; // 浮点数0.456
            1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
            -99; // 负数
            NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示
            Infinity; // Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值时，就表示为Infinity
        Number可以直接做四则运算，规则和数学一致：
            1 + 2; // 3
            (1 + 2) * 5 / 2; // 7.5
            2 / 0; // Infinity
            0 / 0; // NaN
            10 % 3; // 1
            10.5 % 3; // 1.5
    字符串：
        字符串是以单引号'或双引号"括起来的任意文本
    布尔值：
        布尔值只有true、false两种值，要么是true，要么是false
        &&运算是与运算，只有所有都为true，&&运算结果才是true
        ||运算是或运算，只要其中有一个为true，||运算结果就是true
        !运算是非运算

比较运算符：
    ==比较，它会自动转换数据类型再比较，很多时候，会得到非常诡异的结果
    ===比较，它不会自动转换数据类型，如果数据类型不一致，返回false，如果一致，再比较
    由于JavaScript这个设计缺陷，不要使用==比较，始终坚持使用===比较

    另一个例外是NaN这个特殊的Number与所有其他值都不相等，包括它自己：
        NaN === NaN; // false
    唯一能判断NaN的方法是通过isNaN()函数：
        isNaN(NaN); // true

    注意浮点数的相等比较：
        1 / 3 === (1 - 2 / 3); // false
    这不是JavaScript的设计缺陷。浮点数在运算过程中会产生误差，因为计算机无法精确表示无限循环小数
    要比较两个浮点数是否相等，只能计算它们之差的绝对值，看是否小于某个阈值
        Math.abs(1 / 3 - (1 - 2 / 3)) < 0.0000001; // true

null和undefined:
    null表示一个“空”的值，它和0以及空字符串''不同，0是一个数值，''表示长度为0的字符串，而null表示“空”
    在其他语言中，也有类似JavaScript的null的表示，例如Java也用null，Swift用nil，Python用None表示
    undefined仅仅在判断函数参数是否传递的情况下有用

数组：
    数组是一组按顺序排列的集合，集合的每个值称为元素。JavaScript的数组可以包括任意数据类型
    数组用[]表示，元素之间用,分隔
        例如：[1, 2, 3.14, 'Hello', null, true];
    另一种创建数组的方法是通过Array()函数实现：
        new Array(1, 2, 3); // 创建了数组[1, 2, 3]
    出于代码的可读性考虑，强烈建议直接使用[]

    数组的元素可以通过索引来访问，索引的起始值为0
        var arr = [1, 2, 3.14, 'Hello', null, true];
        arr[0]; // 返回索引为0的元素，即1
        arr[5]; // 返回索引为5的元素，即true
        arr[6]; // 索引超出了范围，返回undefined

对象：(类似python的字典)
    JavaScript的对象是一组由键-值组成的无序集合，例如：
        var person = {
            name: 'Bob',
            age: 20,
            tags: ['js', 'web', 'mobile'],
            city: 'Beijing',
            hasCar: true,
            zipcode: null
        };
    JavaScript对象的键都是字符串类型，值可以是任意数据类型。
    上述person对象一共定义了6个键值对，其中每个键又称为对象的属性，例如，person的name属性为'Bob'，zipcode属性为null

    要获取一个对象的属性，我们用对象变量.属性名的方式：
        person.name; // 'Bob'
        person.zipcode; // null

变量：
    变量不仅可以是数字，还可以是任意数据类型
    变量在JavaScript中就是用一个变量名表示，变量名是大小写英文、数字、$和_的组合，且不能用数字开头
    变量名也不能是JavaScript的关键字，如if、while等
    申明一个变量用var语句
        var a; // 申明了变量a，此时a的值为undefined
        var $b = 1;   // 申明了变量$b，同时给$b赋值，此时$b的值为1
        var s_007 = '007'; // s_007是一个字符串
        var Answer = true; // Answer是一个布尔值true
        var t = null; // t的值是null
    使用等号=对变量进行赋值
    可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，但是要注意只能用var申明一次
        var a = 123; // a的值是整数123
        a = 'ABC';   // a变为字符串

strict模式：
    如果一个变量没有通过var申明就被使用，那么该变量就自动被申明为全局变量
        i = 10; // i现在是全局变量
    使用var申明的变量则不是全局变量，它的范围被限制在该变量被申明的函数体内，同名变量在不同的函数体内互不冲突。
    strict模式下运行的JavaScript代码，强制通过var申明变量，未使用var申明变量就使用的，将导致运行错误
    启用strict模式的方法是在JavaScript代码的第一行写上：
        'use strict';
    这是一个字符串，不支持strict模式的浏览器会把它当做一个字符串语句执行，支持strict模式的浏览器将开启strict模式运行JavaScript
    
    如果浏览器支持strict模式，
    下面的代码将报ReferenceError错误:
        'use strict';
        abc = 'Hello, world';
        console.log(abc);

字符串：
    JavaScript的字符串就是用''或""括起来的字符表示
    如果字符串内部既包含'又包含"可以用转义字符\来标识
        'I\'m \"OK\"!';    表示的字符串内容是：I'm "OK"!

多行字符串：
    用反引号 ` ... ` 表示
        `这是一个
         多行
         字符串`;

模板字符串：
    var name = '小明';
    var age = 20;
    var message = `你好, ${name}, 你今年${age}岁了!`;//使用反引号`
    自动替换字符串中的变量

操作字符串：
    var s = 'Hello, world!';
    s.length;  // 13
    要获取字符串某个指定位置的字符，使用类似Array的下标操作，索引号从0开始：
        var s = 'Hello, world!';
        s[0];  // 'H'
        s[6];  // ' '
        s[7];  // 'w'
        s[12]; // '!'
        s[13]; // undefined 超出范围的索引不会报错，但一律返回undefined
    需要特别注意的是，字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但是，也没有任何效果
        var s = 'Test';
        s[0] = 'X';
        alert(s); // s仍然为'Test'

JavaScript为字符串提供了一些常用方法，注意，调用这些方法本身不会改变原有字符串的内容，而是返回一个新字符串

toUpperCase：
    toUpperCase()把一个字符串全部变为大写：
        var s = 'Hello';
        s.toUpperCase(); // 返回'HELLO'

toLowerCase：
    toLowerCase()把一个字符串全部变为小写：
        var s = 'Hello';
        var lower = s.toLowerCase(); // 返回'hello'并赋值给变量lower
        lower; // 'hello'

indexOf：
    indexOf()会搜索指定字符串出现的位置：
        var s = 'hello, world';
        s.indexOf('world'); // 返回7
        s.indexOf('World'); // 没有找到指定的子串，返回-1

substring：
    substring()返回指定索引区间的子串：
        var s = 'hello, world'
        s.substring(0, 5); // 从索引0开始到5（不包括5），返回'hello'
        s.substring(7);    // 从索引7开始到结束，返回'world'

数组：
    JavaScript的Array可以包含任意数据类型，并通过索引来访问每个元素
    要取得Array的长度，直接访问length属性：
        var arr = [1, 2, 3.14, 'Hello', null, true];
        arr.length; // 6
    
    请注意，直接给Array的length赋一个新的值会导致Array大小的变化
        var arr = [1, 2, 3];
        arr.length; // 3
        arr.length = 6;
        arr; // arr变为[1, 2, 3, undefined, undefined, undefined]
        arr.length = 2;
        arr; // arr变为[1, 2]
    Array可以通过索引把对应的元素修改为新的值，因此，对Array的索引进行赋值会直接修改这个Array
        var arr = ['A', 'B', 'C'];
        arr[1] = 99;
        arr; // arr现在变为['A', 99, 'C']
    请注意，如果通过索引赋值时，索引超过了范围，同样会引起Array大小的变化
        var arr = [1, 2, 3];
        arr[5] = 'x';
        arr; // arr变为[1, 2, 3, undefined, undefined, 'x']

    在编写代码时，不建议直接修改Array的大小，访问索引时要确保索引不会越界

indexOf
    与String类似，Array也可以通过indexOf()来搜索一个指定的元素的位置
        var arr = [10, 20, '30', 'xyz'];
        arr.indexOf(10); // 元素10的索引为0
        arr.indexOf(20); // 元素20的索引为1
        arr.indexOf(30); // 元素30没有找到，返回-1
        arr.indexOf('30'); // 元素'30'的索引为2

slice
    slice()就是对应String的substring()版本，它截取Array的部分元素，然后返回一个新的Array：
        var arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
        arr.slice(0, 3);   // 从索引0开始，到索引3结束，但不包括索引3: ['A', 'B', 'C']
        arr.slice(3);      // 从索引3开始到结束: ['D', 'E', 'F', 'G']

    如果不给slice()传递任何参数，它就会从头到尾截取所有元素。利用这一点，我们可以很容易地复制一个Array
        var arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
        var aCopy = arr.slice();
        aCopy; // ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        aCopy === arr; // false

push和pop
    push()向Array的末尾添加若干元素，pop()则把Array的最后一个元素删除掉：
        var arr = [1, 2];
        arr.push('A', 'B'); // 返回Array新的长度: 4
        arr; // [1, 2, 'A', 'B']
        arr.pop(); // pop()返回'B'
        arr; // [1, 2, 'A']
        arr.pop(); arr.pop(); arr.pop(); // 连续pop 3次
        arr; // []
        arr.pop(); // 空数组继续pop不会报错，而是返回undefined
        arr; // []

unshift和shift
    如果要往Array的头部添加若干元素，使用unshift()方法，shift()方法则把Array的第一个元素删掉：
        var arr = [1, 2];
        arr.unshift('A', 'B'); // 返回Array新的长度: 4
        arr; // ['A', 'B', 1, 2]
        arr.shift(); // 'A'
        arr; // ['B', 1, 2]
        arr.shift(); arr.shift(); arr.shift(); // 连续shift 3次
        arr; // []
        arr.shift(); // 空数组继续shift不会报错，而是返回undefined
        arr; // []

sort
    sort()可以对当前Array进行排序，它会直接修改当前Array的元素位置，直接调用时，按照默认顺序排序：
        var arr = ['B', 'C', 'A'];
        arr.sort();
        arr; // ['A', 'B', 'C']

reverse
    reverse()把整个Array的元素给掉个个，也就是反转：
        var arr = ['one', 'two', 'three'];
        arr.reverse(); 
        arr; // ['three', 'two', 'one']

splice
    splice()方法是修改Array的“万能方法”，它可以从指定的索引开始删除若干元素，然后再从该位置添加若干元素：
    splice(索引,删除个数,添加元素)
        var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
        // 从索引2开始删除3个元素,然后再添加两个元素:
        arr.splice(2, 3, 'Google', 'Facebook'); // 返回删除的元素 ['Yahoo', 'AOL', 'Excite']
        arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
        // 只删除,不添加:
        arr.splice(2, 2); // ['Google', 'Facebook']
        arr; // ['Microsoft', 'Apple', 'Oracle']
        // 只添加,不删除:
        arr.splice(2, 0, 'Google', 'Facebook'); // 返回[],因为没有删除任何元素
        arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']

concat
    concat()方法把当前的Array和另一个Array连接起来，并返回一个新的Array
    concat()方法并没有修改当前Array，而是返回了一个新的Array
        var arr = ['A', 'B', 'C'];
        var added = arr.concat([1, 2, 3]);
        added; // ['A', 'B', 'C', 1, 2, 3]
        arr; // ['A', 'B', 'C']

    concat()方法可以接收任意个元素和Array，并且自动把Array拆开，然后全部添加到新的Array里
        var arr = ['A', 'B', 'C'];
        arr.concat(1, 2, [3, 4]); // ['A', 'B', 'C', 1, 2, 3, 4]

join
    join()方法把当前Array的每个元素都用指定的字符串连接起来，然后返回连接后的字符串
    如果Array的元素不是字符串，将自动转换为字符串后再连接
        var arr = ['A', 'B', 'C', 1, 2, 3];
        arr.join('-'); // 'A-B-C-1-2-3'

多维数组
    如果数组的某个元素又是一个Array，则可以形成多维数组，例如：
        var arr = [[1, 2, 3], [400, 500, 600], '-'];
    上述Array包含3个元素，其中头两个元素本身也是Array

