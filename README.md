# GraphicSeqCalculator
This a python App that is supposed to calculate boolean function based on number of input/output variables + the cases where output variables are 1 or X or 0 
The frame of this project was in a school subject (real time OS systems) where some of the problems , most of them were sequential ; In cases we're the output/input variables are few we can do the coding with switch case with no problem , but when the variables are many I suggested that we make a function that takes inputs states and set outputs through boolean function
The App contain a GUI so you enter how much INPUT/OUTPUT you've got and you set the cases where you have 1/0/X and you get the boolean function
The calculations are made following the McCluskey algorithm , I used a library called logicmin for the implementation of the algorithm
The filling of the input cases (Truth table) is made with a library called itertools , both of these library are already in github
This a project to solve a problem that I faced , I'm sharing it so that people can use it since I could not find some easy to use app on internet (except from web apps but there was no source code and the number of inputs was limited) , to point from this app is to embed it in a bigger project so that you don't have to code the cases by yourself without using the GUI , or you can just use it as it is , that's why I added the GUI.

