// Copy Text to clipboard
// Message will be displayed near the element and disappear soon after
function showFloatingMessage(message, element) {
    var rect = element.getBoundingClientRect();
    const tip = document.createElement('span');
    tip.innerText = message;
    tip.classList.add("floating-message");
    tip.style.position = "absolute";
    var top = rect.top + ((document.documentElement && document.documentElement.scrollTop) || document.body.scrollTop);
    tip.style.top = top + "px";
    tip.style.left = (rect.left + ((rect.right - rect.left) / 2)) + "px";
    document.body.appendChild(tip);

    // apply 'fade-message-out' to make it fade with css animation -- and then remove it altogether.
    setTimeout(function () {
        tip.classList.add("fade-message-out");
        setTimeout(function () { tip.parentNode.removeChild(tip); }, 1000);
    }, 10);
}
function copyToClipboard(value, element) {
    const textArea = document.createElement('textarea');
    textArea.style.position = "absolute";
    // top is at current height, to avoid causing a scroll on IE/Safari.
    var lastScrollHeight = element.scrollHeight; // this is used to prevent any unwanted scrolling (particularly in IE and Safari)
    textArea.style.left = "-100%"; // off screen
    textArea.style.width = "200px";
    textArea.textContent = value.trim();
    element.parentNode.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    textArea.parentNode.removeChild(textArea);
    showFloatingMessage("copied to clipboard.", element);
    var scrollDiff = element.scrollHeight - lastScrollHeight;
    element.scrollTop += scrollDiff; // scroll us back where we were... if there has been any change.

}
// Inject a button before every pre...
$("<button type='button' class='copy-text btn btn-secondary btn-sm' data-bs-toggle='tooltip' data-bs-placement='top' data-bs-html='true' data-bs-placement='right' title='Copy code to clipboard'><i class='fa-solid fa-copy'></i> Copy</button>").insertBefore($("pre"));

// And have it call 'copy to clipboard'
$(".copy-text").click(function (e) {
    copyToClipboard($(this).next("pre").text(), this); // that final *this* is the DOM element.
    // stop any other consequence fo this click from occurring.
    e.preventDefault();
    return false;
});

// Initiate tool tips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
});

// Update this if you add new code blocks to the webpages
const code_blocks = ["Accelerometer","Buttons","Capacitive_Touch","Morse_Code_Starter","Nightlight_starter","Robot_Button_Starter","LCD_Bitmap","LCD_Text_and_Background","LCD_Turtle","Light_Sensor","Microphone","NeoPixels","Servo","Speaker","Switch_and_red_LED","Temperature","Lab_Robot","Lab_Temp_Sensor"]

$(function () {
    //Highlights components of Bluefruit board in pop-out window
    $('.map').maphilight({
        fill: true,
        fillColor: '00ffff',
        strokeColor: 'ffff00',
        strokeWidth: 2,
    });
    $('#rstBtnList').mouseover(function (e) {
        $('#rstBtn').mouseover();
    }).mouseout(function (e) {
        $('#rstBtn').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#capList').mouseover(function (e) {
        $('#A2').mouseover();
    }).mouseout(function (e) {
        $('#A2').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#pixelList').mouseover(function (e) {
        $('#NP0').mouseover();
    }).mouseout(function (e) {
        $('#NP0').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#switchList').mouseover(function (e) {
        $('#switch').mouseover();
    }).mouseout(function (e) {
        $('#switch').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#tempList').mouseover(function (e) {
        $('#tempSensor').mouseover();
    }).mouseout(function (e) {
        $('#tempSensor').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#micList').mouseover(function (e) {
        $('#micSensor').mouseover();
    }).mouseout(function (e) {
        $('#micSensor').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#accelList').mouseover(function (e) {
        $('#accelSensor').mouseover();
    }).mouseout(function (e) {
        $('#accelSensor').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#lightList').mouseover(function (e) {
        $('#lightSensor').mouseover();
    }).mouseout(function (e) {
        $('#lightSensor').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#btnAList').mouseover(function (e) {
        $('#btnA').mouseover();
    }).mouseout(function (e) {
        $('#btnA').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#btnBList').mouseover(function (e) {
        $('#btnB').mouseover();
    }).mouseout(function (e) {
        $('#btnB').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#speakerList').mouseover(function (e) {
        $('#speaker').mouseover();
    }).mouseout(function (e) {
        $('#speaker').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#redLEDList').mouseover(function (e) {
        $('#redLED').mouseover();
    }).mouseout(function (e) {
        $('#redLED').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#greenLEDList').mouseover(function (e) {
        $('#greenLED').mouseover();
    }).mouseout(function (e) {
        $('#greenLED').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#USBList').mouseover(function (e) {
        $('#USB').mouseover();
    }).mouseout(function (e) {
        $('#USB').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#CPUList').mouseover(function (e) {
        $('#CPU').mouseover();
    }).mouseout(function (e) {
        $('#CPU').mouseout();
    }).click(function (e) { e.preventDefault(); });
    //Highlights wiring in Robotics Lab
    $('#gndWireTbl').mouseover(function (e) {
        $('#gndWire1').mouseover();
    }).mouseout(function (e) {
        $('#gndWire1').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#pwrWireTbl').mouseover(function (e) {
        $('#pwrWire1').mouseover();
    }).mouseout(function (e) {
        $('#pwrWire1').mouseout();
    }).click(function (e) { e.preventDefault(); });
    $('#ctlWireTbl').mouseover(function (e) {
        $('#ctlWire1').mouseover();
    }).mouseout(function (e) {
        $('#ctlWire1').mouseout();
    }).click(function (e) { e.preventDefault(); });

    //Loads the .py file code and places it in the correct location finding the <pre><code> tags by id
    for (let code of code_blocks) {
        console.log(code)
        $.get("https://raw.githubusercontent.com/usma-eecs/CY105_Lab/main/lab%20code/"+code+".py", function(data, status){
            
            const collection = document.getElementsByClassName(code+"_code" );
            for (let elem of collection) {
                elem.innerHTML = data;
                hljs.highlightElement(elem);
            };
        });
    };
});

