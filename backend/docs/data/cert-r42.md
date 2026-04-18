# CERT Insider Threat Test Dataset r4.2

Source: CMU KiltHub (https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247)

Contains synthetic logs for ~1000 employees over 18 months.
Five malicious scenarios (S1–S5) covering data exfiltration, sabotage, and IP theft.
Log types: logon, device, file, http, email, psychometric (LDAP snapshots).
Ground truth labels in the 'answers/' folder — one CSV per scenario.

Used exclusively for training and evaluation; never shipped with the application.
