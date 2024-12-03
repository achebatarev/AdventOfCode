defmodule Aoc2024D3 do
  def input(filename) do 
    File.read(filename) 
    |> elem(1) 
  end
end

input = Aoc2024D3.input("input.d3")
Regex.scan(~r/mul\(\d+,\d+\)/, input)
|> Enum.reduce(0, fn str, sum -> 
  Regex.scan(~r/\d+/, to_string(str))
  |> List.flatten() 
  |> Enum.reduce(1, fn e, product -> 
    e
    |> String.to_integer()
    |> Kernel.*(product)
  end)
  |> Kernel.+(sum)
end)
|> IO.inspect()
