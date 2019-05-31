#!/usr/bin/python3

import requests, socket, psutil, sys

def wrong_param():
    print ("\n  List of options:\n")
    print ("    -ext  External  IP")
    print ("    -int  Internal network IP")
    print ("    -all  All IP adresses\n")
    exit()

def get_ip(param):

    feedback = []
    if 'ext' in str(param) or 'all' in str(param):
        feedback.append(('external',requests.get('https://api.ipify.org').text))
    if 'int' in str(param) or 'all' in str(param):
        dt = psutil.net_if_addrs()
        for i in dt.keys():
            if 'AF_INET' in str(dt[i][0][0]) and i != 'lo':
                feedback.append((i,dt[i][0][1]))
    else:
        wrong_param()

    return feedback


if __name__ == "__main__":
    try:
        param = sys.argv[1]
        ips = get_ip(param)
        row=0
        for i in ips:
            print(ips[row][0],"-",ips[row][1])
            row+=1
    except:
        wrong_param()

