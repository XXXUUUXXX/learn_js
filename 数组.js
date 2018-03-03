//如何通过索引取到500这个值：
'use strict';
var arr = [[1, 2, 3], [400, 500, 600], '-'];
//var x =
var x = arr[1][1];
console.log(x); // x应该为500

//在新生欢迎会上，你已经拿到了新同学的名单，请排序后显示：欢迎XXX，XXX，XXX和XXX同学！：
'use strict';
var arr = ['小明', '小红', '大军', '阿黄'];
//console.log('???');
console.log(`欢迎,${arr[0]},${arr[1]},${arr[2]}和${arr[3]}同学！`);