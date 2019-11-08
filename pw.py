#! python3
#　pw.py

PASSW = {
    'email': 'PASS_EMAIL',
    'sns': 'PASS_SNS',
    'blog': 'PASS_BLOG'
}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('NG')
    sys.exit()

account = sys.argv[1]

if account in PASSW:
    pyperclip.copy(PASSW[account])
    print('copy!')
else:
    print('nothing...')