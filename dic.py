dic = {'name' : 'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)

#a에 key와 value가 각각 2와 b인 2:b 라는 딕셔너리 쌍이 추가
a = {1:'a'}
a[2] = 'b'
print(a)

#딕셔너리 요소 삭제 key에 해당하는 key:value 쌍 삭제!
del a[1]
print(a)

#딕셔너리에서 key를 사용해 value 얻기
grade = {'pey' : 10, 'julliet' : 99}
print(grade['pey'])

#딕셔너리에서 Key는 고유한 값이므로 중복되는 key값을 설정해 놓으면 안됨!
#또한 Key에는 리스트를 쓸 수 없음(리스트는 변하는데 key값은 변하면 안되므로)

#key로 반환되는 객체인 dict_keys를 리스트로 변환하려면 list를 써주면 됨!
print(list(dic.keys()))

#key value쌍 모두 얻으려면 items함수를 써서 dict_items객체로 돌려줌
print(dic.items())

#key: value쌍 모두 지우기(clear) --> 딕셔너리 안의 모든 요소를 삭제

#Key로 value얻기 --> get방법 a.get('name') 이 방법 과 일반 a['name']과 다른점은 get의 경우
#존재하지 않는 키를 get할때 none을 돌려주지만 일반적인 방법은 없는 키이기 때문에 오류 발생!
#딕셔너리 안에 찾으려는 Key값이 없는 경우 미리 정해둔 디폴트 값 사용가능 --> a.get('key', 'default')
#해당 Key가 딕셔너리 안에 있는지 조사 --> in 
c = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in c)
print('email' in c) 