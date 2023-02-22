
lst=[1,2,4,3,5]

iterator=iter(lst)


try:

    ele=next(iterator)

    while(ele is not StopIteration):

        print(ele)

        ele=next(iterator)


except (StopIteration) as obj:

    print("End of the iteration")



