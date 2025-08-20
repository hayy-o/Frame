window.onload= function() {
    document.querySelector("h3").style.color= "red";
};

// comment
/*
multi
5

// ES6
var myname = "lala";
console.log("Hello" + myname);
console.log(`Hello ${myname}`);
console.creatElement(l);

console.log('Hello');

// concatenation
let a = "We love"
let b = "JavaScript"
let c = " "

document.write(a + c +b);
document.write(a + " " +b);
console.log(a , b)*/


let cTitle = "Elzero" , cDescription = "Elzero Web School" , cDate = "25/10" ;

let m = `
 <div class= "m" >
   <h3> ${cTitle} </h3>
   <p> ${cDescription} </p>
   <span> ${cDate} </span>
 </div>
`;

console.log(` ${cTitle}   ${cDescription}  ${cDate} `)
document.body.innerHTML = m.repeat(4);


hello.innerHTML = "Option";