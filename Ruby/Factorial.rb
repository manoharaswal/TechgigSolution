#!/usr/bin/ruby

def main()
	n = gets
	fac = 1
	i = 2
	while i.to_i <= n.to_i do
		fac = fac * i
		i += 1
	end
	print fac,"\n"
end
main()

