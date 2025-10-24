//const code_blocks = ["Accelerometer","Buttons","Capacitive_Touch","LCD_Bitmap","LCD_Text_and_Background","LCD_Turtle","Light_Sensor","Microphone","NeoPixels","Servo","Speaker","Switch_and_red_LED","Temperature","Lab_Robot","Lab_Temp_Sensor","bluetooth_example"]
$(function () {
    for (let code of code_blocks) {
        $( "."+code+"_code" ).load("https://raw.githubusercontent.com/brianpetty3/CY105_Lab/main/lab%20code/"+code+".py");
    } 

});
