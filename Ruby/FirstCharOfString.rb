#!/usr/bin/ruby

class String
	def FirstChar
		self[0,1]
	end
end

def main()
	str = gets
	print str.FirstChar,"\n"	
end
main()

