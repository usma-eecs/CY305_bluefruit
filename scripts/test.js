const code_blocks = ["Accelerometer","Buttons","Capacitive_Touch","LCD_Bitmap","LCD Text and Background","LCD Turtle","Light Sensor","Microphone","NeoPixels","Servo","Speaker","Switch and red_LED","Temperature"]
$(function () {
    for (let code of code_blocks) {
        console.log(code);
        $( "#"+code ).load("https://raw.githubusercontent.com/regnjere/CY105_Lab/e6c9bfa1509232b8dcf44d39481b4c2d452ce450/lab%20code/Starter%20Code/"+code+".py");
    } 
});
