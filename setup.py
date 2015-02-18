#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('util', 'lib/util.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum-drk requires Python version >= 2.7.0...")



if (len(sys.argv) > 1) and (sys.argv[1] == "install"): 
    # or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files = []
    usr_share = util.usr_share_dir()
    if not os.access(usr_share, os.W_OK):
        try:
            os.mkdir(usr_share)
        except:
            sys.exit("Error: cannot write to %s.\nIf you do not have root permissions, you may install Electrum-drk in a virtualenv.\nAlso, please note that you can run Electrum-drk without installing it on your system."%usr_share)

    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-drk.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-drk.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum-drk.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum-drk.mo' % lang]))


    appdata_dir = os.path.join(usr_share, "electrum-drk")
    data_files += [
        (appdata_dir, ["data/README"]),
        (os.path.join(appdata_dir, "cleanlook"), [
            "data/cleanlook/name.cfg",
            "data/cleanlook/style.css"
        ]),
        (os.path.join(appdata_dir, "sahara"), [
            "data/sahara/name.cfg",
            "data/sahara/style.css"
        ]),
        (os.path.join(appdata_dir, "dark"), [
            "data/dark/name.cfg",
            "data/dark/style.css"
        ])
    ]

    for lang in os.listdir('data/wordlist'):
        data_files.append((os.path.join(appdata_dir, 'wordlist'), ['data/wordlist/%s' % lang]))
else:
    data_files = []

setup(
    name="Electrum-drk-DRK",
    version=version.ELECTRUM-DRK_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'pyasn1-modules',
        'pyasn1',
        'qrcode',
        'SocksiPy-branch',
        'protobuf',
        'tlslite'
    ],
    package_dir={
        'electrum-drk': 'lib',
        'electrum-drk_gui': 'gui',
        'electrum-drk_plugins': 'plugins',
    },
    scripts=['electrum-drk-drk'],
    data_files=data_files,
    py_modules=[
        'electrum-drk.account',
        'electrum-drk.bitcoin',
        'electrum-drk.blockchain',
        'electrum-drk.bmp',
        'electrum-drk.commands',
        'electrum-drk.daemon',
        'electrum-drk.i18n',
        'electrum-drk.interface',
        'electrum-drk.mnemonic',
        'electrum-drk.msqr',
        'electrum-drk.network',
        'electrum-drk.network_proxy',
        'electrum-drk.old_mnemonic',
        'electrum-drk.paymentrequest',
        'electrum-drk.paymentrequest_pb2',
        'electrum-drk.plugins',
        'electrum-drk.qrscanner',
        'electrum-drk.simple_config',
        'electrum-drk.synchronizer',
        'electrum-drk.transaction',
        'electrum-drk.util',
        'electrum-drk.verifier',
        'electrum-drk.version',
        'electrum-drk.wallet',
        'electrum-drk.x509',
        'electrum-drk_gui.gtk',
        'electrum-drk_gui.qt.__init__',
        'electrum-drk_gui.qt.amountedit',
        'electrum-drk_gui.qt.console',
        'electrum-drk_gui.qt.history_widget',
        'electrum-drk_gui.qt.icons_rc',
        'electrum-drk_gui.qt.installwizard',
        'electrum-drk_gui.qt.lite_window',
        'electrum-drk_gui.qt.main_window',
        'electrum-drk_gui.qt.network_dialog',
        'electrum-drk_gui.qt.password_dialog',
        'electrum-drk_gui.qt.paytoedit',
        'electrum-drk_gui.qt.qrcodewidget',
        'electrum-drk_gui.qt.qrtextedit',
        'electrum-drk_gui.qt.qrwindow',
        'electrum-drk_gui.qt.receiving_widget',
        'electrum-drk_gui.qt.seed_dialog',
        'electrum-drk_gui.qt.transaction_dialog',
        'electrum-drk_gui.qt.util',
        'electrum-drk_gui.qt.version_getter',
        'electrum-drk_gui.stdio',
        'electrum-drk_gui.text',
        'electrum-drk_plugins.btchipwallet',
        'electrum-drk_plugins.coinbase_buyback',
        'electrum-drk_plugins.cosigner_pool',
        'electrum-drk_plugins.exchange_rate',
        'electrum-drk_plugins.greenaddress_instant',
        'electrum-drk_plugins.labels',
        'electrum-drk_plugins.trezor',
        'electrum-drk_plugins.virtualkeyboard',
        'electrum-drk_plugins.plot',

    ],
    description="Lightweight Darkcoin Testnet Wallet",
    author="Thomas Voegtlin, Propulsion",
    author_email="thomasv1@gmx.de, Propulsion@DarkcoinTalk.org",
    license="GNU GPLv3",
    url="https://electrum-drk.org, https://github.com/Propulsions/electrum-drk-drk",
    long_description="""Lightweight Darkcoin Testnet Wallet"""
)
