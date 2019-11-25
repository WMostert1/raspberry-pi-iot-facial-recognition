# coding: utf-8
import subprocess
from playsound import playsound
import codecs
import os.path
from os import path


def generate_mp3(text, mp3_file_name):
    if path.exists(mp3_file_name + ".mp3"):
        return

    file_names = ''
    cnt = 0
    for line in text:
        line = line.replace('"', '\\"')
        command = 'aws polly synthesize-speech --text-type ssml --output-format "mp3" --voice-id "Salli" --text "{0}" {1}'

        rendered = '<speak><amazon:effect name=\\"drc\\">' + line.strip() + '<break time=\\"1s\\"/></amazon:effect></speak>'

        file_name = ' polly_out{0}.mp3'.format(u''.join(str(cnt)).encode('utf-8'))
        cnt += 1
        command = command.format(rendered.encode('utf-8'), file_name)
        file_names += file_name
        print command
        subprocess.call(command, shell=True)

    print file_names
    execute_command = 'cat ' + file_names + '>' + mp3_file_name + '.mp3'
    subprocess.call(execute_command, shell=True)

    execute_command = 'rm ' + file_names
    print 'Removing temporary files: ' + execute_command
    subprocess.call(execute_command, shell=True)


def generate_intruder():
    generate_mp3(
        ["Unauthorized presence detected in two two eight Wembley Square.", "Dispatching alert to Master."], "intruder")



def generate_greeting(name):
    generate_mp3(["Welcome home " + name], "welcome_" + name)

def play_greeting(name):
    generate_greeting(name)
    print("Playing greeting")
    playsound('welcome_'+name+'.mp3')

def play_intruder():
    generate_intruder()
    print("Playing intruder alert")
    playsound('intruder.mp3')


generate_intruder()
generate_greeting("Master")
