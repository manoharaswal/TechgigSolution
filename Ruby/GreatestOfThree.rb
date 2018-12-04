#!/usr/bin/ruby
def main()
	num1 = gets
	num2 = gets
	num3 = gets
	larg = 0
	if(num1 > num2 and num1 > num3)
		larg = num1
	elsif(num2 > num1 and num2 > num3)
		larg = num2
	else
		larg = num3
	end
	puts larg
end
main()
