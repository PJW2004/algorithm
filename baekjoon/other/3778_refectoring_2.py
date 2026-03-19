import sys
output_stdout = sys.stdout.write
n, *r = open(0) # 한번에 읽어버리고.
output_list = []
for index in range(0,int(n)<<1,2):
    alphabet_a,alphabet_b=r[index].rstrip(),r[index+1].rstrip()
    output_list.append(f'Case #{(index>>1)+1}: {sum([abs(alphabet_a.count(alphabet) - alphabet_b.count(alphabet)) for alphabet in set(alphabet_a + alphabet_b)])}')
output_stdout('\n'.join(output_list))