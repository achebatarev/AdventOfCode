# I want to somehow get these tuples into separate lists, basically slice these tuples vertically
# How would I do it normally?
# Create two lists, 
# iterate over all the rows, 
# put elements in respective lists
# Sort both
# find diffs

# Pairs are still linked, I need to somehow unlink them

# Part 2:
# For each element find it's occurence in other list
# Iterate over first list
# While iterating search for an element in another list

File.read("input1.txt") 
|> elem(1) 
|> String.split("\n", trim: true)
|> Enum.map(&String.split/1)
|> Enum.map(fn [a, b] -> %{:f=>[String.to_integer(a)], :s=>[String.to_integer(b)]} end )
|> Enum.reduce(fn m1,m2 -> Map.merge(m1, m2, fn _k, v1, v2 -> v2 ++ v1 end) end)
|> Map.values()
|> Enum.map(&Enum.sort/1)
|> Enum.zip()
|> Enum.map(fn {a, b} -> abs(a-b) end)
|> Enum.sum()
|> IO.inspect() 

l = File.read("input1.txt")
|> elem(1)
|> String.split("\n", trim: true) 
|> Enum.map(&String.split/1)
|> Enum.map(fn [a, b] -> %{:f=>[String.to_integer(a)], :s=>[String.to_integer(b)]} end )
|> Enum.reduce(fn m1,m2 -> Map.merge(m1, m2, fn _k, v1, v2 -> v2 ++ v1 end) end)
|> Map.values()

goal = hd(tl(l))
hd(l) 
|> Enum.map(fn e -> Enum.count(goal, &(&1 == e)) end)
|> Enum.zip(hd(l))
|> Enum.map(fn {a, b} -> a*b end)
|> Enum.sum()
|> IO.inspect() 


