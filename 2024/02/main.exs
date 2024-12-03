# What I want to do is:
# 1. Iterate over each list
# 2. For each list iterate over elements
# 3. For each element check if it's greater or less then the previous element
# I need memory, of the past, I can achieve it with the reduce acc set to {[], []}, where first list will be filled up with true, false values, and second with latest checked
defmodule Aoc2024D2 do
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
  end
end

Aoc2024D2.input("input.d2")
|> Aoc2024D2.parse
|> Enum.map(fn l ->
  chunked = l
  |> Enum.chunk_every(2, 1, :discard)
  [a, b] = hd(chunked)
  increasing = if a < b, do: true, else: false
  val = chunked
  |> Enum.reduce(0, fn [a, b], acc -> 
    cond do
      increasing and a < b and abs(a-b) >=1 and abs(a-b) <= 3 -> 1
      !increasing and a > b and abs(a-b) >=1 and abs(a-b) <= 3 -> 1 
      true -> 0 
    end
    |> Kernel.+(acc)
  end)
  if val == length(chunked), do: 1, else: 0
end)
|> Enum.sum()
|> IO.inspect()

# part2
Aoc2024D2.input("input.d2")
|> Aoc2024D2.parse
|> Enum.map(fn l ->
  chunked = l
  |> Enum.chunk_every(2, 1, :discard)
  [a, b] = hd(chunked)
  increasing = if a < b, do: true, else: false
  val = chunked
  |> Enum.reduce(0, fn [a, b], acc -> 
    cond do
      increasing and a < b and abs(a-b) >=1 and abs(a-b) <= 3 -> 1
      !increasing and a > b and abs(a-b) >=1 and abs(a-b) <= 3 -> 1 
      true -> 0 
    end
    |> Kernel.+(acc)
  end)
  if val == length(chunked) or val == length(chunked) - 1, do: 1, else: 0
end)
|> Enum.sum()
|> IO.inspect()
