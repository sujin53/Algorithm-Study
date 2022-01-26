def solution(jobs):
    answer = 0
    jobs.sort()
    position = 0
    L = len(jobs)
    while(len(jobs)>0):
        minn = 1001
        minn_idex = 501
        minn_start = 501
        for idx, ele in enumerate(jobs):
            if(ele[0]<=position):
                if(minn > ele[1]):
                    minn_start = ele[0]
                    minn = ele[1]
                    minn_idex = idx
        if minn_idex == 501:
            position += 1
        else:
            position = position + minn
            jobs.pop(minn_idex)
            answer = answer + (position-minn_start)
    return answer//L

