import aiml
import sqlite3
import datetime
import time
import sys


def my_print(output):
    if output.find(";") != -1:
        sys.stdout.write("Bot >> ")
        for line in output.split(";"):
            sys.stdout.write(line+"\n")
        sys.stdout.flush()
    else:
        print "Bot >> "+output


#Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
bot_file = open("bot.txt", "r")

for line in bot_file:
    k, v = line.split(',')
    kernel.setBotPredicate(k, v)
# Press CTRL-C to break this loop
print "Enter 1.Chat with Bot 2. To see previous conversations"
ch = int(raw_input())
'''
DB connect code
'''
con = sqlite3.connect("test.db")
cursor = con.cursor()

if ch == 1:
    sid = time.time()
    while True:
        bot_input = raw_input("Human >> ")
        bot_output = kernel.respond(bot_input)
        bot_output = bot_output.decode("utf-8")
        bot_output = bot_output.encode("ascii")
        #print "BOT >> "+bot_output
        my_print(bot_output)
        cursor.execute("INSERT INTO AI VALUES(?, ?, ?)", [sid, bot_input, bot_output])
        con.commit()
        if bot_output == "bye":
            con.close()
            break
elif ch == 2:
    chat_time = []
    print "Enter Number to view Chat Log"
    count = 1
    for row in cursor.execute("SELECT DISTINCT sid FROM AI"):
        temp = row[0].decode('utf-8')
        chat_time.append(temp)
        print str(count) + ") " + datetime.datetime.strftime(datetime.datetime.fromtimestamp(float(temp)), "%d/%m/%Y %I:%M:%S %p")
        count += 1
    opt = int(raw_input())
    sid = str(chat_time[opt-1])
    row = cursor.execute("SELECT qstn,ans FROM AI WHERE sid = ?", [sid])
    for data in row.fetchall():
        print "Human >> "+data[0]
        print "Bot >> "+data[1]
