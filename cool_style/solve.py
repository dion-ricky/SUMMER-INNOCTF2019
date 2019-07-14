#!/usr/bin/env python3
import caesar
import re

raw = '''<link rel="stylesheet" href="../assets/css/IUJgvjjbgCbKNhuooTCR.css">
<link rel="stylesheet" href="../assets/css/nrggdsmoNhmuJZyEAO.css">
<link rel="stylesheet" href="../assets/css/nWZLixTshtzrBHHKZCon.css">
<link rel="stylesheet" href="../assets/css/oQuHektPeOJXaDJeOTXkm.css">
<link rel="stylesheet" href="../assets/css/CLwgNvHIyAofgmbn.css">
<link rel="stylesheet" href="../assets/css/TGtIHPDbTWGoqTVlEQWvB.css">
<link rel="stylesheet" href="../assets/css/FKwNJEiFHjRodCdJrJci.css">
<link rel="stylesheet" href="../assets/css/{YQEIQDHnzxwyJkU.css">
<link rel="stylesheet" href="../assets/css/gEDwcIynEQjsppax.css">
<link rel="stylesheet" href="../assets/css/RvHvyvigdvBLKDCInkc.css">
<link rel="stylesheet" href="../assets/css/CiOVSFfEMZPiVtAXSjaqT.css">
<link rel="stylesheet" href="../assets/css/FtllZbvLdBROpAUWKYt.css">
<link rel="stylesheet" href="../assets/css/VnGWYEMVrAWHgSsMj.css">
<link rel="stylesheet" href="../assets/css/XksbQXoCxSpvxVfzmDJ.css">
<link rel="stylesheet" href="../assets/css/eOVjmQFXBGqCfRrAd.css">
<link rel="stylesheet" href="../assets/css/LVjWWtAIMhLvSBSFFpm.css">
<link rel="stylesheet" href="../assets/css/HSUTjCoXhUSgdFmnRB.css">
<link rel="stylesheet" href="../assets/css/TQUXAjeVcBsBuvVLuZ.css">
<link rel="stylesheet" href="../assets/css/EuTwNIWdpJyGzEPaGt.css">
<link rel="stylesheet" href="../assets/css/yQGOJexeijQAipYU.css">
<link rel="stylesheet" href="../assets/css/FbaYSRCtRvomasKvr.css">
<link rel="stylesheet" href="../assets/css/tHnoLzeHWytJlBrhyjTP.css">
<link rel="stylesheet" href="../assets/css/JjQXzSfmtfzgphLJOwfh.css">
<link rel="stylesheet" href="../assets/css/ojtDvXjngAToaxCh.css">
<link rel="stylesheet" href="../assets/css/qjeydFqsuxHoUzfTSWbW.css">
<link rel="stylesheet" href="../assets/css/tqOolAXffGoFsAiQEL.css">
<link rel="stylesheet" href="../assets/css/CBLrZUeuNRpwoFZxetiA.css">
<link rel="stylesheet" href="../assets/css/tLPrudKCwTQQYzch.css">
<link rel="stylesheet" href="../assets/css/bKwAsDWPQSyFthAwZag.css">
<link rel="stylesheet" href="../assets/css/HpGAkKhTVrzJkTCmQUx.css">
<link rel="stylesheet" href="../assets/css/TMkcPBxGAujFcusJ.css">
<link rel="stylesheet" href="../assets/css/eTkGskwYettEFMRFzrR.css">
<link rel="stylesheet" href="../assets/css/ckkemHUQOnFQtRlLfVVb.css">
<link rel="stylesheet" href="../assets/css/UqdvWSnUYLBhdbNWskir.css">
<link rel="stylesheet" href="../assets/css/bCkkEsuAWYlxDMLcP.css">
<link rel="stylesheet" href="../assets/css/jtDBgZWGpIafLxFViIkc.css">
<link rel="stylesheet" href="../assets/css/QCrQUMfWuxkhidvYGf.css">
<link rel="stylesheet" href="../assets/css/iKLnJqUxJTTVUoop.css">
<link rel="stylesheet" href="../assets/css/kiXBnPbrCAsTKhEU.css">
<link rel="stylesheet" href="../assets/css/GGVGRjfiRrXDAVsV.css">
<link rel="stylesheet" href="../assets/css/}fLQxrIgFIcArXEXnXd.css">'''

styles = re.findall("\/css\/([^.]+).css", raw)

for style in styles:
    print("Checking {}".format(style))
    for i in range(1, 27):
        print("{} => {}".format(i, caesar.decode(style, i)))
# print(styles)
