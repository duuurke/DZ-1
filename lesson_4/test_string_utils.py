import pytest
from StringUtils import StringUtils

StUtils = StringUtils()

#capitilize
@pytest.mark.parametrize('input_string, expected_output', [
    #позитив
    ("katya","Katya"),
    ('enot','Enot'),
    #негатив
    ('12345', '12345'),
    ('@#$%','@#$%'),
    ('',''),
    (' ',' ')
    ])

def test_capitilize (input_string, expected_output):
    assert StUtils.capitilize (input_string) == expected_output

#TRIM

@pytest.mark.parametrize ('input_string, expected_output', [
    #позитив
    (' good', 'good'),
    ('    dog', 'dog'),
    ('    dog & cat', 'dog & cat'),
    #негатив
    ('',''),
    ])
def test_trim(input_string, expected_output):
   assert StUtils.trim (input_string) == expected_output


@pytest.mark.xfail()
def test_trim():
    assert StUtils.trim ( 'hello' ) == 'hello'

@pytest.mark.xfail()
def test_trim():
    assert StUtils.trim ( ' 123 ' ) == '123'

#TO_LIST
@pytest.mark.parametrize('string, divider, result', [
    #позитив
    ('чашка;блюдце;чай', ';', ['чашка', 'блюдце', 'чай']),
    ('DuCk:DoG:CaT', ':', ['DuCk', 'DoG', 'CaT']),
    ('9,10,8,7,5,4,3,2,1', ',', ['9', '10', '8', '7', '5', '4', '3', '2', '1']),
    #негатив
    ("", None, []),
    ('стакан,ложка,вилка', None, ['стакан', 'ложка', 'вилка']), 
])
    
def test_to_list(string, divider, result):
    if divider is None:
        res = StUtils.to_list(string)
    else:
        res = StUtils.to_list(string, divider)
    assert res == result

#CONTAINT 
@pytest.mark.parametrize('string, symbol, result', [
    ('dog', 'd', True),
    ('enot ', 'n', True),
    ('KaZeL', 'Z', True),
    ('S+M', '+', True),
    (' duck', 'd', True),
    ('123', 'ф', False),
    ('wow', '3', False),
    ('гамбит', 't', False),
])
def test_contains(string, symbol, result):
    res = StUtils.contains(string, symbol)
    assert res == result

#DELITE_SYMBOL
@pytest.mark.parametrize('string, symbol, result', [
#позитив
    ('dog', 'g', 'do'),
    ('enot ', 't', 'eno'),
    ('KaZeL', 'eL', 'KaZ'),
    ('S+M', '+', 'SM'),
    (' duck', ' ', 'duck'),
    ('wow', 'w', 'o'),
    #негатив
    ('', 'g', ''),
    ('123', '7', '123'),
])
def test_delete_symbol(string, symbol, result):
    res = StUtils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.xfail()
def test_delete_symbol():
    assert StUtils.delete_symbol('гамбит', 'a', 'гмбит')

#STARTS_WITH
@pytest.mark.parametrize('string, symbol, result', [
#нигатив
    ('dog', 'd', True),
    ('enot ', 'e', True),
    ('KaZeL', 'K', True),
    ('S+M', 'S', True),
    (' duck', 'd', True),
    ('wow', 'w', True),
    ('', 'g', False),
    ('123', '2', False),
    ('гамбит', '2', False),
])
def test_starts_with(string, symbol, result):
    res = StUtils.starts_with(string, symbol)
    assert res == result


#END.WITE
@pytest.mark.parametrize('string, symbol, result', [
    ('dog', 'g', True),
    ('enot ', 't', True),
    ('KaZeL', 'L', True),
    ('S+M', 'M', True),
    (' duck', 'k', True),
    ('wow', 'w', True),
    ('', 'g', False),
    ('123', '1', False),
    ('гамбит', 'б', False),
])
def test_end_with(string, symbol, result):
    res = StUtils.end_with(string, symbol)
    assert res == result

#IS_EMPTY
@pytest.mark.parametrize('string, result', [
    ('', True),
    ('   ', True),
    ('5', False),
    ('   .', False),
    ('гамбит', False),
])
def test_is_empty(string, result):

    res = StUtils.is_empty(string)
    assert res == result

#LIST_TO_STRING
@pytest.mark.parametrize('lst, joiner, result', [
    #позитив
    ([1, 2], None, '1, 2'),
    (['M','S'], '+', 'M+S'),
    (['M','S'], ' ', 'M S'),
    (['трасса','м95'], '-', 'трасса-м95'),
    (['календарь','перевернул'], ' он ', 'календарь он перевернул'),
    #негатив
    ([], None, ''),
    ([], '*', '')
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = StUtils.list_to_string(lst)
    else:
        res = StUtils.list_to_string(lst, joiner)
    assert res == result
