# ColorPredictor
This is an interactive web app live at https://color-predictor.herokuapp.com/index.html. It uses a single hidden layer(3 neurons) neural network model using tensorflow.

## Instructions on how to use the application:
1.) Enter a line of text.\
2.) Now steadily change the background color using the color picker tool provided at bottom-right(Use the slider also).\
3.) As you are gradually changing the background color, the moment you reach a point where the text is not clear, the AI detects it and changes the text color so that the text is visible again.\
4.) Continue changing the background color. The AI changes text color from black to white or vice-versa.

It's a simple app to demonstrate how Machine Learning is used for predictions. The app tries to predict if a given text color is readable for a given background color. For simplicity I have fixed the text color only to black or white, while the background color can be any combination of RGB(i.e. 256^3 possibilities).
So as the user gradually changes the background color using the color picker tool, the model continuously predicts "Can See"(1) or "Can't See"(0). The forward propagation continuously happens in the front-end itself using numjs in the browser. If it is "Can See"(1) then the model doesn't change the text color. The moment the model predicts "Can't See"(0), it changes the text color either to black or white so that the text is readable for that background color.

The code for generating data is in "data_generator.py". The color combinations were scraped from https://contrast-ratio.com/. The 5 data columns in the csv file are "Red", "Green", "Blue", "Black text or white text(0 or 1)", "Can see or can't see(0 or 1)". The first 3 column values give RGB of background color. The 4th column indicates if the current text color is black(0) or white(1). The last column indicates if a user can see the text or no(0 or 1).

The model code is in color_predictor.ipynb. The model was trained on google-colab. Around 99.8% accuracy with training set(normalized to 1, size around 60k). 1000 epochs, batch-size of 20 and learning rate of 0.0001. Around 99% accuracy was on both test and dev set without regularization.
