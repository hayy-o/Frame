// alert("Welcome to my site");
// let name1= prompt("Enter your name");
// let color = prompt("Choose a color: red, green, or blue");
// do {
// color = prompt("Choose a color: red, green, or blue");
// } while (color !== "red" && color !== "green" && color !== "blue");
// console.log(name1)
// console.log(`Welcome ${name1}`)



// ////task2///

// let word = prompt("Enter a word");
// let choice = prompt("Consider case? (ok / no)");
// if (choice === "no") {
// word = word.toLowerCase();
// };
// let reversed = "";
// for (let i = word.length - 1; i >= 0; i--) {
// reversed += word[i];
// };
// if (word === reversed) {
// console.log("is palindrome");
// } else {
// console.log("not a palindrome");
// };


// ///1.3///
// let name = prompt("Enter your name (letters only):");
// let phone = prompt("Enter your phone number (8 digits):");
// let mobile = prompt("Enter your mobile number (11 digits, starts with 010/011/012):");
// let email = prompt("Enter your email:");

// //VALIDATION
// if (!/^[A-Za-z]+$/.test(name)) {
// console.log("Name must contain only letters.");
// } else if (!/^\d{8}$/.test(phone)) {
// console.log("Phone number must be exactly 8 digits.");
// } else if (!/^(010|011|012)\d{8}$/.test(mobile)) {
// console.log("Mobile number must be 11 digits and start with 010, 011, or 012.");
// } else if (!/^[\w\.-]+@[\w\.-]+\.\w+$/.test(email)) {
// console.log("Invalid email format.");
// } else {
// console.log(`Welcome ${name}! Your information is valid.`);
// };

////task3///
// let a
// do {
//     a = prompt("Enter first number:")
// } while(isNaN(parseInt(a)))

// let b = parseInt(prompt("Enter second number:"))
// let c = parseInt(prompt("Enter third number:"))

// let sum = a + b + c ;
// let multiplication = a * b * c;
// let division = a / b / c;

// console.log(`sum of the 3 values ${a} + ${b} + ${c} = ${sum}`);
// console.log(`multiplication of the 3 values ${a} * ${b} * ${c} = ${multiplication}`);
// console.log(`division of the 3 values ${a} / ${b} / ${c} = ${division}`);

// ///task4//
// let a
// do {
//     a = prompt("Enter first number:")
// } while(isNaN(parseInt(a)))
// let numbers = [];
// for (let i = 0; i < 5; i++) {
// let num = +prompt("Enter number " + (i + 1));
// numbers.push(num);
// }
// let x =[...numbers];
// let ascending = [...numbers].sort(function(a, b) {
// return a - b;
// });
// let descending = [...numbers].sort(function(a, b) {
// return b - a;
// });
// console.log("You've entered:");
// for (let i = 0; i < x.length; i++) {
// console.log(x[i]);
// };
// console.log("Ascending:");
// for (let i = 0; i < ascending.length; i++) {
// console.log(ascending[i]);
// };
// console.log("Descending:");
// for (let i = 0; i < descending.length; i++) {
// console.log(descending[i]);
// };


// //task5//
// let radius = +prompt("Enter the radius of the circle");
// let area = Math.PI * Math.pow(radius, 2);
// alert("The area of the circle is: " + area);
