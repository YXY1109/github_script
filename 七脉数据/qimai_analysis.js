const p = "analysis";
const d = "xyz517cda96efgh";

function o(n) {
    let t = "";
    ["66", "72", "6f", "6d", "43", "68", "61", "72", "43", "6f", "64", "65"].forEach(function (n) {
        t += unescape("%u00" + n)
    });
    let e = t;
    return String.fromCharCode(n)
}

function v(t) {
    t = encodeURIComponent(t).replace(/%([0-9A-F]{2})/g, function (n, t) {
        return o("0x" + t)
    });
    try {
        return btoa(t)
    } catch (n) {
        return ArrayBuffer.from(t).toString("base64")
    }
}


function h(n, t) {
    let e = (n = n.split("")).length, r = t.length, a = "charCodeAt", i = 0;
    for (; i < e; i++)
        n[i] = o(n[i].charCodeAt(0) ^ t[(i + 10) % r].charCodeAt(0));
    return n.join("")
}


function getAnalysis(t) {
    try {
        let e, r = +new Date() - 1661224081041, a = [];
        // return void 0 === t.params && (t.params = {}),
        Object.keys(t.params).forEach(function (n) {
            if (n === p)
                return !1;
            t.params.hasOwnProperty(n) && a.push(t.params[n])
        })
        a = a.sort().join("")
        a = v(a)
        a = (a += "@#" + t.url.replace(t.baseURL, "")) + ("@#" + r) + ("@#" + 3)
        e = v(h(a, d))
        console.log("JS返回的加密，Analysis：" + e)
        return e
    } catch (t) {
    }
}

//测试使用
const ttt = {
    "url": "/andapp/info",
    "params": {
        "appid": "8932947",
        "market": "3"
    },
    "baseURL": "https://api.qimai.cn",
};
getAnalysis(ttt)