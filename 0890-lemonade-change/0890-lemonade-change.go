
func lemonadeChange(bills []int) bool {
    ch := make(map[int]int)
    for _,i:= range bills{
        if i == 5{
            ch[i]+=1
        }else if i == 10{
            if ch[5]>0{
                ch[5] -= 1
                ch[10]+=1
            }else{
                return false
            }
        }else{
            rem := i-5
            times := rem/10
            if ch[10]>= times{
                ch[10] -= times
                if ch[5]>0{
                    ch[5]-=1
                }else{
                    return false
                }
            }else{
                if rem/5<= ch[5]{
                    ch[5] -= rem/5
                }else{
                    return false
                }
            }
        }
    } 
    return true
}