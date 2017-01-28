
# coding: utf-8

import pandas as pd

keep_columns = ['CNT', 'SUBNATIO', 'STRATUM', 'NC', 'ST01Q01', 'ST06Q01', 'ST13Q01', 'ST18Q01', 'ST21Q01', 'ST27Q02', 'ST26Q02', 'ST26Q04', 'ST26Q06', 'PV1MATH', 'PV2MATH', 'PV3MATH', 'PV4MATH', 'PV5MATH', 'PV1READ', 'PV2READ', 'PV3READ', 'PV4READ', 'PV5READ', 'PV1SCIE', 'PV2SCIE', 'PV3SCIE', 'PV4SCIE', 'PV5SCIE', 'W_FSTUWT']

pisa = pd.read_csv('pisa2012.csv', names=keep_columns)

pisa.to_csv('truncatedPisa.csv')
