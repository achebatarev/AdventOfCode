defmodule Aoc2024D1 do
  def input(filename) do 
    File.read(filename) 
    |> elem(1) 
  end

  def parse(str) do 
    str 
    |> String.split("\n", trim: true)
    |> Enum.map(fn x -> 
      x
      |> String.split 
      |> Enum.map(&String.to_integer/1)
    end)
  |> Enum.reduce([[], []], fn [a, b], [acc1, acc2] -> [[a | acc1], [b | acc2]] end)
  end
end

Aoc2024D1.input("input_test.txt")
|> Aoc2024D1.parse
|> Enum.map(&Enum.sort/1)
|> Enum.zip() 
|> Enum.map(fn {a, b} -> abs(a - b) end)
|> Enum.sum()
|> IO.inspect()

# part2
[l1, goal] = Aoc2024D1.input("input_test.txt") 
|> Aoc2024D1.parse()

l1
|> Enum.map(fn e -> Enum.count(goal, &(&1 == e)) end)
|> IO.inspect() 
|> Enum.zip(l1)
|> Enum.map(&Tuple.product/1)
|> Enum.sum()
|> IO.inspect() 



