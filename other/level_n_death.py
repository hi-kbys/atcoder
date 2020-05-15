import sys
from itertools import combinations

def main(lines):
    #最大公約数の計算
    def gcd(x,y):
        r= x%y
        if r ==0:
            return y
        return gcd(y,r)
    
    #最小公倍数の計算
    def lcm(k,args):
        u = 1
        
        for arg in args:
            u *= arg
        print(u)
        ret = u/(k**(len(args)-1))
        return int(ret)

    #level n倍に該当する敵を排除する。
    def n_death(num):
        ret = r//num - l //num
        if l%num ==0:
            ret += 1
        return ret

    #変数の読み込み
    l,r = map(int,lines[0].split())
    m = int(lines[1])
    magic_list = list(map(int,lines[2].split()))
    
    magic_list.sort()
    gcd_dict = {}

    #level　n の倍数になっているものは魔法の候補から排除する。
    # 後の作業のために最大公約数が共通するものを集めた辞書を作っておく。
    for i,n_i in enumerate(magic_list,1):
        for n_j in magic_list[i:]:
            if n_j%n_i == 0:
                magic_list.remove(n_j)
                continue
            num_gcd = gcd(n_i,n_j)

            if num_gcd !=1:
                if num_gcd in gcd_dict:
                    gcd_dict[num_gcd].append(n_j)
                else:
                    gcd_dict[num_gcd] = [n_i,n_j]
    
    #辞書内にある数字から順次k個選んでいき最小公倍数を作っていく。
    magic_add = [] #敵を重複して減らしてしまった分を加える
    magic_sub = magic_list #敵を減らすための魔法の候補
    for num_gcd,values in zip(gcd_dict,gcd_dict.values()):
        for k in range(2,len(values)+1):
            comb = list(combinations(values,k))
            
            for comb_ in comb:
                lcm_num = lcm(num_gcd,comb_)
                if k%2 == 0:
                    magic_add.append(lcm_num)
                else:
                    magic_sub.append(lcm_num)

    remain  = r-l+1

    for n_i in magic_sub:
        remain -= n_death(n_i)
    for n_i in  magic_add:
        remain += n_death(n_i)

    print(remain)

if __name__ == '__main__':
    sys.stdin = open("./input.txt")
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
