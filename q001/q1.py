s3 = [x for x in range(3,1000,3)]
s5 = [x for x in range(5,1000,5)]
diff = list(set(s3) - set(s5))
sum(diff + s5)