const CryptoJS = require("crypto-js");//npm install crypto-js

/*
js，headers处理
 */


function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = 'B3978D054A72A7002063637CCDF6B2E5' + l(t);
    return u(n).toLocaleLowerCase()
}

function l(t) {
    for (var e = Object.keys(t).sort(s), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]] instanceof Object || t[e[a]] instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}

function s(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}


function u(t) {
    // return function (e) {
    //     return new Md5(!0).update(e)[t]()
    // }
    return CryptoJS.MD5(t).toString()
}


t = {
    "ts": 1712813275138,
    "pageNo": 1,
    "pageSize": 20,
    "total": 3575,
    "KIND": "GCJS",
    "GGTYPE": "1",
    "timeType": "6",
    "BeginTime": "2023-10-11 00:00:00",
    "EndTime": "2024-04-11 23:59:59",
    "createTime": []
}
console.log(d(t))