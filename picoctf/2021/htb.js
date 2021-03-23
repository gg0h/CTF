//This javascript code looks strange...is it obfuscated???
eval(
  (function (p, a, c, k, e, r) {
    e = function (c) {
      return c.toString(a);
    };
    if (true) {
      while (c--) r[e(c)] = k[c] || e(c);
      k = [
        function (e) {
          return r[e];
        },
      ];
      e = function () {
        return "\\w+";
      };
      c = 1;
    }
    while (c--)
      if (k[c]) p = p.replace(new RegExp("\\b" + e(c) + "\\b", "g"), k[c]);
    return p;
  })(
    '0 3(){$.4({5:"6",7:"8",9:\'/b/c/d/e/f\',g:0(a){1.2(a)},h:0(a){1.2(a)}})}', // p
    18, // a
    18, // c
    "function|console|log|makeInviteCode|ajax|type|POST|dataType|json|url||api|invite|how|to|generate|success|error".split("|"), //k
    0, // e
    {} // r
  )
);

// {
//     "0": "function",
//     "1": "console",
//     "2": "log",
//     "3": "makeInviteCode",
//     "4": "ajax",
//     "5": "type",
//     "6": "POST",
//     "7": "dataType",
//     "8": "json",
//     "9": "url",
//     "h": "error",
//     "g": "success",
//     "f": "generate",
//     "e": "to",
//     "d": "how",
//     "c": "invite",
//     "b": "api",
//     "a": "a"
//   }

function makeInviteCode() {
  $.ajax({
    type: "POST",
    dataType: "json",
    url: "/api/invite/how/to/generate",
    success: function (a) {
      console.log(a);
    },
    error: function (a) {
      console.log(a);
    },
  });
}
