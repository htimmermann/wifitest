# wifitest
A code that analyzes WiFi speeds and outputs a graph with the points (X-axis being download speeds and Y-axis being upload speeds). The user has the option of printing out all data.

REQUIREMENTS:
-  speedtest-cli, tqdm, time, matplotlib.pyplot
- to install any of these, use pip install ... 

NOTES:
- Since the ping speed remains constant during the test, it is printed at the end
- The less spread out the points are, the more consistent the WiFi is
- The actual test itself does take time however, the speed of the test is not based on Wifi speeds
