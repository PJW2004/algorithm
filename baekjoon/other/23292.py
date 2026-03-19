Y_1,Y_2,Y_3,Y_4,M_1,M_2,D_1,D_2 = map(int,input())
def bio_rhythm(string_date:str) -> str:
    y_1,y_2,y_3,y_4,m_1,m_2,d_1,d_2=map(int,string_date)
    return (((Y_1-y_1)**2+(Y_2-y_2)**2+(Y_3-y_3)**2+(Y_4-y_4)**2)
            *((M_1-m_1)**2+(M_2-m_2)**2)
            *((D_1-d_1)**2+(D_2-d_2)**2))

answer:tuple = ("",0)
for _ in range(int(input())):
    coding_string_date:str = input()
    integer_bio_rhythm:int = bio_rhythm(coding_string_date)
    if answer[-1] <= integer_bio_rhythm:
        answer = (coding_string_date,integer_bio_rhythm)
print(answer[0])