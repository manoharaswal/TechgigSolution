#!/usr/bin/ruby
include Math

class Numeric
    def sqrt
      Math.sqrt self
    end
end

def main()
    n = gets
    print (n.to_i.sqrt).to_i,"\n"
end
main()

