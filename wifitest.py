#pip install speedtest-cli
import speedtest
from tqdm import tqdm
import matplotlib.pyplot as plt
import time 

def wifitest():
    
    """ This is a test to see WiFi speeds. Download speed is graphed on the X-axis and upload speed in graphed on the Y-axis. The ping, since it remains constant during the test, will be printed out.""" 
    
    m1 = input('How many data points would you like to collect? (enter an integer)  ')
    
    start_time = time.perf_counter()
    st = speedtest.Speedtest()
    download = []
    upload = []
    ping = []
    for i in tqdm(range(int(m1))):
        x = st.download()   
        y = st.upload()
        servernames = []
        st.get_servers(servernames)
        z = st.results.ping
        
        #multiplying by 0.000001 is necessary as it converts the units to Mpbs
        download.append((x*0.000001))    
        upload.append((y*0.000001))
        ping.append(z)
    end_time =  time.perf_counter()
        
    times = end_time - start_time
    
    if times < 60:
        print('\n' + "This took", times,  "seconds.")
    if 3600 > times > 60:
        minutes = (float(times)/60)
        print('\n' + "This took", minutes,  "minutes.")
    if times > 3600:
        hours = (float(times)/3600)
        print('\n' + "This took", hours,  "hours.")
    print("The ping is: ", ping[0])    
    
    plt.scatter(download, upload, ping)
    plt.xlabel('Download Speed (Mbps)')
    plt.ylabel('Upload Speed (Mbps)')
    plt.show()
    datapoints(download, upload, ping)
    
def datapoints(download, upload, ping):
    if answer =='Y':
        print('\n'+'Download speeds:', download,'\n'+'Upload speeds:', upload,'\n'+'Ping speeds:', ping)
    if answer == 'N':
        print('')

answer = input('Would you like the data (Upload/download/ping speed) printed out? (Y/N)  ')

if answer == 'Y':
    wifitest()
if answer == 'N':
    wifitest()