function forwardPropagation() {
  var X = nj.array([[1,5,6,7]], dtype="float32")
  X = X.divide(256)
  X = X.T
  var w1 = nj.array([[1,2,3,5],[5,6,7,8],[9,10,11,12]], dtype="float32")
  var b1 = nj.array([[1],[1],[1]], dtype="float32")
  var w2 = nj.array([[1,2,3]], dtype="float32")
  var b2 = nj.array([[1]], dtype="float32")

  var z1 = nj.dot(w1,X)
  z1 = z1.add(b1)

  for(i=0; i < z1.size; i++) {
    if(z1.get(i) < 0 ) {
      z1.set(i,0)
    }
  }

  var z2 = nj.dot(w2,z1)
  z2 = z2.add(b2)
  var a2 = nj.sigmoid(z2)
  return a2
}

a2 = forwardPropagation()
console.log(a2.toString())


var demoColorPicker = new iro.ColorPicker("#color-picker-container", {
  // Set the size of the color picker UI
  width: 200,
  height: 200,
  // Set the initial color to red
  color: {r: 45, g: 0, b: 224},
  borderColor: "#000",
  borderWidth: 1
});

demoColorPicker.on("color:change", function(color, changes) {
  // Log the color's hex RGB value to the dev console

  console.log(color.rgbString);
  $("#home").css("background-color",color.rgbString)
});
