import os, sys, time
from optparse import OptionParser
import logging

import serial
import xmodem

class pgfile(object):
    def __init__(self, filepath, callback):
        self.btotal = os.stat(filepath).st_size
        self.bread = 0
        self.f = file(filepath, "rb")
        self.cb = callback
        self.t_start = time.time()

    def read(self, size=1):
        r = self.f.read(size)
        self.bread += len(r)
        t_now = time.time()
        if t_now > self.t_start + 1 or self.bread == self.btotal:
            self.cb(self.bread, self.btotal)
            self.t_start = t_now
        return r

    def close(self):
        return self.f.close()

    def write(self, data):
        return 0

class COMport(object):
    def __init__(self, port, baudrate):
        self.s = serial.Serial(opt.com_port, 115200)
        self.buffer = ""

    def send(self, text):
        self.s.write(text + chr(13))

    def waitfor(self, text, timeout = None):
        t_start = time.time()
        while True:
            if timeout and (time.time() > t_start + timeout):
                return False
            l = self.s.inWaiting()
            if not l:
                time.sleep(0.1)
                continue
            self.buffer += self.s.read(l)

            #print >> sys.stderr, "[log] buffer =", self.buffer

            while len(self.buffer) >= len(text):
                if self.buffer.startswith(text):
                    self.buffer = self.buffer[len(text):]
                    return True

                self.buffer = self.buffer[1:]

    def sendXmodem(self, filepath):

        def getc(size, timeout=1):
            return self.s.read(size)

        def putc(data, timeout=1):  
            return self.s.write(data)

        def pgupdate(read, total):
            print "\r%d/%d bytes (%2.f%%) ..." % (read, total, read*100/total),

        m = xmodem.XMODEM(getc, putc)
        f = pgfile(filepath, pgupdate)
        return m.send(f)

def main(port, baud_rate, bin_path, recovery_mode=True):
    try:
        s = COMport(port, baud_rate)
    except serial.serialutil.SerialException as e:
        print >> sys.stderr, "Error opening", opt.com_port, "!!!! :", e
        sys.exit(-1)

    if recovery_mode:
        s.send("AT#Reboot")
        if not s.waitfor("Recovery Mode", 2):
            print "Failed to enter 'Recovery Mode' automatically, please press reset key manually"
            s.waitfor("Recovery Mode")

        print "Recovery Mode entered, Starting to upload..."

    s.send("AT#UpdateFW")
    s.waitfor("C")
    if s.sendXmodem(opt.bin_path):
        print "Update done! bye"
        return True
    else:
        print "Error: Fail to update!!!!"
        return False

if __name__ == "__main__":

    logging.basicConfig()

    parser = OptionParser(usage="python %prog [options]")
    parser.add_option("-c", dest="com_port", help="COM port, can be COM1, COM2, ..., COMx", default="COM5")
    parser.add_option("-r", dest="baud_rate", help="Baud rate, can be 9600, 115200, etc...", type="int", default=115200)
    parser.add_option("-s", dest="ssid", help="Ssid of target ap")
    parser.add_option("-p", dest="password", help="Password of target ap")
    (opt, args) = parser.parse_args()

    if not opt.com_port:
        print >> sys.stderr, "\nError: Invalid parameter!! Please specify COM port.\n"
        parser.print_help()
        sys.exit(-1)

    if not opt.ssid:
        print >> sys.stderr, "\nError: Invalid parameter!! Please specify SSID.\n"
        parser.print_help()
        sys.exit(-1)

    try:
        s = COMport(opt.com_port, opt.baud_rate)
    except serial.serialutil.SerialException as e:
        print >> sys.stderr, "Error opening", opt.com_port, "!!!! :", e
        sys.exit(-1)

    s.send("AT#Default")
    s.waitfor("SM=1, Sub=0")

    if opt.password:
        s.send("AT#SetAP -s%s -p%s" % (opt.ssid, opt.password))
        s.waitfor("PMK...")
    else:
        s.send("AT#SetAP -s%s" % opt.ssid)

    print "Configuring...",

    s.waitfor("SetAP Done!")
    print "Done!"

    s.waitfor("Auth with:")
    print "Connecting to AP..."

    s.waitfor("Got IP")
    print "AP Connected!"
