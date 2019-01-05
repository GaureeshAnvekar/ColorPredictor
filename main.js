function forwardPropagation(inputColorList) {
  var X = nj.array([inputColorList], dtype = "float32")
  X = X.T
  console.log(X.toString())
  var w1 = nj.array([
    [3.9428747, 11.59308, 1.8363051, -16.980663],
    [2.668514, 3.8103638, 0.84936374, -1.9624231],
    [0.22013244, -1.5614797, 1.0716099, 4.961385]
  ], dtype = "float32")
  var b1 = nj.array([
    [-0.38128474],
    [-3.9973104],
    [-0.08543456]
  ], dtype = "float32")
  var w2 = nj.array([
    [23.99707, -17.736904, 4.3511972]
  ], dtype = "float32")
  var b2 = nj.array([
    [-6.6498837]
  ], dtype = "float32")

  var z1 = nj.dot(w1, X)
  z1 = z1.add(b1)

  for (i = 0; i < z1.size; i++) {
    if (z1.get(null, i) <= 0) {
      z1.set(null, i, 0)
    }
  }

  var z2 = nj.dot(w2, z1)
  z2 = z2.add(b2)
  console.log(z2.toString())
  var a2 = nj.sigmoid(z2)
  return a2
}


var demoColorPicker = new iro.ColorPicker("#color-picker-container", {
  // Set the size of the color picker UI
  width: 200,
  height: 200,
  color: {
    r: 89,
    g: 0,
    b: 255
  },
  borderColor: "#000",
  borderWidth: 1
});

demoColorPicker.on("color:change", function(color, changes) {
  // Log the color's hex RGB value to the dev console
  $("#light-bulb").tooltip({
    position: {
      my: "center top-80",
      at: "center top",
      using: function(position, feedback) {
        $(this).css(position);
        $("<div>")
          .addClass("arrow")
          .addClass(feedback.vertical)
          .addClass(feedback.horizontal)
          .appendTo(this);
      }
    }
  })
  console.log("selected color " + color.rgbString)
  console.log($("#text").text())


  if ($.trim($("#text").text()) != "ENTER TEXT HERE!") {
    $("#home").css("background-color", color.rgbString)

    //Get the rgb colors from object for forward propagation. Pass it as a list
    inputColorList = [parseFloat(color.rgb["r"]) / 256, parseFloat(color.rgb["g"]) / 256, parseFloat(color.rgb["b"]) / 256]
    //console.log(inputColorList)
    //Get the current text color
    currentTextColor = $("#text").css("color")
    if (currentTextColor == "rgb(255, 255, 255)") {
      inputColorList.push(1.0) //white text
    } else {
      inputColorList.push(0.0) //black text
    }

    //Call forwardpropagation with inputColorList
    //console.log(inputColorList)
    prediction = forwardPropagation(inputColorList)
    //prediction is ndarray like [[ans]].so index it appropriately
    prediction = prediction.get(0, 0)
    console.log("prediction is " + prediction)

    console.log("Color is " + $("#text").css("color"))
    //if prediction less than 0.5 change text color, black to white or vice-versa
    if (prediction < 0.5) {
      color = $("#text").css("color")
      if (color == "rgb(255, 255, 255)") { //if text is white, now change to black
        $("#text").css("color", "black")
      } else { // if text is black change to white
        $("#text").css("color", "white")
      }
      //turn on animations correctly
      $("#light-bulb").mouseover()
      $('#light-bulb2').css({
        'opacity': '1'
      });

      setTimeout(function() {
        $("#light-bulb").mouseout()
        $('#light-bulb2').css({
          'opacity': '0'
        });
      }, 10000)
    }
  }
});
