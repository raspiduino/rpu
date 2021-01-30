# rpu - The stupid realtime Python code updater
## What is this?
rpu is a realtime Python code updater. It means your code's result will be display right after you edit your code. You can use it for GUI editing (I personally use for pygame), preview your code,...
## How this work?
First, the script will import your python script as a module (using importlib). Then it will read your script's content. Some seconds later, it will read again, and if you edit your code, the content will change and your script will be imported again. By that, it keeps your program updated. You can change the delay time between updates.
## Usage
```cmd
rpu.py yourpythonscript.py [delaytime]
```
<br>Delay time is in second. Default is 5 sec
<br>If you just enter ```rpu.py``` or ```rpu.py help```, it will display a simple help.

## Demo
<img src="https://github.com/raspiduino/rpu/raw/main/demo.gif" width="683" height="384"/>

<br>You can download the video <a href="https://github.com/raspiduino/rpu/raw/main/demo.webm">here</a> or <a href="https://user-images.githubusercontent.com/68118236/106348916-73434080-62fc-11eb-9eb6-07bef19a0409.mp4">here</a>
<br>Or you can watch the video in <a href="https://github.com/raspiduino/rpu/releases">Release</a>
<br>You can try hello.py or pygametest.py in the repo.

## License
Under <a href="https://github.com/raspiduino/rpu/blob/main/LICENSE">GPLv3</a>
