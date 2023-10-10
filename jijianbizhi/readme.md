## 破解加密数据的网站-极简壁纸

~~~
https://bz.zzzmh.cn/index?ref=www.zkdh.net
~~~

## 参考的视频

~~~
https://www.bilibili.com/video/BV1t84y1Z7zs/?spm_id_from=333.788&vd_source=4cff3e6a8562f094b3c22779df5e9679
~~~

## hook脚本

~~~
https://blog.csdn.net/xiao_yi_xiao/article/details/127519039
~~~

## 实际使用的

~~~
var my_parse = JSON.parse;
JSON.parse = function (params) {
    //这里可以添加其他逻辑比如 
    debugger
    console.log("json_parse params:",params);
    return my_parse(params);
};
~~~