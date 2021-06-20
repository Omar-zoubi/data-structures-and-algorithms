from Data_Structures.HashTable.hashtable import Hashtable

def test_hash_table():
    hash = Hashtable(1024)
    hash.add('type', 'toyota')
    hash.add('color', 'black')
    hash.add('wheels', 4)
    hash.add('kind', 'camry')
    hash.add('year', 2010) 
    assert hash.contains('type') == True
    assert hash.contains('color') == True
    assert hash.contains('wheels') == True
    assert hash.contains('year') == True 
    assert hash.contains('year') == True
    assert hash.contains('used?') == False
    assert hash.get('type') == 'toyota'
    assert hash.get('color') == 'black'
    assert hash.get('wheels') == 4
    assert hash.get('used?') == None
    assert hash.get('kind') == 'camry'
    assert hash.get('year') == 2010