def firstFit(items, capacity):
    t = 1
    remainingSpace = [capacity]
    bins = [[]]
    for item in items:
        # loop through bins and check to which first item does fit
        for i in range(len(bins)):
            # if item fits then put it in and break the bins loop
            if (remainingSpace[i] - item >= 0):
                remainingSpace[i] -= item
                bins[i].append(item)
                break
            
            # at the last iteration if item was not put into any container
            # create a new container with item in it
            if (i == len(bins) - 1):
                t += 1
                remainingSpace.append(capacity - item)
                bins.append([item])
                
    # display bins
    # for bin in bins:
    #     print(bin)
    return t