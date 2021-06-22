from code_challenges.left_join.left_join import *
def test_full_mach():
    table1=Hashtable(1024)
    table2=Hashtable(1024)
    table1.add('name','omar')
    table1.add('gender','male')
    table1.add('age','26')
    table1.add('dgree','bacha')
    table2.add('name','kaled')
    table2.add('gender','male')
    table2.add('age','29')
    table2.add('dgree','master')
    expected= [['name', 'omar', 'kaled'], ['gender', 'male', 'male'], ['age', '26', '29'], ['dgree', 'bacha', 'master']]
    acctual = left_joined(table1,table2)
    assert expected == acctual

def test_no_mach():
    table1=Hashtable(1024)
    table2=Hashtable(1024)
    table1.add('name','omar')
    table1.add('gender','male')
    table1.add('age','26')
    table1.add('dgree','bacha')
    table2.add('color','red')
    table2.add('model','kia')
    table2.add('year','1999')
    table2.add('wheels','4')
    expected= [['name', 'omar', 'null'], ['gender', 'male', 'null'], ['age', '26', 'null'], ['dgree', 'bacha', 'null']]
    acctual = left_joined(table1,table2)
    assert expected == acctual

def test_one_table():
    table1=Hashtable(1024)
    table2=Hashtable(1024)
    table1.add('name','omar')
    table1.add('gender','male')
    table1.add('age','26')
    table1.add('dgree','bacha')
    expected= [['name', 'omar', 'null'], ['gender', 'male', 'null'], ['age', '26', 'null'], ['dgree', 'bacha', 'null']]
    acctual = left_joined(table1,table2)
    assert expected == acctual
def test_normal_mach():
    table1=Hashtable(1024)
    table2=Hashtable(1024)
    table1.add('name','omar')
    table1.add('gender','male')
    table1.add('age','26')
    table1.add('dgree','bacha')
    table2.add('name','kaled')
    table2.add('gender','male')
    table2.add('tall','185cm')
    table2.add('dgree','master')
    expected= [['name', 'omar', 'kaled'], ['gender', 'male', 'male'], ['age', '26', 'null'], ['dgree', 'bacha', 'master']]
    acctual = left_joined(table1,table2)
    assert expected == acctual
