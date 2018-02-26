# -*- coding: utf-8 -*-

# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.


#【レッスン９】
# カルマンフィルタは観測更新(z)と動作予測(x)を繰り返しながら動作する
 
#【レッスン１７】
# 観測系(z)の更新をupdateと呼称	updateはベイズ掛け算に基づく複雑系
# 予測系(x)の更新をpredictと呼称	predictは畳み込みに基づく単純加算系

# Insert code here

for n in range(len(measurements)):
	[mu,sig]=update(mu,sig,measurements[n],measurement_sig)
#	print 'update: ' , [mu,sig]

	[mu,sig]=predict(mu,sig,motion[n],motion_sig)
#	print 'update: ' , [mu,sig]


print [mu, sig]

