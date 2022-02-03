var XMLHttpRequest = require('xhr2');
var request = new XMLHttpRequest();
var body = "test";
request.open("POST", "http://127.0.0.1:8888/");
request.setRequestHeader('Content-Type', 'text/html');
request.send(process.argv[2]);
//# sourceMappingURL=app.js.map