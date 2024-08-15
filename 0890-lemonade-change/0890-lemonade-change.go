type change struct{
    five int
    ten int
    twenty int
}
func lemonadeChange(bills []int) bool {
    ch := change{}
    for _,i:= range bills{
        fmt.Println(ch)
        if i == 5{
            ch.five+=1
        }else if i == 10{
            if ch.five>0{
                ch.five -= 1
                ch.ten+=1
            }else{
                return false
            }
        }else{
            rem := i-5
            times := rem/10
            if ch.ten>= times{
                ch.ten -= times
                if ch.five>0{
                    ch.five-=1
                }else{
                    return false
                }
            }else{
                if rem/5<= ch.five{
                    ch.five -= rem/5
                }else{
                    return false
                }
            }
        }
    } 
    return true
}