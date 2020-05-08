// 从 python-shell 导入一个 PythonShell 对象 (注意大小写)
const {PythonShell}  = require("python-shell")
// PythonShell 主要有 run() 和 runString() 两个方法, 这里我们用 run()
// run() 第一个参数是要调用的 py01 文件的路径
// 第二个参数是可选配置 (一般传 null)
// 第三个参数是回调函数

let options = {
  mode: 'text',
  pythonPath: 'py',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: 'py',   // python文件目录，以项目为基准
  args: ['value1', 'value2', 'value3']
};

PythonShell.run('engine.py', options, function (err, results) {
  console.log(123);
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
});