#! /usr/bin/env ruby
require 'open-uri'


def count_em(string, substring)
  string.scan(/(?=#{substring})/).count
end


# Fetch and parse HTML document
s = 'https://cmsc420.cs.umd.edu/meeshquest/part3/input/'
tests = {}

# change this term based on what you want to search for, 
# which test you want to start at, and when to stop
search_term = "nearestCity"
min = 1600
max = 1750

while min < max do
    test_num = min.to_s
    
    html =  open(s + test_num).read
    
    # checks size of current file
    puts html.length + " " + min
    
    # not doing stuff that take too long, change if you want
    if html.length < 200000
        # using slice because gsub is inefficient af
        html = html.slice((html.index('<pre>'))..html.length-1)
        html = html.slice(0..(html.index('</pre>')))

        if html.include? search_term
            tests[test_num] = count_em(html, search_term)
        end
    end
    min += 1
end

# prints a hashmap of test number => number of occurrences
puts tests 

# prints it sorted in reverse because I can
puts tests.sort_by {|_key, value| value}.reverse.to_h