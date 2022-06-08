#!/usr/bin/python3.8
import os

for i in range(1, 4):
	os.system('mkdir {}'.format(i))
	print('[*]pasta {} criada'.format(i))
	os.system('cd {}'.format(i))
	print('[*] acessando a pasta {}'.format(i))
	for j in range(1, 3):
		os.system('mkdir {}/{}'.format(i, j))
		print('[*]subpasta {} criada'.format(j))
		print('[*]acessando a subpasta')
		os.system('cd {}'.format(j))
		for z in range(1, 4):
			os.system('echo arquivo {} > {}/{}/{}.txt'.format(z, i, j, z))
			print('[*]arquivo {}.txt criado'.format(z))
			os.system('cd ..')
	os.system('cd ..')
