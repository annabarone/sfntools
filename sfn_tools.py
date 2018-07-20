import click
import random
import time
from lib.utils import *
from DNS.dns import *

@click.group()
def cli():
    pass

@click.command()
@click.option('--config', help='Settings file')
@click.option('--host', help='Host to send generated log messages to', default='localhost')
@click.option('--port', help='Host port to connect - default is 5514', default=5514)
def dns(config,host,port,totNumEvents,daysPast,daysFuture):
    # Set up default values for variables
    totNumEvents = 1000000
    daysPast = 30
    daysFuture = 30
    

    click.echo("In DNS")
    if config:
        click.echo(f"File is {config}")
        host="Tester"
        port=1024
    else:
        config="DNS/dns.config"
    click.echo(f"Config is {config}")        
    click.echo(f"Host is {host}")
    click.echo(f"Port is {port}")

    flag = True
    count = 0
    start = time.time()
    while count < totNumEvents:
        numEvents = random.randint(1,25)
        sleepTime = random.randint(1,3)
        for event in range(numEvents):
            startDate = f"{datetime.datetime.now()- timedelta(days=daysPast):%Y/%m/%d %H:%M:%S}"
            endDate = f"{datetime.datetime.now()- timedelta(days=daysFuture):%Y/%m/%d %H:%M:%S}"
            print(f"Start Date is {startDate} and End Date is {endDate}")
            exit()
            
            startDate = "2018/7/15 01:30:00"
            endDate = "2018/7/30 01:30:00"
            genDate = randomDate(startDate,endDate,random.random())
            srcIP = randomLine(open("lib/srcIPs.txt"))
            srcIP = srcIP.strip()
            dstIP = randomLine(open("lib/dnsServers.txt"))
            dstIP = dstIP.strip()
            threatID = randomLine(open("lib/sigs_list.txt"))
            threatID = threatID.strip()
            #threatID = "Suspicious DNS Query (Backdoor.bifrose:ggdstrojan.ddns.net)(3800001)"
            severity = "medium"
            msg = f'1,{genDate},015351000011583,THREAT,dns,2049,{genDate},{srcIP},{dstIP},192.168.55.20,{dstIP},SFN-Logging,,,dns,vsys1,trust,untrust,ethernet1/2,ethernet1/1,SFN-Log-Fowarding,{genDate},18680,1,54848,53,7771,53,0x402000,udp,sinkhole,"",{threatID},any,medium,client-to-server,50115,0x2000000000000000,192.168.0.0-192.168.255.255,United States,0,,0,,,0,,,,,,,,0,12,0,0,0,,FW-{sleepTime},,,,,0,,0,,N/A,dns,AppThreat-2606-3102,0x0,0,4294967295'

            sendLog(f"{host}",port,msg)

            #time.sleep(sleepTime)
            #print(f"Domain is {threatID}")
            count += 1
            
        print(f"Started at {start}")
        print(f"Ended at {time.time()}")
        print(f"Time to send {count} events: {str(time.time() - start)} seconds")
        flag = False
        #time.sleep(1)
                    
@click.command()
def iot():
    click.echo("In IoT")

@click.command()
def url():
    click.echo("In URL")

cli.add_command(dns)
cli.add_command(iot)
cli.add_command(url)

