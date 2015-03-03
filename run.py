from ftplib import FTP
from differ import DictDiffer

import settings
import pprint
import pickle
import os

def connectFtp(url, cwd, login, passwd):
    ftp = FTP(url)
    if login is not None and passwd is not None:
        ftp.login(login, passwd)
    else:
        ftp.login()
    ftp.cwd(cwd)
    return ftp

def main():
    pp = pprint.PrettyPrinter(indent=4)
    ftp = connectFtp(settings.FTP_URL, 
                     settings.BASE,
                     settings.LOGIN,
                     settings.PASSWD)
    tasks = []
    hist = {}
    if os.path.isfile('hist.pkl'):
        hist_pkl = open('hist.pkl', 'rb')
        hist = pickle.load(hist_pkl)
        hist_pkl.close()


    for folder in settings.FOLDERS:
        print folder

        if not hist.has_key(folder):
            hist[folder] = {}

        latest = {s : folder+'/'+s for s in ftp.nlst(folder)}
        diff = DictDiffer(latest, hist[folder])

        if len(diff.added()) > 0:
            tasks += [(item, latest[item]) for item in diff.added()]

        if diff.changed():
            hist[folder] = latest

    hist_pkl = open('hist.pkl', 'wb')
    pickle.dump(hist, hist_pkl)
    hist_pkl.close()

    print 'To be downloaded:'
    pp.pprint(tasks)
    c = raw_input('Continue? (y/n)')
    if c == 'y' or c == 'Y':
        for fname, path in tasks:
            print 'Downloading... %s' % fname 
            if not os.path.exists(settings.DOWNLOAD):
                os.makedirs(settings.DOWNLOAD)
            ftp.retrbinary('RETR %s' % path, open(settings.DOWNLOAD+'/'+fname, 'wb').write)
        else:
            print 'diff stored, bye!'

    ftp.close()

if __name__ == "__main__":
    main()
