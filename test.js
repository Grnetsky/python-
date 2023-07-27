async function foo (){
    var p,x
    await new Promise(resolve => setTimeout(function (num){ p = 0;  x = num;resolve()},1000,123))
    console.log(p)
    console.log(x)
}
foo()