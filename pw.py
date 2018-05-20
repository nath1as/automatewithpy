#! python3
#pw.py - An insecure password locker

import sys, pyperclip

PASSWORDS = { 'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
              'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
              'luggage': '12345' }


if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.' + PASSWORDS[account])
else:
    print('There is no account named ' + account)
