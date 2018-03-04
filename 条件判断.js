'use strict';
var age = 20;
if (age >= 18) {
    console.log('adault');
} else if (age >= 6) {
    console.log('teenager');
} else {
    console.log('kid');
}

/*
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
*/
'use strict';

var height = parseFloat(prompt('请输入身高(m):'));
var weight = parseFloat(prompt('请输入体重(kg):'));
var bmi = weight/Math.pow(height,2);
if (bmi < 18.5) {
    console.log('过轻');
} else if (bmi <= 25) {
    console.log('正常');
} else if (bmi <= 28) {
    console.log('过重');
} else if (bmi <= 32) {
    console.log('肥胖');
} else {
    console.log('严重肥胖');
}
