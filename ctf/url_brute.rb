#! /usr/bin/env ruby

require 'nokogiri'
require 'open-uri'

# Fetch and parse HTML document
s = 'https://ggpuzzles.appspot.com/disarm?key='
n = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
wrong = 116
place = 1

while wrong > 0 do 
    doc = Nokogiri::HTML(open(s + n.to_s))
    curr = doc.css('p')
    if curr.to_s =~ /([0-9]+)/ then
        test = $1               #the test value must go down
        #print "Test: " + $1.to_s + "Num_Wrong: " + (wrong - 1).to_s + "\n"
        print "wrong: " + wrong.to_s + " test: " + test.to_s + ": " + n.to_s + "\n"
        if (test.to_i == (wrong - 1)) then
            wrong = wrong - 1
            place = place*10
        elsif (test.to_i == wrong + 1) then
            n = n - 1*place
            place = place*10
        else    
            n = n + 1*place
        end
    else 
        print curr.to_s + n.to_s + "\n"
        break
    end
end
